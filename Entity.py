import math
import os
from colorama import Fore
import time
enemy = "X"
player = "O"
distance = "  "
tile = "#"
lvl_1 = "1"
lvl_2 = "2"
lvl_3 = "3"
lvl_4 = "4"
Exit = "0"
tileSprite = Fore.GREEN + tile
limit_x = 49
limit_y = 16
down = "\n"
key = "K"



tiles = []

#*TOD0 :assinging ints for each class
playerInt = 0
keyInt = 1
tileInt = 2
enemyInt = 3

#! assinging world limit for the world
worldLimitY = 100
worldLimitX = 100

#* Remeber to add all types here for reffereral 
tile_type = "TileSet"
key_type = "Key"
player_type ="Player"

class Pos:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
        self.tuple = (x,y)
    def dist(self,pos)->float:return math.sqrt((pos.x-self.x)**2+ (pos.y-self.y)**2)

class CollidingObj:
    def __init__(self,colliding:bool,typ:str) -> None:
        self.colliding = colliding
        self.type = typ

class Gate:
    def __init__(self,x:int,y:int,destination:int,key_needed:bool = False,key:list=None) -> None:
        self.type = "Gate"
        self.x = x
        self.y = y
        self.destination = destination
        self.key_needed = key_needed
        self.key = key
    def get_pos(self) -> Pos: return Pos(self.x,self.y)
    def check_entry(self,keys:list) ->bool:
        if self.key != None:
            if self.key == keys: return True
            else: return False
        else:
            return True
    def is_there(self,x,y) -> bool:
        for item in self.items:
            if item.get_pos().tuple == (x,y):
                return True
        else:
            return False
class Player:
    def __init__(self,x:int,y:int,sprite:str,game):
        self.type = "Player"
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
        self.sprite = sprite
        self.path = []
        self.game = game
        self.keys = []
    def update_path(self,x,y):
        self.path.append((x,y))
    def collishion_check(self,x,y,entities:list,typ:str = "Tile")->bool:
        #[tile,tile,player]
        for entity in entities:
            if (x,y) == (entity.x,entity.y):
                match entity.type:
                    case "Tile":
                        return True if typ == "Tile" else False
                    case "Enemy":
                        
                        return True if typ == "Enemy" else False
                    case "Gate":
                        return True if not entity.check_entry(self.keys) else False
                    case "Key":
                        self.keys.append(entity.key)
                        entity.visible = False
                        entity.collected = True
                        return False
    def get_pos(self) -> Pos: return Pos(self.x,self.y)
    def move(self,direction):
        self.collishion_check(self.x,self.y,self.game.entities)
        if direction == "a":
            self.x -= 1
        elif direction == "d":
            self.x += 1
        elif direction == "w":
            self.y -= 1
        elif direction == "s":
            self.y += 1
        if self.collishion_check(self.x,self.y,self.game.entities):
            self.x = self.af_x
            self.y = self.af_y
        else:
            self.af_x,self.af_y = self.x,self.y
        for i in self.game.gates:
            if (self.x,self.y) == i.get_pos().tuple:
                
                self.game.lvl_change(i.destination)
                
class Key:
    def __init__(self,x:int,y:int,sprite:str,key:int):
        self.type = "Key"
        self.c_x = x
        self.c_y = y
        self.x = x
        self.y = y
        self.sprite = sprite
        self.visible = False
        self.key = key
        self.collected = False
    def get_pos(self) -> Pos: return Pos(self.x,self.y)
class Tile:
    def __init__(self,x,y,sprite):
        self.type = "Tile"
        self.sprite = sprite
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
    def get_pos(self) -> Pos: return Pos(self.x,self.y)
class TileSet():
    def __init__(self,tiles:list) -> None:
        self.tiles = tiles
    def is_there(self,x,y) -> bool:
        for tile in self.tiles:
            if (tile.x,tile.y) == (x,y):
                return True
        else:
            return False
class Set():
    def __init__(self,items:list) -> None:
        self.items = items
    def is_there(self,x,y,item_needed = False) -> bool:
        for item in self.items:
            if item.get_pos().tuple == (x,y):
                return True
        else:
            return False
