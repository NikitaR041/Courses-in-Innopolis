'''
Реализовать платформер, где персонаж должен двигаться из точки А в точку Б перепрыгивая препятствия с помощью библиотеки Arcade.
Также реализовать победу и поражение.
'''
import arcade,random
import arcade.gui

WIDTH = 800
HEIGHT = 800

# размеры спрайтов
SPRITE_IMAGE_SIZE = 128
SPRITE_SCALING_PLAYER = 0.4 # задается размер персонажа
# SPRITE_SCALING_TILES = 0.4 - нужна если мы загружаем карту
# SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

# переменные для физики
GRAVITY = 1500
PLAYER_MOVE_FORCE_ON_GROUND = 10000 # сила с которой мы воздействуем на персонажа когда говорим иди влево или вправо
DEFAULT_DAMPING = 0.4  # затухание от 0 до 1
PLAYER_FRICTION = 1.0   # сила трения  от 0 до 1
WALL_FRICTION = 0.7 #Сцепляемость с землей(и не только)!
DYN_ITEM_FRICTION = 0.6
PLAYER_MASS = 2.0 #Масса игрока
PL_MAX_HOR_SPEED = 500 #сила воздействия горизонтально
PL_MAX_VER_SPEED = 1600 #сила воздействия вертикально

#СДЕЛАЛИ ЧТОБЫ, ЕСЛИ ПЕРС ПОВЕРНУЛСЯ ВПРАВО ИЛИ ВЛЕВО, ТО АНИМАЦИИЯ БЫЛА СООТВЕСТВУЮЩЕЙ!
RIGHT = 0
LEFT = 1
DISTANCE = 20 # сколько шагов надо пройти чтобы поменяьт картинку ходьбы


