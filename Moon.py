import pygame
from pygame.locals import *

from dynamics import *

import random
class Moon(pygame.sprite.Sprite):


    def __init__(self, screen_size):
        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        self.SCREEN_WIDTH            = screen_size[0]
        self.SCREEN_HEIGHT           = screen_size[1]

        self.SURFACE_HEIGHT_MEAN     = self.SCREEN_HEIGHT - 100
        self.rect      = (0, self.SURFACE_HEIGHT_MEAN, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self._surface_points = self.generate_craters()

    def draw(self, screen):

        SURFACE_COLOR = 120, 120, 120 # gray

        pygame.draw.polygon(screen, SURFACE_COLOR, self._surface_points)

    def generate_craters(self):
        CRATER_HEIGHT_MEAN      = self.SCREEN_HEIGHT - 50

        SURFACE_RESOLUTION  = 40 # how many pixels in a surface "block"
        # Note: 40 seems good for the width of the lander

        CRATER_WIDTH        = SURFACE_RESOLUTION

        # list of points on x axis from 0 to SCREEN_WIDTH
        # start list with left corner of screen
        # first point is a surface point
        # we do this to create a polygon
        surface = [
                    (0,self.SCREEN_HEIGHT),
                    (0,self.SURFACE_HEIGHT_MEAN)
                    ]
    
        x_pts = range(50, self.SCREEN_WIDTH, SURFACE_RESOLUTION)
        
        # create 5 random craters
        crater_pts = random.sample(x_pts, 5) 

        # iterate throught the list of xaxis points, if theres a crater generate a crater height
        for x_pt in x_pts:
            if x_pt in crater_pts:
                crater_height = CRATER_HEIGHT_MEAN*(1 + random.randrange(-2, 2)/100) # this varies the depth of the crater by +/- 3%
                # create a trapezoid shaped crater
                surface.append( (x_pt-CRATER_WIDTH/2, crater_height) )
                surface.append( (x_pt, crater_height) )
                surface.append( (x_pt+CRATER_WIDTH/2, crater_height) )
            else:
                surface_height = self.SURFACE_HEIGHT_MEAN*(1 + random.randrange(-2, 2)/100) # this varies the height of the surface by +/- 3%
                surface.append( (x_pt, surface_height) )
        
        # add last point to close the polygon
        surface.append( (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        
        return surface

    def update(self, dt, action):

        # fun = gravity2D
        t = 0
        # self.state = propagate(fun, t, self.state, dt, action)

        
        #print(self.state)
