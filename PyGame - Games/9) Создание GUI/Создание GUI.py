'''См домашку'''

import arcade
import arcade.gui #Отдельный модуль, в котором можно вызвать отдельные окошки

WIDTH = 800
HEIGHT = 600
text = "Птицы — класс теплокровных яйцекладущих высших позвоночных животных, которые передвигаются на двух ногах, а их передние конечности превратились в крылья.\n" \
       "По состоянию на 2007 год насчитывается от 9800 до 10 500 видов птиц.\n" \
       "Они населяют все экосистемы земного шара от Арктики до Антарктики.\n" \
       "Размеры видов колеблются от 5 см (колибри) до 2,75 м (страус)."

class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        '''Вызываем менеджера - главное окно, в котором закидываем разные объекты для взаимодействия'''
        self.manager = arcade.gui.UIManager() # вызывали менеджера
        self.manager.enable() # Включили менеджера
        #-----------------------------------------------
        '''Вызываем новое окно - вертикальный(по умолчанию) бокс'''
        self.v_box = arcade.gui.UIBoxLayout()  #Удобен для того, чтобы перемещать кнопки (старта и тд) туда куда захочешь
        self.manager.add(arcade.gui.UIAnchorWidget(
            #align_x = 100 #включи и посмотри (просто делает отступ)
            anchor_x= 'center_x', #команды: left/right - якорь по оси Ox
            anchor_y= 'center_y', #команды: top/bottom - якорь по оси Oy
            child=self.v_box #добавляем аргумент v_box в параметр self.manager.add(arcade.gui.UIAnchorWidget)
        ))
        #Создание кнопки старта - команда кнопки -> UIFlatButton
        self.start_botton = arcade.gui.UIFlatButton(text="Start Game", widht=300)
        #....with_space_around(bottom = 20) -> нужен для того,чтобы были отступы между кнопок
        self.v_box.add(self.start_botton.with_space_around(bottom=20)) #Добавляем эту кнопку в v_box
        #Создание кнопки настройки
        self.setting_menu = arcade.gui.UIFlatButton(text="Setting", widht=200)
        self.v_box.add(self.setting_menu.with_space_around(bottom=20))
        #Создание кнопки выхода
        self.exit_menu = arcade.gui.UIFlatButton(text="Exit",widht=200)
        self.v_box.add(self.exit_menu.with_space_around(bottom=20))
        '''Создаем проверку на клика -> создать свой метод on_click_exit  | on_click -> такая команда!'''
        self.exit_menu.on_click = self.on_click_exit
        #Создание отдельной кнопки
        self.some_button = arcade.gui.UITextureButton(texture=arcade.load_texture(":resources:onscreen_controls/flat_dark/play.png"))
        self.v_box.add(self.some_button.with_space_around(bottom=20))
        #Создание текста
        self.ui_text = arcade.gui.UITextArea(text='Супер пупер игра',
                                             widht= 300, height=50,font_size=20)
        self.v_box.add(self.ui_text.with_space_around(bottom=20,left=180))
        #Создание виртуальной доски, в которой будет огромный текст
        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        self.text_area = arcade.gui.UITextArea(text=text, x=50,y=200, width=200,height=300,text_color=(0,0,0,255))
        #Так как огромный текст, то мы размещаем в само окно manager
        self.manager.add(arcade.gui.UITexturePane(self.text_area.with_space_around(right=20),
                                                  tex=bg_tex,padding=(10,10,10,10) ) )



    def on_click_exit(self,event): #обязательно нужно передать event - параметр,отвечающий за отклик
        arcade.close_window()
        print("Вы вышли из игры")

    def on_draw(self):
        self.clear()
        self.manager.draw()

window = arcade.Window(WIDTH,HEIGHT) #Создали окно
main_menu = MainMenu() # Создаем объект класса MainMenu
window.show_view(main_menu) # Присваиваем созданный объект window к созданному объекту main_menu
arcade.run() #запускаем в работу цикл on_draw()



