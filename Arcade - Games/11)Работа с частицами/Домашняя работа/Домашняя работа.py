import arcade,random
import arcade.gui #Отдельный модуль, в котором можно вызвать отдельные окошки
#Математика
import time
import math
#Скрипты, которые нужжны для  создание частиц
from array import array
from dataclasses import dataclass #ускоряющий процесс
import arcade.gl

WIDHT = 800
HEIGHT = 800
text = "Что добавлено:\n" \
       "1)Добавлена пауза при помощи GUI\n" \
       "2)Добавлена стартовое меню при помощи GUI\n" \
       "3)Добавлена кнопка выхода и кнопка старта при помощи GUI\n" \
       "4)Добавлен счётчик, который считает сколько прошел времени игрок\n" \
       "5)Добавлены частицы в главном меню, а также в самой игре, когда нажимаешь на SPACE, но проблема в том,\n" \
       "что он ЧАСТИЦЫ в ПРАВОМ НИЖНЕМ УГЛУ\n" \
       "P.S. спасибо учителю! Семёну Николаевичу за объяснение этой темы!"
#Константы для частиц
PARTICLE_COUNT = 200 # количество частиц
MAX_FADE_TIME = 1.5 #всПЫШКА
MIN_FATE_TIME = 0.25 #затухание

'''Создаем класс ВСПЫШКИ'''
@dataclass #Используем, чтобы процесс шел быстро
class Burst: # Взрыв
    '''Необходимые две переменные, которые друг с другом дружат'''
    buffer: arcade.gl.Buffer
    vao: arcade.gl.geometry
    '''Делаем время, чтобы увидеть через сколько секунд исчезают частицы'''
    start_time: float

#Создание старта при помощи модуля GUI
class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        '''Создаем переменные частиц'''
        self.burst_list = [] #Пустой список взрывов             было: vertex_shader_v1.glsl
        self.program = self.window.ctx.load_program(vertex_shader='new_color_new_vertex_shader.glsl',
                                                    fragment_shader='fragment_shader.glsl')
        self.window.ctx.enable_only() #Включаем его, ctx - объект window
        #-------------Вызываем менеджера---------------
        self.manager = arcade.gui.UIManager() # вызывали менеджера
        self.manager.enable() # Включили менеджера
        '''Вызываем новое окно - вертикальный(по умолчанию) бокс'''
        self.v_box = arcade.gui.UIBoxLayout()  #Удобен для того, чтобы перемещать кнопки (старта и тд) туда куда захочешь
        self.manager.add(arcade.gui.UIAnchorWidget(
            #align_x = 100 #включи и посмотри (просто делает отступ)
            anchor_x= 'center_x', #команды: left/right - якорь по оси Ox
            anchor_y= 'center_y', #команды: top/bottom - якорь по оси Oy
            child=self.v_box #добавляем аргумент v_box в параметр self.manager.add(arcade.gui.UIAnchorWidget)
        ))
        #----------------------------------------
        #Создание кнопки старта - команда кнопки -> UIFlatButton
        self.start_botton = arcade.gui.UIFlatButton(text="Start Game", widht=300)
        #....with_space_around(bottom = 20) -> нужен для того,чтобы были отступы между кнопок
        self.v_box.add(self.start_botton.with_space_around(bottom=20)) #Добавляем эту кнопку в v_box
        self.start_botton.on_click = self.on_click_start
        #----------------------------------------
        #Создание кнопки выхода
        self.exit_menu = arcade.gui.UIFlatButton(text="Exit",widht=200)
        self.v_box.add(self.exit_menu.with_space_around(bottom=20))
        '''Создаем проверку на клика -> создать свой метод on_click_exit  | on_click -> такая команда!'''
        self.exit_menu.on_click = self.on_click_exit
        #---------------------------------
        #Создание игровой доски - доски почёта:)
        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        self.text_area = arcade.gui.UITextArea(text=text, x=50,y=200, width=200,height=300,text_color=(0,0,0,255))
        # Так как огромный текст, то мы размещаем в само окно manager
        self.manager.add(arcade.gui.UITexturePane(self.text_area.with_space_around(right=20),
                                                  tex=bg_tex, padding=(10, 10, 10, 10)))
        #padding -> команда, которая позволяет делать отступы внутри доски от текста

    #Создаем update для того, чтобы проверялось появление частиц и когда нужно затушить
    def on_update(self, delta_time: float):
        temp_list = self.burst_list.copy() #Копируем, чтобы изменить цвет
        #Изменяем цвет
        for burst in temp_list:
            if time.time() - burst.start_time > MAX_FADE_TIME:
                self.burst_list.remove(burst)

    def on_click_start(self,event):
        my_game = MyGame()
        my_game.setup()
        window.show_view(my_game)

    def on_click_exit(self,event): #обязательно нужно передать event - параметр,отвечающий за отклик
        arcade.close_window()
        print("Вы вышли из игры")

    def on_draw(self):
        self.clear()
        self.manager.draw()
        #Все про частицы
        self.window.ctx.point_size = 2*self.window.get_pixel_ratio() # РАзмер частицы
        for burst in self.burst_list: #Все взрывы из списка взрывов - пустой
            #отрисовать
            self.program['time'] = time.time() - burst.start_time

            burst.vao.render(self.program, mode = self.window.ctx.POINTS)

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


