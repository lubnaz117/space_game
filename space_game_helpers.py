import pygame
from pygame.locals import *

def check_crash(ship, moon):
    return pygame.sprite.collide_rect(ship, moon)

def check_screen_color(is_crashed):
    if is_crashed == True:
        return (255, 0, 0) # red 
    else:
        return (0, 0, 0) # black
