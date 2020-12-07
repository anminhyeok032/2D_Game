from pico2d import *
import gfw
import gobj
from player import Player
import life_gauge

class Boss:
    def __init__(self):
        global angle
        angle = 0
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.image = gfw.image.load('res/boss.png')
        self.target = None
        self.frame = 0
        self.time = 0
        self.move = 0
        self.jump_speed = 0

        self.max_life = 100
        self.life = self.max_life


        self.c_pos = 0, 0
        self.hx = 150
        self.hy = 150
        self.moving = False


    def set_click(self, c_pos_x, c_pos_y):
        self.c_pos = c_pos_x, c_pos_y



    def draw(self):
        global angle
        target_x, target_y = self.c_pos
        x, y = self.pos
        dx, dy = target_x - x, target_y - y

        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return
        dx, dy = dx / distance, dy / distance

        if dx > 0 and x > target_x: x = target_x
        if dx < 0 and x < target_x: x = target_x
        if dy > 0 and y > target_y: y = target_y
        if dy < 0 and y < target_y: y = target_y


        angle = math.atan2(dy, dx) - math.pi / 2
        #print(angle)
        if angle > 0 or angle < -3.1:
            self.image.composite_draw(angle, 'v', *self.pos, 200, 200)
        else:
            self.image.composite_draw(angle, 'v', *self.pos, 200, 200)

        rate = self.life / self.max_life
        life_gauge.draw(get_canvas_width() // 2, get_canvas_height() - 100, get_canvas_width() - 100, rate)
        #print(self.life)





    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def update(self):

        x, y = self.pos
        if self.life < 50:

            if x < 75 :
                self.moving = True
            if self.moving:
                x += 2
                if x > 725:
                    self.moving = False
            else:
                x -= 2

        self.pos = x, y
        if x < - 100:
            self.remove()



    def get_bb(self):
        hw = self.hx
        hh = self.hy
        x, y = self.pos
        return x - hw / 2 + 4, y - hh / 2 + 4, x + hw / 2 - 4, y + hh / 2 - 4

    def remove(self):
        gfw.world.remove(self)

