from html import entities
from typing import List
from colorama import Fore, Back, Style
import math
import Entity

enemy = "X"
player = "O"
distance = "  "
tile = "#"
tileSprite = Fore.GREEN + tile
limit_x = 49
limit_y = 17
down = "\n"
loot = "L"

#*TOD0 :assinging ints for each class
playerInt = 0
lootInt = 1
tileInt = 2
enemyInt = 3

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

def collide_tile(entity,tiles:list,x_move:int,y_move:int):
    canMove = False
    for i in tiles:
        if i.y == entity.y and i.x == entity.x:
            canMove = False
        else:
            canMove = True

    return canMove

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
        elif i == enemy:
            entities.append(Entity.Enemy(x,y,enemy))
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
                if entities[i].sprite == tile:
                    game = game +Fore.GREEN+ "\n" +entities[i].sprite
                elif entities[i].sprite == player:
                    game = game +Fore.BLUE+ "\n" +entities[i].sprite
                elif entities[i].sprite == enemy:
                    game = game + Fore.RED +  "\n" +entities[i].sprite
                else:
                    game = game +Fore.WHITE+ "\n" +entities[i].sprite
                af_y = entities[i].y
                x += 1
                if not i > len(entities):
                    i += 1
                else:
                    break

            else :
                if not i > len(entities)-1:
                    if entities[i].sprite == tile:
                        game = game +Fore.GREEN+ entities[i].sprite
                    elif entities[i].sprite == player:
                        game = game +Fore.BLUE +entities[i].sprite
                    elif entities[i].sprite == enemy:
                        game = game + Fore.RED +entities[i].sprite
                    elif entities[i].sprite == loot:
                        game = game + Fore.YELLOW +entities[i].sprite
                    else:
                        game = game +Fore.WHITE+ entities[i].sprite
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
    elif Sprite == enemy:
        Etype = enemyInt

    if Etype == playerInt:
        c = Entity.Player(x,y,player)
        sprite = player
    elif Etype == lootInt:
        c = Entity.Loot(x,y,loot)
        sprite = loot
    elif Etype == tileInt:
        c = Entity.Tile(x,y,tile)
        sprite = tile
    elif Etype == enemyInt:
        c = Entity.Enemy(x,y,enemy)
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
    loot = None
    #entities = sort_lvl(entities=entities)
    for i in entities:
        if i.type == "Player":
            i.af_x = i.x
            i.af_y = i.y
            player = i
            
        if i.type == "Loot":
            loot = i
    if direction == "a":
        player.x -= 1
    elif direction == "d":
        player.x += 1
    elif direction == "w":
        player.y -= 1
    elif direction == "s":
        player.y += 1
    
    if player.x == loot.x and player.y == loot.y:
        print(Fore.YELLOW+"██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗\n╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║\n░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║\n░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║\n░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝")
        player.x = player.af_x 
        player.y = player.af_y
    for i in entities:
        if i.type == "Player":
            i = player
            i.update_path(player.x,player.y)



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

def enemy_update(entities:list):
    player = None
    enemy = None
    tiles = []
    for i in entities:
        if i.type == "Player":
            player = i
        elif i.type == "Enemy":
            enemy = i
        elif i.type == "Tile":
            tiles.append((i.x,i.y))
    
    #O
    #X
    if enemy.y < player.y :
        # #O#
        if not (enemy.x + 1 ,enemy.y) in tiles or not(enemy.x - 1,enemy.y) in tiles:
            enemy.y += 1
        # #
        ##O#
        elif not (enemy.x ,enemy.y + 1) in tiles:
            enemy.y += 1
        if (enemy.x,enemy.y) in tiles:
            enemy.y -= 1
            if enemy.x > player.x:
                enemy.x -= 1
            else:
                enemy.x += 1 
            if (enemy.x,enemy.y) in tiles:
                enemy.x -= 1
    #X
    #O
    elif enemy.y > player.y:
        if not (enemy.x + 1 ,enemy.y) in tiles or not(enemy.x - 1,enemy.y) in tiles:
            enemy.y -= 1
        elif not (enemy.x,enemy.y - 1) in tiles:
            if not(enemy.x + 1,enemy.y)in tiles and enemy.x < player.x:
                enemy.x += 1
                
            elif not(enemy.x - 1,enemy.y)in tiles and enemy.x > player.x:
                enemy.x -= 1

        if (enemy.x,enemy.y) in tiles:
            enemy.y += 1
            enemy.x -= 1
            if (enemy.x,enemy.y) in tiles:
                enemy.x += 1
    elif enemy.y == player.y:
        if enemy.x > player.x:
            enemy.x -= 1 
            if (enemy.x,enemy.y) in tiles:
                enemy.x -= 1   
        elif enemy.x < player.x:
            enemy.x += 1
            if (enemy.x,enemy.y) in tiles:
                enemy.x -= 1  
    for i in entities:
        if i.type == "Enemy":
            i = enemy
    if enemy.x == player.x and enemy.y == player.y:
        print(Fore.RED+"██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗░░░██████╗░███████╗████████╗████████╗███████╗██████╗░\n╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝░░░██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗\n░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░░░░██████╦╝█████╗░░░░░██║░░░░░░██║░░░█████╗░░██████╔╝\n░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░██╗██╔══██╗██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗\n░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗╚█║██████╦╝███████╗░░░██║░░░░░░██║░░░███████╗██║░░██║\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝░╚╝╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n\n██╗░░░░░██╗░░░██╗░█████╗░██╗░░██╗  ███╗░░██╗███████╗██╗░░██╗████████╗  ████████╗██╗███╗░░░███╗███████╗\n██║░░░░░██║░░░██║██╔══██╗██║░██╔╝  ████╗░██║██╔════╝╚██╗██╔╝╚══██╔══╝  ╚══██╔══╝██║████╗░████║██╔════╝\n██║░░░░░██║░░░██║██║░░╚═╝█████═╝░  ██╔██╗██║█████╗░░░╚███╔╝░░░░██║░░░  ░░░██║░░░██║██╔████╔██║█████╗░░\n██║░░░░░██║░░░██║██║░░██╗██╔═██╗░  ██║╚████║██╔══╝░░░██╔██╗░░░░██║░░░  ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░\n███████╗╚██████╔╝╚█████╔╝██║░╚██╗  ██║░╚███║███████╗██╔╝╚██╗░░░██║░░░  ░░░██║░░░██║██║░╚═╝░██║███████╗\n╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝")
    return entities
        
        
    
