from pico2d import *
import gfw
from gobj import *
import random

SIZE = 70
HOLE_SIZE = 350
class Pipe:
    #SIZE = 167

    def __init__(self, speed, pipe_y):
        #self.x, self.y = get_canvas_width(), (get_canvas_height() // 2 - HOLE_SIZE) #+ pipe_y
        self.dx, self.dy = speed, 0
        self.pos = get_canvas_width() + 100, (get_canvas_height() // 2 - HOLE_SIZE) + pipe_y

        self.image = gfw.image.load('res/pipe_low.png')

        self.fidx = 0
        self.ran_pipe_y = pipe_y



    def draw(self):
        global ran_pipe_y
        x, y = self.pos
        y = (get_canvas_height() // 2 + HOLE_SIZE) + self.ran_pipe_y
        upper_pos = x, y
        self.image.composite_draw(3.14159, 'right', *upper_pos, SIZE, SIZE*7.5)
        self.image.clip_draw(0, 0, 72, 786, *self.pos, SIZE, SIZE*7.5)




    def update(self):
        x, y = self.pos
        x -= 2
        self.pos = x, y

    def get_bb(self):
        pass
    def remove(self):
        pass