import pygame
import pymunk
import pymunk.pygame_util
import math
from Shapes import SHAPES, Circle, Rectangle

# -------------------------
# Global Parameters
# -------------------------
WIDTH, HEIGHT = 1000, 800
FPS = 60
BACKGROUND = "white"

# -------------------------
# Main methods
# -------------------------
def pygame_init()-> pygame.Surface:
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT))

def draw(window: pygame.Surface):
    window.fill(BACKGROUND)
    for shape in SHAPES:
        shape.draw(window)
    pygame.display.update()

def loop(window: pygame.Surface):
    run = True
    clock = pygame.time.Clock()

    while run:
        # read events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # frame rate
        dt = clock.tick(FPS)

        # debug draw
        draw(window)


    pygame.quit()

def main():
    print("Launching application...")

    window = pygame_init()

    loop(window)

    print("Closing application")

if __name__ == "__main__":
    main()