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
    is_crashed = check_crash(ship, moon)
    
    ship.update(dt, action, is_crashed)

def draw(screen, ship, moon, fps):
    """
    Draw things to the window. Called once per frame.
    """
    #is_crashed = check_crash(ship, moon)
    #screen_color = check_screen_color(is_crashed)
    #screen.fill(screen_color)
    screen.fill((0, 0, 0))
    
    # TODO: make screen text object
    
    # Display FPS
    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    text_surface = font.render(str(int(fps)), True, (0, 255, 0))
    screen.blit(text_surface, (10, 10))
    
    # Draw sprites
    ship.draw(screen)
    moon.draw(screen)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()

def runPyGame():
    # Initialise PyGame.
    pygame.init()
    pygame.font.init()

    # Set up the clock
    fps = 60
    dt = 1 / fps 
    clock = pygame.time.Clock()

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
        # Update sprites
        update(controller, dt, ship, moon)
        
        # Get time stuff
        dt = clock.tick(fps)
        fps_real = clock.get_fps()
        
        # Update screen
        draw(screen, ship, moon, fps_real)
        

def check_crash(ship, moon):
    return pygame.sprite.collide_rect(ship, moon)

def check_screen_color(is_crashed):
    if is_crashed == True:
        return (255, 0, 0) # red 
    else:
        return (0, 0, 0) # black
        
if __name__ == "__main__":
    runPyGame()