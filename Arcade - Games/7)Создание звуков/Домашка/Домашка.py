'''
Добавить в игру из прошлого домашнего задания звуки. Звуки можно найти в стандартной библиотеке arcade, либо загрузить свои.
'''
import arcade, random
WIDHT = 800
HEIGHT = 800

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDHT,HEIGHT)
        self.background = arcade.load_texture('Resource/space.png')
    def setup(self):
        self.isGame = True #Если игра продолжается
        self.player = Penguin()
        self.columns_list = arcade.SpriteList()
        for i in range(3):
            column_top = ColumnTop('Resource/column_top.png',scale=2)
            column_top.center_x = 350 * i  + WIDHT #Частота появлений колон
            column_top.center_y = random.randint(600,750)
            column_top.change_x = 7 #Двигаем колонну со скоростью 4
            self.columns_list.append(column_top)
        self.columns_list_down = arcade.SpriteList()
        for i in range(3):
            column_down = ColumnDown('Resource/column_bottom.png',scale = 2)
            column_down.center_x = 350 * i + WIDHT
            column_down.center_y = random.randint(0,150)
            column_down.change_x = 7
            self.columns_list_down.append(column_down)

        self.sound1 = arcade.load_sound('Resource/Aloe_Blacc_-_I_Need_A_Dollar_47925532.mp3')
        self.sound = arcade.load_sound('Resource/lose.wav')
    def on_draw(self):
        self.clear()
        #Создаем задний фон
        arcade.draw_lrwh_rectangle_textured(0,0,WIDHT,HEIGHT,self.background)
        self.player.draw()
        self.columns_list.draw()
        self.columns_list_down.draw()

    # Для смена костюмов(каритнок - анимация)
    def update(self, delta_time: float):
        if self.isGame:
            self.player.update_animation() # update_animation() - запускаем его, которого раннее переопределяли
            self.player.update()
            self.columns_list.update()
            self.columns_list_down.update()
            #Создаем колизию соприкосновения
            hit = arcade.check_for_collision_with_list(self.player,self.columns_list,self.columns_list_down)
            hit1 = arcade.check_for_collision_with_list(self.player,self.columns_list_down)
            if hit or hit1:
                self.isGame = False #Игра остановится
                self.sound_player1 = arcade.play_sound(self.sound1, volume=0.1) #Пасхалочка



    #Создаем управление персонажа  - изменение по Y
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 5
            self.player.change_angle = 5

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


window = MyGame()
window.setup()
arcade.run()