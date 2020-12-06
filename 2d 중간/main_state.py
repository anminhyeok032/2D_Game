from pico2d import *
import gobj
from player import Player, boss_mode_player
from boss import Boss
from collision import *
from bg import HorzScrollBackground
import gfw
import generator

STATE_IN_GAME, STATE_BOSS = range(2)

def enter():
    global state, boss_bool
    state = STATE_IN_GAME
    boss_bool = False
    gfw.world.init(['bg', 'shell_green', 'shell_red', 'pipe', 'enemy', 'item', 'boss', 'player'])

    global bg
    bg = HorzScrollBackground('background.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load('res/FlappyBird.ttf', 40)

    global time
    time = 0
    global score
    score = 10


    global player,boss

    player = Player()
    #player.bg = bg
    gfw.world.add(gfw.layer.player, player)


    # player = boss_mode_player()
    # player.bg = bg
    # gfw.world.add(gfw.layer.player, player)
    #
    # boss = Boss(player.pos)
    # boss.bg = bg
    # gfw.world.add(gfw.layer.boss, boss)






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
    global time, score, state, boss_bool
    time += gfw.delta_time
    gfw.world.update()
    if state == STATE_IN_GAME:
        generator.update(time)

    global boss
    boss = Boss(*player.pos)

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

    if score > 9 and boss_bool == False:
        boss_bool = True
        boss_round()
    ends = dead
    if ends:
        print('end')

def draw():
    gfw.world.draw()
    score_pos = get_canvas_width() // 2, get_canvas_height() - 60

    font.draw(*score_pos, '%d' % score, (255, 255, 255))
    gobj.draw_collision_box()


def boss_round():

    global player, boss, state, bg
    bg.remove()
    player.remove()
    for e in gfw.world.objects_at(gfw.layer.shell_green):
        e.remove()
    for e in gfw.world.objects_at(gfw.layer.pipe):
        e.remove()
    for e in gfw.world.objects_at(gfw.layer.shell_red):
        e.remove()


    state = STATE_BOSS

    #bg = load_image
    player = boss_mode_player()
    gfw.world.add(gfw.layer.player, player)


    gfw.world.add(gfw.layer.boss, boss)



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
