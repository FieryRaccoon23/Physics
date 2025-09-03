import pygame
import pymunk
import pymunk.pygame_util
import math

# Global Parameters
WIDTH, HEIGHT = 1000, 800
FPS = 60

# Methods
def pygame_init()-> pygame.Surface:
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT))

def loop(window, width, height):
    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        dt = clock.tick(FPS)

    pygame.quit()

def main():
    print("Launching application...")

    window = pygame_init()
    loop(window, WIDTH, HEIGHT)

    print("Closing application")

if __name__ == "__main__":
    main()