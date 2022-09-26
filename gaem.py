import math
import os
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

class Player:
    def __init__(self,x:int,y:int,sprite:str):
        self.x = x
        self.y = y
        self.sprite = sprite
class Loot:
    def __init__(self,x:int,y:int,sprite:str):
        self.x = x
        self.y = y
        self.sprite = sprite

def draw(entity):
    x = int(entity.x)
    y = int(entity.y)
    if player in entity.sprite:
        entity.sprite = player
    elif loot in entity.sprite:
        entity.sprite = loot
    for i in range(x):
        entity.sprite = distance + entity.sprite
    for i in range(y):
        entity.sprite = "\n{}".format(entity.sprite)
    return entity


def move(c_player:Player,direction):
    x = c_player.x
    y = c_player.y
    if direction == "right" or direction =="d":
        c_player.x = x + 1
        c_player = draw(c_player)
    elif direction == "left" or direction =="a":
        c_player.x = x - 1
        c_player = draw(c_player)
    elif direction == "up" or direction =="w":
        c_player.y = y - 1
        c_player = draw(c_player)
    elif direction == "down" or direction == "s":
        c_player.y = y + 1
        c_player = draw(c_player)
    else:
        c_player = draw(c_player)
    return c_player

def update_loot(d:int,loot,x:int,y:int,player,px:int,py:int):
    pass

def player_update(player:Player):
    if player.x > limit_x:
        player.x = limit_x
    elif player.y > limit_y:
        player.y = limit_y
    elif player.x < 0 :
        player.x = 0
    elif player.y < 0 :
        player.y = 0
    return player

def entity_update(player:Player,loot:Loot,direction:str):
    if direction == "right" or direction =="d":
        if player.y == loot.y:
            loot.x -= 1
    elif direction == "left" or direction =="a":
        if player.y == loot.y:
            loot.x += 1
    elif direction == "down" or direction =="s":
        loot.y -= 1
    elif direction == "up" or direction =="w":
        loot.y += 1
    return player,loot

c_player = Player(x,y,player)
c_loot = Loot(10, 10, loot)
while True:
    direction = input("You'r move : ")
    sleep(0.1)
    os.system('cls')
    direction = direction.lower()
    if direction == "esc":
        break
    c_player = move(c_player,direction)
    c_player = player_update(c_player)
    c_loot = draw(c_loot)
    c_player,c_loot = entity_update(c_player, c_loot, direction)
    print(c_player.sprite)
    print(c_loot.sprite)
    if c_player.y == c_loot.y :
        print(c_player.sprite,end='\r')
        print(c_loot.sprite)




