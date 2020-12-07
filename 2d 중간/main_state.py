from pico2d import *
import gobj
from player import Player, boss_mode_player
from boss import Boss
from shell import Shell_red_boss, Shell_green_boss
from bg import HorzScrollBackground
import gfw
import generator
import life_gauge


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
    score = 0


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
    global boss_bool
    if gobj.collides_box(player, e):
        if not boss_bool:
            e.remove()
        return True
    return False
def check_boss(e):
    if gobj.collides_box(boss, e):
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

    boss_dead = False
    hit, hits, dead, item = False, False, False, None
    if not boss_bool:

        for e in gfw.world.objects_at(gfw.layer.shell_green):
            hit = check_enemy(e)
            if hit:
                dead = player.decrease_life(time)

        for e in gfw.world.objects_at(gfw.layer.pipe):
            hits = check_enemy(e)
            if hits:
                dead = player.decrease_life(time)

        for e in gfw.world.objects_at(gfw.layer.shell_red):
            item = check_enemy(e)
            if item:
                player.increase_life()
                score += 1

        if score > 9 and boss_bool == False:
            boss_bool = True
            boss_round()


    else:
        boss.set_click(*player.pos)
        for e in gfw.world.objects_at(gfw.layer.boss):
            hits = check_enemy(e)
            if hits:
                dead = player.decrease_life(time)

        if player.space and not player.cooltime:
            global shell
            shell = Shell_red_boss(10, *player.pos, player.target_x, player.target_y)
            shell.shell = shell
            gfw.world.add(gfw.layer.shell_red, shell)

        global shell1
        shell1 = Shell_green_boss(5, *boss.pos, *player.pos)
        shell1.shell = shell1
        gfw.world.add(gfw.layer.shell_green, shell1)

        for e in gfw.world.objects_at(gfw.layer.shell_red):
            hit = check_boss(e)
            if hit:
                boss_dead = boss.decrease_life(2)
            item = check_enemy(e)
            if item:
                score += 1


        for e in gfw.world.objects_at(gfw.layer.shell_green):
            hits = check_enemy(e)
            if hits:
                dead = player.decrease_life(time)


    ends = dead
    if ends:
        print('end')
    if boss_dead:
        print('boss dead')

def draw():
    global boss_bool, bg
    if boss_bool:
        bg = gfw.image.load('res/boss_bg.png')

        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
        bg.draw(*center, get_canvas_width(), get_canvas_height() + 200)
    gfw.world.draw()
    score_pos = get_canvas_width() // 2, get_canvas_height() - 60

    font.draw(*score_pos, '%d' % score, (255, 255, 255))
    #gobj.draw_collision_box()

        #gfw.world.add(gfw.layer.bg, bg)


def boss_round():

    global player, boss, state, bg
    bg.remove()
    exlife = player.remove()
    for e in gfw.world.objects_at(gfw.layer.shell_green):
        e.remove()
    for e in gfw.world.objects_at(gfw.layer.pipe):
        e.remove()
    for e in gfw.world.objects_at(gfw.layer.shell_red):
        e.remove()


    state = STATE_BOSS
    life_gauge.load()

    player = boss_mode_player(exlife)
    gfw.world.add(gfw.layer.player, player)

    boss = Boss()
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
