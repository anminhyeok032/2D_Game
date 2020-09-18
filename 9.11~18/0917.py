from pico2d import *
from random import randint as rint
from random import random as rfloat
import os
class Boy:
    def __init__(self):
        self.x, self.y = get_canvas_width() // 2, 85
        self.image = load_image('run_animation.png')
        self.dx = 0
        self.fidx = rint(0, 7)
    def draw(self):
        self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.x += self.dx * 5
        self.fidx = (self.fidx + 1) % 8

class Grass:
    def __init__(self):
        self.x, self.y = 400, 30
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running, boy
    events = get_events()
    for event in events:
          if event.type == SDL_QUIT:
              running = False
          elif event.type == SDL_KEYDOWN:
              if event.key == SDLK_ESCAPE:
                  running = False
          elif event.type == SDL_KEYUP:
             if event.key == SDLK_LEFT:
                 boy.dx -= 1
             elif event.key == SDLK_RIGHT:
                 boy.dx += 1
          elif event.type == SDL_MOUSEMOTION:
              boy.x,boy.y = event.x,get_canvas_height() - event.y - 1



open_canvas()
#os.chdir('C:\\Program Files\\Python37')


team = [Boy() for i in range(11)]
#for b in team:
#    b.x = rint[100, 700]
#    b.y = rint[100 ,500]
#boy = team[0]
boy = Boy()
grass = Grass()

running = True
hide_cursor()

while(running):
    clear_canvas()
    grass.draw()
    #for b in team: b.draw()
    boy.draw()
    update_canvas()

    handle_events()
    for b in team : boy.update()
    
    
    get_events()
    
close_canvas()
