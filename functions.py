from html import entities
from typing import List
import Entity


player = "O"
distance = "  "
tile = "#"
limit_x = 49
limit_y = 17
down = "\n"
loot = "L"

#*TOD0 :assinging ints for each class
playerInt = 0
lootInt = 1
tileInt = 2

#! assinging world limit for the world
worldLimitY = 100
worldLimitX = 100

#* Remeber to add all types here for reffereral 
tile_type = "TileSet"
loot_type = "Loot"
player_type ="Player"


def lvl_collision(entities:list):
    #* At last got to collision
    pass

def sort_lvl(entities:list):
    sorted_list = []
    makeShiftList = []
    x = 1
    y = 0
    i = 0
    for i in entities:
        makeShiftList.append((i.y,i.x,i.sprite))
    makeShiftList.sort()
    for i in makeShiftList:
        entity = classify(i[2],i[1],i[0])
        sorted_list.append(entity)
    return sorted_list

def lvl_load(filename:str):
    entities = []
    x = 0
    y = 0
    lvl_file = open(filename,'r')
    lvl_string = lvl_file.read()
    for i in lvl_string:
        x += 1
        if x > 50:
            x = 1
            y +=1
        if i == player:
            # print("player : ",x," ",y)
            entities.append(Entity.Player(x,y,player))
        elif i == tile:
            # print("tile : ",x," ",y)
            entities.append(Entity.Tile(x,y,tile))
        elif i == loot:
            # print("loot : ",x," ",y)
            entities.append(Entity.Loot(x,y,loot))
    return entities

def lvl_draw(entities:list):
    game = ""
    af_y = 0
    y = 0
    x = 1
    i = 0
    # out of range check
    entities = sort_lvl(entities)

    while i<len(entities):
        if x > 50:
            x = 1
            y += 1 # incrementing the y value
        if entities[i].y == y and entities[i].x == x:
            if af_y != entities[i].y :
                game = game + "\n" + entities[i].sprite
                af_y = entities[i].y
                x += 1
                if not i > len(entities):
                    i += 1
                else:
                    break

            else :
                if not i > len(entities)-1:
                    game = game + entities[i].sprite
                    x += 1
                    i += 1
        else:
            game = game + " "
            x += 1
                #if  i != 0:
                    #i -= 1
                #else:
                    #i += 1
    return game

def classify(Sprite:str,x:int,y:int):
    if Sprite == player:
        Etype = playerInt
    elif Sprite == loot:
        Etype = lootInt
    elif Sprite == tile:
        Etype = tileInt
    if Etype == playerInt:
        c = Entity.Player(x,y,player)
        sprite = player
    elif Etype == lootInt:
        c = Entity.Loot(x,y,loot)
        sprite = loot
    elif Etype == tileInt:
        c = Entity.Tile(x,y,tile)
        sprite = tile
    return c

def draw(entity):
    if entity.type != tile_type:
        x = int(entity.x)
        y = int(entity.y)
        if player in entity.sprite:
            entity.sprite = player
        elif loot in entity.sprite:
            entity.sprite = loot
        entity.sprite = distance*x + entity.sprite
        entity.sprite = "\n"*y + entity.sprite
        return entity



def move(c_player:Entity.Player,direction):
    x = c_player.x
    y = c_player.y
    if direction == "right" or direction =="d":
        c_player.af_x = x
        c_player.af_y = y
        c_player.x = x + 1
        c_player = draw(c_player)
    elif direction == "left" or direction =="a":
        c_player.af_x = x
        c_player.af_y = y
        c_player.x = x - 1
        c_player = draw(c_player)
    elif direction == "up" or direction =="w":
        c_player.af_x = x
        c_player.af_y = y
        c_player.y = y - 1
        c_player = draw(c_player)
    elif direction == "down" or direction == "s":
        c_player.af_x = x
        c_player.af_y =  y
        c_player.y = y + 1
        c_player = draw(c_player)
    else:
        c_player = draw(c_player)
    return c_player


def player_update(entities:list,direction:str):
    tiles = []
    loot = []
    #entities = sort_lvl(entities=entities)
    # for i in entities:
    #     if type(i) == Entity.Player:
    #         player = i

    if direction == "a":
        for entity in entities:
            if type(entity) == Entity.Player:
                entity.x -= 1
    elif direction == "d":
        for entity in entities:
            if type(entity) == Entity.Player:
                entity.x += 1
    elif direction == "w":
        for entity in entities:
            if type(entity) == Entity.Player:
                entity.y -= 1

    elif direction == "s":
        for entity in entities:
            if type(entity) == Entity.Player:
                entity.y += 1

    return entities
        

def update_loot(d:int,loot,x:int,y:int,player,px:int,py:int):
    pass

# def player_update(player:Entity.Player):
#     if player.x > limit_x:
#         player.x = limit_x
#     elif player.x < 0 :
#         player.x = 0
#     elif player.y < 0 :
#         player.y = 0
#     return player

def entity_update(C_player,C_loot,direction:str):
    if direction == "right" or direction =="d":
        if C_player.y != C_loot.c_y:C_loot.x = C_loot.c_x
        C_loot.x -= 1
    elif direction == "left" or direction =="a":
        if C_player.y != C_loot.c_y:C_loot.x = C_loot.c_x
        C_loot.x += 1
    elif direction == "down" or direction =="s" :
        C_loot.y -= 1
    elif direction == "up" or direction =="w" and C_player.y != C_loot.y :
        C_loot.y += 1
    return C_player,C_loot

