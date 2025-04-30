from playercharacters import *
from level import Level

class GameMaster:
    def __init__(self):
        self.current_monsters = 0
        self.difficulty = 0
        self.level_complete = True if len(self.new_level()) == 0 else False

    def new_level(self, difficulty):
        level = Level()
        return level.new(difficulty)

    def next_turn(self):
        pass