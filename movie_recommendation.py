# Example file showing a circle moving on screen
from setting import *
from button import Button
from menu import Menu
from result import Result



# pygame setup
pygame.init()



screen = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('icon.ico')
pygame.display.set_icon(img)
clock = pygame.time.Clock()
running = True
dt = 0


# State 1 => home   2 => result
state = 1
m = Menu()



while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    if state == 1:
        m.draw(font,main_font)
    elif state == 2:
        r.runner()
    if state == 2 and r.back:
        m = Menu()
        r.back = False
        state = 1
    if m.submit == True:
        state = 2
        r = Result(m.movie)
        m.movie.clear()
        m.submit = False
    

   
    

    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        



    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    pygame.display.update()
pygame.quit()