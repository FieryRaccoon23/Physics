import pygame
import pymunk
import pymunk.pygame_util
import math
from Shapes import SHAPES, Circle, Rectangle
import Sim

# -------------------------
# Debug Parameters
# -------------------------
SHOW_TEXT = True
PAUSE = False

# -------------------------
# Global Parameters
# -------------------------
WIDTH, HEIGHT = 1000, 800
FPS = 60
BACKGROUND = "white"
FONT = None
FONT_SIZE = 10
FONT_TYPE = "Arial"

# -------------------------
# Main methods
# -------------------------

# Init pygame parameters
def pygame_init()-> pygame.Surface:
    global FONT
    pygame.init()
    pygame.font.init()
    FONT = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)
    return pygame.display.set_mode((WIDTH, HEIGHT))

# Draw shapes and also text
def main_draw(window: pygame.Surface):
    window.fill(BACKGROUND)
    for shape in SHAPES:
        shape.draw(window)
        if SHOW_TEXT:
            shape.display_text(window, FONT)
    pygame.display.update()

# All pygame events are to be placed here
def read_pygame_events(event: pygame.event) -> bool:
    global SHOW_TEXT
    global PAUSE

    if event.type == pygame.QUIT:
                return False
    
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_SPACE: # Space - Pause simulation
            PAUSE = not PAUSE
        if event.key == pygame.K_d: # D - Debug enable/disbale - NOTE inefficient as it will still loop through all objects
            SHOW_TEXT = not SHOW_TEXT
    
    return True

# main loop of application
def main_loop(window: pygame.Surface):
    run = True
    clock = pygame.time.Clock()

    while run:
        # read events
        for event in pygame.event.get():
            run = read_pygame_events(event)
        
        dt_ms = clock.tick(FPS)

        # simulate physics
        if not PAUSE:
            Sim.sim_loop(dt_ms)

        # debug draw
        main_draw(window)


    pygame.quit()

# start here
def main():
    print("Launching application...")

    window = pygame_init()

    Sim.sim_init()

    main_loop(window)

    print("Closing application")

if __name__ == "__main__":
    main()