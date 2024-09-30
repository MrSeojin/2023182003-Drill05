from pico2d import*

open_canvas()
back_ground = load_image('TUK_GROUND.png')
character = load_image('my_character.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

# 전역 변수
running = True

while running:
    clear_canvas()
    back_ground.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
