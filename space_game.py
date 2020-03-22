# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *

# Import custom classes
from Spaceship import *
from Moon import *

 
def update(dt, ship, moon):
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
        
        # Movement keys
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
<<<<<<< HEAD
            
    # Update state
=======

>>>>>>> 1996b6e351b1172a0fa973266b82598712baf102
    ship.update(dt, action)
    moon.update(dt, action)

def draw(screen, ship, moon):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0)) # Fill the screen with black.
    ship.draw(screen)
    moon.draw(screen)

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
    screen_size = (1200, 1200) # width, height
    screen = pygame.display.set_mode(screen_size)

    # Initialize Spaceship
    ship = Spaceship()
    moon = Moon()

    # Main game loop.
    dt = 1/fps # dt is the time since last frame.
    while True: # Loop forever!
        action = update(dt, ship, moon) 
        
        draw(screen, ship, moon)

        dt = fpsClock.tick(fps)

if __name__ == "__main__":
    runPyGame()