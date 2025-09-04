import pygame
import math

def draw_arrow(surface, color, start, end, width=3, head_length=15, head_angle=30):
    # Draw line
    pygame.draw.line(surface, color, start, end, width)

    # Calculate direction
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.atan2(dy, dx)

    # Left head point
    left_x = end[0] - head_length * math.cos(angle - math.radians(head_angle))
    left_y = end[1] - head_length * math.sin(angle - math.radians(head_angle))

    # Right head point
    right_x = end[0] - head_length * math.cos(angle + math.radians(head_angle))
    right_y = end[1] - head_length * math.sin(angle + math.radians(head_angle))

    # Draw head (triangle)
    pygame.draw.polygon(surface, color, [end, (left_x, left_y), (right_x, right_y)])