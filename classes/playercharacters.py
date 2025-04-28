from character import Character
import random

character_list = ["Warrior", "Brute", "Ninja", "Healer"]

class Warrior(Character):
    def __init__(self, name):
        super().__init__()
        self.health = 100
        self.defense = 14
        self.moveset = {
            "slash": 25,
            "sheild": {"defense": 10}
        }

class Brute(Character):
    def __init__(self, name):
        super().__init__()
        self.health = 200
        self.defense = 38
        self.moveset = {
            "punch": {"damage": 35},
            "roar": {"damage": 15}
        }

class Ninja(Character):
    def __init__(self, name):
        super().__init__()
        self.health = 70
        self.defense = 7
        self.moveset = {
            "shuriken": {"damage": 30},
            "dodge": {random.randint(0, 1)} #0 means didnt doge 1 means dodged move
        }

class Healer(Character):
    def __init__(self):
        super().__init__()
        self.defense = 10
        self.moveset = {
            "staff-strike": {"damage": 15},
            "heal": {"heal": 15}
        }