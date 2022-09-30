import math
import os
import functions
import Entity
from time import sleep

player = "0"
distance = "  "
x = 0
y = 0
limit_x = 100
limit_y = 100
down = "\n"
loot = "L"
l_x =10
l_y = 10
d=0


c_player = Entity.Player(x,y,player)
c_loot = Entity.Loot(10, 10, loot)
while True:
    direction = input("You'r move : ")
    sleep(0.1)
    os.system('cls')
    direction = direction.lower()
    if direction == "esc":
        break
    c_player = functions.move(c_player,direction)
    c_loot = functions.draw(c_loot)
    c_player,c_loot = functions.entity_update(c_player, c_loot, direction)
    c_player = functions.player_update(c_player)
    game = c_player.sprite + '\r' + c_loot.sprite
    print(game)




