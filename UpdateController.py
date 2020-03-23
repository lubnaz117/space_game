# Import non-standard modules.
import pygame
from pygame.locals import *

import sys

class UpdateController():
    '''
    This keeps track of what keys are being pressed and whether a key is being
    held.
    '''

    previous_action = 0

    def get_action(self):
        '''
        Actions:
        0   No action
        1   Move left
        2   Move up
        3   Move right
        4   Move down
        '''
        # No action
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
                    action = 1
                elif event.key == K_w or event.key == K_UP:
                    action = 2
                elif event.key == K_d or event.key == K_RIGHT:
                    action = 3
                elif event.key == K_s or event.key == K_DOWN:
                    action = 4          
            
            # Check key release event to stop action
            if event.type == KEYUP:
                action = 0
            
            #print(action)
            
        self.previous_action = action
        
        return action