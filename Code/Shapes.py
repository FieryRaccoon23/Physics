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
    @abstractmethod
    def draw(self, window: pygame.Surface) -> None:
        pass

    def AddShape(self) -> None:
        SHAPES.append(self)

# -------------------------
# Circle class
# -------------------------
class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, color: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

# -------------------------
# Rectangle class
# -------------------------
class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))