from pico2d import *
import gfw
import gobj

PLAYER_SIZE = 27
MOVE_PPS = 300
MAX_LIFE = 5

class Player:

    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    JUMPING, FALLING, BASIC, DASH = range(4)
    GRAVITY = 3000
    JUMP = 1000
    global fn, op, time
    fn = 0

    def __init__(self):

        self.pos = get_canvas_width() // 2 , get_canvas_height() // 2
        Player.image = gfw.image.load('res/bird_fly.png')
        self.target = None
        self.frame = 0
        self.time = 0
        self.move = 0


        self.hx = 27*2
        self.hy = 20*2


        self.life = MAX_LIFE

        self.state = Player.FALLING
        self.FPS = 10
        self.mag = 1
        self.mag_speed = 0
        self.delta_x, self.delta_y = 0, 0
        #delta_x, delta_y = 0, 0

        global decrease, rt
        decrease = False
        rt = 0
        global heart_red, heart_white
        heart_red = gfw.image.load('res/heart_red.png')
        heart_white = gfw.image.load('res/heart_white.png')

        # if Bird.image == None:

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state


    def reset(self):

        self.pos = get_canvas_width() // 2, get_canvas_height() // 2


        global angle
        angle = 0


        self.life = MAX_LIFE

    def update(self):

        global fn, rt
        fn += 1
        self.frame = ((self.frame + fn) // 10) % 3

        rt += gfw.delta_time

        # global delta_x, delta_y
        x, y = self.pos
        x += self.delta_x * MOVE_PPS * gfw.delta_time
        y += self.delta_y * MOVE_PPS * gfw.delta_time
        global gravity
        gravity = 2
        # y -= gravity
        # print(y)

        self.time += gfw.delta_time
        if self.state != Player.FALLING:
            # print('jump speed:', self.jump_speed)
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * gfw.delta_time

        #hw, hh = self.image.w // 2, self.image.h // 2
        x = clamp(self.hx / 2, x, get_canvas_width() - self.hx / 2)
        y = clamp(self.hy / 2, y, get_canvas_height() - self.hx / 2)
        self.pos = x, y

        global decrease, time
        if decrease:
            self.image.opacify(100)

            if time + 1.5 < rt:
                print(1)
                decrease = False
        else:
            self.image.opacify(1)




    def increase_life(self):
        pass


    def decrease_life(self, real_time):
        global  decrease, time
        self.life -= 1
        time = real_time
        decrease = True

        return self.life <= 0



    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)


    def draw(self):

        self.image.clip_draw(self.frame * (27*2), 0, 27*2, 20*2, *self.pos)

        x, y = get_canvas_width() - 30, get_canvas_height() - 30
        for i in range(MAX_LIFE):
            heart = heart_red if i < self.life else heart_white
            heart.draw(x, y)
            x -= heart.w






    def get_bb(self):
        hw = self.hx
        hh = self.hy
        x, y = self.pos
        return x - hw / 2 + 8, y - hh / 2 + 8, x + hw / 2 - 8, y + hh / 2 - 8

    def handle_event(self, e):
        #global delta_x, delta_y
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.delta_x -= 1
            elif e.key == SDLK_d:
                self.delta_x += 1
            elif e.key == SDLK_s:
                self.delta_y -= 1
            elif e.key == SDLK_w:
                self.delta_y += 1



        elif e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.delta_x += 1
            elif e.key == SDLK_d:
                self.delta_x -= 1
            elif e.key == SDLK_s:
                self.delta_y += 1
            elif e.key == SDLK_w:
                self.delta_y -= 1


    def remove(self):
        gfw.world.remove(self)
        return self.life


