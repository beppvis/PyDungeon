
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
game = Entity.Game("level1.txt")
print(Fore.GREEN+"────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n─██████████████─████████──████████─████████████───██████──██████─██████──────────██████─██████████████─██████████████─██████████████─██████──────────██████─\n─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░████─██░░██──██░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████──██░░██─\n─██░░██████░░██─████░░██──██░░████─██░░████░░░░██─██░░██──██░░██─██░░░░░░░░░░██──██░░██─██░░██████████─██░░██████████─██░░██████░░██─██░░░░░░░░░░██──██░░██─\n─██░░██──██░░██───██░░░░██░░░░██───██░░██──██░░██─██░░██──██░░██─██░░██████░░██──██░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██████░░██──██░░██─\n─██░░██████░░██───████░░░░░░████───██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██─────────██░░██████████─██░░██──██░░██─██░░██──██░░██──██░░██─\n─██░░░░░░░░░░██─────████░░████─────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██──██████─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██──██░░██─\n─██░░██████████───────██░░██───────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░██──██░░██─██░░██──██░░██──██░░██─\n─██░░██───────────────██░░██───────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██████░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██──██░░██████░░██─\n─██░░██───────────────██░░██───────██░░████░░░░██─██░░██████░░██─██░░██──██░░░░░░░░░░██─██░░██████░░██─██░░██████████─██░░██████░░██─██░░██──██░░░░░░░░░░██─\n─██░░██───────────────██░░██───────██░░░░░░░░████─██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██████████░░██─\n─██████───────────────██████───────████████████───██████████████─██████──────────██████─██████████████─██████████████─██████████████─██████──────────██████─\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
#stime.sleep(3)
os.system('cls')
print(Fore.WHITE+ game.lv1_draw())
while not game.game_over :


    direction = input(Fore.CYAN+"You'r move : ")
    os.system("cls")
    direction = direction.lower()
    if direction == "esc":
        game.lvl_save()
        break
    game.player.move(direction)
    print(game.lv1_draw())




