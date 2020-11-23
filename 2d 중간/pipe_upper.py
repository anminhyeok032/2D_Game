from pico2d import *
import gfw
from gobj import *
import random
class Pipe_high:
    #SIZE = 167
    SIZE = 36
    def __init__(self, speed, pipe_y):
        self.x, self.y = get_canvas_width(), get_canvas_height() // 2
        self.dx, self.dy = speed, 0
        self.pos = get_canvas_width(), pipe_y


        self.image = gfw.image.load('res/pipe_high.png')


        self.fidx = 0



    def draw(self):

        self.image.clip_draw(0, 0, 36*2, 167*2, *self.pos)




    def update(self):
        x, y = self.pos
        x -= 2
        self.pos = x, y



    def remove(self):
        pass

