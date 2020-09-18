from pico2d import *

def handle_events():
    global running, x, y, dx
    events = get_events()
    for event in events:
          if event.type == SDL_QUIT:
              running = False
          elif event.type == SDL_KEYDOWN:
              if event.key == SDLK_ESCAPE:
                  running = False
          elif event.type == SDL_KEYUP:
             if event.key == SDLK_LEFT:
                 dx -= 1
             elif event.key == SDLK_RIGHT:
                 dx += 1
          elif event.type == SDL_MOUSEMOTION:
              x,y = event.x,get_canvas_height() - event.y - 1

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

running = True
x,y = get_canvas_width() // 2, 85
dx = 0
hide_cursor()

while(running):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    handle_events()
    x += dx
    get_events()
    
close_canvas()
