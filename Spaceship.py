import pygame
from pygame.locals import *

from dynamics import *

class Spaceship():

    def __init__(self):
    
        self.state = np.array([50, 50, 0.05, 0])
        
        self._pos = [self.state[0], self.state[1]]
        self._radius = 10
        self._color = 0, 255, 0

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, self._pos, self._radius)

    def update(self, dt, action):
        #self.color = GREEN
        
        fun = gravity2D
        t = 0
        self.state = propagate(fun, t, self.state, dt, action)

        self._pos = [int(self.state[0]), int(self.state[1])]
        
        #print(self.state)
