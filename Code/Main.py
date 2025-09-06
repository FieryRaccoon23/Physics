import pygame
import pymunk
import pymunk.pygame_util
import math
from Shapes import SHAPES, Circle, Rectangle
import Sim
import Inputs
import DebugShapes
import Util

# -------------------------
# Debug Parameters
# -------------------------
SHOW_DEBUG_DETAILS = True
PAUSE = False
STEPPING = False

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

# Draw Axes
def draw_axes(window: pygame.Surface):
    origin = (5,5)
    axis_length = 50
    x_axis = origin + (axis_length * Util.X_AXIS)
    y_axis = origin + (axis_length * Util.Y_AXIS)
    offset = 5

    # X axis
    DebugShapes.draw_arrow(window, (0,255,0), origin, x_axis, 1, 5)
    text = FONT.render("X", True, (0,255,0))
    window.blit(text, (int(x_axis[0] + offset), int(x_axis[1] - offset)))

    # Y axis
    DebugShapes.draw_arrow(window, (0,0,255), origin, y_axis, 1, 5)
    text = FONT.render("Y", True, (0,0,255))
    window.blit(text, (int(y_axis[0] + offset), int(y_axis[1] - offset)))

# Draw shapes and also text
def main_draw(window: pygame.Surface):
    window.fill(BACKGROUND)

    draw_axes(window)

    for shape in SHAPES:
        shape.draw(window)
        if SHOW_DEBUG_DETAILS:
            shape.display_text(window, FONT)

    if SHOW_DEBUG_DETAILS:
         Sim.sim_debug_display()

    pygame.display.update()

# All pygame events are to be placed here
def read_pygame_events(event: pygame.event) -> bool:
    global SHOW_DEBUG_DETAILS
    global PAUSE
    global STEPPING

    if event.type == pygame.QUIT:
                return False
    
    if event.type == pygame.KEYDOWN: 
        if event.key == Inputs.Pause:
            PAUSE = not PAUSE
        if event.key == Inputs.Debug: # NOTE: inefficient as it will still loop through all objects
            SHOW_DEBUG_DETAILS = not SHOW_DEBUG_DETAILS
        if event.key == Inputs.Step:
             STEPPING = True
    
    return True

# main loop of application
def main_loop(window: pygame.Surface):
    global STEPPING
    
    run = True
    clock = pygame.time.Clock()

    while run:
        # read events
        for event in pygame.event.get():
            run = read_pygame_events(event)
        
        dt_ms = clock.tick(FPS)

        # simulate physics
        if (not PAUSE) or (PAUSE and STEPPING) :
            Sim.sim_loop(dt_ms)

        STEPPING = False

        # debug draw
        main_draw(window)


    pygame.quit()

# start here
def main():
    print("Launching application...")

    window = pygame_init()

    Sim.sim_init(window)

    main_loop(window)

    print("Closing application")

if __name__ == "__main__":
    main()