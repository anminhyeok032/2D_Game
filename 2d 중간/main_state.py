from pico2d import *
import gobj
from player import Player
#from boss import Boss
from collision import *
from bg import HorzScrollBackground
import gfw
import generator


def enter():
    gfw.world.init(['bg', 'shell_green', 'shell_red', 'pipe', 'enemy', 'item', 'boss', 'player'])

    bg = HorzScrollBackground('background.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load('res/FlappyBird.ttf', 40)

    global time
    time = 0
    global score
    score = 0

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    #global boss
    #boss = Boss()
    #boss.bg = bg
    #gfw.world.add(gfw.layer.boss, boss)


def exit():
    pass



def check_enemy(e):
    if gobj.collides_box(player, e):
        e.remove()
        return True

    return False

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
    global time, score
    time += gfw.delta_time
    gfw.world.update()
    generator.update(time)


    hit, hits, dead, item = False, False, False, None
    for e in gfw.world.objects_at(gfw.layer.shell_green):
        hit = check_enemy(e)
        if hit:
            dead = player.decrease_life()

    for e in gfw.world.objects_at(gfw.layer.pipe):
        hits = check_enemy(e)
        if hits:
            dead = player.decrease_life()

    for e in gfw.world.objects_at(gfw.layer.shell_red):
        item = check_enemy(e)
        if item:
            player.increase_life()
            score += 1


    ends = dead
    if ends:
        print('end')

def draw():
    gfw.world.draw()
    score_pos = get_canvas_width() // 2, get_canvas_height() - 60

    font.draw(*score_pos, '%d' % score, (255, 255, 255))
    #gobj.draw_collision_box()



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
