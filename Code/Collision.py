import math
import pygame
from pygame.math import Vector2
from typing import List, Tuple, Union
from Shapes import Shape, Circle, Rectangle
import Util
import DebugShapes
import BasicForces

EPS = 1e-8
POS_CORRECT_PERCENT = 0.8   # 0..1: how aggressively to un-penetrate
POS_CORRECT_SLOP = 0.01     # small allowed overlap

Window = None

N_POS = Util.ZERO_VECTOR.copy()
N_VEC = Util.ZERO_VECTOR.copy()

def init(window: pygame.Surface) -> None:
    global Window
    Window = window

def inv_mass(body: Shape) -> float:
    if body.static_object:
        return 0.0
    return 1.0 / max(body.mass, EPS)

def positional_correction(a: Shape, b: Shape, normal: pygame.math.Vector2, penetration: float) -> None:
    invA = inv_mass(a)
    invB = inv_mass(b)
    inv_sum = invA + invB
    if inv_sum <= EPS:
        return

    correction_mag = max(penetration - POS_CORRECT_SLOP, 0.0) * (POS_CORRECT_PERCENT / inv_sum)
    correction = correction_mag * normal

    if invA > 0.0:
        a.pos += correction * invA
    if invB > 0.0:
        b.pos -= correction * invB

# -------------------------
# Circle vs Oriented Rectangle (OBB)
# -------------------------
def collide_circle_rect_obb(c: Circle, r: Rectangle, restitution: float) -> None:
    rect_local_axis_x = r.get_x_axis_local().copy()
    rect_local_axis_y = r.get_y_axis_local().copy()

    x_half_extent = r.width / 2.0
    y_half_extent = r.height / 2.0

    circle_pos = c.pos.copy()
    rect_pos = r.pos.copy()

    vec_r_to_c = circle_pos - rect_pos

    closest_point = rect_pos.copy()

    # check rect x axis
    dist_x = Util.dot(vec_r_to_c, rect_local_axis_x)

    if dist_x > x_half_extent:
        dist_x = x_half_extent
    if dist_x < -x_half_extent:
        dist_x = -x_half_extent

    closest_point += (dist_x * rect_local_axis_x)

    # check rect y axis
    dist_y = Util.dot(vec_r_to_c, rect_local_axis_y)

    if dist_y > y_half_extent:
        dist_y = y_half_extent
    if dist_y < -y_half_extent:
        dist_y = -y_half_extent

    closest_point += (dist_y * rect_local_axis_y)
    
    # Reuse length to normalize
    normal_vec = circle_pos - closest_point

    normal_vec_len = Util.length(normal_vec)

    normal_vec = Util.normalize(normal_vec)

    is_penetrating = (normal_vec_len < c.radius)

    global N_VEC
    global N_POS
    if is_penetrating:
        penetration_amount = c.radius - normal_vec_len
        N_VEC = normal_vec
        N_POS = closest_point
        positional_correction(c, r, normal_vec, penetration_amount)
        BasicForces.apply_impulse(normal_vec, c, restitution, inv_mass(c))
        BasicForces.apply_impulse(normal_vec, r, restitution, inv_mass(r))

# -------------------------
# Public: resolve all collisions among objects
# -------------------------
def resolve_collisions(objects: List[Shape], restitution: float = 0.5) -> None:
    
    n = len(objects)
    
    for i in range(n):
        A = objects[i]

        # circle vs rect (check all rects against each circle)
        if isinstance(A, Circle):
            for j in range(n):
                if i == j:
                    continue
                B = objects[j]
                if isinstance(B, Rectangle):
                    collide_circle_rect_obb(A, B, restitution)

        # circle vs circle (pairwise once)
        # for j in range(i + 1, n):
        #     B = objects[j]
        #     if isinstance(A, Circle) and isinstance(B, Circle):
        #         _collide_circle_circle(A, B, restitution)

def debug_display():
    arrow_length = 50.0
    DebugShapes.draw_arrow(Window, (0,0,255), N_POS, N_POS + (arrow_length * N_VEC), 1, 5)
