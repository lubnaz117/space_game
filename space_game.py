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
    screen.fill((0, 0, 0)) # Fill the screen with black.
    ship.draw(screen)
    moon.draw(screen)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()

def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Initialize Spaceship
    ship = Spaceship()

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
    moon = Moon()

    # Main game loop
    while True: 
        action = update(controller, dt, ship, moon) 
        draw(screen, ship, moon)
        dt = fpsClock.tick(fps)

if __name__ == "__main__":
    runPyGame()