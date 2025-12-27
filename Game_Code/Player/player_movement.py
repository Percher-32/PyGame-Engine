import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math



import Game_Code.Player.player_movement_core as player_movement_core
import Game_Code.Player.logic_spindash as logic_spindash
import Game_Code.Player.logic_homingattack as logic_homingattack
import Game_Code.Player.logic_trick as logic_trick
import Game_Code.Player.logic_dashbar as logic_dashbar
import Game_Code.Player.logic_airdash as logic_airdash

import Game_Code.Player.player_init as player_init




em = Gamemananager.em
tm = Gamemananager.tm
fm = Gamemananager.fm
om = Gamemananager.om
Tiled = Gamemananager.Tiled
cam =Gamemananager.cam
cm = Gamemananager.cm
sd = Gamemananager.sd
sm = Gamemananager.sm
um = Gamemananager.um
bg = Gamemananager.bg
pm = Gamemananager.pm

def main(self):
    um.elements["Speed-timer"]["text"]  = str(round(float(um.elements["Speed-timer"]["text"]) + (self.dt/60 *self.publicvariables["gamespeed"] ),2))
    um.elements["attemps"]["text"]  = str(self.timesdone)
    
    self.sp("wantime",self.publicvariables["gamespeed"])

    collision = om.collide9("player",0,cam,self.dim,ignore= ["playersprite","skateboard"])
    lonepoint1 = om.collidep([om.objects["player"]["pos"][0] + 60,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
    lonepoint2 = om.collidep([om.objects["player"]["pos"][0] - 50,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
    collisionbox = om.collide("player",0,cam,extra=20)
    smallcollisionbox = om.collide("player",1,cam,extra=-60)
    bigcollisionbox = om.collide("player",0,cam,extra=600)
    attackbox = om.colliderect([cm.getcam("playercam","pos")[0] +(self.lookahead*0),cm.getcam("playercam","pos")[1] + (self.lookaheady*0)],[1300,700],0,cam)

    ground1 = len(collision["botmid"]["inst"]) > 0
    ground2 = len(collision["botleft"]["inst"]) > 0    and not (len(collision["topleft"]["inst"])  > 0  ) and not (len(collision["midleft"]["inst"])  > 0  )
    ground3 = len(collision["botright"]["inst"]) > 0   and not (len(collision["topright"]["inst"]) > 0  ) and not (len(collision["midright"]["inst"]) > 0  )
    ground = ground1 or ground2 or ground3
    instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"]
    collisionlisttype = [i.type for i in instlist]
    collisionboxtype = [i.type for i in collisionbox["inst"]] 

    
    rail = False
    if len(collisionboxtype) > 0:
        rail = collisionboxtype[0] == "rail"
        
    
    self.rail = rail
    self.railrot = 0
    self.raildir = "r"
    

    if abs(self.key["x"]) > 0:
        if self.key["x"] > 0:
            self.lastdirslant = "l"
        else:
            self.lastdirslant = "r"


    if len(collisionboxtype) > 0:
        if "slantl"  in collisionboxtype or "slantr" in collisionboxtype:
            slanted = True
            if "slantr" in collisionboxtype:
                if self.lastdirslant == "r":
                    if len(lonepoint2["inst"]) > 0:
                        slanted = False
                        om.objects["player"]["pos"] = [lonepoint2["inst"][0].realpos[0] + univars.grandim,lonepoint2["inst"][0].realpos[1] - 32]
            else:
                if self.lastdirslant == "l":
                    if len(lonepoint1["inst"]) > 0 :
                        slanted = False
                        om.objects["player"]["pos"] = [lonepoint1["inst"][0].realpos[0] + univars.grandim,lonepoint1["inst"][0].realpos[1] - 32]

            
        else:
            slanted = False	
    else: 
        slanted = False
    

    if self.key["attack"] and self.attackheld > 13:
        self.sp("wantime",max([3/self.attackheld,0.4]))

    if not self.key["attack"] and self.lastkey["attack"] and not self.isthere("cooldownattack"):
        if self.attackheld < 10:
            self.wait("attack",0.4)
            self.wait("cooldownattack",0.5)
            
            self.spin(30,0.3)
        else:
            self.wait("skatego",0.5,barrier=1)
            self.spin(30,1)
            
            # self.bailable = 1
            self.skatevel = [
                                (self.key["x"] * 1000 * 2 )  + om.objects["player"]["pos"][0],
                                (self.key["y"] * -500 * 2 )  + om.objects["player"]["pos"][1]
                            ]	
            
                
    if self.key["x"] > 0:
        self.lastdir = "r"
    if self.key["x"] < 0:
        self.lastdir = "l"

    axis = [self.key["x"],self.key["y"] * 1]
    vecaxis = pygame.math.Vector2(axis[0],axis[1])
    if vecaxis.length()> 0:
        vecaxis.normalize()
        vecaxis.scale_to_length(1.2)
    axis = [vecaxis.x,vecaxis.y]
    axis[1] = round(axis[1],2)

    
    selected_obj= None
    #HOMING ATTACK SELECT
    if len(attackbox["obj"]):
        om.objects["enemyzoom"]["rendercond"] = 1
        if pygame.math.Vector2(self.key["x"],self.key["y"] ).length() > 0:
            self.joyaxis = pygame.math.Vector2(-1 *self.key["x"],1 *self.key["y"] )
            self.joyaxis.normalize()
        enaxis = self.joyaxis
        selected_obj= None
        closeness = None
        playervec = pygame.math.Vector2(om.objects["player"]["pos"])
        for obj in attackbox["obj"]:	
            if not obj == None:
                emvec = pygame.math.Vector2(obj.info["pos"])
                distvec = playervec - emvec
                if distvec.length() > 0:
                    distvec.normalize()
                    if obj.info["type"] in self.typesofhoming and om.get_value(obj.name,"canhome"):
                        if selected_obj== None:
                            selected_obj= obj
                            closeness = 1 - distvec.dot(enaxis) 
                        else:
                            if 1-distvec.dot(enaxis) < closeness:
                                selected_obj= obj
                                closeness = 1 - distvec.dot(enaxis) 
        if selected_obj== None:
            om.objects["enemyzoom"]["rendercond"] = 0
        else:
            om.objects["enemyzoom"]["pos"] = selected_obj.info["pos"]
            om.objects["enemyzoom"]["sizen"] = self.listadd((selected_obj.info["sizen"],[0.5,0.5]))





        

    

        if self.gp("homing") == 2:
            selected_obj= self.gp("target")

    else:
        om.objects["enemyzoom"]["rendercond"] = 0






    #LOGIC
    
    
    
    
    logic_dashbar.main(self,ground,rail)
    logic_spindash.main(self,collisionbox["inst"],ground)
    logic_homingattack.main(self,collisionlisttype,selected_obj,axis,ground)
    logic_trick.main(self,collisionbox,ground)
    logic_airdash.main(self,ground,axis)


    #MAIN
    player_movement_core.main(self,collisionbox,slanted,rail,collision,collisionlisttype,axis,selected_obj,instlist,collisionboxtype,smallcollisionbox,ground)


    
    
    for ty in ["HURT:laser"]:
        if ty in [ i.info["type"] for i in smallcollisionbox["obj"]]:
            if self.gp("homing") == 0:
                if not self.isthere("inv"):
                    self.wait("BAIL",0.5)
    
    
    
    
    











                                

            
    


    #LOOK AHEAD


    




    if self.key["attack"] and not self.key["trick"]:
        self.attackheld += self.dt
    else:
        self.attackheld = 0

        
    
    self.lastground = ground
    self.sp("lastframewall",self.gp("leftwall") or self.gp("rightwall"))
    om.speed = univars.func.lerp(om.speed,self.gp("wantime"),5,roundto=2)
    
    
    if self.ondone("show-score"):
        um.state = "maingame"
        # self.wait()
        player_init.main(self,[0,60])
        
        
    
    self.lastframeslanted = slanted

