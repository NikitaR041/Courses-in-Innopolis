'''
    Введение: будем изучать сначала Arcade, а затем PyGame; говорят, что работать с Arcade лучше, чем с PyGame
    Для Arcade нужен python 3.6 и выше!, лучше пользоваться новым версием, а не старым

    1)Важные переменные, которые мы не будем менять -> следует писать большими буквами!
    2)Запуск окна работает только при помощи специального цикла -> run!
    3)Чтобы рисовать различные фигуры, то закиыдваем из в def on_draw(self), их нужно прописывать после self.clear!!!
    4)Для того, чтобы создавать какие-нибудь фигуры(дома, машины), то их лучше создать в отдельные методы, так как по правилу  программировании должно быть без трудов

    RGB (0.0.0) - черный -> можно задавать кортежем!
    1) 0 ... 255 красный
    2) 0 ... 255 зеленый
    3) 0 ... 255 синий

    Если нужно, то можешь вставить в метод def on_draw(self) -> обязательно после функции clear
        arcade.draw_circle_filled(300, 300, 200, arcade.color.GOLD)  # рисует кружочек
        arcade.draw_circle_outline(300, 300, 200, arcade.color.RED, 15) #Рисует только контур, 4 параметр толщина
        arcade.draw_arc_outline(350,200,150,80,(100,0,0),180,360,10) # Рисует дугу
                            #   х,  y   шир выс  цвет     угл1 угл2 толщина
        arcade.draw_parabola_outline(20,20,40,50,(10,0,0),10,10) #рисует параболу

    Если нужно, то можешь вставить в метод def on_draw(self) -> обязательно после функции clear
            #рисуем пейзажик
        arcade.draw_rectangle_filled(500,100,1000,200,(0,255,50)) #Рисует землю
        #Ниже вызываем методы, которые будут рисовать домики, птички
        self.house(100,100)
        self.house(550,130)
        self.bird(400,500)
    def house(self,x,y):
        arcade.draw_rectangle_filled(x,y,100,80,arcade.color.CORN)#стена
        arcade.draw_rectangle_filled(x,y,30,30,arcade.color.LIGHT_BLUE)#окно
        arcade.draw_triangle_filled(x1=x,y1=y+80,x2=x-50,y2=y+40,x3=x+50,y3=y+40,color=arcade.color.RED_BROWN)#крыша
    def bird(selfx,x,y):
        arcade.draw_arc_outline(x,y,20,20,arcade.color.BLACK,0,90)#левое крыло
        arcade.draw_arc_outline(x+20,y,20,20,arcade.color.BLACK,90,180)#Права крыло

'''
import arcade #Вызов модуля
from random import randint

SCREEN_WIGHT = 1000 #Ширина
SCREEN_HEIGHT = 650 #высота
SCREEN_TITLE = 'Заголовок окна'

#Чтобы создать окно -> создаем класс!
#Класс - чертёж
class MyGame(arcade.Window): #наследуемся класса ОКНА(window),наследуемся от главного класса окна в библ Arcade
    def __init__(self): #вызов __init__ родителя, чтобы переопределить ширину,высоту и заголовок (внутри __INIT__ уже поумолчанию что-то стоит)
        super().__init__(SCREEN_WIGHT,SCREEN_HEIGHT,SCREEN_TITLE,fullscreen=False, resizable=True) #4пар - фул скрин, 5пар - позволяет изменять окно в реал времени
        arcade.set_background_color(arcade.color.AQUA) #установить фоновый цвет
    def on_draw(self): # Специальный метод -> метод, который сам обновляет частоту экрана.
        '''здесь все прописывается, как человек ходит, как ездит машина и т.д.'''
        '''Так как этот метод, который постоянно меняет картинки(частоту обновлений экрана),а нужно чтобы один раз, то создаем в самом __init__
            или создаем новый метод (так мы и сделали назвали метод def setup(self))'''
        self.clear() # стирает все с экрана и остовляет только примененный раннее цвет фона
##        arcade.draw_arc_filled(center_x=400,center_y=300,width=155,height=155,color=(0, 0, 0),start_angle=0,end_angle=160,tilt_angle=0,num_segments=10)
##        arcade.draw_circle_outline(center_x=400,center_y=300,radius=100,color=(0, 0, 0),tilt_angle=0,num_segments=-1,border_width=2)
    '''Ниже это наш МЕТОД!!!'''
    def setup(self): #Её нужно вызвать в def main()
        '''Здесь в будущем будут применятся параметры персонажа (патроны и т.д)'''
        print('Начало игры')

##    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
##        print('произошел клик')
##        self.set_size(randint(500,1000),randint(300,800))#размер окна
##        self.set_caption('Новый заголовок после клика')
##        self.background_color = (0,100,200)
##        self.set_location(randint(0,1000),randint(0,1000)) #Двигаем окошко в другую часть экрана
def main():
    window = MyGame() #Создаём объект класса!
    window.setup()
    arcade.run() #специальный цикл, который ежесекундно обновляет частоту экрана (вспонмите понятие ФПС), без неё окно просто свернется ч/з сек
    '''Чтобы попасть в цикл run -> создаём новый метод в классе (назовём def on_draw(self))'''

#Запуск функции main - так правильней, так профиссиональней!
if __name__ == "__main__":
    main()

