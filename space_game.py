# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *

# Import custom classes
from Spaceship import *
from Moon import *
from UpdateController import *

def update(controller, dt, ship, moon):
    """
    Update game. Called once per frame.
    """
    action = controller.get_action()
    ship.update(dt, action)

def draw(screen, ship, moon):
    """
    Draw things to the window. Called once per frame.
    """

    screen_color = check_crash(ship, moon)
    screen.fill(screen_color) # Fill the screen with black.
    ship.draw(screen)
    moon.draw(screen)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()

def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Set up the clock
    fps = 60.0
    dt = 1 / fps 
    fpsClock = pygame.time.Clock()

    # Set up the window.
    screen_size = (1200, 800) # width, height
    screen = pygame.display.set_mode(screen_size)
        
    # Intialize input controller
    controller = UpdateController()
    
    # Initialize Spaceship
    ship = Spaceship()
    moon = Moon(screen_size)

    # Setup Sprites:
    sprite_list = pygame.sprite.Group()
    sprite_list.add(ship)
    sprite_list.add(moon) # TODO: The moon surface points are gonn have to be individual sprites

    # Main game loop
    while True: 
        action = update(controller, dt, ship, moon) 
        draw(screen, ship, moon)
        dt = fpsClock.tick(fps)

def check_crash(ship, moon):
    is_crashed = pygame.sprite.collide_rect(ship, moon)

    if is_crashed == True:
        return (255, 0, 0) # red 
    else:
        return (0, 0, 0) # black

if __name__ == "__main__":
    runPyGame()