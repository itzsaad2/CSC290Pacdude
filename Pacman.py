from typing import List

class Pacman(Actor):
    movement_direction = "left" #movement_direction is either "left", "right", "up" or "down"

    def __init__(self, start_xpos: float, start_ypos: float):
        super().__init__(start_xpos, start_ypos, 5,
                         {"left": None, "right": None, "bottom": None, "up": None})

    def Move(self, barriers: List):
        #TODO: implement this
        # variable movement_direction specifies the direction pacman is going
        pass