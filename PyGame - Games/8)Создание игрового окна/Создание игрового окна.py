import arcade, random
'''Создание двух уровней и переключаться между ними -> существует View (позволяет переключатся между конами, классами)'''
'''
Идея:
1)Создаем в (1) сначала окно меющки, а в классе меню (2) вызваем окно MyGame() при помощи клика мыши on_mouse_press  
'''
WIDHT = 800
HEIGHT = 600
'''Класс меню'''
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
    '''Здесь создадим метод on_show_view -> получше чем def __init__, так как не будет сбрасывать игру по занавой! А продолжит, где он останавливался (продолжит прежний объект)'''
    def __init__(self): #вызывает ОДИН  раз при создании окна
        super().__init__()
    '''Создадим персонажа'''
    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player.center_x = 50
        self.player.center_y = 50
        #Создадим монетки
        self.coin_list = arcade.SpriteList()
        for i in range(20):
            self.coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.2)
            self.coin.center_x = random.randint(0, WIDHT)
            self.coin.center_y = random.randint(0, HEIGHT)
            self.coin_list.append(self.coin)

    def update(self, delta_time: float):
        hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for i in hit:
            i.remove_from_sprite_lists() #удаляет монеты
        if len(self.coin_list) == 0:
            victory = VictoryView()
            window.show_view(victory)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.center_x = x
        self.player.center_y = y


    '''Метод, который продолжает тот метод, который был запущен раннее'''
    def on_show_view(self):
        arcade.set_background_color(arcade.color.RED)
        self.window.set_mouse_visible(False)

    def on_draw(self):
        self.clear()
        self.coin_list.draw()
        self.player.draw()

    '''ПРОВЕРКА НА НАЖАТИЕ КНОПКИ ESCAPE - вызываем себя'''
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            pause_view = PauseView(self)
            window.show_view(pause_view)

'''Создание класса МЕНЮШКИ'''
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


'''Создание победного окна'''
class VictoryView(arcade.View):
    def __init__(self): # (4)
        super().__init__()
        arcade.set_background_color(arcade.color.RED)
    def on_draw(self):
        self.clear()
        arcade.draw_text("VICTORY!!!!", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=70,
                         anchor_x='center', font_name="Kenney Blocks")

window = arcade.Window(WIDHT, HEIGHT)
start_menu = StartMenu() # (1)
window.show_view(start_menu) # (1)
arcade.run()