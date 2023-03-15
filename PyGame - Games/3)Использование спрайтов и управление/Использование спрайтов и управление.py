'''
    Использование спрайтов и их управление - создание персонажа, создание простейшей физики!

    Сайт: https://api.arcade.academy/en/latest/resources.html

    Важно:
    В библиотеке Arcade очень много нарисованных персонажей(а также их раазличные состояния движений) и не только,
    пожеланию можно создавать своих персонажей!
    Спрайт - название объекта -> найти точное определение

    Для того, чтобы создать персонажа нужно зайти на сайт, там выбрать полнуй путь этой картинки и вызвать её
    Для того, чтобы что-то создавать (персонажа, машину  и т.д) есть два метода: 1) использование класса; 2)просто вызывать в setup(без класса)
    1)Чтобы создать персонажа воспользуемся классом, который назовём Player
    2)Далее нужно будет создать переменные персонажа, для этого переменную засунем в def setup(), где пропишем:
        2.1)self.player = Player() -> создание объекта класса Player
        2.2)self.player_list = arcade.SpriteList() -> Создание список картинок (так как персонаж состоит из несколько картинок)
    3)Инициализируем его в def __init__() -вспомните зачем
        3.1) self.player = None -> создаем пустую переменную для персонажа
        3.2) self.player_list = None -> создаем пустую переменную для списка персонажей (на будущее, для анимаций)
    4)Кроме этого нужно добавлять персонажа в список
        4.1) self.player_list.append(self.player) -> добавляем персонажа в список
    5)В def on_draw() создаем переменную player_listd.draw() -> чтобы персонаж не исчезал на экране, а постоянно обновлялся вместе с экраном
    6)После всех этих махинаций нужно в def main() вызвать персонажа
        6.1)window.setup() -> вызываем setup

    Вызываем без класса -> используя цикл for
    Так как используем без класса, то создаем объект какого класса? -> классаSprite (от него исходим)
    2)Создаем переменные в def __init__ (инициализируем)

    Для того, чтобы персонаж двигался нужно знать методы клавиш:
    1)Создаем два метода - процесс нажатия клваиш и процесс отпускание клавиш
    2)100% в on_draw создаем self.player.update(), а в классе прописать метод update
      пофакту он не нужен, если вы применяете только движение влево или вправо, но если у вас что-то крутое, то нужно переопределять update
    3)
'''
import arcade

