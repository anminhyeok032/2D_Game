from pico2d import *
import gobj
from player import Player

from bg import HorzScrollBackground
import gfw
import generator


def enter():
    gfw.world.init(['bg', 'shell', 'pipe', 'enemy', 'item', 'player'])

    bg = HorzScrollBackground('background.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load('res/ConsolaMalgun.ttf', 40)

    global score
    score = 0

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)


def exit():
    pass



def check_enemy(e):
    if gobj.collides_box(player, e):
        e.remove()
        return

    # for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
    #     if gobj.collides_box(b, e):
    #         # print('Collision', e, b)
    #         dead = e.decrease_life(b.power)
    #         if dead:
    #             score.score += e.level * 10
    #             e.remove()
    #         b.remove()
    #         return



def update():
    global score
    score += gfw.delta_time
    gfw.world.update()
    generator.update(score)

    for e in gfw.world.objects_at(gfw.layer.pipe):
        check_enemy(e)

    for e in gfw.world.objects_at(gfw.layer.shell):
        check_enemy(e)


def draw():
    gfw.world.draw()
    score_pos = 30, get_canvas_height() - 30

    font.draw(*score_pos, 'Score: %d' % score, (255, 255, 255))
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
