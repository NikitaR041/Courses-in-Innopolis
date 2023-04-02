import arcade, random
WIDTH = 1024
HEIGHT = 768
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH,HEIGHT)
    def setup(self):
        self.sound = arcade.load_sound(':resources:sounds/lose5.wav')
        self.isGame = True
        self.background = arcade.load_texture(':resources:images/cybercity_background/far-buildings.png')
        self.player = Penguin()
        self.columns_list = arcade.SpriteList()
        for i in range(3):
            column_top = ColumnTop(':resources:gui_basic_assets/red_button_hover.png',scale=2,angle=90)
            column_top.center_x = 350*i + WIDTH
            column_top.center_y = random.randint(600,750)
            column_top.change_x =7 # двигаем колону со скоростью 7 по оси Х
            self.columns_list.append(column_top)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0,0,WIDTH,HEIGHT,self.background)
        self.player.draw()
        self.columns_list.draw()
    def update(self, delta_time: float):
        if self.isGame:
            self.player.update()
            self.player.update_animation()
            self.columns_list.update()
            if arcade.check_for_collision_with_list(self.player, self.columns_list):
                self.isGame = False
                print("Вы проиграли))))))))))))))))))))))))))")
                arcade.play_sound(self.sound,volume=0.2)
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE: # пробел
            self.player.change_y = 5
            self.player.change_angle = 5
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == 1:
            self.player.change_y = 5
            self.player.change_angle = 5
class Penguin(arcade.Sprite):
    def __init__(self):
        super().__init__(scale=1)
        for i in range(1,4): # 1 2 3
            self.textures.append(arcade.load_texture(f':resources:images/enemies/bee.png',flipped_horizontally=True))
        self.center_x = 100
        self.center_y = 500
        self.change_y = 0
        self.cur_texture = 0
        self.angle = 0
        self.texture = self.textures[int(self.cur_texture)]

    def update_animation(self, delta_time: float = 1 / 60):
        self.cur_texture += 0.05
        if self.cur_texture > 3:
            self.cur_texture = 0
        self.texture = self.textures[int(self.cur_texture)]
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.4
        self.angle += self.change_angle
        self.change_angle -= 0.4
        if self.center_y < 0:
            self.center_y = 0
        if self.center_y > HEIGHT:
            self.center_y = HEIGHT
        if self.angle >= 40:
            self.angle = 40
        if self.angle <= -30:
            self.angle = -30

class ColumnTop(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x < 0 - self.width:
            self.center_x = 50 + WIDTH
            self.center_y = random.randint(600,750)
window = MyGame()
window.setup()
arcade.run()
# 1 - добавить нижние трубы
# 2 - загрузить это в домашку(если еще не грузили ничего в эту домашку)
# 3 - доп задание - авторские доработки - сделать постепенное ускорение труб, сделать счетчик времени,
# чтобы знать сколько вы продержались пока не врезались, сделать перезапуск по правой кнопке мыши