#Главное игровое меню
class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
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
        self.start_botton = arcade.gui.UIFlatButton(text="Start Game", width=200)
        #....with_space_around(bottom = 20) -> нужен для того,чтобы были отступы между кнопок
        self.v_box.add(self.start_botton.with_space_around(bottom=20)) #Добавляем эту кнопку в v_box
        self.start_botton.on_click = self.on_click_start
        #----------------------------------------
        #Создание кнопки выхода
        self.exit_menu = arcade.gui.UIFlatButton(text="Exit",width=200)
        self.v_box.add(self.exit_menu.with_space_around(bottom=20))
        '''Создаем проверку на клика -> создать свой метод on_click_exit  | on_click -> такая команда!'''
        self.exit_menu.on_click = self.on_click_exit

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
#Пауза-меню
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
        #Создание кнопки выхода
        self.exit_menu = arcade.gui.UIFlatButton(text="Exit", width=200)
        self.v_box2.add(self.exit_menu.with_space_around(bottom=20))
        '''Создаем проверку на клика -> создать свой метод on_click_exit  | on_click -> такая команда!'''
        self.exit_menu.on_click = self.on_click_exit

    def on_click_exit(self,event): #обязательно нужно передать event - параметр,отвечающий за отклик
        arcade.close_window()
        print("Вы вышли из игры")

    def on_draw(self):
        self.clear()
        self.manager2.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            window.show_view(self.my_game) #Вызываем самого себя

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        '''Создание сцены для того, чтобы были взаимодействия персонажа с "внешними миром"'''
        self.scene = None
        '''Создание физики-усовершентсованной'''
        self.physics_engine = None
        '''Переменные для управление игроком'''
        self.left_pressed = False
        self.right_pressed = False
        self.top_pressed = False

        '''Создали камеру, которая будет следить за персонажем'''
        self.camera = None

        '''Создание игрока'''
        self.player = None
        '''Создание плохиша:)'''
        self.zombie = None
        '''Создание Бонуса'''
        self.bonus = None
        '''Создание финиша'''
        self.finish = None

        '''Создание платформы'''
        self.ground = None
        self.ground_list = None
        '''Создание платформы 2'''
        self.platform = None
        self.platform_list = None
        self.platform_list_coords = [[640,150],[1000,300],[1360,150]]

    def setup(self):
        '''Создание игрока'''
        self.player = Player()
        '''Создание зомби'''
        self.zombie = Zombie()
        '''Создание бонуса'''
        self.bonus = Bonus()
        '''Создание финиша'''
        self.finish = Finish()

        '''Присваиваем камеру к Функции Camera'''
        self.camera = arcade.Camera() #Параметры: 1) Ширина 2) Высота

        '''Создаем сцену'''
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")#Добавляем игрока - называем list - Player
        self.scene.add_sprite_list("Walls")#Добавляем землю(платформа) - назвыаем list - Walls
        self.scene.add_sprite_list("Zombie")#Добавляем зомби - названием list - Zombie
        self.scene.add_sprite_list("Bonus")#Добавляем бонус - названием list - Bonus
        self.scene.add_sprite_list("Finish")#Добавляем финиш - названием list - Finish
        #Присваивание
        self.scene.add_sprite("Player", self.player)#Присваиваем list-Player к переменной player
        self.scene.add_sprite("Zombie",self.zombie)#Присваиваем list-Zombie к переменной zombie
        self.scene.add_sprite("Bonus",self.bonus)#Присваиваем list-Bonus к переменной bonus
        self.scene.add_sprite("Finish",self.finish)#Присваиваем list-Finish к переменной finish

        self.ground_list = arcade.SpriteList()
        '''Создаем площадку'''
        for i in range(0,2000,128):
            self.ground = arcade.Sprite(':resources:images/tiles/grassMid.png',scale=1)
            self.ground.center_x = i
            self.ground.center_y = 16
            self.ground_list.append(self.ground) #добавляем платформу в список ground_list
            self.scene.add_sprite("Walls",self.ground) #Присваиваем list-Walls к переменной ground

        self.platform_list = arcade.SpriteList()
        for i in self.platform_list_coords:
            self.platform = arcade.Sprite(':resources:images/tiles/planetHalf.png',scale=1)
            self.platform.position = i #position - такая команда, которая выискиывает кооринаты и пргружает
            self.platform_list.append(self.platform) #добавляем платформу в список platform_list
            self.scene.add_sprite("Walls",self.platform) #Присваиваем list-Walls к переменной platform

        #Подключаем физику построенную для персонажа!
        gravity = (0, -GRAVITY)  # Воздействия вертикального (Оу)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=DEFAULT_DAMPING, gravity=gravity) #здесь его создаем
        self.physics_engine.add_sprite(self.player, friction=PLAYER_FRICTION, mass=PLAYER_MASS,
                                     moment = arcade.PymunkPhysicsEngine.MOMENT_INF, collision_type="player",
                                       max_horizontal_velocity=PL_MAX_HOR_SPEED,
                                       max_vertical_velocity=PL_MAX_VER_SPEED)
        self.physics_engine.add_sprite_list(self.scene["Walls"], friction=WALL_FRICTION,collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)


    def on_show_view(self):
        #возможно надо исправить
        arcade.set_background_color((117, 187, 253))

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.player.draw()  # загружаем игрока
        self.zombie.draw() #загружаем врага
        self.camera.use() #Вызываем здесь камеру!

    '''Функция камеры (собственная функция)'''
    def center_camera_to_player(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width/2)
        screen_center_y = self.player.center_y - (self.camera.viewport_height/2)
        '''Условие, чтобы камера не следила за персонажем, если он провалится вниз'''
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        self.camera.move_to((screen_center_x,screen_center_y)) #Слежка за персонажем

    '''Создание управление!!!'''
    def on_key_press(self, symbol: int, modifiers: int):
        '''Кнопка ESCAPE, который возвращает пауза и непауза'''
        if symbol == arcade.key.ESCAPE:
            pause_menu = PauseMenu(self) #self -> самого себя вызываем
            window.show_view(pause_menu)
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

    def update(self, delta_time: float):
        '''Вызов камеры'''
        self.center_camera_to_player()  # Вызываем саму камеру
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
            force = (0, 50000)
            self.physics_engine.apply_force(self.player, force)
        else:
            self.physics_engine.set_friction(self.player, PLAYER_FRICTION)  # сила трения
        '''Спецаильно включаем эту физ.движок'''
        self.physics_engine.step()  # используем физ движок

        if arcade.check_for_collision(self.player,self.zombie):
            self.player.kill()
            arcade.close_window()
            print("Аккуратнее")
        if arcade.check_for_collision(self.player,self.bonus):
            selfв.bonus.kill()
        if arcade.check_for_collision(self.player,self.finish):
            arcade.close_window()
            print("Ты молодец!")
#Анимация его лучше сдеть
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

class Zombie(arcade.Sprite):
    def __init__(self):
        super().__init__()
        super().__init__(':resources:images/animated_characters/zombie/zombie_idle.png',scale = 0.5)
        self.center_x = 1000
        self.center_y = 115

class Bonus(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/items/gemYellow.png',scale = 1)
        self.center_x = 1000
        self.center_y = 400

class Finish(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/items/flagRed2.png",scale=0.7)
        self.center_x = 1900
        self.center_y = 100

window = arcade.Window(WIDTH, HEIGHT,fullscreen=True, resizable=True)  # Создали окно
main_menu = MainMenu()  # Создаем объект класса MainMenu
window.show_view(main_menu)  # Присваиваем созданный объект window к созданному объекту main_menu
my_game = MyGame() #Неизвестно будет ли это еще нужна
my_game.setup() #Неизвестно будет ли это еще нужна
arcade.run()  # запускаем в работу цикл on_draw()
