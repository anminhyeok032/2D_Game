from pico2d import *
import gobj
from player import Player, boss_mode_player
from boss import Boss
from shell import Shell_red_boss, Shell_green_boss
from bg import HorzScrollBackground
import gfw
import generator
import life_gauge
import highscore


STATE_IN_GAME, STATE_BOSS, STATE_GAME_OVER = range(3)


def start_game():
    global state
    if state != STATE_GAME_OVER:
        return
    state = STATE_IN_GAME
    global player, boss, bg
    player.reset()

    bg = HorzScrollBackground('background.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)
    gfw.world.clear_at(gfw.layer.player)
    player = Player()
    gfw.world.add(gfw.layer.player, player)
    #player = Player()
    #boss.reset()
    #boss = Boss()

    # for e in gfw.world.objects_at(gfw.layer.shell_green):
    #     e.remove()
    # for e in gfw.world.objects_at(gfw.layer.pipe):
    #     e.remove()
    # for e in gfw.world.objects_at(gfw.layer.shell_red):
    #     e.remove()
    gfw.world.clear_at(gfw.layer.shell_red)
    gfw.world.clear_at(gfw.layer.shell_green)
    gfw.world.clear_at(gfw.layer.boss)


    gfw.world.remove(highscore)


    global score
    score = 9
    global time
    time = 0

    global boss_bool
    boss_bool = False


    music_bg.repeat_play()

def end_game():
    global state, score
    print('Dead')
    state = STATE_GAME_OVER
    music_bg.stop()

    highscore.add(score)
    gfw.world.add(gfw.layer.ui, highscore)





def enter():
    global boss_bool
    boss_bool = False
    gfw.world.init(['bg', 'shell_green', 'shell_red', 'pipe', 'enemy', 'item', 'boss', 'player', 'ui'])

    # global bg
    # bg = HorzScrollBackground('background.png')
    # bg.speed = 10
    # gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load('res/FlappyBird.ttf', 40)

    global game_over_image
    game_over_image = gfw.image.load('res/game_over_0.png')

    global music_bg, wav_item, wav_hit, wav_boss
    music_bg = load_music('res/boss_music.mp3')
    wav_item = load_wav('res/point.wav')
    wav_hit = load_wav('res/hit.wav')
    wav_boss = load_wav('res/swoosh.wav')
    wav_item.set_volume(10)
    wav_hit.set_volume(5)
    wav_boss.set_volume(5)

    global time
    time = 0
    global score
    score = 0


    global boss, player

    player = Player()
    # gfw.world.add(gfw.layer.player, player)

    highscore.load()

    global state
    state = STATE_GAME_OVER

    start_game()





def exit():
    global music_bg, wav_item, wav_hit, wav_boss
    del music_bg
    del wav_item
    del wav_hit
    del wav_boss



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
                wav_hit.play()
                dead = player.decrease_life(time)

        for e in gfw.world.objects_at(gfw.layer.pipe):
            hits = check_enemy(e)
            if hits:
                wav_hit.play()
                dead = player.decrease_life(time)

        for e in gfw.world.objects_at(gfw.layer.shell_red):
            item = check_enemy(e)
            if item:
                wav_item.play()
                player.increase_life()
                score += 1

        if score > 9 and boss_bool == False:
            boss_bool = True
            boss_round()


    else:
        if state == STATE_BOSS:
            boss.set_click(*player.pos)
            for e in gfw.world.objects_at(gfw.layer.boss):
                hits = check_enemy(e)
                if hits:
                    wav_hit.play()
                    dead = player.decrease_life(time)

            if player.space and not player.cooltime:
                global shell
                shell = Shell_red_boss(10, *player.pos, player.target_x, player.target_y)
                shell.shell = shell
                gfw.world.add(gfw.layer.shell_red, shell)
                if score < 2:
                    end_game()
                score -= 2

            global shell1
            shell1 = Shell_green_boss(5, *boss.pos, *player.pos)
            shell1.shell = shell1
            gfw.world.add(gfw.layer.shell_green, shell1)


            for e in gfw.world.objects_at(gfw.layer.shell_red):
                hit = check_boss(e)
                if hit:
                    boss_dead = boss.decrease_life(5)
                    wav_boss.play()
                item = check_enemy(e)
                if item:
                    wav_item.play()
                    score += 1

            for e in gfw.world.objects_at(gfw.layer.shell_green):
                hits = check_enemy(e)
                if hits:
                    wav_hit.play()
                    dead = player.decrease_life(time)

    global ends
    ends = dead

    if ends:
        state = STATE_GAME_OVER
        end_game()
        print('end')
    if boss_dead:
        end_game()
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

    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height() // 2
        game_over_image.draw(*center)
    #gobj.draw_collision_box()

        #gfw.world.add(gfw.layer.bg, bg)


def boss_round():

    global player, boss, state, bg
    if state == STATE_GAME_OVER:
        return
    bg.remove()
    delta = player.get_delta()
    exlife = player.remove()
    for e in gfw.world.objects_at(gfw.layer.shell_green):
        e.remove()
    for e in gfw.world.objects_at(gfw.layer.pipe):
        e.remove()
    for e in gfw.world.objects_at(gfw.layer.shell_red):
        e.remove()


    state = STATE_BOSS
    life_gauge.load()

    player = boss_mode_player(exlife, *delta)
    gfw.world.add(gfw.layer.player, player)

    boss = Boss()
    gfw.world.add(gfw.layer.boss, boss)





def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.quit()
        elif e.key == SDLK_RETURN:
            start_game()

    player.handle_event(e)


# if __name__ == '__main__':
#     gfw.run_main()
