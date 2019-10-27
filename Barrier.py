from typing import List
import pygame, Actor

class Barrier(Actor):

    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, sprite):
        super().__init__(start_xpos, start_ypos, width, height, 0, sprite)
       
    # Overrides the Actor's move methods below, since the Barriers cannot move.
    def move_left(self) -> None:
        return None
    
    def move_right(self) -> None:
        return None
    
    def move_up(self) -> None:
        return None
    
    def move_down(self) -> None:
        return None
