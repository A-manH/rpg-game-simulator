from enemycharacters import *

class Level:
    def new(self, difficulty):
        enemies = []
        for i in range(difficulty):
            enemy = Theif()
            enemies.append(enemy)

        return enemies