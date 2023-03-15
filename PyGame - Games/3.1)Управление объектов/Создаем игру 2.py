'''Создаем космический корабль с врагами в космосе

 buttom - кнопка - готовая функция

 top - верхний - готовая функция
 bottom - нижний - готовая функция

'''
import random
import arcade
WIDTH = 800
HEIGHT = 600
#Обозначим переменные, при помощи которых можно изменять параметры наших объектов
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_LASER = 0.3
SPRITE_SCALING_ENEMY = 0.5
#-------------------------
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT)
        '''Загрузили фон'''
        self.background_texture = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.player = None
        self.laser = None
        self.laser_list = None
        self.enemy = None
        self.enemy_list = None
        '''Функция, которая прячет курсор мыши'''
        self.set_mouse_visible(False) # прячем курсор мыши
        '''status -> чисто флажок, при помощи которого можно опреределять что-то'''
        self.status = True  # Если True, то игра продолжается

    def setup(self):
        self.player = Player()
        self.laser_list = arcade.SpriteList() #Картинки в списке
        self.enemy_list = arcade.SpriteList() #Картинки в списке
        '''Создаем врагов '''
        for i in range(1,31): # спауним 30 врагов
            self.enemy = Enemy() #Создали объект класса ENEMY
            self.enemy.center_x = random.randint(0, WIDTH) #рандомное спавн врагов
            self.enemy.center_y = HEIGHT + i*75 #HEIGHT + i*75, где i*75 промежуток между врагами
            self.enemy_list.append(self.enemy) #Закидываем картиники в список
    '''Функция - ключик, который рисует нам объекты'''
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT,self.background_texture)
        self.player.draw()
        self.laser_list.draw()
        self.enemy_list.draw()

    '''ЗДесь мы используем лазеры -> создаём лазеры'''
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int): # НАЖАТИЯ МЫШИ ЛОВИМ
        if self.status: # если игра продолжается
            if button == arcade.MOUSE_BUTTON_LEFT: #Если button(КНОПКА НАЖАТАЯ ВАМИ) РАВНА СООТВЕСТВУЮЩЕЙ КНОПКЕ, то!
                self.laser = Laser() #Создаем лазер
                self.laser.bottom = self.player.top # задаем y лазера равной координате корабля (нижнее) = (верхнему)
                self.laser.center_x = self.player.center_x # задаем x лазера как у корабля
                self.laser_list.append(self.laser)

    '''Нужно, чтобы корабль следил за мышью!'''
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int): # ЛОВИМ ДВИЖЕНИЕ МЫШИ
        if self.status: # если игра продолжается
            self.player.center_x = x
            self.player.center_y = y
            '''ЧТобы не выходил выше середины экрана!'''
            if self.player.center_y >= HEIGHT/2:
                self.player.center_y = HEIGHT/2

    def update(self, delta_time: float):
        if self.status: # если игра продолжается
            self.enemy_list.update()
            self.laser_list.update()
            '''Перебираем лазеры в списке картинок из лазеров'''
            for laser in self.laser_list: # проверяем попадания лазеров в игроков
                shot_list = arcade.check_for_collision_with_list(laser,self.enemy_list) # проверяем столкновения лазера и списка врагов
                if shot_list: #если попал
                    laser.kill() #ТО уничтожаем лазер, чтобы не нагружать компьютер
                    '''Перебираем соотвествующего врага, который попал под лазер'''
                    for enemy in shot_list:
                        enemy.kill() #ТО уничтожаем его
        if not self.enemy_list: # если уничтожили всех врагов
            self.status = False # завершаем игру
'''Создали три класса - наши объекты'''
#нащ корабль
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png', SPRITE_SCALING_PLAYER)
        self.center_x = WIDTH // 2 #Спавнится в середине экрана
        self.center_y = 30
#Лазеры, которые вылетают из нашего коробля
class Laser(arcade.Sprite):
    def __init__(self): #:resources:images/items/coinGold.png
        super().__init__(':resources:images/space_shooter/laserBlue01.png', SPRITE_SCALING_LASER, angle=90)
        self.change_y = 2
    '''Нужен, чтобы изменяло координаты лазера (идёт вверх против ракеты)'''
    def update(self):
        self.center_y += self.change_y #прибавляем, чтобы шёл вверх
        if self.bottom >= HEIGHT: #bottom - ниже
            self.kill() #уничтожается лазер, если он выше экрана(ушел с поле зреня)
#Враги
class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png', SPRITE_SCALING_ENEMY, angle=180)
        self.change_y = 1
    '''Нужен, чтобы враги шли к нам на встречу(т.е. сверху вниз!)'''
    def update(self):
        self.center_y -= self.change_y #Вычитаем, чтобы шли сверху вниз

def main():
    window = MyGame()
    window.setup()
    arcade.run()
main()
'''Дополнительные задачки:
1) Разобраться в коде еще раз, написать комментарии там где боитесь забыть что то
2) написать в чат какие строчки хотели бы разобрать еще раз
3) доп задание - доработать на свой вкус -свои картинки использовать или еще что-то
4) сделать услвоие поражения при касании с врагом и когда враг заходит за нижнюю часть экрана
'''