import pygame
from abc import ABC, abstractmethod

# -------------------------
# Global Parameters
# -------------------------
SHAPES: list["Shape"] = []

# -------------------------
# Base class
# -------------------------
class Shape(ABC):
    def __init__(self, x: int, y: int, mass: float, id: int):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.mass = mass
        self.id = id
        self.text = ""
        self.text_offset_x = 0
        self.text_offset_y = 0
        self.text_color: tuple[int, int, int] = (0, 0, 0)
        self.static_object = False
        self.angle: float = 0.0                 # degrees
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
        window.blit(text, (int(self.x + self.text_offset_x), int(self.y - self.text_offset_y)))

# -------------------------
# Circle class
# -------------------------
class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, mass: int, id: int, color: tuple[int, int, int]):
        super().__init__(x, y, mass, id)
        self.radius = radius
        self.color = color

    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

# -------------------------
# Rectangle class
# -------------------------
class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int, mass: int, id: int, color: tuple[int, int, int]):
        super().__init__(x, y, mass, id)
        self.width = width
        self.height = height
        self.color = color

        # draw the rect once to an offscreen Surface so we can rotate it
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height))

    def draw(self, window: pygame.Surface) -> None:
        rotated = pygame.transform.rotate(self.surface, self.angle)
        # center around geometric center (x + w/2, y + h/2) to preserve current top-left semantics
        rect = rotated.get_rect(center=(self.x + self.width * 0.5, self.y + self.height * 0.5))
        window.blit(rotated, rect.topleft)