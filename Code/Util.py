import math
import pygame

X_AXIS = pygame.math.Vector2(1.0,0.0)
Y_AXIS = pygame.math.Vector2(0.0,1.0)

RIGHT_AXIS = X_AXIS
DOWN_AXIS = Y_AXIS
LEFT_AXIS = -1.0 * X_AXIS
UP_AXIS = -1.0 * Y_AXIS

ZERO_VECTOR = pygame.math.Vector2(0.0,0.0)

def clamp(x, lo, hi) -> float:
    return max(lo, min(x, hi))

def length(v: pygame.math.Vector2) -> float:
    return math.sqrt(v.x*v.x + v.y*v.y)

def normalize(v: pygame.math.Vector2) -> pygame.math.Vector2:
    d = length(v)
    if d == 0.0:
        return ZERO_VECTOR.copy()
    return pygame.math.Vector2(v.x/d, v.y/d)

def dot(a: pygame.math.Vector2, b: pygame.math.Vector2) -> float:
    return a.x*b.x + a.y*b.y