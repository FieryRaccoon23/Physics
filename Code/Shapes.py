import pygame
from abc import ABC, abstractmethod
import Util
import math

# -------------------------
# Global Parameters
# -------------------------
SHAPES: list["Shape"] = []

# -------------------------
# Base class
# -------------------------
class Shape(ABC):
    def __init__(self, pos: pygame.math.Vector2, mass: float, id: int, angle: float = 0.0):
        self.pos = pos
        self.vel = Util.ZERO_VECTOR.copy()
        self.mass = mass
        self.id = id
        self.text = ""
        self.text_offset_x = 0
        self.text_offset_y = 0
        self.text_color: tuple[int, int, int] = (0, 0, 0)
        self.static_object = False
        self.angle: float = angle
        self.angle_previous: float = 0.0
        self.surface: pygame.Surface | None = None
    
    @abstractmethod
    def draw(self, window: pygame.Surface) -> None:
        pass

    def add_shape(self) -> None:
        SHAPES.append(self)

    def set_text(self, text: str, text_offset_x: int, text_offset_y: int, text_color: tuple[int, int, int]) -> None:
        self.text = text
        self.text_offset_x = text_offset_x
        self.text_offset_y = text_offset_y
        self.text_color = text_color

    def display_text(self, window: pygame.Surface, font: pygame.font.Font) -> None:
        text = font.render(self.text, True, self.text_color)
        window.blit(text, (int(self.pos.x + self.text_offset_x), int(self.pos.y - self.text_offset_y)))

# -------------------------
# Circle class
# -------------------------
class Circle(Shape):
    def __init__(self, pos: pygame.math.Vector2, radius: float, mass: float, id: int, color: tuple[int, int, int]):
        super().__init__(pos, mass, id)
        self.radius = radius
        self.color = color
        self.radius_sqr = radius * radius

    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.radius)

# -------------------------
# Rectangle class
# width = x axis & height = y axis
# -------------------------
class Rectangle(Shape):
    def __init__(self, pos: pygame.math.Vector2, width: int, height: int, mass: float, id: int, angle: float, color: tuple[int, int, int]):
        super().__init__(pos, mass, id, angle)
        self.width = width
        self.height = height
        self.color = color
        self.x_axis_local = Util.X_AXIS
        self.y_axis_local = Util.Y_AXIS
        self.set_local_axis()

        # draw the rect once to an offscreen Surface so we can rotate it
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height))

    def draw(self, window: pygame.Surface) -> None:
        rotated = pygame.transform.rotate(self.surface, self.angle)
        rect = rotated.get_rect(center=(self.pos.x, self.pos.y))
        window.blit(rotated, rect.topleft)

    def set_local_axis(self):
        self.x_axis_local = self.x_axis_local.rotate(-self.angle)
        self.y_axis_local = self.y_axis_local.rotate(-self.angle)
        self.angle_previous = self.angle

    def get_x_axis_local(self) -> pygame.math.Vector2:
        if not math.isclose(self.angle_previous, self.angle):
            self.set_local_axis()
        return self.x_axis_local
    
    def get_y_axis_local(self) -> pygame.math.Vector2:
        if not math.isclose(self.angle_previous, self.angle):
            self.set_local_axis()
        return self.y_axis_local