import gfw
from pico2d import *
import main_state


def enter():
    global image
    image = load_image('res/logo.png')

    gfw.world.init(['bg', 'shell_green', 'shell_red', 'pipe', 'enemy', 'item', 'boss', 'player', 'ui'])

    global bg
    bg = main_state.HorzScrollBackground('background.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = main_state.Player()
    gfw.world.add(gfw.layer.bg, player)
    # gfw.world.add(gfw.layer.player, player)

    global font
    font = gfw.font.load('res/FlappyBird.ttf', 40)


def draw():
    gfw.world.draw()
    image.draw(400, 400, 91 * 3, 27 * 3)
    font.draw(get_canvas_width() // 2 - 150, 200, 'Press SpaceBar', (0, 0, 0))


def update():
    gfw.world.update()

def pause():
    pass


def resume():
    pass


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()

    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)

def exit():
    global image
    del image

if __name__ == '__main__':
    gfw.run_main()