import pygame
from pygame.locals import *

from dynamics import *

class Moon():

    def __init__(self):

        self.state = np.array([600, 600, 0.05, 0])

        self._pos = [self.state[0], self.state[1]]
        self._radius = 100
        self._color = 255, 255, 255

    def draw(self, screen):
        self._pos = [int(self.state[0]), int(self.state[1])]
        points = [
            (0, 1000), 
            (100, 800), 
            (200, 800),
            (300, 800),
            (400, 1000),
            (500, 800),
            (550, 800),
            (600, 1000),
            (700, 1000),
            (800, 800),
            (900, 800),
            (1000, 1000),
            (1100, 1000),
            (1200, 1000), # Needs to end at 1200
            ]    
        pygame.draw.lines(screen, self._color, False, points)

    def update(self, dt, action):

        # fun = gravity2D
        t = 0
        # self.state = propagate(fun, t, self.state, dt, action)

        
        #print(self.state)
