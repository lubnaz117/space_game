from enum import Enum

class Actions(Enum):
    # 0   No action
    # 1   Move left
    # 2   Move up
    # 3   Move right
    # 4   Move down
    # 5   Rotate counter-clockwise
    # 6   Rotate clockwise
    NONE    = 0
    LEFT    = 1
    UP      = 2
    RIGHT   = 3
    DOWN    = 4
    ROT_CCW = 5
    ROT_CW  = 6