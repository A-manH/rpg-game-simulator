from classes.characters import Warrior
from classes.enemy import Theif
# char_selection = input("Select your character: ")

player = Warrior("xXGamerXx")
enemy = Theif()

print(enemy.health)
player.attack("slash", enemy)
print(enemy.health)