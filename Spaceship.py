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
 
    def draw(self, screen):
        # Rotate image
        theta = int(self.state[4])
        #graphic = pygame.transform.rotate(self.image, theta)
    
        # Position on screen
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
        
        
    def update(self, dt, action, is_crashed):
        """
        Spaceship physics
        """
    
        # Interpret action
        T = 4E-4
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