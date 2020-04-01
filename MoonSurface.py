import pygame
from pygame.locals import *

from dynamics import *

import space_game_config as settings

import random

class MoonSurface(pygame.sprite.Sprite):


    def __init__(self):
        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)
        self.IS_CRATER = False

    def update(self, dt, action):
        # TODO: This should update with horizonal scroll?
        t = 0