import pygame
import pymunk
import pymunk.pygame_util
import math
from Shapes import SHAPES, Circle, Rectangle
import Sim

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
def pygame_init()-> pygame.Surface:
    global FONT
    pygame.init()
    pygame.font.init()
    FONT = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)
    return pygame.display.set_mode((WIDTH, HEIGHT))

def main_draw(window: pygame.Surface):
    window.fill(BACKGROUND)
    for shape in SHAPES:
        shape.draw(window)
        shape.display_text(window, FONT)
    pygame.display.update()

def main_loop(window: pygame.Surface):
    run = True
    clock = pygame.time.Clock()

    while run:
        # read events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # frame rate
        dt_ms = clock.tick(FPS)

        # simulate physics
        Sim.sim_loop(dt_ms)

        # debug draw
        main_draw(window)


    pygame.quit()

def main():
    print("Launching application...")

    window = pygame_init()

    Sim.sim_init()

    main_loop(window)

    print("Closing application")

if __name__ == "__main__":
    main()