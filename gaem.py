
import os
import functions
from colorama import Fore
import Entity
import time
from time import sleep

player = "0"
distance = "  "
tile_sprite = "#"
x = 0
y = 0
limit_x = 100
limit_y = 100
down = "\n"
loot = "L"
l_x =10
l_y = 10
game_over = False

d=0
#* r is used to disable special characters

# c_player = Entity.Player(x,y,player)
# c_loot = Entity.Loot(10, 10, loot)
# tile_data = functions.tile_data('tiles.json')
entities = functions.lvl_load("level1.txt")
print(Fore.GREEN+"██████╗░██╗░░░██╗██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░  ███╗░░██╗\n██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗  ████╗░██║\n██████╔╝░╚████╔╝░██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║  ██╔██╗██║\n██╔═══╝░░░╚██╔╝░░██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║  ██║╚████║\n██║░░░░░░░░██║░░░██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝  ██║░╚███║\n╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░  ╚═╝░░╚══╝")
time.sleep(3)
os.system('cls')
game = functions.lvl_draw(entities)
print(Fore.WHITE + game)
while game_over == False:


    direction = input(Fore.CYAN+"You'r move : ")
    os.system("cls")
    direction = direction.lower()
    if direction == "esc":
        break
    entities,game_over = functions.player_update(entities,direction)
    if game_over:
        break
    entities,game_over = functions.enemy_update(entities)
    if game_over:
        break
    game = functions.lvl_draw(entities=entities)
    print(game)

    # c_player = functions.move(c_player,direction)
    # c_player = functions.player_update(c_player)
    # c_player,c_loot = functions.entity_update(c_player, c_loot, direction)
    # c_loot = functions.draw(c_loot)
    # tile_string = functions.tile_draw(tile_data,tile_sprite)
    # game = c_player.sprite + c_loot.sprite
    # print(game)




