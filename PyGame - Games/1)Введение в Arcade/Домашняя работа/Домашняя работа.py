'''
№1
Создать графическое приложение и отрисовать там снеговика.
'''
import arcade

SCREEN_HEIGHT = 600
SCREEN_WIGHT = 480
SCREEN_TITLE = 'Моя первая игра'

class GA(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_HEIGHT,SCREEN_WIGHT,SCREEN_TITLE,fullscreen=False,resizable=True)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
    def on_draw(self):
        self.clear()
        arcade.draw_rectangle_filled(500, 100, 1000, 200, arcade.color.WHITE)
        arcade.draw_circle_filled(600,480,100,arcade.color.GOLD)
        self.snegovik()
    def snegovik(self):
        for y in range(0,150,50):
            for z in range(30,60,10):
                arcade.draw_circle_filled(150,150+y,z-15,arcade.color.WHITE)
                arcade.draw_circle_outline(150,150+y,z-15,arcade.color.BLACK,2)
        arcade.draw_line(200,100,200,240,arcade.color.BROWN,2)
        arcade.draw_circle_filled(200,240,10,arcade.color.RED)
        arcade.draw_circle_filled(170,260,3,arcade.color.BLACK)
        arcade.draw_circle_filled(160, 260, 3, arcade.color.BLACK)
        arcade.draw_arc_outline(165, 245, 20, 2,arcade.color.BLACK, 180, 360, 10)  # Рисует дугу

def main():
    window = GA()
    window.run()

if __name__== "__main__":
    main()

'''
№2
Создать графическое приложение размерами 600 на 480. Указать заголовок "Моя первая игра". Установить желтый цвет фона.
'''
import arcade

SCREEN_HEIGHT = 600
SCREEN_WIGHT = 480
SCREEN_TITLE = 'Моя первая игра'

class GA(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_HEIGHT,SCREEN_WIGHT,SCREEN_TITLE,fullscreen=False,resizable=True)
        arcade.set_background_color(arcade.color.YELLOW)

    def on_draw(self):
        self.clear()

def main():
    window = GA()
    window.run()

if __name__== "__main__":
    main()