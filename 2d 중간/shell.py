from pico2d import *
import gfw
from gobj import *
import random


global fn
fn = 0

class Shell:
    #SIZE = 167

    def __init__(self, speed):
        #self.x, self.y = get_canvas_width(), (get_canvas_height() // 2 - HOLE_SIZE) #+ pipe_y

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
        self.frame = ((self.frame + fn) // 40) % 17

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


# class Pipe_up:
#     #SIZE = 167
#
#     def __init__(self, speed, pipe_y):
#         #self.x, self.y = get_canvas_width(), (get_canvas_height() // 2 - HOLE_SIZE) #+ pipe_y
#         self.dx, self.dy = speed, 0
#         self.pos = get_canvas_width() + 100, (get_canvas_height() // 2 - HOLE_SIZE) + pipe_y
#
#         self.image = gfw.image.load('res/pipe_low.png')
#
#         self.fidx = 0
#         self.ran_pipe_y = pipe_y
#
#         self.hx = SIZE
#         self.hy = SIZE*7.5
#
#     def draw(self):
#         global ran_pipe_y
#         x, y = self.pos
#         y = (get_canvas_height() // 2 + HOLE_SIZE) + self.ran_pipe_y
#
#         self.pos = x, y
#         self.image.composite_draw(3.14159, 'h', *self.pos, SIZE, SIZE*7.5)
#         #self.image.clip_draw(0, 0, 72, 786, *self.pos, SIZE, SIZE*7.5)
#
#
#
#
#     def update(self):
#         x, y = self.pos
#         x -= 2
#         self.pos = x, y
#         if x < - 100:
#             self.remove()
#
#     def get_bb(self):
#         global upper_pos
#         hw = self.hx
#         hh = self.hy
#         x, y = self.pos
#         return x - hw / 2 + 4, y - hh / 2 + 4, x + hw / 2 - 4, y + hh / 2 - 4
#
#     def remove(self):
#         gfw.world.remove(self)