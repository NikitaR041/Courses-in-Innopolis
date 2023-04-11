'''
Отрисовать графическое окно. Добавить персонажа из стандартной библиотеки. Добавить в игру сторонние объекты и реализовать коллизию столкновения объектов.
'''
import arcade

WIDTH = 800
HEIGHT = 600
#Создаем движок
GRAVITY = 0.5
PLAYER_MOVEMENT_SPEED = 5
JUMP = 15

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT)
        self.background_color = (0, 100, 150)
        '''Создание объектов'''
        #Создали игрока
        self.player = None
        #Создали врага
        self.enemy = None
        #Создали площадку - без класса
        self.ground = None
        self.ground_list = None
        #---------------------------------

        "Создание задних процедур - бекендр"
        self.scene = None
        self.physics_engine = None
        self.camera = None


    def setup(self):
        self.player = Player()
        # self.player_list -> такого не делаем, так как мы будем закидывать только персонажа в сцену - создать сцену!
        self.enemy = Enemy()
        self.camera = arcade.Camera(self.width,self.height) #Параметры: 1) Ширина 2) Высота

       #Создали список картинок площадки - без класса
        self.ground_list = arcade.SpriteList()

        self.scene = arcade.Scene() #Создали сцену -> присвоили ей род.класс
        '''Добавляем объекты в scene! - add_sprite_list'''
        self.scene.add_sprite_list("Player")  # сцена 1 -> персонаж
        self.scene.add_sprite_list("Enemy")
        self.scene.add_sprite_list("Walls")  # сюда поместим землю и ящики сцена 2 -> создаем стены
        '''Присываиваем сцене объекты'''
        self.scene.add_sprite("Player",self.player)  # Присваиваем сцене персонажа, предварительно назвав сцену 'Player'
        self.scene.add_sprite("Enemy",self.enemy)

        '''Рисуем площадку через цикл'''
        for i in range(0,800,128):
            self.ground = arcade.Sprite(':resources:images/tiles/stoneMid.png',scale=1) # создаем землю
            self.ground.center_x = i
            self.ground.center_y = 32
            self.ground_list.append(self.ground)
            self.scene.add_sprite("Walls",self.ground)

        '''Создаем движок, где присваиваем ей функцию физики(улучшенную)'''
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=GRAVITY, walls=self.scene["Walls"])
    def on_draw(self):
        self.clear()
        # Вызываем сцену, чтобы сцена всех вызвала(коробки, врага,персонажа и тд)
        self.scene.draw()
        # Вызываем камеру
        self.camera.use()

    '''Обязательно нужно создать функцию камеры -> создали свой метод!'''
    def center_camera_to_player(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (self.camera.viewport_height / 2)
        '''Условие, чтобы камера не следила за персонажем, если он провалится вниз'''
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        self.camera.move_to((screen_center_x, screen_center_y))  # Слежка за персонажем

    '''Бекенд'''
    def update(self, delta_time: float):
        self.physics_engine.update() # Вызываем саму функцию физики
        self.center_camera_to_player() #Вызываем свою функцию
        '''Прописываем столкновение коллизий'''
        if arcade.check_for_collision(self.player,self.enemy):
            self.player.kill()
            arcade.close_window()
            print("Будь акуратнее")

    '''Создаем механизм нажатия клавиш и отпускания клавиш'''
    def on_key_press(self, symbol: int, modifiers: int): # ловит нажатия клавиш
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED # изменение по оси X = 3
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED # изменение по оси X = -3
        elif symbol == arcade.key.UP or symbol == arcade.key.W:
            #Применяется физика
            if self.physics_engine.can_jump():
                self.player.change_y = JUMP

    def on_key_release(self, symbol: int, modifiers: int): # ловит отпускания клавиш
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 0  # изменение по оси X = 0
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = 0  # изменение по оси X = 0
        elif symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.change_y = 0 # изменение по оси Y = 0

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png',scale= 1 )
        self.center_x = 122
        self.center_y = 400

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/animated_characters/zombie/zombie_idle.png',scale = 1)
        self.center_x = 600
        self.center_y = 160

#Не понятно почему если использовать этот класс, то не получается отрисовать площадку полностью
# class Ground(arcade.Sprite):
#     def __init__(self):
#         super().__init__(':resources:images/tiles/stoneMid.png',scale = 1)
#         for i in range(0,800,100):
#             self.center_x = i
#             self.center_y = 32

def main():
    window = MyGame()
    window.setup()
    window.run()

main()