#Создание игровой паузы при помощи модуля GUI
class PauseMenu(arcade.View):
    def __init__(self,my_game):
        super().__init__()
        #Переносим данные класса MyGame здесь
        self.my_game = my_game
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        '''Создаем менеджера'''
        self.manager2 = arcade.gui.UIManager()  # вызывали менеджера
        self.manager2.enable()  # Включили менеджера
        '''Создание бокса(вертикального)'''
        self.v_box2 = arcade.gui.UIBoxLayout()  # Удобен для того, чтобы перемещать кнопки (старта и тд) туда куда захочешь
        self.manager2.add(arcade.gui.UIAnchorWidget(
            # align_x = 100 #включи и посмотри (просто делает отступ)
            anchor_x='center_x',  # команды: left/right - якорь по оси Ox
            anchor_y='center_y',  # команды: top/bottom - якорь по оси Oy
            child=self.v_box2  # добавляем аргумент v_box в параметр self.manager.add(arcade.gui.UIAnchorWidget)
        ))
        '''Создаем текст'''
        self.ui_text = arcade.gui.UITextArea(text="Pause", width=300,height=50,font_size=20,font_name="Kenney Future")
        self.ui_text1 = arcade.gui.UITextArea(text="Нажми ESCAPE, чтобы вернутся в игру", width=600,height=200,font_size=20,font_name="Kenney Future")
        self.v_box2.add(self.ui_text.with_space_around(bottom=20,left=180))
        self.v_box2.add(self.ui_text1.with_space_around(bottom=20, left=180))
    def on_draw(self):
        self.clear()
        self.manager2.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            window.show_view(self.my_game) #Вызываем самого себя

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        '''Создаем переменные частиц'''
        self.burst_list = []  # Пустой список взрывов             было: vertex_shader_v1.glsl
        self.program = self.window.ctx.load_program(vertex_shader='new_color_new_vertex_shader.glsl',
                                                    fragment_shader='fragment_shader.glsl')
        self.window.ctx.enable_only()  # Включаем его, ctx - объект window

    def setup(self):
        '''Создаём очки при помощи времени'''
        self.score = 0
        self.manager1 = arcade.gui.UIManager()
        self.manager1.enable()
        self.v_box1 = arcade.gui.UIBoxLayout()
        self.manager1.add(arcade.gui.UIAnchorWidget(
            anchor_x='left',
            anchor_y='top',
            child=self.v_box1
        ))
        self.ui_text1 = arcade.gui.UITextArea(text=f"Score: {int(self.score)}", width=300,height=50,font_size=30, font_name="Kenney Blocks")
        self.v_box1.add(self.ui_text1.with_space_around(bottom=60,left=60))
        #---------------------------------------------------------
        '''Начало игры'''
        self.isGame = True #Если игра продолжается
        self.player = Penguin()
        self.columns_list = arcade.SpriteList()
        self.speed_change_x = 2 #Добавили переменную для изменение скорости колонн
        for i in range(3):
            column_top = ColumnTop('Resource/column_top.png',scale=2)
            column_top.center_x = 350 * i  + WIDHT #Частота появлений колон
            column_top.center_y = random.randint(600,750)
            column_top.change_x = self.speed_change_x #Двигаем колонну с изменением переменным
            self.columns_list.append(column_top)
        #------------------------------------------------------
            column_down = ColumnDown('Resource/column_bottom.png', scale=2)
            column_down.center_x = 350 * i + WIDHT
            column_down.center_y = random.randint(0, 150)
            column_down.change_x = self.speed_change_x #Двигаем колонну с изменением переменным
            self.columns_list.append(column_down)

        self.sound1 = arcade.load_sound('Resource/Aloe_Blacc_-_I_Need_A_Dollar_47925532.mp3')

    def on_show_view(self):
        self.background = arcade.load_texture('Resource/space.png')

    def on_draw(self):
        self.clear()
        #Создаем задний фон
        arcade.draw_lrwh_rectangle_textured(0,0,WIDHT,HEIGHT,self.background)
        self.player.draw()
        self.columns_list.draw()
        '''Вызываем менеджера'''
        self.manager1.draw()
        '''Все про частицы'''
        self.window.ctx.point_size = 2*self.window.get_pixel_ratio() # РАзмер частицы
        for burst in self.burst_list: #Все взрывы из списка взрывов - пустой
            #отрисовать
            self.program['time'] = time.time() - burst.start_time

            burst.vao.render(self.program, mode = self.window.ctx.POINTS)

    # Для смена костюмов(каритнок - анимация)
    def update(self, delta_time: float): #изменение картиник за 60 сек  это много
        if self.isGame:
            '''счетчик'''
            self.score += 0.01 # 0.01 - так как за 60 сек меняется
            #print(int(self.score))
            self.player.update_animation() # update_animation() - запускаем его, которого раннее переопределяли
            self.player.update()
            self.columns_list.update()
            #Создаем колизию соприкосновения
            hit = arcade.check_for_collision_with_list(self.player,self.columns_list)
            if hit :
                self.isGame = False #Игра остановится
                self.sound_player1 = arcade.play_sound(self.sound1, volume=0.1) #Пасхалочка
            self.speed_change_x +=0.01
            for i in self.columns_list:
                i.change_x = self.speed_change_x
            '''Счётчик'''
            self.ui_text1.text = f"Score: {int(self.score)}"
                        #...text =  -> такая команда
        '''Все про частицы'''
        temp_list = self.burst_list.copy() #Копируем, чтобы изменить цвет
        #Изменяем цвет
        for burst in temp_list:
            if time.time() - burst.start_time > MAX_FADE_TIME:
                self.burst_list.remove(burst)

    #Создаем управление персонажа  - изменение по Y
    def on_key_press(self, symbol: int, modifiers: int):
        '''Создаем свой метод - генератор'''
        def _gen_initial_data(initial_x, initial_y):
            '''Цикл для того,чтобы появлялись частицы'''
            for i in range(PARTICLE_COUNT):
                if symbol == arcade.key.SPACE:
                    self.player.change_y = 5
                    self.player.change_angle = 5
                    # задаем рандомный угол
                    angle = random.uniform(0, 2 * math.pi)  # uniform - команда такая
                    speed = random.uniform(0.0, 0.3)
                    # задаем рандомную скоростьи при помощи тригон.функ - делаем окрудность (типо салют)
                    dx = math.sin(angle) * speed
                    dy = math.cos(angle) * speed
                    # Задаем цвет
                    red = random.uniform(0, 1)
                    green = random.uniform(0, 1)
                    blue = random.uniform(0, 1)
                    fade_rate = random.uniform(1 / MAX_FADE_TIME, 1 / MIN_FATE_TIME)
                    # --------------Возвращаем----------------------------------------------
                    yield initial_x
                    yield initial_y
                    yield dx
                    yield dy
                    yield red
                    yield green
                    yield blue
                    yield fade_rate

        x2 = symbol / self.window.width * 2 - 1  # нормализуем значение (от -1 до 1)  - это лучше для нашей видеокарты
        y2 = symbol / self.window.height * 2 - 1  # нормализуем значение (от -1 до 1)  - это лучше для нашей видеокарты
        # 600 /1024 * 2 - 1 Ответ = -0.7
        initial_data = _gen_initial_data(x2, y2)
        buffer = self.window.ctx.buffer(data=array('f', initial_data))
        buffer_description = arcade.gl.BufferDescription(buffer, '2f 2f 3f f', ['in_pos', 'in_vel', 'in_color',
                                                                                'in_fade_rate'])  # Описание координат, 'in_vel' - скорость частиц
        vao = self.window.ctx.geometry([buffer_description])  # геометрия
        burst = Burst(buffer, vao, start_time=time.time())  #
        self.burst_list.append(burst)

        if symbol == arcade.key.ESCAPE:
            pause_menu = PauseMenu(self) #self -> самого себя вызываем
            window.show_view(pause_menu)

