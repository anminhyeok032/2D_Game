from pico2d import *
import gfw
from gobj import *


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