'''
Реализовать в графическом окне анимацию персонажа при движении влево-вправо.
В состоянии покоя должен отображаться обычный спрайт, а при движении происходить смена спрайтов для анимации.
'''
WIDTH = 600
HEIGHT = 400
SPEED = 5
# PERSON_MOVEMENT_SPEED = 5
JUMP = 1
RIGHT = 0
LEFT = 1

'''Создаем анимацию персонажа, когда вправо когда влево'''
def load_texture_pair(filename):
    return [arcade.load_texture(filename), arcade.load_texture(filename,flipped_horizontally=True)]

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH,HEIGHT)
        self.physics_engine = None

    def setup(self):
        '''Рисуем задний фон'''
        self.bg_layer_1 = arcade.load_texture('resources/bg/background.png')
        self.bg_layer_2 = arcade.load_texture('resources/bg/middleground.png')
        '''Создаем землю'''
        self.ground_list = arcade.SpriteList() #Своеобразный список спрайтов
        for i in range(0,self.width,16):
            number = random.randint(1,2) #случайное число для выбора спрайта 1 или 2
            self.ground = arcade.Sprite(f'resources/enviroments/wall-{number}.png')
            self.ground.center_x = i
            self.ground.center_y = 6
            self.ground_list.append(self.ground) #Загружаем в список и загружаем в on_darw
        '''Создаем домики'''
        self.house_list = arcade.SpriteList()
        for i in range(0,3):
            self.house = arcade.Sprite(f"resources/enviroments/house-{i}.png")
            self.house.center_x = 80 + (i * 220) #Координаты спавна - насколько рядом будут стоять домики
            if i != 1:
                self.house.center_y = 100
            else:
                self.house.center_y = 130
            self.house_list.append(self.house)
        '''Создаем объект класса Person'''
        self.person = Person()
        self.person.center_x = 50
        self.person.bottom = self.ground_list[0].top #ноги персонажа будут ровно касаться поверхности земли
        '''Создаем физику'''
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.person, gravity_constant=1,walls=self.ground_list)

    def on_draw(self):
        self.clear()
        '''Прорисовываем задний фон'''
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.bg_layer_1)
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.bg_layer_2)
        self.ground_list.draw()
        self.house_list.draw()
        self.person.draw()

    def update(self, delta_time: float):
        '''Включаем физику'''
        self.physics_engine.update()
        '''Включаем анимацию'''
        self.person.update_animation()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.person.change_x = -SPEED
            self.person.idle = False  # МЫ ИДЕМ
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.person.change_x = SPEED
            self.person.idle = False  # МЫ ИДЕМ

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.person.change_x = 0
            self.person.idle = True  # МЫ СТОИМ
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.person.change_x = 0
            self.person.idle = True  # МЫ СТОИМ


class Person(arcade.Sprite):
    def __init__(self):
        super().__init__()
        '''Дополняет персонажа для анимации'''
        self.player_face_direction = RIGHT
        self.cur_texture = 0 #Счетчик
        self.scale = 1
        self.idle = True  # True - если мы стоим на месте
        # списки для хранения изображений стойки и ходьбы
        self.idle_textures = []
        self.run_textures = []
        # загрузим изображения стандартной стойки (5 штук)
        for i in range(1, 6):  # 1 2 3 4 5 - зависит сколько картинок у нас
            texture = load_texture_pair(f'resources/person/bearded-idle/bearded-idle-{i}.png')
            self.idle_textures.append(texture)
        # аналогично для ходьбы
        for i in range(1, 7):  # 1 2 3 4 5 6 - зависит сколько картинок у нас
            texture = load_texture_pair(f'resources/person/bearded-walk/bearded-walk-{i}.png')
            self.run_textures.append(texture)
        self.texture = self.idle_textures[0][0]  # стандартно персонаж стоит под первой картинкой и смотрит вправо
    '''Специальная функция для смены костюмов персонажа'''
    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0:  # если идем влево, выбираем картинки которые относятся к человеку смотрящему влево
            self.player_face_direction = LEFT
        if self.change_x > 0:  # если идем вправо, выбираем картинки которые относятся к человеку смотрящему вправо
            self.player_face_direction = RIGHT

        # Начинаем отрисовку(смену) костюмов
        if self.change_x == 0:  # если стоим на месте
            self.cur_texture += 0.1  # скорость смены картинок - счетчик - индекс картинки # 0 1 2 3 4
            if self.cur_texture >= 5:
                self.cur_texture = 0
            # выбираем текстуру
            self.texture = self.idle_textures[int(self.cur_texture)][self.player_face_direction]
        # Начинаем отрисовку(смену) костюмов  для ХОДЬБЫ
        if self.idle == False: # если мы ходим
            self.cur_texture += 0.1 # скорость смены картинок - счетчик - индекс картинки # 0 1 2 3 4
            if self.cur_texture >= 5:
                self.cur_texture = 0
            # выбираем текстуру
            self.texture = self.run_textures[int(self.cur_texture)][self.player_face_direction]


window = MyGame()
window.setup()
arcade.run()