class boss_mode_player(Player):

    def __init__(self, exlife):
        global mouse_click
        mouse_click = False
        self.pos = get_canvas_width() // 2 , get_canvas_height() // 2
        Player.image = gfw.image.load('res/bird_fly.png')
        self.target = None
        self.frame = 0
        self.time = 0
        self.move = 0


        self.hx = 27*2
        self.hy = 20*2


        self.life = exlife

        self.state = Player.FALLING
        self.FPS = 10
        self.mag = 1
        self.mag_speed = 0

        global heart_red, heart_white
        heart_red = gfw.image.load('res/heart_red.png')
        heart_white = gfw.image.load('res/heart_white.png')
        self.target_x, self.target_y = get_canvas_width() // 2, get_canvas_height() // 2

        self.delta_x, self.delta_y = 0,0

        global pipe
        pipe = gfw.image.load('res/pipe_low.png')
        #delta_x, delta_y = 0, 0
        global start_boss
        start_boss = True

    def draw(self):

        global angle, mouse_click, pipe_size


        x, y = self.pos
        dx, dy = self.target_x - x, self.target_y - y
        angle = math.atan2(dy, dx) - math.pi / 2

        px, py = self.pos
        plx, ply = self.pos


        plx, ply = self.target_x - plx, self.target_y - ply

        #print(pipe_pos)

        pipe_size = math.sqrt(plx ** 2 + ply ** 2)
        px += (self.target_x - px) // 2
        py += (self.target_y - py) // 2
        pipe_pos = px, py

        if mouse_click:
            pipe.composite_draw(angle, 'h', *pipe_pos, 40, pipe_size)


        if angle > 0 or angle < -3.1:
            self.image.clip_composite_draw(self.frame * (27 * 2), 0, 27 * 2, 20 * 2, angle + 1.5708, 'v', *self.pos, 27*2, 20*2)
        else:
            self.image.clip_composite_draw(self.frame * (27 * 2), 0, 27 * 2, 20 * 2, angle + 1.5708, '', *self.pos,
                                           27 * 2, 20 * 2)


        x, y = get_canvas_width() - 30, get_canvas_height() - 30
        for i in range(MAX_LIFE):
            heart = heart_red if i < self.life else heart_white
            heart.draw(x, y)
            x -= heart.w


    def update(self):
        global fn
        fn += 1
        self.frame = ((self.frame + fn) // 10) % 3

        self.follow_mouse_target()

        x, y = self.pos
        x += self.delta_x * MOVE_PPS * gfw.delta_time
        y += self.delta_y * MOVE_PPS * gfw.delta_time
        global gravity
        gravity = 2
        # y -= gravity
        # print(y)

        self.time += gfw.delta_time


        #hw, hh = self.image.w // 2, self.image.h // 2
        x = clamp(self.hx/2, x, get_canvas_width() - self.hx/2)
        y = clamp(self.hy/2, y, get_canvas_height() - self.hx/2)
        self.pos = x, y

        # global decrease, time
        # if decrease:
        #     self.image.opacify(100)
        #
        #     if time + 1.5 < rt:
        #         print(1)
        #         decrease = False
        # else:
        #     self.image.opacify(1)



    def get_bb(self):
        hw = self.hx
        hh = self.hy
        x, y = self.pos
        return x - hh / 2 + 10, y - hh / 2 + 10, x + hh / 2 - 10, y + hh / 2 - 10

    def follow_mouse_target(self):
        global angle

        x, y = self.pos
        dx, dy = self.target_x - x, self.target_y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return
        dx, dy = dx / distance, dy / distance
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        if dx > 0 and x > self.target_x: x = self.target_x
        if dx < 0 and x < self.target_x: x = self.target_x
        if dy > 0 and y > self.target_y: y = self.target_y
        if dy < 0 and y < self.target_y: y = self.target_y
        #self.pos = x, y

        angle = math.atan2(dy, dx) - math.pi / 2
        #print('Angle: %.3f' % angle)


    def teleport_pipe(self):
        pass

    def teleport(self):
        self.pos = self.target_x, self.target_y

    def handle_event(self, e):
        #global delta_x, delta_y


        global mouse_click, start_boss
        if e.type == SDL_MOUSEBUTTONDOWN:
            mouse_click = True
            self.set_target(e)

        elif e.type == SDL_MOUSEMOTION:
            self.set_target(e)

        if e.type == SDL_MOUSEBUTTONUP:
            mouse_click = False
            self.set_target(e)
            self.teleport()

        if start_boss and e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
            self.delta_x = 0
            self.delta_Y = 0

            start_boss = False


        else:

            if e.type == SDL_KEYDOWN:

                if e.key == SDLK_a:
                    self.delta_x -= 1
                elif e.key == SDLK_d:
                    self.delta_x += 1
                elif e.key == SDLK_s:
                    self.delta_y -= 1
                elif e.key == SDLK_w:
                    self.delta_y += 1

            elif e.type == SDL_KEYUP:
                if e.key == SDLK_a:
                    self.delta_x += 1
                elif e.key == SDLK_d:
                    self.delta_x -= 1
                elif e.key == SDLK_s:
                    self.delta_y += 1
                elif e.key == SDLK_w:
                    self.delta_y -= 1

    def set_target(self, e):
        #global target_x, target_y
        self.target_x, self.target_y = e.x, get_canvas_height() - e.y - 1