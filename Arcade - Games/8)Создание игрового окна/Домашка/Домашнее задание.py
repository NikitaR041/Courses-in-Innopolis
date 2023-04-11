'''
Добавить в платформер стартовое меню с возможностью запуска игры, выхода из игры.
'''

import arcade

WIDTH = 800
HEIGHT = 600
#-----Для изменение движение персонажа
PLAYER_MOVEMENT_SPEED = 5
JUMP = 15
GRAVITY = 2
#-----

class StartMenu(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color((100,100,20))
    def on_draw(self):
        self.clear()
        arcade.draw_text("MY Game", self.window.width/2, self.window.height/2, arcade.color.WHITE, font_size = 45, anchor_x= 'center', font_name = "Kenney Blocks")
        #Создаем кнопку и загружаем текстуру
        arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2 - 100, width=200, height= 70, texture=arcade.load_texture(':resources:gui_basic_assets/red_button_normal.png'))
        arcade.draw_text("Start",self.window.width/2, self.window.height/2 - 105, arcade.color.WHITE, font_size = 17, anchor_x= 'center', font_name = "Kenney Mini")
        arcade.draw_texture_rectangle(self.window.width / 2, self.window.height / 2 - 200, width=200, height=70, texture=arcade.load_texture(':resources:gui_basic_assets/red_button_normal.png'))
        arcade.draw_text("Exit", self.window.width / 2, self.window.height / 2 - 205, arcade.color.WHITE, font_size=17, anchor_x='center', font_name="Kenney Mini")
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        print(x,y)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 300 < x < 500 and 165 < y < 235 :
            my_game = MyGame() # (2)
            #Обязательно для взаимодействия с предметами
            my_game.setup()
            window.show_view(my_game) # (2)
        if 300 < x < 500 and 65 < y < 135:
            arcade.close_window() #Кнопка выхода!!! или exit

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        '''Персонаж - переменные'''
        self.player = None  # создаем пустую переменную
        self.player_list = None  # создаем пустую переменную для списка персонажей (для анимации)
        '''Площадка - переменные'''
        self.ground = None
        self.ground_list = None

    def on_show_view(self):
        self.background_color = (0, 150, 200) #Фон


    def setup(self):
        '''Создание персонажа'''
        self.player = Player() #Создание объекта класса Player
        self.player_list = arcade.SpriteList() #создание список картинок для персонажа
        self.player_list.append(self.player) #добавляем в список картинок для персонажа
        '''Создание площадки'''
        self.ground_list = arcade.SpriteList()

        for i in range(0,800,128):
            self.ground = arcade.Sprite(':resources:images/tiles/stoneMid.png',scale = 1)
            self.ground.center_x = i
            self.ground.center_y = 32
            self.ground_list.append(self.ground)  # добавляем площадку в список

    def on_draw(self):
        self.clear()
        self.player_list.draw() #Будет рисовать персонажа из картинок (частое обновление персонажа вместе с экраном)
        self.player.update()
        self.ground_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif (symbol == arcade.key.W or symbol == arcade.key.UP) and self.player.on_the_ground == True:
            self.player.change_y = JUMP
            self.player.on_the_ground = False #(обязательно используем класс player, т.к. on_the_game - из другого класса)
        '''ПРОВЕРКА НА НАЖАТИЕ КНОПКИ ESCAPE - вызываем себя'''
        if symbol == arcade.key.ESCAPE:
            pause_view = PauseView(self)
            window.show_view(pause_view)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 0
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = 0
        elif (symbol == arcade.key.W or symbol == arcade.key.UP):
            self.player.change_y = 0

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/animated_characters/robot/robot_idle.png',scale= 1)
        '''Здесь задаем ему расположение на созданном окне'''
        self.center_x = 32
        self.center_y = 160
        '''Создадим реалистичность, чтоб on_the_ground -> если на земле, то можно прыгать, если нет - нет'''
        self.on_the_ground = False
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.center_y -= GRAVITY # действуем на игрока силой гравитации
        '''Условие, чтобы персонаж не падал всколзь вниз - т.е. даем ему границу'''
        if self.center_y <= 160: #чтобы не провалиться ниже земли
            self.center_y = 160
            self.on_the_ground = True #стоим на земле (по умолчанию)

class PauseView(arcade.View):
    def __init__(self, my_game): # (4)
        super().__init__()
        self.my_game = my_game #(3) определяем его и создаем объект объекта
        arcade.set_background_color(arcade.color.PRUNE)
    def on_draw(self):
        self.clear()
        arcade.draw_text("MENU", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=45,
                         anchor_x='center', font_name="Kenney Blocks")
        arcade.draw_text("Нажми на ESCAPE,чтобы продолжить игру", self.window.width / 2, self.window.height / 2 - 105, arcade.color.WHITE, font_size=17,
                         anchor_x='center', font_name="Kenney Mini")
    '''Здесь принимается, то что мы возвращаемся к классу MyGame тип продолжаем игру, но ноужно вставить параметр-аргумент my_game в (3) и (4)'''

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            window.show_view(self.my_game)

window = arcade.Window(WIDTH, HEIGHT)
start_menu = StartMenu() # (1)
window.show_view(start_menu) # (1)
arcade.run()
