# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import  pygame
from    pygame.locals import *

# Import custom classes
from Spaceship import *
from Moon import *
from UpdateController import *

import  space_game_config as settings
from    space_game_helpers import *

def update(controller, dt, ship, moon):
    """
    Update game. Called once per frame.
    """
    action = controller.get_action()
    is_crashed = check_crash(ship, moon)
    
    ship.update(dt, action, is_crashed)

def draw(screen, ship, moon, fps):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))
    
    # Check for collision
    is_crashed = check_crash(ship, moon)
    # Display Crash
    if is_crashed:
        text_surface = settings.font.render('RIP :(', True, (255, 0, 0))
        screen.blit(text_surface, settings.text_xy_RIP)
        #screen_color = check_screen_color(is_crashed)
        #screen.fill(screen_color)

    # Display FPS
    text_surface = settings.font.render('FPS: ' + str(int(fps)), True, (0, 255, 0))
    screen.blit(text_surface, settings.text_xy_FPS)

    # Draw ship
    ship.draw(screen)

    # Draw moon if ship is low enough
    if ship.altitude < settings.SCREEN_HEIGHT:
        moon.draw(screen)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()

def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Set up the clock
    fps = 60
    dt = 1 / fps 
    clock = pygame.time.Clock()

    # Set up the window.
    screen_size = (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
        
    # Intialize input controller
    controller = UpdateController()
    
    # Initialize Spaceship
    ship = Spaceship()
    moon = Moon()

    # Setup Sprites:
    sprite_list = pygame.sprite.Group()
    sprite_list.add(ship)
    sprite_list.add(moon) # TODO: The moon surface points are gonn have to be individual sprites

    # Main game loop
    while True:
        # Update sprites
        update(controller, dt, ship, moon)
        
        # Get time stuff
        dt = clock.tick(fps)
        fps_real = clock.get_fps()
        
        # Update screen
        draw(screen, ship, moon, fps_real)

if __name__ == "__main__":
    runPyGame()