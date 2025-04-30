from classes.gamemaster import GameMaster
from classes.playercharacters import Warrior
from classes.enemycharacters import Theif

game_master = GameMaster()
player = Warrior("xXGamerXx")
enemy = Theif()

while True:
    current_level = game_master.new_level()
    if game_master.level_complete == True:
        game_master.difficulty += 1
        current_level = game_master.new_level()


    print(enemy.health)
    enemy.attack("slash", player)
    player.attack("slash", enemy)
    print(enemy.health)