from pico2d import *
import gfw
import gobj

PLAYER_SIZE = 27
MOVE_PPS = 300
class Player:

    JUMPING, FALLING, BASIC, DASH = range(4)
    GRAVITY = 3000
    JUMP = 1000
    global fn
    fn = 0
    def __init__(self):
        self.delta = 0, 0
        self.pos = get_canvas_width() // 2 , get_canvas_height() // 2
        Player.image = gfw.image.load('res/bird_fly.png')
        self.target = None
        self.frame = 0
        self.time = 0
        self.move = 0
        self.jump_speed = 0

        self.hx = 27*2
        self.hy = 20*2

        self.state = Player.FALLING
        self.FPS = 10
        self.mag = 1
        self.mag_speed = 0
        global delta_x, delta_y
        delta_x, delta_y = 0, 0

        # if Bird.image == None:

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state


    def update(self):
        global fn
        fn += 1
        self.frame = ((self.frame + fn) // 10) % 3

        global delta_x, delta_y
        x, y = self.pos
        x += delta_x * MOVE_PPS * gfw.delta_time
        y += delta_y * MOVE_PPS * gfw.delta_time
        global gravity
        gravity = 2
        # y -= gravity
        # print(y)

        self.time += gfw.delta_time
        if self.state != Player.FALLING:
            # print('jump speed:', self.jump_speed)
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * gfw.delta_time

        hw, hh = self.image.w // 2, self.image.h // 2
        x = clamp(hw, x, get_canvas_width() - hw)
        y = clamp(hh, y, get_canvas_height() - hh)
        self.pos = x, y




    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)


    def draw(self):

        self.image.clip_draw(self.frame * (27*2), 0, 27*2, 20*2, *self.pos)



    def jump(self):
        if self.state in [Player.JUMPING, Player.BASIC, Player.DASH]:
            return
        if self.state == Player.FALLING:
            self.state = Player.JUMPING

        self.jump_speed = Player.JUMP * self.mag


    def get_bb(self):
        hw = self.hx
        hh = self.hy
        x, y = self.pos
        return x - hw / 2 + 8, y - hh / 2 + 8, x + hw / 2 - 8, y + hh / 2 - 8

    def handle_event(self, e):
        global delta_x, delta_y
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                delta_x -= 1
            elif e.key == SDLK_RIGHT:
                delta_x += 1
            elif e.key == SDLK_DOWN:
                delta_y -= 1
            elif e.key == SDLK_UP:
                delta_y += 1



        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                delta_x += 1
            elif e.key == SDLK_RIGHT:
                delta_x -= 1
            elif e.key == SDLK_DOWN:
                delta_y += 1
            elif e.key == SDLK_UP:
                delta_y -= 1