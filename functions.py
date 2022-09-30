import Entity

player = "0"
distance = "  "
limit_x = 100
limit_y = 100
down = "\n"
loot = "L"

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


def move(c_player:Entity.Player,direction):
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

def player_update(player:Entity.Player):
    if player.x > limit_x:
        player.x = limit_x
    elif player.y > limit_y:
        player.y = limit_y
    elif player.x < 0 :
        player.x = 0
    elif player.y < 0 :
        player.y = 0
    return player

def entity_update(player:Entity.Player,loot:Entity.Loot,direction:str):
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
