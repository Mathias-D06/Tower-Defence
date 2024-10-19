from pygame import *
import math
init()
display.set_caption('Frontlines')

class Tower:
    def __init__(self,pos):
        self.range = 10
        self.damage = 20
        self.pos = pos
        self.target = None
        self.type1 = image.load("Code\Tower Defense Assets\PNG\Retina\towerDefense_tile249.png")
        self.type2 = image.load("Code\Tower Defense Assets\PNG\Retina\towerDefense_tile250.png")
        self.projectile = image.load("Code\Tower Defense Assets\PNG\Retina\towerDefense_tile251.png")
        self.type1_cost = 100
        self.type2_cost = 150
    
    def inRange(self,enemy):
        centre_x = self.tower.pos[0] + self.type1.get_height()//2
        centre_y = self.tower.pos[1] + self.type2.get_width()//2
        enemy_centre_x = self.enemy.x + self.enemy.image.get_height()//2
        enemy_centre_y = self.enemy.y + enemy.image.get_width()//2
        distance = math.sqrt((centre_x - enemy_centre_x)**2 + (centre_y - enemy_centre_y)**2)
        return distance <= self.range
    def attack (self,enemy,target,inRange,newTarget):
        self.willhit = inRange(self,target,enemy[target])
        if self.target and self.willhit:
            self.target.take_damage(self.damage)
            if self.target.health <= 0:
                self.target = None
        else:
            self.new_target = newTarget(self,enemies)

            if self.new_target is not None:
                self.target = self.new_target
                self.target = self.take_damage(self.damage)
            else:
                self.target = None
    def newTarget(self,):
        self.area = inRange(self,enemy)
        for enemy in enemies:
            if self.area:
                return enemy
        return None

class TowerSelection:
    def __init__(self):
        self.selected_tower = None
        self.money = 250
    def selected_tower(self,tower_type):
        if tower_type == "Tower1":
            self.selected_tower = self.type1
        elif tower_type == "Tower2":
            self.selected_tower = self.type2
    def place_tower(self):
        if self.selected_tower == self.type1:
            if self.money >= self.type1_cost:
                if self.game_map.pos_valid(pos) == True:
                    self.game_map.add_tower(selected_tower,pos)
                    self.money -= self.type1_cost
                    self.selected_tower.draw()
                    selected_tower = None
        elif self.selected_tower == self.type2:
            if self.money >= self.type2_cost:
                if self.game_map.pos_valid(pos) == True:
                    self.game_map.add_tower(selected_tower,pos)
                    self.money -= self.type2_cost
                    self.selected_tower.draw()
                    selected_tower = None
class Enemy:
    def __init__(self,image):
        self.image = image.load("D:\Code\Tower Defense Assets\PNG\Retina\towerDefense_tile248.png")
        self.health = 40
        self.number = 4
        self.speed = 6
        self.pos = []
        self.round = round
        
        
        

                    


    


class MainLoop:
    def __init__(self):
        self.exit_game = False
        self.game_screen = display.set_mode((1288,728))
        self.map = image.load("D:\Code\Protoype 1\map.png")
    def gamescreen(self):
        while not self.exit_game:
            for e in event.get():
                if e.type == QUIT:
                    self.exit_game = True
                elif e.type == MOUSEBUTTONDOWN:
                    if mouse_clicked == True:
                        start_selection.select_tower()
                
                self.game_screen.blit(self.map,(0,0))
                display.flip()

loop = MainLoop()
loop.gamescreen()





