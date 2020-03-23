import pygame
from pygame.locals import *

from dynamics import *

class Spaceship():

    def __init__(self):
        # Initial state: [x, y, vx, vy]
        self.state = np.array([50, 50, 0.05, 0])
        
        # Load lander image
        self.graphic = pygame.image.load('graphics/lander.png')
        self.graphic = pygame.transform.scale(self.graphic, (50, 50))

    def draw(self, screen):
        #self._pos = [int(self.state[0]), int(self.state[1])]

        x = int(self.state[0])
        y = int(self.state[1])
        
        screen.blit(self.graphic, (x, y))
        
    def update(self, dt, action):
        
        fun = gravity2D
        t = 0
        self.state = propagate(fun, t, self.state, dt, action)
        
        #print(self.state)
