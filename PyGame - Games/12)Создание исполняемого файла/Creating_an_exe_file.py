'''
    Первым делом нужно открыть консоль -> Terminal
    Там сделать прописать это: 1) pip install pyinstaller
                                2)pyinstaller "main.py" --onefile, где "main.py" имя вашего файла (должно быть на английском языке)
'''
import arcade
import random

#Размеры спрайтов:
SPRITE_SCALING_PLAYER = 0.5 #Игрока
SPRITE_SCALING_ENEMY = 0.5  #Врага
SPRITE_SCALING_LASER = 0.8  #Пуль
#Размеры экрана
WIDTH = 800
HEIGHT = 600
#Скорость
BULLET_SPEED = 5 #Пуль
ENEMY_SPEED = 2 #Врага

#Доп.параметры
MAX_PLAYER_BULLETS = 3 #Количество пуль игрока (мб не пригодится)
ENEMY_VERTICAL_MARGIN = 15 #Проверка на вертикальное перемещение
RIGHT_ENEMY_BORDER = WIDTH - ENEMY_VERTICAL_MARGIN # Идет обратно, достиг правого края
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN # Идет обратно, если достиг левого края
ENEMY_MOVE_DOWN_AMOUNT = 30 #Смещение врага по оси Oy
#Статус игры
GAME_OVER = 1
PLAY_GAME = 0

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.game_state = PLAY_GAME #Игра будет идти (по умолчанию 0)
        self.score = 0
        self.enemy_change_x = -ENEMY_SPEED #Перемещение врага
        self.window.set_mouse_visible(False) #Отключаем видимость указателя мыши
        #Загружаем звуки пуль и хитшота
        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")
        arcade.set_background_color(arcade.color.AMAZON)
    #Здесь устанавливаем самих персонажей и их параметры
    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/"
                                    "femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player.center_x = 50
        self.player.center_y = 40
        #Создается список:
        self.enemy_list = arcade.SpriteList() # список врагов
        self.player_bullet_list = arcade.SpriteList() #список кол-во побежденных врагов от рук г.г.
        self.enemy_bullet_list = arcade.SpriteList() #список побежденных врагов
        #Правило хорошего тона, здесь просто подключается другая функция, чтобы было удобно читать код
        self.setup_level_1() #По факту это не обязательно, но в знак этикета - это применяется

    #Таким образом создаются разные уровни прохождение игры
    def setup_level_1(self):
        self.enemy_textures = [] #нужен для того, чтобы менялся вид врага (т.е. туда куда он смотрит)
        #Функция load_texture_pair - функция, которая отзеркаливает картинку (при этом сохраняет оригинал), следовательно в списке будет 2-е картинки
        self.enemy_textures.append(arcade.load_texture_pair(':resources:images/enemies/slimeBlue.png')) #загружаем это в enemy_texture - в итоге два списка
        #Параметра врага
        x_count, x_start, x_spacing, y_count, y_start, y_spacing = 7, 380, 60, 5, 420, 40
        for x in range(x_start,x_spacing*x_count + x_start, x_spacing):
            for y in range(y_start, y_spacing*y_count + y_start, y_spacing):
                #благодаря тому, что мы использовали load_texture_pair - создается новый список(с двумя картинками) 1)[] - это обращение к элементу списка(но там элемент-список), 2[] - обратились к списку и получается из второго списка просим вызвать конкретный элемент
                enemy = arcade.Sprite(texture=self.enemy_textures[0][0], scale=SPRITE_SCALING_ENEMY, center_x=x,center_y=y)# Загружаем злодея
                self.enemy_list.append(enemy) #добавляем злодея в список
    #отрисовка
    def on_draw(self):
        self.clear()
        #Проверка на то, что игра проиграна
        if self.game_state == GAME_OVER:
            arcade.draw_text(f'GAME OVER', 240, 300, arcade.color.WHITE, 38, font_name="Kenney Blocks")
            return # заверши метод
        #Проверка на то, если количество злодеев равняется 0
        if len(self.enemy_list) == 0:
            arcade.draw_text(f'YOU WINNER!', 240, 300, arcade.color.WHITE, 38, font_name="Kenney Blocks")
            return
        self.player.draw()
        self.enemy_list.draw()
        self.enemy_bullet_list.draw()
        self.player_bullet_list.draw()
        arcade.draw_text(f'Score: {self.score}', 10,20,arcade.color.WHITE,18,font_name="Kenney Blocks") #Да, так можно

    #Частота изменения процесса
    def update(self, delta_time: float):
        if self.game_state == GAME_OVER:#Проверка если процесс игры являвется "1", то останавливается всё из-за return
            return # заверши метод
        self.update_enemies() #наш созданный метод
        self.enemy_bullets()#наш созданный метод
        self.update_player_bullets() #наш созданный метод

    #Частота изменений передвежений пуль - Созданный нами метод
    def enemy_bullets(self):
        for enemy in self.enemy_list:
            chance = 4 + len(self.enemy_list)*6 #Специально придуманная формула для того, чтобы появлялись пули
            if random.randrange(chance) == 0: #непомню что за модуль randrange()
                bullet = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_LASER,angle=180)#загружаем пули
                bullet.change_y = -BULLET_SPEED #Вертикально движутся вниз
                bullet.center_x = enemy.center_x # Исходят от самого врага
                bullet.top = enemy.bottom # top и bottom специальные команды
                self.enemy_bullet_list.append(bullet) #
        self.enemy_bullet_list.update() #Делаем так, как пули часто обновляются

        #Проверка на то, что если пуля попадёт на персонажа - игра закончится
        for bullet in self.enemy_bullet_list:
            hit = arcade.check_for_collision(bullet,self.player)
            if hit:
                bullet.remove_from_sprite_lists() #remove_from_sprite_lists() - специальня функция удаляющая весь список пуль
                self.game_state = GAME_OVER #Изменение статуса, вместо '0' на '1'

    #Частота изменение передвижение врага - созданный нами метод
    def update_enemies(self):
        #берет каждый элемент врага и изменяет ему скорсоть при помощи команды center_x
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        move_down = False #Проверка на то, что столкунся какого-нибудь вертикального края - созданная переменная, чтобы перемещатся вниз
        # берет каждый элемент врага и делает проверку
        for enemy in self.enemy_list:
            #если коснулся правого края и продолжает идти, то изменяем его положение (примерно таке с другим усл)
            if enemy.right > RIGHT_ENEMY_BORDER and self.enemy_change_x > 0:
                self.enemy_change_x = -self.enemy_change_x
                move_down = True # Если столкнулась с вертикальным краяем, то статус меняется
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x = -self.enemy_change_x
                move_down = True# Если столкнулась с вертикальным краяем, то статус меняется

        #Проверка на move_down
        if move_down == True:
            for enemy in self.enemy_list:
                enemy.center_y -= ENEMY_MOVE_DOWN_AMOUNT
                if self.enemy_change_x > 0:
                    enemy.texture = self.enemy_textures[0][0] #Меняет вид врага
                else:
                    enemy.texture = self.enemy_textures[0][1] #Меняет вид врага

    #----------------------------------------------------------------------------------------------
    #передвижение игрока через мышью
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int): # ЛОВИМ ДВИЖЕНИЕ МЫШИ
        self.player.center_x = x

    #Стрельба из мыши лазером
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int): # НАЖАТИЯ МЫШИ ЛОВИМ
        arcade.play_sound(self.gun_sound,volume=0.3)
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER, angle=90)
        bullet.change_y = BULLET_SPEED
        bullet.center_x = self.player.center_x
        bullet.bottom = self.player.top
        self.player_bullet_list.append(bullet)

    #Обязательно нужно отрисовать в update - это созданная нами функция
    def update_player_bullets(self):
        self.player_bullet_list.update() #Это нужно, чтобы двигались пули
        for bullet in self.player_bullet_list:
            #check_for_collision_with_list - ИМЕННО WITH_LIST так как у нас список врагов, а там только один персонаж
            hit = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if hit:
                for i in hit: # находим тех кого подбили
                    arcade.play_sound(self.hit_sound,volume=0.3) #Проигрывать музыку
                    self.score +=1 #Считаем счётчик
                    i.remove_from_sprite_lists() # Удалеям пули с игры remove_from_sprite_list - специальная команда
                bullet.remove_from_sprite_lists() #Удаляем злодеев с игры remove_from_sprite_list - специальная команда

window = arcade.Window(WIDTH,HEIGHT)
my_game = MyGame()
my_game.setup()
window.show_view(my_game)
arcade.run()
