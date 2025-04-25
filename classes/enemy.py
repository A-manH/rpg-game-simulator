from classes.character import Character

class Theif(Character):
    def __init__(self):
        super().__init__()
        self.health = 95
        self.moveset = {
            "stab": {"damage": 15},
        }