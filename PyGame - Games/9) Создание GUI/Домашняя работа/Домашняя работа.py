'''
Реализовать в платформере систему жизней и очков, а также gui с отображение жизней и очков.
'''
import arcade,random
import arcade.gui #Отдельный модуль, в котором можно вызвать отдельные окошки

WIDHT = 800
HEIGHT = 800
text = "Что добавлено:\n" \
       "1)Добавлена пауза при помощи GUI\n" \
       "2)Добавлена стартовое меню при помощи GUI\n" \
       "3)Добавлена кнопка выхода и кнопка старта при помощи GUI\n" \
       "4)Добавлен счётчик, который считает сколько прошел времени игрок\n" \
       "P.S. спасибо учителю! Семёну Николаевичу за объяснение этой темы!"
#Создание старта при помощи модуля GUI
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
        self.start_botton = arcade.gui.UIFlatButton(text="Start Game", widht=300)
        #....with_space_around(bottom = 20) -> нужен для того,чтобы были отступы между кнопок
        self.v_box.add(self.start_botton.with_space_around(bottom=20)) #Добавляем эту кнопку в v_box
        self.start_botton.on_click = self.on_click_start
        #----------------------------------------
        #Создание кнопки выхода
        self.exit_menu = arcade.gui.UIFlatButton(text="Exit",widht=200)
        self.v_box.add(self.exit_menu.with_space_around(bottom=20))
        '''Создаем проверку на клика -> создать свой метод on_click_exit  | on_click -> такая команда!'''
        self.exit_menu.on_click = self.on_click_exit
        #---------------------------------
        #Создание игровой доски - доски почёта:)
        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        self.text_area = arcade.gui.UITextArea(text=text, x=50,y=200, width=200,height=300,text_color=(0,0,0,255))
        # Так как огромный текст, то мы размещаем в само окно manager
        self.manager.add(arcade.gui.UITexturePane(self.text_area.with_space_around(right=20),
                                                  tex=bg_tex, padding=(10, 10, 10, 10)))
        #padding -> команда, которая позволяет делать отступы внутри доски от текста
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

#Создание игровой паузы при помощи модуля GUI
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
    def on_draw(self):
        self.clear()
        self.manager2.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            window.show_view(self.my_game) #Вызываем самого себя

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        '''Создаём очки при помощи времени'''
        self.score = 0
        self.manager1 = arcade.gui.UIManager()
        self.manager1.enable()
        self.v_box1 = arcade.gui.UIBoxLayout()
        self.manager1.add(arcade.gui.UIAnchorWidget(
            anchor_x='left',
            anchor_y='top',
            child=self.v_box1
        ))
        self.ui_text1 = arcade.gui.UITextArea(text=f"Score: {int(self.score)}", width=300,height=50,font_size=30, font_name="Kenney Blocks")
        self.v_box1.add(self.ui_text1.with_space_around(bottom=60,left=60))
        #---------------------------------------------------------
        '''Начало игры'''
        self.isGame = True #Если игра продолжается
        self.player = Penguin()
        self.columns_list = arcade.SpriteList()
        self.speed_change_x = 2 #Добавили переменную для изменение скорости колонн
        for i in range(3):
            column_top = ColumnTop('Resource/column_top.png',scale=2)
            column_top.center_x = 350 * i  + WIDHT #Частота появлений колон
            column_top.center_y = random.randint(600,750)
            column_top.change_x = self.speed_change_x #Двигаем колонну с изменением переменным
            self.columns_list.append(column_top)
        #------------------------------------------------------
            column_down = ColumnDown('Resource/column_bottom.png', scale=2)
            column_down.center_x = 350 * i + WIDHT
            column_down.center_y = random.randint(0, 150)
            column_down.change_x = self.speed_change_x #Двигаем колонну с изменением переменным
            self.columns_list.append(column_down)

        self.sound1 = arcade.load_sound('Resource/Aloe_Blacc_-_I_Need_A_Dollar_47925532.mp3')

    def on_show_view(self):
        self.background = arcade.load_texture('Resource/space.png')

    def on_draw(self):
        self.clear()
        #Создаем задний фон
        arcade.draw_lrwh_rectangle_textured(0,0,WIDHT,HEIGHT,self.background)
        self.player.draw()
        self.columns_list.draw()
        '''Вызываем менеджера'''
        self.manager1.draw()

    # Для смена костюмов(каритнок - анимация)
    def update(self, delta_time: float): #изменение картиник за 60 сек  это много
        if self.isGame:
            '''счетчик'''
            self.score += 0.01 # 0.01 - так как за 60 сек меняется
            #print(int(self.score))
            self.player.update_animation() # update_animation() - запускаем его, которого раннее переопределяли
            self.player.update()
            self.columns_list.update()
            #Создаем колизию соприкосновения
            hit = arcade.check_for_collision_with_list(self.player,self.columns_list)
            if hit :
                self.isGame = False #Игра остановится
                self.sound_player1 = arcade.play_sound(self.sound1, volume=0.1) #Пасхалочка
            self.speed_change_x +=0.01
            for i in self.columns_list:
                i.change_x = self.speed_change_x
            '''Счётчик'''
            self.ui_text1.text = f"Score: {int(self.score)}"
                        #...text =  -> такая команда

    #Создаем управление персонажа  - изменение по Y
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.player.change_y = 5
            self.player.change_angle = 5
        if symbol == arcade.key.ESCAPE:
            pause_menu = PauseMenu(self) #self -> самого себя вызываем
            window.show_view(pause_menu)

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

window = arcade.Window(WIDHT,HEIGHT) #Создали окно
main_menu = MainMenu() # Создаем объект класса MainMenu
window.show_view(main_menu) # Присваиваем созданный объект window к созданному объекту main_menu
arcade.run() #запускаем в работу цикл on_draw()

# window = MyGame()
# window.setup()
# arcade.run()