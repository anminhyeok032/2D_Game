from pico2d import *
import gfw
from pipe import Pipe
import random

TIME = 0

def update(time):
    global TIME
    if time // 2 > TIME:
        generate_pipe()
        TIME += 1


def generate_pipe():
    hh = random.randint(-100, 100)

    global pipe
    pipe = Pipe(10, hh)
    pipe.pipe = pipe
    gfw.world.add(gfw.layer.pipe, pipe)

