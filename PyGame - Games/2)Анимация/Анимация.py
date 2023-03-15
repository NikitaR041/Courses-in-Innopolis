'''
Научимся рисовать картинки, двигать картинки и загружать текстуры!

Параметры у фигурах:
    start_angle - начала точки рисования
    end_angle - конец точки рисования
    tilt_angle - задаем конкрентной фигуре угол наклона!

При создании каких либо фигур, можно приписывать название параметра и вводить ему аргумент, чтобы не запутаться!
    draw_cicrle_filled(color = (200,200,100), center_y=100,center_x=200,radius=50)
                    Параметр = аргумент     Параметр=аргумент П=А       П=Арг
    Арки (Параметры ), на самом деле это такая линия, которая рисует 'окружность', но это не совсем так, т.к.
    можно создавать ему аргументы, которые мы ограничиываем ему зону рисования
    start_angle - начала точки рисования, end_angle - конец точки рисования!
    tilt_angle - задаем конкрентной фигуре угол наклона!
    Нужно представить тригонометрическую 'окружность' (опять же не совсем окружность, так как мы можем и создать овал и т.п.)
    К примеру:
    arcade.draw_arc_outline(center_x = 500, center_y = 200, widht = 200, height = 100, color=(255,255,255), start_angle = 90,end_angle = 180)
    Элипсы
    arcade.draw_ellipse_filled(center_x = 500, center_y = 200, widht = 200, height = 100, color=(255,255,255), tilt_angle = 60, num_segments = -1)
    num_segments=-1 -> -1 задаем нулевое значение, то есть рисует просто значение
    ПО ФАКТУ: он задает количество точек(углов) (к примеру 10-угольник, 16-угольник и т.д)
    Ломаная линия: (принимает в себе список значений)
    arcade.draw_lrtb_rectangle_filled(left=100,right=500,top=300,bottom=100,color=(0,0,0))
                    точки:          левая       правая  верхняя  нижняя;    цвет
'''
# Пример №1
'''
import arcade
WIDHT = 1000
HEIGHT = 800
TITLE = 'Заголовок'

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDHT,HEIGHT,TITLE)
        self.background_color = (100,0,50)
        self.coords = [(random.randint(100,700),random.randint(100,700),random.randint(100,500),random.randint(100,300))]
    # def dod(self,x,y):
    #     arcade.draw_ellipse_filled(center_x= x,center_y=y,width=200,height=80,color=(0,100,150),tilt_angle=0)
    #     arcade.draw_ellipse_filled(center_x=x+30, center_y=y+40, width=150, height=80, color=(0, 100, 150), tilt_angle=20)
    #     arcade.draw_ellipse_filled(center_x=x+55, center_y=y+30, width=200, height=80, color=(0, 100, 150), tilt_angle=0)
    #     arcade.draw_ellipse_filled(center_x=x + 55, center_y=y + 30, width=200, height=80, color=(0, 100, 150),tilt_angle=0)
    def on_draw(self):
        self.clear() # очищаем картинку, тем самым происходит обновление экрана
        # #Рисуем тучку
        # for i in self.coords:
        #     self.dod(i[0],i[1])
        # # Рисуем круг
        # arcade.draw_circle_filled(color = (200,200,100), center_y=100,center_x=200,radius=50)
        # #Арки
        # arcade.draw_arc_outline(center_x=500, center_y=200, width=200, height=100, color=(255, 255, 255),
        #                         start_angle=90, end_angle=180)
        # #Элипсы
        # arcade.draw_ellipse_filled(center_x=500, center_y=200, width=200, height=100, color=(255, 255, 255),
        #                            tilt_angle=60, num_segments=-1)
        # #Рисуем ломаную линию
        # arcade.draw_line_strip(point_list=[(100,100),(400,300),(500,200),(600,300)], color=(0,0,0), line_width=10)
        #Рисуем специальный прямоугольник, где задаем координаты левую,правую,верхнюю,нижню границу
        # arcade.draw_lrtb_rectangle_filled(left=100,right=500,top=300,bottom=100,color=(0,0,0))

def main():
    window = MyGame()
    arcade.run()
main()
'''
#Задачки
'''
1)Нарисовать облачка (тучки и дождь)
2)Все вот это попробовать оптимизировать код - использовать циклы и функции 
'''

