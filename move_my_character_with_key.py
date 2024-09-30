from pico2d import*

open_canvas()
back_ground = load_image('TUK_GROUND.png')
character = load_image('my_character.png')

def handle_events():
    global running, dir, moving, frame, size
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_DOWN:
                dir = 3
                moving = True
            elif event.key == SDLK_UP:
                dir = 2
                moving = True
            elif event.key == SDLK_LEFT:
                dir = 1
                moving = True
            elif event.key == SDLK_RIGHT:
                dir = 0
                moving = True
            elif event.key == SDLK_EQUALS:
                if size < 20:
                    size += 1
            elif event.key == SDLK_MINUS:
                if size > 5:
                    size -= 1
        elif event.type == SDL_KEYUP:
            moving = False
            if dir == 0:
                frame = 1
            else:
                frame = 0

# 전역 변수
running = True
frame = 1
dir = 0
moving = False
x = 40
y = 600 // 4
size = 10

while running:
    clear_canvas()
    back_ground.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    character.clip_draw(frame * 135, dir * 200, 135, 200, x, y, 4 * size, 6 * size)
    update_canvas()
    handle_events()
    if moving:
        if dir == 3:
            y -= 10
            if y - 3 * size <= 0:
                y = 3 * size
        elif dir == 2:
            y += 10
            if y + 3 * size >= 599:
                y = 599 - 3 * size
        elif dir == 1:
            x -= 10
            if x - 2 * size <= 0:
                x = 2 * size
        elif dir == 0:
            x += 10
            if x + 2 * size >= 799:
                x = 799 - 2 * size
        frame = (frame + 1)%4
    delay(0.05)

close_canvas()