class Penguin(arcade.Sprite):
    def __init__(self):
        super().__init__(scale=1)
        #Начальное расположение
        self.center_x = 100
        self.center_y = 500
        #Анимация пингвина (всего 3 штуки)
        for i in range(1,4): # 1 2 3 картинки
            self.textures.append(arcade.load_texture(f"Resource/penguin{i}.png"))
        self.cur_texture = 0 #Созданный счетчик, чтобы менять каритнки от 1 до 3
        #присваиваем переменную texture от переменной textures
        self.texture = self.textures[int(self.cur_texture)]
        #Изменений параметров движение-----------------------------------------------------
        self.change_y = 0 #Чтобы персонаж изменял свое положение по Y
        self.change_angle = 0 #Чтоюы перс крутился
    #Для смена костюмов(каритнок - анимация) - будем переопределять update_animation
    def update_animation(self, delta_time: float = 1 / 60):
        self.cur_texture += 0.05
        # если индекс картинок больше 3, то обнуляется и начинается заного, так и происходит анимация
        if self.cur_texture > 3 :
            self.cur_texture = 0
        self.texture = self.textures[int(self.cur_texture)]

    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.4 #Что-то типо с гравитацией
        self.angle += self.change_angle
        self.change_angle -= 0.4 #Изменяет угла персонажа

        #Условие, чтобы перс не уходил за край карты -----------------
        if self.center_y < 0:
            self.center_y =  0
        if self.center_y > HEIGHT:
            self.center_y = HEIGHT
        #Условие, чтобы перс неслишком сильно крутился
        if self.angle >= 40:
            self.angle = 40
        if self.angle <= -30:
            self.angle = -30

class ColumnTop(arcade.Sprite):#Врехняя колонна
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0 - self.width/2:
            self.center_x = 50 + WIDHT
            self.center_y = random.randint(600,750)

class ColumnDown(arcade.Sprite):#Нижняя колонна
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0 - self.width/2:
            self.center_x = 50 + WIDHT
            self.center_y = random.randint(0,150)

window = arcade.Window(WIDHT,HEIGHT) #Создали окно
main_menu = MainMenu() # Создаем объект класса MainMenu
window.show_view(main_menu) # Присваиваем созданный объект window к созданному объекту main_menu
arcade.run() #запускаем в работу цикл on_draw()
