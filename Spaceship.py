import pygame
from pygame.locals import *

from dynamics import *

import space_game_config as settings

class Spaceship(pygame.sprite.Sprite):
    fuel = 100
    main_isp = 1
    acs_isp = 1
    altitude = 1500
    
    # Initial state: [x, y, vx, vy, th, omega]
    state = np.array([0, 0, 0.05, 0, 0, 0]) # Other states allocated in init()

    def __init__(self):
        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Load lander image    
        image = pygame.image.load('graphics/lander.png')
        image = pygame.transform.scale(image, (50, 50))       
        self.image = image

        self.rect = image.get_rect()

        # Initial state: [x, y, vx, vy, th, omega]
        state = np.array([50, self.altitude, 0.05, 0, 0, 0])

    def draw(self, screen):
        # Rotate image
        theta = int(self.state[4])
        graphic = pygame.transform.rotate(self.image, theta)
    
        # Position on screen
        if self.altitude > settings.SCREEN_HEIGHT:
            self.rect.x = int(self.state[0])
            self.rect.y = 50
        else:
            self.rect.x = int(self.state[0])
            self.rect.y = int(self.state[1])
        
        # Draw on screen
        screen.blit(graphic, (self.rect.x, self.rect.y))

        self.disp_alt(screen)
        self.disp_vel(screen)

    def disp_alt(self, screen):
        text_surface = settings.font.render(
            'Altitude: '
            + str(int(self.altitude)),
            True, (255, 0, 0))
        screen.blit(text_surface, settings.text_xy_ALT)

    def disp_vel(self, screen):
        text_surface = settings.font.render(
            'Vel Y:  '
            + str(-int(self.state[3]*1000)), # Oof switch this direction so - means down
            True, (0, 0, 250))
        screen.blit(text_surface, settings.text_xy_VELY)
        
    def update(self, dt, action, is_crashed):
        """
        Spaceship physics
        """
    
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
            
        # Check crash
        if is_crashed:
            bounce(self.state)
    
        # Propagate spaceship
        fun = gravity2DAttitude
        self.state = propagate(fun, 0, self.state, dt, u)

        # Calculate Altitude
        self.altitude = settings.SCREEN_HEIGHT - self.state[1]