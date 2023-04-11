'''
import arcade
#Скрипты, которые нужжны для  создание частиц
from array import array
from dataclasses import dataclass #ускоряющий процесс
import arcade.gl
#Математика
import math
import random
import time

WIDTH = 1024
HEIGHT = 768
#потом нужно
PARTICLE_COUNT = 300
MAX_FADE_TIME = 1.5 #всПЫШКА
MIN_FATE_TIME = 0.25 #затухание

@dataclass #Используем, чтобы процесс шел быстро
class Burst: # Взрыв
    #Необходимые две переменные, которые друг с другом дружат
    buffer: arcade.gl.Buffer
    vao: arcade.gl.geometry

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.burst_list = [] #Пустой список взрывов
        self.program = self.window.ctx.load_program(vertex_shader='vertex_shader_v1.glsl',
                                                    fragment_shader='fragment_shader.glsl')
        self.window.ctx.enable_only() #Включаем его, ctx - объект window

    def setup(self):
        pass
    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        self.clear()
        self.window.ctx.point_size = 2*self.window.get_pixel_ratio() # Две частицы
        for burst in self.burst_list: #Все взрывы из списка взрывов - пустой
            #отрисовать
            burst.vao.render(self.program, mode = self.window.ctx.POINTS)
    #Это процесс - в дз можно закинуть при столкновении с врагом
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        #Создаем свой метод - генератор
        def _gen_initial_data(initial_x,initial_y):
            yield initial_x
            yield initial_y

        x2 = x/self.window.width*2 - 1 #нормализуем значение (от -1 до 1)  - это лучше для нашей видеокарты
        y2 = y/self.window.height*2 -1 #нормализуем значение (от -1 до 1)  - это лучше для нашей видеокарты
        # 600 /1024 * 2 - 1 Ответ = -0.7
        initial_data = _gen_initial_data(x2,y2)
        buffer = self.window.ctx.buffer(data=array('f',initial_data))
        buffer_description = arcade.gl.BufferDescription(buffer,'2f', ['in_pos']) #Описание координат
        vao = self.window.ctx.geometry([buffer_description]) #геометрия
        burst = Burst(buffer,vao)
        self.burst_list.append(burst)

window = arcade.Window(WIDTH,HEIGHT)
my_game = MyGame()
my_game.setup()
window.show_view(my_game)
arcade.run()
'''
#То что наверху - это можно сказать база
import arcade
#Скрипты, которые нужжны для  создание частиц
from array import array
from dataclasses import dataclass #ускоряющий процесс
import arcade.gl
#Математика
import math
import random
import time

WIDTH = 1024
HEIGHT = 768
#потом нужно
PARTICLE_COUNT = 200 # количество частиц
MAX_FADE_TIME = 1.5 #всПЫШКА
MIN_FATE_TIME = 0.25 #затухание

@dataclass #Используем, чтобы процесс шел быстро
class Burst: # Взрыв
    '''Необходимые две переменные, которые друг с другом дружат'''
    buffer: arcade.gl.Buffer
    vao: arcade.gl.geometry
    '''Делаем время, чтобы увидеть через сколько секунд исчезают частицы'''
    start_time: float

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.burst_list = [] #Пустой список взрывов             было: vertex_shader_v1.glsl
        self.program = self.window.ctx.load_program(vertex_shader='new_color_new_vertex_shader.glsl',
                                                    fragment_shader='fragment_shader.glsl')
        self.window.ctx.enable_only() #Включаем его, ctx - объект window

    def setup(self):
        pass

    def on_update(self, delta_time: float):
        temp_list = self.burst_list.copy() #Копируем, чтобы изменить цвет
        #Изменяем цвет
        for burst in temp_list:
            if time.time() - burst.start_time > MAX_FADE_TIME:
                self.burst_list.remove(burst)

    def on_draw(self):
        self.clear()
        self.window.ctx.point_size = 2*self.window.get_pixel_ratio() # РАзмер частицы
        for burst in self.burst_list: #Все взрывы из списка взрывов - пустой
            #отрисовать
            self.program['time'] = time.time() - burst.start_time

            burst.vao.render(self.program, mode = self.window.ctx.POINTS)
    '''Это процесс - в дз можно закинуть при столкновении с врагом'''
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        '''Создаем свой метод - генератор'''
        def _gen_initial_data(initial_x,initial_y):
            '''Цикл для того,чтобы появлялись частицы'''
            for i in range(PARTICLE_COUNT):
                #задаем рандомный угол
                angle = random.uniform(0, 2*math.pi) #uniform - команда такая
                speed = random.uniform(0.0, 0.3)
                #задаем рандомную скоростьи при помощи тригон.функ - делаем окрудность (типо салют)
                dx = math.sin(angle) * speed
                dy = math.cos(angle) * speed
                #Задаем цвет
                red = random.uniform(0, 1)
                green = random.uniform(0, 1)
                blue = random.uniform(0, 1)
                fade_rate = random.uniform(1 / MAX_FADE_TIME, 1 / MIN_FATE_TIME)
                #--------------Возвращаем----------------------------------------------
                yield initial_x
                yield initial_y
                yield dx
                yield dy
                yield red
                yield green
                yield blue
                yield fade_rate

        x2 = x/self.window.width*2 - 1 #нормализуем значение (от -1 до 1)  - это лучше для нашей видеокарты
        y2 = y/self.window.height*2 -1 #нормализуем значение (от -1 до 1)  - это лучше для нашей видеокарты
        # 600 /1024 * 2 - 1 Ответ = -0.7
        initial_data = _gen_initial_data(x2,y2)
        buffer = self.window.ctx.buffer(data=array('f',initial_data))
        buffer_description = arcade.gl.BufferDescription(buffer,'2f 2f 3f f', ['in_pos','in_vel','in_color','in_fade_rate']) #Описание координат, 'in_vel' - скорость частиц
        vao = self.window.ctx.geometry([buffer_description]) #геометрия
        burst = Burst(buffer,vao, start_time=time.time())#
        self.burst_list.append(burst)

window = arcade.Window(WIDTH,HEIGHT)
my_game = MyGame()
my_game.setup()
window.show_view(my_game)
arcade.run()

