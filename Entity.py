import math
from colorama import Fore, Back, Style

enemy = "X"
player = "O"
distance = "  "
tile = "#"
tileSprite = Fore.GREEN + tile
limit_x = 49
limit_y = 17
down = "\n"
loot = "L"

tiles = []

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
class Player:
    def __init__(self,x:int,y:int,sprite:str):
        self.type = "Player"
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
        self.sprite = sprite
        self.path = []
    def update_path(self,x,y):
        self.path.append((x,y))
    def get_pos(self) -> tuple: return(self.x,self.y)
    def move(self,direction):
        if direction == "a":
            self.x -= 1
        elif direction == "d":
            self.x += 1
        elif direction == "w":
            self.y -= 1
        elif direction == "s":
            self.y += 1
class Loot:
    def __init__(self,x:int,y:int,sprite:str,):
        self.type = "Loot"
        self.c_x = x
        self.c_y = y
        self.x = x
        self.y = y
        self.sprite = sprite
class Tile:
    def __init__(self,x,y,sprite):
        self.type = "Tile"
        self.sprite = sprite
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
class TileSet():
    def __init__(self,tiles:list) -> None:
        self.tiles = tiles
    def is_there(self,x,y) -> bool:
        for tile in self.tiles:
            if (tile.x,tile.y) == (x,y):
                return True
        else:
            return False
class Enemy:
    print("NOPE not tils")
    def __init__(self,x:int,y:int,sprite:str):
        self.type = "Enemy"
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
        self.sprite = sprite
        self.game_over = False
        self.states = ["FOLLOW","HIT"]
        self.state = self.states[0]
    def get_pos(self) -> tuple: return (self.x,self.y)
    def collishion_check(self,x,y,entities:list,typ:str = "Tile")->bool:
        #[tile,tile,player]
        for entity in entities:
            match entity.type:
                case "Tile":
                    if (x,y) == (entity.x,entity.y):
                        return True if typ == "Tile" else False
                case "Player":
                    if (x,y) == (entity.x,entity.y):
                        return True if typ == "Player" else False
                case "Enemy":
                    if (x,y) == (entity.x,entity.y):
                        return True if typ == "Enemy" else False
    def move(self,player:Player):
        pass
    def follow(self,game_obj):
        #*Wall collishion
        #self.collishion_check(entities,"Tile")
        player = game_obj.player
        x = self.x
        y = self.y
        self.af_x = x
        self.af_y = y
        targ_x = player.x
        targ_y = player.y


        #[top,bottom,left,right]
        possible = self.possible(x,y,game_obj.tiles)
        if targ_y>y and possible["bottom"]:
            y+=1
        elif targ_y < y and possible["top"]:
            y-=1
        if targ_x > x and possible["right"]:
            x += 1
        elif targ_x < x and possible["left"]:
            x -= 1
        if targ_y == y :
            if possible["right"] or possible["left"]:
                if targ_x > x:
                    x += 1
                elif targ_x < x :
                    x -= 1
            else:
                if possible["top"] or possible["bottom"]:
                    if math.dist([x,y+1],[targ_x,targ_y]) < math.dist([x.y-1],[targ_x,targ_y]):
                        y += 1
                    else:
                        y -= 1
        self.x = x
        self.y = y
        game_obj.enemy = self
    def possible(self,x,y,entities) -> dict:
        top,bottom,left,right = 1,2,2,3
        if not self.collishion_check(x,y-1,entities):
            top = True
        elif not self.collishion_check(x,y+1,entities):
            bottom = True
        elif not self.collishion_check(x-1,y,entities):
            left = True
        elif not self.collishion_check(x+1,y,entities):
            right = True
        return{"top":top,"bottom":bottom,"left":left,"right":right}
class Game():
    def __init__(self,file_name) -> None:
        self.entities = self.lvl_load(file_name)
        self.tiles=[]
        self.game_over = False
        for entity in self.entities:
            if entity.type == "Enemy":
                self.enemy:Enemy = entity
            elif entity.type == "Player":
                self.player:Player = entity
            elif entity.type == "Tile":
                self.tiles.append(entity)
            elif entity.type == "Loot":
                self.loot = entity
        self.tilesSet = TileSet(self.tiles)
    def get_player(self)->Player:return self.player
    def get_enemy(self)->Enemy: return self.enemy                        
    def lvl_load(self,file_name:str):
        entities = []
        x = 0
        y = 0
        lvl_file = open(file_name,'r')
        self.lvl_filename = file_name
        lvl_string = lvl_file.readline()
        while lvl_string:
            for i in lvl_string:
                x += 1
                if x > 50:
                    x = 1
                    y +=1
            
                if i == player:
                    entities.append(Player(x,y,player))
                elif i == tile :
                    entities.append(Tile(x,y,tile))
                elif i == loot:
                    entities.append(Loot(x,y,loot))
                elif i == enemy:
                    entities.append(Enemy(x,y,enemy))
            lvl_string = lvl_file.readline()
        lvl_file.close()
        return entities

    def lv1_draw(self) -> str:
        x = 0 
        y = 0
        game = ""
        self.game = ""
        while True:
            if self.tilesSet.is_there(x,y):
                game = game + Fore.WHITE    +tile
                self.game = self.game + tile
            elif self.player.get_pos() == (x,y):
                game = game + Fore.BLUE+player
                self.game = self.game + player
            elif self.enemy.get_pos() == (x,y):
                game = game +Fore.RED+ enemy
                self.game = self.game + enemy
            else:
                game = game + " "
                self.game = self.game + " "
            x += 1
            if x > 50:
                x = 0
                y += 1
                game = game + "\n"
                self.game = self.game + "\n"
            if y > 17:
                break
        return game
    def lvl_save(self):
        f = open(self.lvl_filename,'w')
        f.write(self.game)
        f.close()

            