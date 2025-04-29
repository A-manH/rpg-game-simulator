from enemycharacters import *

class Level:
    def new(self, difficulty):
        enemies = []
        for i in self.difficulty:
            enemy = Theif()
            enemies.append(enemy)

        return enemies        