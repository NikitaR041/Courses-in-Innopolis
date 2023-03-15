'''
Попытаемся сделать столкновение объектов, перемещение объектов, космический корабль и т.д.
'''
#Пример, как выглядит основа:
'''
import arcade

WIDTH = 800
HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT)
        self.background_color= (0,100,150)
    def on_draw(self):
        self.clear()
    def setup(self):
        pass
    def update(self, delta_time: float):
        pass
        
def main():
    window = MyGame()
    window.run()
    window.setup()

main()
'''

import arcade
WIDTH = 800
HEIGHT = 600
GRAVITY = 0.8 #физика -> переменная, коготорая взаимодействуюет с притяжением
PLAYER_MOVEMENT_SPEED = 5
JUMP = 15

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT)
        self.background_color = (0,100,150)
        #Игрок
        self.player = None
        #Зелмя
        self.ground = None
        self.ground_list = None
        #Коробки
        self.box = None
        self.box_list = None
        self.box_list_coords = [[512,96],[256,300],[768,200]]
        '''Создали сцену, где помещняем наши объекты внутрь сцены(коробка,земля,персонажа)'''
        self.scene = None #Нужен для того, чтобы персонаж взаимодействовал с окружающим миром(не проваливался, не проходил сквозь объектов)
        self.physics_engine = None #Создали перемену физики, как и сцену
        '''Создали камеру, которая будет следить за персонажем'''
        self.camera = None
        '''Cоздали врага, при соприкосновении с ним что-то случалось с персонажем'''
        self.enemy = None
        '''Создали выход игрока'''
        self.exit_player = None

    def setup(self):
        self.player = Player()
        '''Присваиваем камеру к Функции Camera'''
        self.camera = arcade.Camera(self.width,self.height) #Параметры: 1) Ширина 2) Высота

        '''Создадим врага (без класса)'''
        self.enemy = arcade.Sprite(':resources:images/animated_characters/zombie/zombie_idle.png',scale=1)
        self.enemy.center_x = 600
        self.enemy.center_y = 150

        '''Создали выход игрока'''
        self.exit_player = arcade.Sprite(":resources:images/tiles/signExit.png",1)
        self.exit_player.center_x = 300
        self.exit_player.center_y = 200

        self.ground_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        '''Создаем СЦЕНУ'''
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player") # сцена 1 -> персонаж
        self.scene.add_sprite_list("Walls") # сюда поместим землю и ящики сцена 2 -> создаем стены
        '''Присваиваем кому что нужно'''
        self.scene.add_sprite("Player",self.player) #Присваиваем сцене персонажа, предварительно назвав сцену 'Pleyer'
        '''Присваиваем врага к сцене'''
        self.scene.add_sprite('Enemy',self.enemy)
        '''Присваиваем выход к сцене'''
        self.scene.add_sprite("Exit", self.exit_player)

        '''Создаем площадку-землю'''
        for i in range(0,800,128):
            self.ground = arcade.Sprite(':resources:images/tiles/grassMid.png',scale=1) # создаем землю
            self.ground.center_x = i
            self.ground.center_y = 32
            self.ground_list.append(self.ground) # добавляем землю в список
            '''Присваиваем кому что нужно'''
            self.scene.add_sprite("Walls", self.ground) #Присваиваем сцене стену, предварительно назвав сцену 'Walls',чтобы было взаимодействие с землей

        '''Создаем коробки'''
        for i in self.box_list_coords:
            self.box = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",scale=1)
            self.box.position = i
            self.box_list.append(self.box)
            '''Присваиваем кому что нужно'''
            self.scene.add_sprite("Walls", self.box) #Присваиваем сцене коробки, предварительно назвав сцену 'Walls'

        '''Создаем переменную, где присваиваем ей функцию физики(улучшенную)'''
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=GRAVITY,walls=self.scene["Walls"])
                                    #Параметры: 1)Присваиваем игрока 2)Подключаем гравитацию 3) Даем ей 'стены'(коробки и землю)
    def on_draw(self):
        self.clear()
        #Вызываем сцену, чтобы сцена всех вызвала(коробки, врага,персонажа и тд)
        self.scene.draw()
        #Вызываем здесь камеру!
        self.camera.use()

    '''Обязательно нужно создать функцию камеры-создали свой метод(такого нет по умолчанию)'''
    def center_camera_to_player(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width/2)
        screen_center_y = self.player.center_y - (self.camera.viewport_height/2)
        '''Условие, чтобы камера не следила за персонажем, если он провалится вниз'''
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        self.camera.move_to((screen_center_x,screen_center_y)) #Слежка за персонажем

    def update(self, delta_time: float):
        self.physics_engine.update() #Вызываем саму функцию физики
        self.center_camera_to_player() #Вызываем саму камеру
        '''Прописываем условие, если есть соприкосновение с каким-то объектом'''
        if arcade.check_for_collision(self.player, self.enemy):
            self.player.kill()
            arcade.close_window()
            print('Вы проиграли!')
        '''Прописываем условие, если есть соприкосновение с каким-то объектом, то выводим выход персонажа'''
        if arcade.check_for_collision(self.player, self.exit_player):
            arcade.close_window()
            print('Вы победили')

    '''Создаем механизм нажатия клавиш и отпускания клавиш'''
    def on_key_press(self, symbol: int, modifiers: int): # ловит нажатия клавиш
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED # изменение по оси X = 3
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED # изменение по оси X = -3
        elif symbol == arcade.key.UP or symbol == arcade.key.W:
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
        super().__init__(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png',scale=1)
        self.center_x = 122
        self.center_y = 400

def main():
    window = MyGame()
    window.setup()
    arcade.run()

main()
'''ДОПОЛНИТЕЛЬНАЯ ЗАДАЧА
Сделать выход игры, если мы соприкоснулись с врагом
'''