class Enemy:
    
    def __init__(self,x:int,y:int,sprite:str):
        self.type = "Enemy"
        self.x = x
        self.y = y
        self.af_x = x
        self.af_y = y
        self.sprite = sprite
        self.game_over = False
        self.game = ""
        self.states = ["FOLLOW","HIT"]
        self.state = self.states[0]
        self.times_traped = 0
    
    def get_pos(self) -> Pos: return Pos(self.x,self.y)
    def collishion_check(self,x,y,entities:list,typ:str = "Tile")->bool:
        #[tile,tile,player]
        for entity in entities:
            if (x,y) == (entity.x,entity.y):
                match entity.type:
                    case "Tile":
                            return True if typ == "Tile" else False
                    case "Player":
                            self.game.game_over = True
                            return False
                    case "Enemy":
                            return True if typ == "Enemy" else False
    def move(self,player:Player):
        pass
    def follow(self,game_obj):
        #*Wall collishion
        #sis colliding -> CollidingObs
        self.collishion_check(self.x,self.y,game_obj.entities)
        player_pos = game_obj.player.get_pos()
        enemy_pos = self.get_pos()
        up_pos = Pos(enemy_pos.x,enemy_pos.y - 1)
        down_pos = Pos(enemy_pos.x ,enemy_pos.y + 1)
        right_pos = Pos(enemy_pos.x + 1,enemy_pos.y)
        left_pos = Pos(enemy_pos.x - 1,enemy_pos.y)
        updist = up_pos.dist(player_pos)
        downdist = down_pos.dist(player_pos)
        rightdist = right_pos.dist(player_pos)
        leftdist = left_pos.dist(player_pos)
        self.af_x = self.x
        self.af_y = self.y 
        if updist < downdist and not game_obj.is_colliding(up_pos.tuple):
            enemy_pos.y -= 1
        elif updist > downdist and not game_obj.is_colliding(down_pos.tuple):
            enemy_pos.y += 1
        elif rightdist < leftdist and not game_obj.is_colliding(right_pos.tuple):
            enemy_pos.x += 1
        elif rightdist > leftdist and not  game_obj.is_colliding(left_pos.tuple):
            enemy_pos.x -= 1
        self.x = enemy_pos.x
        self.y = enemy_pos.y
        if (self.af_x,self.af_y) == (self.x,self.y):
            self.times_traped += 1
        
        game_obj.enemy = self
            





 

        
