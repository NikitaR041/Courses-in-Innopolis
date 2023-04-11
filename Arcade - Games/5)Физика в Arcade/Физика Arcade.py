'''
    Этот раздел будет посвящен продвинутой физики arcade (сила ветра, трения, прыжка и т.п)
    Теперь можно управлять чел-а без изменения его координат!

    При загрузке обычной карты из load_tilemap('путь к карте в формате json') создается специальный список sprite_list в нём есть специальные объекты, которые нужно прописывать в коде, чтобы их отрисовать
'''
import arcade

# размеры экрана
SCREEN_WIDTH = 1300
SCRENN_HEIGHT = 800

# размеры спрайтов
SPRITE_IMAGE_SIZE = 128
SPRITE_SCALING_PLAYER = 0.4 # задается размер персонажа
SPRITE_SCALING_TILES = 0.4 #по идеи тоже рамер только для карты но он не меняется
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

# переменные для физики
GRAVITY = 1500
PLAYER_MOVE_FORCE_ON_GROUND = 10000 # сила с которой мы воздействуем на персонажа когда говорим иди влево или вправо
DEFAULT_DAMPING = 0.4  # затухание от 0 до 1
PLAYER_FRICTION = 1.0   # сила трения  от 0 до 1
WALL_FRICTION = 0.7 #Сцепляемость с землей(и не только)!
DYN_ITEM_FRICTION = 0.6
PLAYER_MASS = 2.0 #Масса игрока
PL_MAX_HOR_SPEED = 500 #сила воздействия горизонтально
PL_MAX_VER_SPEED = 1600 #сила воздействия вертикальнов

