# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *

# Import custom classes
from Spaceship import *
 
def update(dt, ship):
    """
    Update game. Called once per frame.
    """
    action = np.array([0, 0])
    T = 0.005
    
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        
        
        if event.type == KEYDOWN:

            if event.key == 115 or event.key == 274:
                action = np.array([0, T])
            elif event.key == 119 or event.key == 273:
                action = np.array([0, -T])
            elif event.key == 100 or event.key == 275:
                action = np.array([T, 0])
            elif event.key == 97 or event.key == 276:
                action = np.array([-T, 0])            
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
            
    ship.update(dt, action)

    
def draw(screen, ship):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0)) # Fill the screen with black.
    ship.draw(screen)

    # Redraw screen here.

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()
 
def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Initialize Spaceship
    ship = Spaceship()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 30.0
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = 1000, 480
    screen = pygame.display.set_mode((width, height))

    # Main game loop.
    dt = 1 / fps
    while True:
        # Update ship and draw
        update(dt, ship) 
        draw(screen, ship)
    
        # Get time since last frame.
        dt = fpsClock.tick(fps)

if __name__ == "__main__":
    runPyGame()