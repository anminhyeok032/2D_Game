from pico2d import *
import gfw
import gobj
from player import Player

class Boss:
    def __init__(self, c_pos_x, c_pos_y):
        global angle
        angle = 0
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.image = gfw.image.load('res/boss.png')
        self.target = None
        self.frame = 0
        self.time = 0
        self.move = 0
        self.jump_speed = 0
        global c_pos
        c_pos = c_pos_x, c_pos_y
        self.hx = 150
        self.hy = 150


    def draw(self):
        global angle, c_pos
        target_x, target_y = c_pos
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







    def update(self):
        x, y = self.pos
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

