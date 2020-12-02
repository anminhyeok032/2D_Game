from pico2d import *
import gfw
from pipe import Pipe_up, Pipe_down
from shell import Shell
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
    pipe = Pipe_up(10, hh)
    pipe.pipe = pipe
    gfw.world.add(gfw.layer.pipe, pipe)

    global pipe1
    pipe1 = Pipe_down(10, hh)
    pipe1.pipe = pipe1
    gfw.world.add(gfw.layer.pipe, pipe1)

    global shell
    shell = Shell(2)
    shell.shell = shell
    gfw.world.add(gfw.layer.shell, shell)

