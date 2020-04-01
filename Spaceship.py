import pygame
from pygame.locals import *

from dynamics import *

import space_game_config as settings
from   Actions import *

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
        #graphic = pygame.transform.rotate(self.image, theta)
    
        # Position on screen
        if self.altitude > settings.SCREEN_HEIGHT:
            self.rect.x = int(self.state[0])
            self.rect.y = 50
        else:
            self.rect.x = int(self.state[0])
            self.rect.y = int(self.state[1])
        
        # Draw on screen
        # screen.blit(graphic, (self.rect.x, self.rect.y))
        
        # ------------------ Test for new rotation ------------------------
        angle = theta
        w = 25
        h = 25
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])     
        
        pivot = pygame.math.Vector2(w/2, -h/2)
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot
        
        origin = (self.rect.x + min_box[0] - pivot_move[0], self.rect.y - max_box[1] + pivot_move[1])

        rotated_image = pygame.transform.rotate(self.image,angle)
        screen.blit(rotated_image, origin)
        
        #screen.blit(graphic, (self.rect.x, self.rect.y))

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
        if action == Actions.NONE:
            u = np.array([0, 0, 0])
        elif action == Actions.LEFT:
            u = np.array([-T, 0, 0])
        elif action == Actions.UP:
            u = np.array([0, -T, 0])
        elif action == Actions.RIGHT:
            u = np.array([T, 0, 0])
        elif action == Actions.DOWN:
            u = np.array([0, T, 0])
        elif action == Actions.ROT_CCW:
            u = np.array([0, 0, T]) 
        elif action == Actions.ROT_CW:
            u = np.array([0, 0, -T])
            
        # Check crash
        if is_crashed:
            bounce(self.state)
    
        # Propagate spaceship
        fun = gravity2DAttitude
        self.state = propagate(fun, 0, self.state, dt, u)

        # Calculate Altitude
        self.altitude = settings.SCREEN_HEIGHT - self.state[1]