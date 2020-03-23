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
            (0, 780), 
            (100, 600), 
            (200, 600),
            (300, 600),
            (400, 780),
            (500, 600),
            (550, 600),
            (600, 780),
            (700, 780),
            (800, 600),
            (900, 600),
            (1000, 780),
            (1100, 780),
            (1200, 780),
            ]    
        pygame.draw.lines(screen, self._color, False, points)

    def update(self, dt, action):

        # fun = gravity2D
        t = 0
        # self.state = propagate(fun, t, self.state, dt, action)

        
        #print(self.state)
