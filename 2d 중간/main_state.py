from pico2d import *
import gobj
from player import Player

from pipe import Pipe
from bg import HorzScrollBackground
import random
import gfw
import generator


def enter():
    gfw.world.init(['bg', 'pipe', 'enemy', 'item', 'player'])

    bg = HorzScrollBackground('background.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    global score
    score = 0

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    # hh = random.randint(-100, 100)
    #
    # global pipe
    # pipe = Pipe(10, hh)
    # pipe.pipe = pipe
    # gfw.world.add(gfw.layer.pipe, pipe)


def exit():
    pass


def update():
    global score
    score += gfw.delta_time
    gfw.world.update()
    generator.update(score)


def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:
            pass

    player.handle_event(e)


if __name__ == '__main__':
    gfw.run_main()
