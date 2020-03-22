import pygame
from pygame.locals import *

from dynamics import *

class Spaceship():

    def __init__(self):
        # Initial state: [x, y, vx, vy]
        self.state = np.array([50, 50, 0.05, 0])
        
        
        self._pos = [self.state[0], self.state[1]]
        self._radius = 10
        self._color = 0, 255, 0
        
        # Load image
        self.graphic = pygame.image.load('graphics/lander.png')
        self.graphic = pygame.transform.scale(self.graphic, (50, 50))

    def draw(self, screen):
        self._pos = [int(self.state[0]), int(self.state[1])]

        #pygame.draw.circle(screen, self._color, self._pos, self._radius)
        
        x = int(self.state[0])
        y = int(self.state[1])
        
        screen.blit(self.graphic, (x, y))
        
    def update(self, dt, action):
        
        fun = gravity2D
        t = 0
        self.state = propagate(fun, t, self.state, dt, action)
        
        #print(self.state)
