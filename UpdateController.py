# Import non-standard modules.
import pygame
from pygame.locals import *

import sys

from Actions import *

class UpdateController():
    """
    This keeps track of what keys are being pressed and whether a key is being
    held.
    """

    previous_action = Actions.NONE

    def get_action(self):
        
        # Get previous action
        action = self.previous_action
    
        # Go through events that are passed to the script by the window.
        for event in pygame.event.get():
            # Check for close
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 

            # Check key press event
            if event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    action = Actions.LEFT
                elif event.key == K_w or event.key == K_UP:
                    action = Actions.UP
                elif event.key == K_d or event.key == K_RIGHT:
                    action = Actions.RIGHT
                elif event.key == K_s or event.key == K_DOWN:
                    action = Actions.DOWN
                elif event.key == K_q or event.key == K_PAGEUP:
                    action = Actions.ROT_CCW
                elif event.key == K_e or event.key == K_PAGEDOWN:
                    action = Actions.ROT_CW
            
            # Check key release event to stop action
            if event.type == KEYUP:
                action = Actions.NONE 
        
        # Save action
        self.previous_action = action
        
        return action