
import os
from colorama import Fore
import Entity
import time
from time import sleep

player = None
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
with open("assets/pydungeon.txt",encoding="utf8") as title_f:
    title = title_f.read()
    print(Fore.GREEN + title)
    time.sleep(1)
level_1 = Entity.Level("assets/level1.txt",1)
level_2 = Entity.Level("assets/level2.txt",2)
level_3 = Entity.Level("assets/level3.txt",3)
level_4 = Entity.Level("assets/level4.txt",4)
curr_lvl = level_1
#time.sleep(3)
print(os.name)
if os.name =="posix":
    os.system("clear")
else:
    os.system("cls")
while not game_over:
    if player != None:
        nxt_lvl, player = curr_lvl.run(player)
        game_over = curr_lvl.game_obj.game_over
        
    else:
        nxt_lvl,player = curr_lvl.run() 
        game_over = curr_lvl.game_obj.game_over
    if nxt_lvl == 1:
        curr_lvl = level_1
    elif nxt_lvl == 2:
        curr_lvl = level_2
    elif nxt_lvl == 3:
        curr_lvl = level_3
    elif nxt_lvl == 4:
        curr_lvl = level_4  
    elif nxt_lvl == -1:
        break
    elif nxt_lvl == 0:
        f = open("assets/thankyou.txt")
        thankyou = f.read()
        print(thankyou)
        f.close()
        time.sleep(3)
        break
    player.game = curr_lvl.game_obj
    game_over = curr_lvl.game_obj.game_over