WIDTH = 800
HEIGHT = 800
#-----Для изменение движение персонажа
PLAYER_MOVEMENT_SPEED = 3
JUMP = 15
GRAVITY = 2
#-----

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width = WIDTH, height = HEIGHT,resizable= True)
        self.background_color = (0,150,200)
        '''---------------Создание персонажа----------------'''
        self.player = None  # создаем пустую переменную
        self.player_list = None # создаем пустую переменную для списка персонажей (для анимации)
        '''---------------Создание земли--------------------'''
        self.ground = None
        self.ground_list = None
        '''---------------Дополнительная задача-------------'''
        self.box = None
        self.box_list = None
        self.box_list_coords = [[512,96],[256,96],[768,96]] #Создаем три бочки - их координаты

    def setup(self): # использование на один раз
        '''-------------------Создадим персонажа------------------------------'''
        self.player = Player() #Создание объекта путем созданного класса Player
        self.player_list = arcade.SpriteList() #Создаем список картинок для персонажей
        self.player_list.append(self.player) #добавляем персонажа в список
        '''-------------------Дополнительная задача---------------------------'''
        self.box_list = arcade.SpriteList()
        '''-------------------Создадим землю без КЛАССА-----------------------'''
        self.ground_list = arcade.SpriteList() #Создание объекта путем класса sprite , одновременно создание список картинок для земли

        for i in range(0,800,128):
            self.ground = arcade.Sprite(':resources:images/tiles/grassMid.png',scale = 1) # Используем картину таким путём (для сравнения смотри на Класс Player)
            self.ground.center_x = i
            self.ground.center_y = 32
            self.ground_list.append(self.ground) # добавляем землю в список
        '''------------------Дополнительная задача---------------------------'''
        for i in self.box_list_coords:
            self.box = arcade.Sprite(':resources:images/tiles/boxCrate_single.png',scale = 1)
            # self.box = Box()
            self.box.position = i
            self.box_list.append(self.box)

    '''Здесь происходит отрисовка различных фигур, картинок (вспонить это!)'''
    def on_draw(self): #Частота изменение экрана - постоянное
        self.clear()
        self.player_list.draw() # Будет вырисовывать персонажа
        self.ground_list.draw() # Будет отрисовка земли
        self.box_list.draw()
        '''СТАНДАРТНЫЙ МЕТОД UPDATE - чтобы позволял изменять местоположение картинки при помощи клавиш'''
        self.player.update() # 'ключик для разрешение игры' - для себя написал так
        self.box_list.update()
    '''ЗДЕСЬ ЧАСТО БУДЕТ ИСПОЛЬЗОВАТЬСЯ PLAYER!!!!,ЧТОБЫ ВЫЗЫВАТЬ КЛАСС'''
    def on_key_press(self, symbol: int, modifiers: int):
        '''Движение вправо (непрекращается)'''
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED # изменение по оси х = 3
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            '''движение влево (непрекращается)'''
            self.player.change_x = -PLAYER_MOVEMENT_SPEED # изменение по оси х = -3
        elif (symbol == arcade.key.W or symbol == arcade.key.UP) and self.player.on_the_ground == True:
            '''движение прыжка (непрекращается)''' #(обязательно используем класс player, т.к. on_the_game - из другого класса)прыгаем если нажали на кнопку и если стоим на земле
            self.player.change_y = JUMP #Изменение по оси Y = 15
            self.player.on_the_ground = False #(обязательно используем класс player, т.к. on_the_game - из другого класса)

    def on_key_release(self, symbol: int, modifiers: int):
        '''Движение вправо (с прекращением)'''
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 0 # изменение по оси х = 0
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            '''Движение влево (с прекращением)'''
            self.player.change_x = 0 # изменение по оси х = 0
        elif symbol == arcade.key.W or symbol == arcade.key.UP:
            '''Движение прыжка (с прекращением)'''
            self.player.change_y = 0

''' Создание персонажа (1 метод)'''
class Player(arcade.Sprite): #Наследуемся от класса Спрайт
    def __init__(self): #Инициализация персонажа (его расположение на картинке, различные спрайты, загрузка картинок) ->> чертёжник
        super().__init__(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png',scale = 1) #Параметры: 1)ПОЛНЫЙ путь картинки; 2)его размер
        self.center_x = 32
        self.center_y = 160
        '''создаем переменную on_the_ground -> если на земле, то можно прыгать, если нет - нет'''
        self.on_the_ground = False #переменная которую мы меняем на True - если касается земли, False - если не касается земли
    '''вызываем update, чтобы переопределить его значения (можно не вкл, так как он работает по умолчанию)'''
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.center_y -= GRAVITY # действуем на игрока силой гравитации
        '''Условие, чтобы персонаж не падал всколзь вниз - т.е. даем ему границу'''
        if self.center_y <= 160: #чтобы не провалиться ниже земли
            self.center_y = 160
            self.on_the_ground = True #стоим на земле (по умолчанию)
'''Дополнительная задача - если хочешь то можешь раскоментировать Box()'''
class Box(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/tiles/boxCrate_single.png',scale = 1)
    def update(self):
        self.center_x += 2

def main():
    window = MyGame()
    window.setup() # вызываем setup
    arcade.run() # вызываем run
main()

'''ДОПОЛНИТЕЛЬНАЯ ЗАДАЧКА: 1)
Создать двумерный список с любыми координатами для любых объектов, например для бочек или ящиков
отрисовать их при помощи цикла for как мым делали это с землей
'''
'''ДОПОЛНИТЕЛЬНАЯ ЗАДАЧКА: 2)
Cоздать класс Box (или любой другой объект придумать самим, лягушка, ключик, монетка и тд).
Cоздать в классе Box - метод update - заставить объект постоянно двигаться влево вправо на какую-то величину.
'''
