'''
Отрисовать графическое окно и подгрузить туда персонажа и сделать ему простейшее управление влево вправо.

Спрайты можно брать в стандартной библиотеке Arcade https://api.arcade.academy/en/latest/resources.html
'''
import arcade

WIDTH = 800
HEIGHT = 800
#-----Для изменение движение персонажа
PLAYER_MOVEMENT_SPEED = 5
JUMP = 15
GRAVITY = 2
#-----

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT)
        self.background_color = (0, 150, 200) #Фон
        '''Персонаж - переменные'''
        self.player = None  # создаем пустую переменную
        self.player_list = None  # создаем пустую переменную для списка персонажей (для анимации)
        '''Площадка - переменные'''
        self.ground = None
        self.ground_list = None

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

def main():
    window = MyGame()
    window.setup()
    window.run()

main()

'''
Отрисовать графическое окно.
Добавить персонажа из стандартной библиотеки. Добавить в игру сторонние объекты и реализовать коллизию столкновения объектов.
'''
