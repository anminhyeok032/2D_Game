from pico2d import *
import gobj
from player import Player
from pipe_upper import Pipe_high
from pipe_low import Pipe_low
from bg import HorzScrollBackground
import random
import gfw


def enter():
    gfw.world.init(['bg', 'pipe', 'enemy', 'item', 'player'])


    bg = HorzScrollBackground('background.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)




    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)


    hh = random.randint(-50, 50)

    global pipe

    h = get_canvas_height() // 2 + hh
    pipe = Pipe_high(10, h + 200)
    pipe.pipe = pipe
    gfw.world.add(gfw.layer.pipe, pipe)

    global pipe2
    pipe2 = Pipe_low(10, h - 200)
    pipe2.pipe = pipe2
    gfw.world.add(gfw.layer.pipe, pipe2)


def exit():
    pass

def update():
    gfw.world.update()





def draw():
    gfw.world.draw()
    gobj.draw_collision_box()


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