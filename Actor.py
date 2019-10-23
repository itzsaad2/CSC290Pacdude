from typing import List
import math, main

class Actor:
    xpos = 0
    ypos = 0
    mvspeed = 0.0
    sprites = [] #resolution should be RES_WIDTH x RES_HEIGHT

    def is_touching(self, other: Actor) -> bool:
        """
        Determines if this object is touching another object, other,
        using circular based collision detection.
        """

        if (math.sqrt(((self.xpos + main.RES_WIDTH) - (other.xpos + main.RES_WIDTH ))^ 2 
                    + ((other.xpos + main.RES_WIDTH) - (other.ypos + main.RES_HEIGHT))^ 2) <= 10):
            return True
        return False

        
    def __init__(self, xpos: float, ypos: float, mvspeed: float, sprites: List):
        
        self.xpos = xpos
        self.ypos = ypos
        self.mvspeed = mvspeed
        self.sprites = sprites