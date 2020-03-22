import pygame
from pygame.locals import *

class Spaceship():

    def __init__(self):
        self._pos = [50, 50]
        self._radius = 5
        self._color = 0, 255, 0

    def draw(self, screen):
      pygame.draw.circle(screen, self._color, self._pos, self._radius)

    def update(self):
        self.color = GREEN