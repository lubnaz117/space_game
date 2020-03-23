import pygame
from pygame.locals import *

from dynamics import *

class Spaceship():
    fuel = 100
    main_isp = 1
    acs_isp = 1

    def __init__(self):
        # Initial state: [x, y, vx, vy]
        self.state = np.array([50, 50, 0.05, 0])
        
        # Load lander image
        self.graphic = pygame.image.load('graphics/lander.png')
        self.graphic = pygame.transform.scale(self.graphic, (50, 50))

    def draw(self, screen):
        # Position on screen
        x = int(self.state[0])
        y = int(self.state[1])
        screen.blit(self.graphic, (x, y))
        
    def update(self, dt, action):
    
        # Interpret action
        T = 0.0005
        if action == 0:
            u = np.array([0, 0])
        elif action == 1:
            u = np.array([-T, 0])
        elif action == 2:
            u = np.array([0, -T])
        elif action == 3:
            u = np.array([T, 0])        
        elif action == 4:
            u = np.array([0, T]) 
    
        # Propagate spaceship
        fun = gravity2D
        self.state = propagate(fun, 0, self.state, dt, u)