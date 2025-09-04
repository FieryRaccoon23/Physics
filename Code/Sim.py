import pygame
from enum import Enum
import ParticleMergingSplitting.ParticleMergingSplitting as ParticleMergingSplitting

class Project(Enum):
    ParticleMergingSplitting = 1

SELECTED_PROJECT = Project.ParticleMergingSplitting

# Called once
def sim_init(window: pygame.Surface):
    match SELECTED_PROJECT:
        case Project.ParticleMergingSplitting:
            print("Running ParticleMergingSplitting")
            ParticleMergingSplitting.init(window)
        case _:
            print("No project selected")

# Updates every frame
def sim_loop(dt_ms: int):
    match SELECTED_PROJECT:
        case Project.ParticleMergingSplitting:
            ParticleMergingSplitting.loop(dt_ms)
        case _:
            pass

# Update every frame for debug displaying
def sim_debug_display():
    match SELECTED_PROJECT:
        case Project.ParticleMergingSplitting:
            ParticleMergingSplitting.debug_display()
        case _:
            pass