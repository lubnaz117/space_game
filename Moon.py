import pygame
from pygame.locals import *

from dynamics import *
from MoonSurface import *
import space_game_config as settings

import random
class Moon(pygame.sprite.Sprite):


    def __init__(self):
        # Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        self.SURFACE_HEIGHT_MEAN     = settings.SCREEN_HEIGHT - 100
        self.rect      = (0, self.SURFACE_HEIGHT_MEAN, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        self.SURFACE_RESOLUTION  = 100 # how many pixels in a surface "block"
        # Note: 40 seems good for the width of the lander
        
        self._surface_sprites = self.generate_craters()


    def draw(self, screen):
        """
        Draw the whole moon surface as a polygon connecting all the surface sprites
        NOTE: This method creates ez crater trapezoids :)
        """

        SURFACE_COLOR = 120, 120, 120 # gray
        CRATER_WIDTH  = self.SURFACE_RESOLUTION

        draw_pts = [( 0,settings.SCREEN_HEIGHT)]

        for piece in self._surface_sprites:
            if piece.IS_CRATER:
                # create a trapezoid shaped crater
                draw_pts.append((piece.rect.x + 0.2*CRATER_WIDTH, piece.rect.y))
                draw_pts.append((piece.rect.x + 0.8*CRATER_WIDTH, piece.rect.y))
            else:
                draw_pts.append((piece.rect.x, piece.rect.y))
                draw_pts.append((piece.rect.x + CRATER_WIDTH, piece.rect.y))
        
        draw_pts.append((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.draw.polygon(screen, SURFACE_COLOR, draw_pts)

    def generate_craters(self):
        CRATER_HEIGHT_MEAN      = settings.SCREEN_HEIGHT - 20

        CRATER_WIDTH        = self.SURFACE_RESOLUTION
        NUM_CRATERS         = 2

        x_pts = range(0, settings.SCREEN_WIDTH, self.SURFACE_RESOLUTION)
        
        # create X random craters
        crater_pts = random.sample(x_pts, NUM_CRATERS) 

        surface_pieces = []
        # iterate throught the list of xaxis points, if theres a crater generate a crater height
        for x_pt in x_pts:
            new_surface = MoonSurface()

            if x_pt in crater_pts:
                new_surface.IS_CRATER = True
                crater_height = CRATER_HEIGHT_MEAN*(1 + random.randrange(-2, 2)/100) # this varies the depth of the crater by +/- 3%
                new_surface.rect = pygame.Rect(x_pt, crater_height, CRATER_WIDTH, crater_height)
            else:
                new_surface.IS_CRATER = False
                surface_height = self.SURFACE_HEIGHT_MEAN*(1 + random.randrange(-2, 2)/100) # this varies the height of the surface by +/- 3%
                new_surface.rect = pygame.Rect(x_pt, surface_height, CRATER_WIDTH, surface_height)

            surface_pieces.append(new_surface)
        
        return surface_pieces

    def update(self, dt, action):
        # TODO: This should update with horizonal scroll?
        t = 0