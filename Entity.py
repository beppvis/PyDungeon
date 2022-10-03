

class Player:
    def __init__(self,x:int,y:int,sprite:str):
        self.type = "Player"
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
        self.sprite = sprite
class Loot:
    def __init__(self,x:int,y:int,sprite:str):
        self.type = "Loot"
        self.c_x = x
        self.c_y = y
        self.x = x
        self.y = y
        self.sprite = sprite
class Tile:
    def __init__(self,x,y,sprite):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
class TileSet:
    def __init__(self,tile_list):
        self.type = "TileSet"
        self.tiles = tile_list