from classes.playercharacters import Warrior
from classes.enemycharacters import Theif
# char_selection = input("Select your character: ")

player = Warrior("xXGamerXx")
enemy = Theif()

print(enemy.health)
enemy.attack("slash", player)
player.attack("slash", enemy)
print(enemy.health)