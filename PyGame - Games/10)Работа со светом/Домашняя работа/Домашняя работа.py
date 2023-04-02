'''
Добавить в платформер освещение.
'''
import arcade
import random
from arcade.experimental.lights import Light, LightLayer #(3)
import time

WIDTH = 1024
HEIGHT = 768
SPEED = 5
VIEWPORT_MARGIN = 200 # Создаем перемещение камеры на 200 пикселей
AMBIENT_COLOR = (10,10,10) # окружающий свет

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
    def setup(self):
        '''Перемещение камеры'''
        self.view_left = 0 #Левая граница
        self.view_bottom = 0 #Нижняя граница
        #------------------------------------
        '''Все что касается света'''
        self.light_layer = LightLayer(WIDTH, HEIGHT) #Вызываем класс из модуля (3)
        # красный свет(можно любой) - мигающий свет
        self.red_light = Light(300,200,radius=150,color=arcade.color.RED,mode='soft') #Вызываем класс из модуля (3)
        self.light_layer.add(self.red_light)
        self.red_light_time = time.time()
        self.red_light_is_on = False

        # фонарик
        self.player_light = Light(0,0,radius=100,color=arcade.color.WHITE,mode='soft') #Вызываем класс из модуля (3)
        self.isOn = False #Создаем логику, которая будет работать как вкл или выкл
        #-------------------------------------------------------------------------------------------------------------------------
        self.background_sprite_list = arcade.SpriteList() #Это специальный пустой список спрайтов, в котором будем закидывать различные спрайты
        self.wall_list = arcade.SpriteList() # это будет пустой список стен (для себя можно добавить какие-то стены), в общем нужны стены для того, чтобы заработала физика
        #Создание персонажа
        self.player= arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",0.4)
        self.player.center_x = 64
        self.player.center_y = 270
        #Создание врага
        self.zombie_list = arcade.SpriteList()
        for i in range(20):
            self.zombie = Zombie()
            self.zombie.center_x = random.randint(-2000,2000)
            self.zombie.center_y = random.randint(-1500,1500)
            self.zombie_list.append(self.zombie)

        '''Создание карты'''
        for x in range(-5000,5000,128):
            for y in range(-2000,2000,128):
                sprite = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png")
                sprite.position = x,y #position -> команда, которая может расчитывать координаты объекта
                self.background_sprite_list.append(sprite) #закидываем в background_sprite_list !
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list) #Создается объект класса ПРОСТОЙ ФИЗИКИ (т.е. не используется прыжок)

    def on_draw(self):
        self.clear()
        with self.light_layer: #Накладывается слой на эти три объекта
            self.background_sprite_list.draw() #Отрисовываем все имующие спрайты в этом списке
            self.player.draw()
            self.zombie_list.draw()
        self.light_layer.draw(ambient_color=AMBIENT_COLOR) #Отрисовываем свет - слой
        arcade.draw_text("press WASD to walk, press SPACE to turn on light", font_size=20, font_name="KENNEY BLOCKS",
                         start_x=self.view_left+20,start_y=self.view_bottom+20,color=(0,0,0))


    def update(self, delta_time: float):
        self.physics_engine.update() #вызываем простую физику
        '''Создаем свой метод, который следит за перемещением камеры'''
        self.scroll_screen()  # крутим экран нашим методом
        '''Создали логику position - высчитвыает координаты | свет следит за игроком(проще говоря)'''
        self.player_light.position = self.player.position
        '''Проверка касания зомби и персонажа'''
        if arcade.check_for_collision_with_list(self.player,self.zombie_list):
            print('Ты попался')
        '''Создаем мигающий свет'''
        if time.time() - self.red_light_time > 0.5:  # если прошло 0.5 секунды то вклюачем или выключаем свет
            if self.red_light_is_on: #По умолчанию True
                self.light_layer.add(self.red_light)
            else:
                self.light_layer.remove(self.red_light)
            self.red_light_is_on = not self.red_light_is_on #Вместо False -> True
            self.red_light_time = time.time()

    '''Создаем метод, который следит за тем, что если мы изменим разрешение экрана'''
    def on_resize(self, width: int, height: int):
        self.scroll_screen()

    '''Создаем метод, который отвечает, что если персонаж будет двигаться за пределы разрешенной границы(200пкс-умолч), то камера начинает двигаться так, чтобы не ломалась картинка'''
    def scroll_screen(self):
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player.left < left_boundary:  # если персонаж подошел достаточно близко к левой границе экрана
            self.view_left -= left_boundary - self.player.left  # двигаем границу экрана влево, чтобы персонаж не вышел за рамки
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:  # если персонаж подошел достаточно близко к левой границе экрана
            self.view_bottom -= bottom_boundary - self.player.bottom  # двигаем границу экрана влево, чтобы персонаж не вышел за рамки
        # то же самое для правого края и верхнего края
        right_boundary = self.view_left + self.window.width - VIEWPORT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
        top_boundary = self.view_bottom + self.window.height - VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        arcade.set_viewport(self.view_left,self.view_left + self.window.width,self.view_bottom, self.view_bottom + self.window.height)

    '''Создаем управление '''
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = SPEED
        if symbol == arcade.key.S:
            self.player.change_y = -SPEED
        if symbol == arcade.key.A:
            self.player.change_x = -SPEED
        if symbol == arcade.key.D:
            self.player.change_x = SPEED
        '''Проверка на то,что будет ли работать свет(фонарь) при нажатии SPACE'''
        if symbol == arcade.key.SPACE:
            if self.isOn == False:
                self.light_layer.add(self.player_light)
                self.isOn = True
            else:
                self.light_layer.remove(self.player_light)
                self.isOn = False

    def on_key_release(self, symbol: int, _modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = 0
        if symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.A:
            self.player.change_x = 0
        if symbol == arcade.key.D:
            self.player.change_x = 0

    #--------------------------------------------------------------------
class Zombie(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/animated_characters/zombie/zombie_idle.png",1.5)

window = arcade.Window(WIDTH,HEIGHT)
my_game = MyGame()
my_game.setup() #Обязательно его вызывать, если применили его в классе
window.show_view(my_game)
arcade.run()