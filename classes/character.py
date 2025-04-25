class Character:
    def __init__(self, name=None):
        self.name = name

    def attack(self, move, enemy):
        damage = self.moveset.get[move]
        return damage

    def defend(self):
        pass

    def run(self):
        pass