class Character:
    def __init__(self, name=None):
        self.name = name

    def attack(self, move, enemy):
        damage = self.moveset.get(move)
        enemy.health -= damage
        return damage

    def defend(self, damage):
        defense = self.defense
        self.health -= damage * (defense/100)


    def run(self):
        pass