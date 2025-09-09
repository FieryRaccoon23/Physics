import pygame
import Shapes
import Util

GRAVITY = 9.81 * 10.0 

def integrate_position(dt: int, object: Shapes.Shape):
        if object.static_object:
            return
        object.pos += object.vel * dt

def apply_gravity(dt: int, object: Shapes.Shape):
    if not object.static_object:
        object.vel.y += GRAVITY * dt

def apply_impulse(contact_n: pygame.math.Vector2, object: Shapes.Shape, restitution: float, inv_mass: float):
    if inv_mass <= 0.0:
        return
    
    v_rel_n = Util.dot(contact_n, object.vel)

    if v_rel_n >= 0.0:
        return

    jn = -(1.0 + restitution) * v_rel_n / inv_mass

    object.vel += (jn * contact_n) * inv_mass