from Shapes import SHAPES, Circle, Rectangle

GRAVITY = 9.81        
RESTITUTION = 0.5     # 0 = no bounce, 1 = perfectly bouncy
red_circle = None
radius = 50

def sim_init():
    global red_circle
    red_circle = Circle(200, 150, radius, 0, (255, 0, 0))
    red_circle.add_shape()

def sim_loop(dt_ms: int):
    global red_circle

    dt = dt_ms / 1000.0

    red_circle.vy += GRAVITY * dt
    red_circle.y += red_circle.vy * dt

    red_circle.set_text(f"vx: {red_circle.vx:.1f}, vy: {red_circle.vy:.1f}", radius, radius, (255, 0, 0))