#Пример №2 - загружаем текстуры
'''
Чтобы загружать текстуры, нужно создать прямоугольник - область, в которой загружаем картинку
1)Найти на просторах интернета картинку png (важно, чтобы вы нашли картинку с фоном, где есть серо-белые квадратики)
2)В def __init__(self) - создаем переменную texture
3)В этой переменной нужно указать путь(названия файла) - при помощи горячей кнопки ctrl-пробел
4)В on_draw (частота обновления экрана) создаем функцию draw_texture_rectangle()
-------------------------
Для создания анимации картинки нужно создать метод update, который вызывается много раз в секунду, удобен для изменение кол-во патронов и тд

on_draw -> изменяет саму картинку!
update -> изменяет местоположение картинки(или что-то ещё)!
'''
import arcade

WIDHT = 1000
HEIGHT = 800
TITLE = 'Заголовок'

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDHT,HEIGHT,TITLE,resizable=True)
        self.background_color = (100,0,50)

        # self.texture = arcade.load_texture('Колбасевич.png')

        self.texture1= arcade.load_texture('МЫшь.png')

        self.x = 500 #Создали переменные x
        self.y = 400 #Создали переменные y
        self.x_change = 5 #Переменная, которая будет изменять в 5 сек
        self.y_change = 5 #Переменная, которая будет изменять в n сек/ если 0, то по этой оси движения нет

    def on_draw(self): #Изменяет картинку

        self.clear() # очищаем картинку, тем самым происходит обновление экрана

        # arcade.draw_texture_rectangle(center_x=200,center_y=400,height=200,width=300,texture=self.texture)
        arcade.draw_texture_rectangle(center_x=self.x,center_y=self.y,height=200,width=300,texture=self.texture1)
        # arcade.create_text('Вкусная колбаса')
        #Если нужно создать несколько текстур, то делаем всю процедуру также

    #Делаем анимацию картинки; для этого нужно применить метод update, который принимает тип float!!!!
    def update(self, delta_time: float): #метод, который вызывается много раз в секунду, т.е. это он не рисует, а изменяет параметр(кол-во патронов и т.д)

        self.x = self.x + self.x_change #Постоянно изменяем координату x
        self.y = self.y + self.y_change #Постоянно изменяем координату y

        # # Две последующие условия, они не учитвают, то что картинка часть своей картинки поглощается несущестующим экраном (раскоментируй этот 1-2 блока условия и проверь)
        # '''Условие, чтобы мышь не уходила за край экрана (вправо или влево)'''
        # if self.x >= self.width: # self.widht - стоит по умолчанию в классе window #Если вышел за правый край экрана
        #     self.x_change = -self.x_change #Изменения экрана на противоположный
        # elif self.x < 0: #Если вышел за левый край экрана, тут не нужен self.width, так как все по умолчанию начинают с 0
        #     self.x_change = -self.x_change #Изменения экрана на противоположный
        #
        # '''Условие,чтоюы мышь не уходила за край экрана (вверх или вниз)'''
        # if self.y >= self.height:
        #     self.y_change = -self.y_change
        # elif self.y < 0:
        #     self.y_change = -self.y_change

        '''Для того, чтобы отскакивала от ширины или высоты картинки, нужно как раз следовать от того, каков размер этой картинки(имеется ввид-draw_texture_rectangle), раннее указаной вами'''
        if self.x >= self.width - 300//2: # 300 -> ширина картинки раннее указаной нужно её делить пополам и вычитать,т.к. елси шел вправо
            self.x_change = -self.x_change #
        elif self.x < 0 + 300//2: # плюсовать, т.к. если шел влево
            self.x_change = -self.x_change #

        if self.y >= self.height - 200//2: #200 -> высота картинки раннее указаной нужно её делить попалам и вычитать, т.к. если шел вверх
            self.y_change = -self.y_change
        elif self.y < 0 + 200//2: # Плюсовать,т.к. если шёл вниз
            self.y_change = -self.y_change


def main():
    window = MyGame()
    arcade.run()
main()