class Game():
    def __init__(self,file_name,lvl_obj,lvl_num:int) -> None:
        self.lvl_obj = lvl_obj
        self.lvl_num = lvl_num
        self.entities = self.lvl_load(file_name)
        self.gates = []
        self.tiles=[]
        self.enemies = []
        self.exit_gate =[]
        self.game_over = False
        
        for entity in self.entities:
            if entity.type == "Enemy":
                self.enemy:Enemy = entity
                self.enemies.append(entity)
            elif entity.type == "Player":
                self.player:Player = entity
            elif entity.type == "Tile":
                self.tiles.append(entity)
            elif entity.type == "Key":
                self.key = entity
            elif entity.type == "Gate":
                self.gates.append(entity)
                if entity.destination == -1:
                    self.exit_gate.append(entity)
        self.exitgateSet = Set(self.exit_gate)
        self.tilesSet = TileSet(self.tiles)
        self.enemySet = Set(self.enemies)
        
    def get_player(self)->Player:return self.player
    def get_enemy(self)->Enemy: return self.enemy       
    def is_colliding(self,pos:tuple) -> bool:
        obj = None
        colliding = False
        for tile in self.tiles:
            if tile.get_pos().tuple == pos:
                obj = "Tile"
                colliding = True
                return colliding
        if self.player.get_pos().tuple == pos:
            obj = "Player"
            colliding = True
        elif self.enemy.get_pos().tuple == pos:
            obj = "Enemy"
            colliding = True
        elif self.key.get_pos().tuple == pos:
            obj = "Key"
            colliding = True
        else:
            colliding = False
        return colliding
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
                    entities.append(Player(x,y,player,self))
                elif i == tile :
                    entities.append(Tile(x,y,tile))
                elif i == key:
                    entities.append(Key(x,y,key,self.lvl_num))
                elif i == enemy:
                    entities.append(Enemy(x,y,enemy))
                elif i == lvl_1:
                    entities.append(Gate(x,y,1))
                elif i == lvl_2:
                    entities.append(Gate(x,y,2,True,[1]))
                elif i == lvl_3:
                    entities.append(Gate(x,y,3,True,[1,2]))
                elif i == lvl_4:
                    entities.append(Gate(x,y,4,True,[1,2,3]))
                elif i == Exit:
                    entities.append(Gate(x,y,-1,True,[1,2,3,4]))           
            lvl_string = lvl_file.readline()
        lvl_file.close()
        return entities

    def lv1_draw(self) -> str:
        x = 1 
        y = 0
        game = ""
        self.game = ""
        while True and not self.game_over:
            if self.tilesSet.is_there(x,y):
                game = game + Fore.WHITE    +tile
                self.game = self.game + tile
            elif self.player.get_pos().tuple == (x,y):
                game = game + Fore.BLUE+player
                self.game = self.game + player
            elif self.enemySet.is_there(x,y):
                game = game +Fore.RED+ enemy
                self.game = self.game + enemy
            elif self.key.get_pos().tuple == (x,y) and self.key.visible :
                game = game + Fore.YELLOW + key
                self.game = self.game + key
            elif self.exitgateSet.is_there(x,y):
                game = game+ Fore.GREEN + Exit
                self.game = self.game + Exit
            else:
                game = game + " "
                self.game = self.game + " "
            x += 1
            if x > 49:
                x = 1
                y += 1
                game = game + "\n"
                self.game = self.game + "\n"
                self.game = self.game.lstrip()
            if y > 17:
                break
        return game
    def lvl_change(self,to):
        self.lvl_obj.changed_lvl = True
        self.lvl_obj.changed_to = to
    def lvl_save(self):
        f = open(self.lvl_filename,'w')
        f.write(self.game)
        f.close()
    def lvl_update(self,direction):
            if self.enemySet.is_there(self.player.x,self.player.y):
                self.game_over = True
            self.player.move(direction)
            for enemy in self.enemies:
                enemy.follow(self)
            


class Level():
    def __init__(self,lvl_file:str,level_num:int,player:Player = None,win_con:int = 2) -> None:
        self.game_obj = Game(lvl_file,self,level_num)
        self.changed_lvl = False
        self.changed_to = 0
        self.player = self.game_obj.player
        self.win_con = win_con

    def run(self,player:Player =None):
        if player != None:
            self.game_obj.player = player
        
        while not self.changed_lvl and not self.game_obj.game_over:
            
            print(Fore.WHITE + self.game_obj.lv1_draw())
            direction = input(Fore.CYAN+"You'r move : ")
            if os.name == "posix":
                os.system("clear")
            else:
                os.system("cls")
            direction = direction.lower()
            if direction == "esc":
                os._exit(0)
            self.game_obj.lvl_update(direction)
            if self.game_obj.enemy.times_traped > self.win_con and not self.game_obj.key.collected:
                
                self.game_obj.key.visible = True
        pl = self.game_obj.player

        if self.game_obj.game_over:
            with open("assets/gameover.txt",encoding="utf8") as over_f:
                over = over_f.read()
                print(Fore.RED + over)
            time.sleep(2)
            self.changed_to = -1
        
        if pl.y == 0:
            pl.y = limit_y - 1
        elif pl.x == 1:
            pl.x = limit_x - 1 
        elif pl.y == limit_y:
            pl.y = 0 + 1
        elif pl.x == limit_x:
            pl.x  = 0 + 1
        pl.af_x,pl.af_y = (pl.x,pl.y)
        self.changed_lvl = False
        return self.changed_to,pl
