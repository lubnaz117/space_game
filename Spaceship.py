import pygame
from pygame.locals import *

from dynamics import *

class Spaceship(pygame.sprite.Sprite):
    fuel = 100
    main_isp = 1
    acs_isp = 1
    
    # Initial state: [x, y, vx, vy, th, omega]
    state = np.array([50, 50, 0.05, 0, 0, 0])

    def __init__(self): 
        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Load lander image    
        image = pygame.image.load('graphics/lander.png')
        image = pygame.transform.scale(image, (50, 50))       
        self.image = image

        self.rect = image.get_rect()

        self.width = self.rect.w
        self.height = self.rect.h
                
    def draw(self, screen):
        # Position on screen
        self.rect.x = int(self.state[0])
        self.rect.y = int(self.state[1])
        theta = int(self.state[4])

        graphic = pygame.transform.rotate(self.image, theta)
        
        screen.blit(graphic, (self.rect.x, self.rect.y))
        
    def update(self, dt, action):
    
        # Interpret action
        T = 0.0009
        if action == 0:
            u = np.array([0, 0, 0])
        elif action == 1:
            u = np.array([-T, 0, 0])
        elif action == 2:
            u = np.array([0, -T, 0])
        elif action == 3:
            u = np.array([T, 0, 0])        
        elif action == 4:
            u = np.array([0, T, 0])
        elif action == 5:
            u = np.array([0, 0, T]) 
        elif action == 6:
            u = np.array([0, 0, -T]) 
    
        # Propagate spaceship
        fun = gravity2DAttitude
        self.state = propagate(fun, 0, self.state, dt, u)