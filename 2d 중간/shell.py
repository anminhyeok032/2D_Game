from pico2d import *
import gfw
from gobj import *
from player import boss_mode_player

global fn
fn = 0
global pn
pn = 0
class Shell_green:

    def __init__(self, speed):
        self.pos = get_canvas_width() + 100, -100

        self.image = gfw.image.load('res/shell.png')
        self.frame = 0
        self.fidx = 0
        self.speed = speed

        self.hx = 48
        self.hy = 30

    def draw(self):
        self.image.clip_draw(self.frame * 48, 0, 48, 30, *self.pos)


    def update(self):
        global fn
        fn += 1
        self.frame = ((self.frame + fn) // 10) % 8

        x, y = self.pos
        x -= 2
        y += self.speed
        self.pos = x, y
        if x < - 100:
            self.remove()

    def get_bb(self):
        hw = self.hx
        hh = self.hy
        x, y = self.pos
        return x - hw / 2 + 8, y - hh / 2 + 1, x + hw / 2 - 8, y + hh / 2 - 1

    def remove(self):
        gfw.world.remove(self)


class Shell_red(Shell_green):
    def draw(self):
        self.image.clip_draw(self.frame * 48, 0, 48, 30, *self.pos)

    def update(self):
        global pn
        pn += 1
        self.frame = (((self.frame + pn) // 10) % 8) + 8

        x, y = self.pos
        x -= 2
        y += self.speed
        self.pos = x, y
        if x < - 100:
            self.remove()


class Shell_red_boss(Shell_red):
    def __init__(self, speed, pos_x, pos_y, target_x, target_y):
        self.pos = pos_x, pos_y
        self.target = target_x, target_y
        self.image = gfw.image.load('res/shell.png')
        self.frame = 0
        self.fidx = 0
        self.speed = speed

        self.hx = 48
        self.hy = 30

        self.x, self.y = self.pos
        self.tx, self.ty = self.target
        self.d = math.sqrt((self.tx - self.x) ** 2 + (self.ty - self.y) ** 2)
        self.dx, self.dy = (self.tx - self.x) / self.d, (self.ty - self.y) / self.d
        #self.pos = target_x,target_y
        self.tpx, self.tpy = self.pos
        self.tpx = self.tx - self.tpx
        self.tpy = self.ty - self.tpy


    def update(self):
        global pn
        pn += 1
        self.frame = (((self.frame + pn) // 10) % 8) + 8




        self.x += self.dx*self.speed
        self.y += self.dy*self.speed
        self.pos = self.x + self.tpx, self.y + self.tpy
        if self.x < - 100 or self.x > 1000:
            self.remove()

    def draw(self):
        self.image.clip_draw(self.frame * 48, 0, 48, 30, *self.pos)



class Shell_green_boss(Shell_green):
    def __init__(self, speed, pos_x, pos_y, target_x, target_y):
        self.pos = pos_x, pos_y
        self.target = target_x, target_y
        self.image = gfw.image.load('res/shell.png')
        self.frame = 0
        self.fidx = 0
        self.speed = speed

        self.hx = 48
        self.hy = 30

        self.x, self.y = self.pos
        self.tx, self.ty = self.target
        self.d = math.sqrt((self.tx - self.x) ** 2 + (self.ty - self.y) ** 2)
        self.dx, self.dy = (self.tx - self.x) / self.d, (self.ty - self.y) / self.d
        # self.pos = target_x,target_y


    def update(self):
        global pn
        pn += 1
        self.frame = ((self.frame + fn) // 10) % 8

        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        self.pos = self.x , self.y
        if self.x < - 100 or self.x > 1000:
            self.remove()

    def draw(self):
        self.image.clip_draw(self.frame * 48, 0, 48, 30, *self.pos)
