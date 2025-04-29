from playercharacters import *
from level import Level

class GameMaster:
    def __init__(self):
        self.current_monsters = 0
        self.round = 1
    
    def new_level(self, difficulty):
        round += 1
        level = Level()
        level.new(difficulty)

    def next_turn(self):
        pass