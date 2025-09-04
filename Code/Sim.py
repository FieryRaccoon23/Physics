from Shapes import SHAPES, Shape, Circle, Rectangle
import random
import pygame
import DebugShapes

GRAVITY = 9.81        
RESTITUTION = 0.5     # 0 = no bounce, 1 = perfectly bouncy
PHYSICS_OBJECTS: list["Shape"] = []
RADIUS = 10

Floor = None
Window = None

# Called once
def sim_init(window: pygame.Surface):
    global Window
    Window = window

    # Init circles
    count = 10
    x_value = 50
    x_offset = 60
    object_id = 0
    for _ in range(count):
        x = x_value
        x_value += (2* RADIUS) + x_offset
        y = random.randint(50, 100)

        circle_mass = 1.0
        c = Circle(x, y, RADIUS, circle_mass, object_id, (255, 0, 0))
        object_id += 1
        c.add_shape()
        c.text_color = (255, 0, 0)            
        PHYSICS_OBJECTS.append(c)
    

    # Init floor
    global Floor
    floor_mass = 1.0
    Floor = Rectangle(300, 500, 300, 10, floor_mass, object_id, [0, 0, 255])
    Floor.static_object = True
    Floor.text_color = (0, 0, 255)
    Floor.angle = 0.0
    Floor.add_shape()
    PHYSICS_OBJECTS.append(Floor)

# Debug
def show_debug(object: Shape):
    object.set_text(f"id: {object.id}, vx: {object.vx:.1f}, vy: {object.vy:.1f}", RADIUS, RADIUS, object.text_color)

# Gravity
def apply_gravity(dt: int, object: Shape):
    if not object.static_object:
        object.vy += GRAVITY * dt
        object.y += object.vy * dt

# Updates every frame
def sim_loop(dt_ms: int):
    dt = dt_ms / 1000.0

    for obj in PHYSICS_OBJECTS:
        apply_gravity(dt, obj)
        show_debug(obj)

# Update every frame for debug displaying
def sim_debug_display():
    pass