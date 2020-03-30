import pygame
from pygame.locals import *

# Screen Size
SCREEN_WIDTH    = 1200
SCREEN_HEIGHT   = 800

# Text
# -- Font
pygame.font.init() # TBH unsure if this is okay but it sees to work
font = pygame.font.Font(pygame.font.get_default_font(), 40)
# -- Positions
text_xy_FPS     = (10, 10)
text_xy_ALT     = (10, 60)
text_xy_VELY    = (10, 110)
text_xy_RIP     = (SCREEN_WIDTH/2, 40)