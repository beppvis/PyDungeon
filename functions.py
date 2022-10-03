import Entity
import json

player = "0"
distance = "  "
tile = "#"
limit_x = 100
limit_y = 100
down = "\n"
loot = "L"

#* Remeber to add all types here for reffereral 
tile_type = "TileSet"
loot_type = "Loot"
player_type ="Player"

def second_value(val):
    return val[1]

def tile_data(filename):
    tile_list=[]
    with open(filename,'r') as file:
        tile_data = json.load(file)
        for i in tile_data:
            x = int(i['x'])
            y = int(i['y'])
            tile_list.append([x,y])
        return tile_list
def tile_draw(tile_data:list,sprite):
    sprite_list = []
    tile_data.sort()
    y = int(tile_data[0][1])
    for i in tile_data:
        x = int(i[0])
        sprite = sprite + sprite
    sprite = '\n'*y + sprite

    return sprite


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

def update_loot(d:int,loot,x:int,y:int,player,px:int,py:int):
    pass

def player_update(player:Entity.Player):
    if player.x > limit_x:
        player.x = limit_x
    elif player.x < 0 :
        player.x = 0
    elif player.y < 0 :
        player.y = 0
    return player

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