#СДЕЛАЛИ ЧТОБЫ, ЕСЛИ ПЕРС ПОВЕРНУЛСЯ ВПРАВО ИЛИ ВЛЕВО, ТО АНИМАЦИИЯ БЫЛА СООТВЕСТВУЮЩЕЙ!
RIGHT = 0
LEFT = 1
DISTANCE = 20 # сколько шагов надо пройти чтобы поменяьт картинку ходьбы

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCRENN_HEIGHT)
        arcade.set_background_color(arcade.color.AMAZON)
        # переменные для управления игроком (влево, вправо, прыжок)
        self.left_pressed = False
        self.right_pressed = False
        self.top_pressed = False
        #Создание ВРАГА - дз
        self.enemy = None
        self.scene = None #Для этого создадим сцену с колизией
        #Взаимодействие с монеткой(флагом) свое решение
        self.bonus = None

    def setup(self):
        self.enemy = Enemy()
        self.bonus = Bonus()
        self.scene = arcade.Scene()  # Создали сцену -> присвоили ей род.класс
        self.scene.add_sprite_list("Enemy")
        self.scene.add_sprite_list("Bonus")
        self.scene.add_sprite("Enemy", self.enemy)
        self.scene.add_sprite("Bonus",self.bonus)

        tile_map = arcade.load_tilemap(':resources:/tiled_maps/pymunk_test_map.json',SPRITE_SCALING_TILES) # подгружаем карту
        for i in tile_map.sprite_lists:  # sprite_lists - специальный список который содержит объекты
            print(i) # Здесь помжно увидеть специальные объекты
        self.wall_list = tile_map.sprite_lists["Platforms"] #Такие юыли объекты в самой карте json
        self.item_list = tile_map.sprite_lists["Dynamic Items"] #Такие юыли объекты в самой карте json
        self.player = Player()
        gravity = (0,-GRAVITY) #Воздействия вертикального (Оу)
        '''усовершенствованный движок, который полностью подстроен для персонажа'''
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=DEFAULT_DAMPING, gravity=gravity) #здесь его создаем
        '''Здесь добавляем спрайт к персонажу'''
        self.physics_engine.add_sprite(self.player, friction=PLAYER_FRICTION, mass=PLAYER_MASS,
                                     moment = arcade.PymunkPhysicsEngine.MOMENT_INF, collision_type="player",
                                       max_horizontal_velocity=PL_MAX_HOR_SPEED,
                                       max_vertical_velocity=PL_MAX_VER_SPEED)
        self.physics_engine.add_sprite_list(self.wall_list, friction=WALL_FRICTION,collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)
        #добавили второго врага с учителем
        enemy_sprite2 = ":resources:images/animated_characters/zombie/zombie_idle.png"
        self.enemy2 = arcade.Sprite(enemy_sprite2, 0.4)
        self.enemy2.center_x = 600
        self.enemy2.center_y = 200

    def on_draw(self):
        self.clear()
        self.wall_list.draw() #загружаем их
        self.item_list.draw() #загружаем их
        self.player.draw() #загружаем игрока
        self.scene.draw() #сам
        self.enemy2.draw() #с учителем

    '''Создаем управление'''
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A: # влево
            self.left_pressed = True
        if symbol == arcade.key.D: # вправо
            self.right_pressed = True
        if symbol == arcade.key.W:
            self.top_pressed = True
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A: # влево
            self.left_pressed = False
        if symbol == arcade.key.D: # вправо
            self.right_pressed = False
        if symbol == arcade.key.W:
            self.top_pressed = False

    def on_update(self, delta_time: float):
        '''Изменяем управление - так более правильней и грамотней'''
        if self.left_pressed and not self.right_pressed:  # если идем влево
            force = (-PLAYER_MOVE_FORCE_ON_GROUND, 0)  # (Горизонт.сила и вертикал. сила)
            '''apply_force применяем эту силу на игрока, какую силу - force'''
            self.physics_engine.apply_force(self.player, force)  # применяем силу чтобы ходить
            self.physics_engine.set_friction(self.player, 0)  # отключаем силу трения
        elif self.right_pressed and not self.left_pressed:  # если идем влево
            force = (PLAYER_MOVE_FORCE_ON_GROUND, 0)  # (Горизонт.сила и вертикал. сила)
            '''apply_force применяем эту силу на игрока, какую силу - force'''
            self.physics_engine.apply_force(self.player, force)  # применяем силу чтобы ходить
            self.physics_engine.set_friction(self.player, 0)  # отключаем силу трения
            '''Специальная функция is_on_ground -> зелмя для игрока'''
        elif self.top_pressed and self.physics_engine.is_on_ground(self.player):
            force = (0,50000)
            self.physics_engine.apply_force(self.player,force)
        else:
            self.physics_engine.set_friction(self.player, PLAYER_FRICTION)  # сила трения
        '''Спецаильно включаем эту физ.движок'''
        self.physics_engine.step()  # используем физ движок
        #свое
        if arcade.check_for_collision(self.player,self.enemy):
            self.player.kill()
            arcade.close_window()
            print("Будь акуратнее")
        #свое
        if arcade.check_for_collision(self.player,self.bonus):
            self.bonus.kill()

        #С учителем
        items_hit = arcade.check_for_collision_with_list(self.player,self.item_list)
        for i in items_hit:
            i.kill()
        #С учителем
        if arcade.check_for_collision(self.player,self.enemy2):
            arcade.close_window()
            print('Будь аккуратнее')

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 100
        self.center_y = 100
        self.scale = SPRITE_SCALING_PLAYER
        '''load_texture_pair - специальная функция, которая из одной картинки создает две (обычную и отзеркаленную)'''
        self.idle_texture = arcade.load_texture_pair(f":resources:images/animated_characters/female_person/femalePerson_idle.png")
        self.jump_texture = arcade.load_texture_pair(f":resources:images/animated_characters/female_person/femalePerson_jump.png")
        self.fall_texture = arcade.load_texture_pair(f":resources:images/animated_characters/female_person/femalePerson_fall.png")
        self.walk_textures = []
        for  i in range(8): #зависит от того сколько у тебя картинок для изменений есть
            texture = arcade.load_texture_pair(f":resources:images/animated_characters/female_person/femalePerson_walk{i}.png")
            self.walk_textures.append(texture)

        self.texture = self.idle_texture[0] #берем первый элемент
        self.character_face_dir = RIGHT #типо лицо направлено вправо(поумолчанию)
        self.cur_texture = 0 #Счетсик изменений картинок
        self.x_odometer = 0 #здесь мы будем считать сколько шагов мы прошли

        '''Создадим функцию, которая будет соблюдать зависимость хотьбы с ею анимацией(тоесть если чел бегает, то анимация должна соблюдаттся)'''
    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        is_on_ground = physics_engine.is_on_ground(self) # стоим ли мы на земле
        if dx > 0:
            self.character_face_dir = RIGHT
        elif dx < 0:
            self.character_face_dir = LEFT
        if not is_on_ground: #  если мы не на земле
            if dy > 0: # если прыжок
                self.texture = self.jump_texture[self.character_face_dir]
                return
            elif dy < 0: # если падение
                self.texture = self.fall_texture[self.character_face_dir]
                return

        self.x_odometer += dx # сколько прошли
        if abs(dx) <= 0: # если мы ничего не прошли
            self.texture = self.idle_texture[self.character_face_dir]
        if abs(self.x_odometer) > DISTANCE:
            self.x_odometer = 0
            self.cur_texture += 1
            if self.cur_texture > 7:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture][self.character_face_dir]

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/animated_characters/zombie/zombie_idle.png',scale = 0.5)
        self.center_x = 1000
        self.center_y = 80

class Bonus(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/items/flagGreen2.png',scale = 1)
        self.center_x = 300
        self.center_y = 80

window = MyGame()
window.setup()
arcade.run()

