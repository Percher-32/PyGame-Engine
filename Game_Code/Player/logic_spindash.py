import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math





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

def main(self,collisionboxinst,ground):
    #SPIN/DROP DASH
    
    supg = len(collisionboxinst) > 0
    
    if ((not self.key["throw"] and self.lastkey["throw"] and supg) or (supg and self.dropdashinit==1 and self.key["throw"])) and not self.dropdashinit==2 and not self.key["trick"]:
        self.wait("dashrem",0.5)
        self.wait("spindash",1)
        self.wait("attack",0.6)
        self.wait("inv",1)
        # cm.setcond("playercam","shake",10)
        
        if self.dropdashinit:
            self.dropdashinit = 2
        else:
            
            self.dropdashinit = 0

        if self.lastdir == "r":
            self.sp("des_vel",self.homingcharge,0)
            self.sp("act_vel",self.homingcharge,0)
            self.sp("dashav",[self.homingcharge*1/4,0])
            self.sp("dashdv",[self.homingcharge*1/4,0])
        else:
            self.sp("des_vel",self.homingcharge * -1,0)
            self.sp("act_vel",self.homingcharge * -1,0)
            
            self.sp("dashav",[self.homingcharge*-1/4,0])
            self.sp("dashdv",[self.homingcharge*-1/4,0])

        
        pm.particlespawnbluprint(om.objects["player"]["pos"],"exp4",initvel=[self.gp("des_vel",0)/10,10])
        self.homingcharge = 0

    if (not supg or not self.key["throw"]) and self.dropdashinit == 2 and not self.key["trick"]:
        self.dropdashinit = 0

    #BUILD-UP DASH
    if self.key["throw"] and not self.dropdashinit == 2 and not self.key["trick"]:
        
        if supg:
            cm.setcond("playercam","shake",3)
        else:
            
            cm.setcond("playercam","shake",2)

        self.homingcharge += 10 * self.dt * om.speed
        if self.homingcharge > 260:
            self.homingcharge = 260
    else:
        self.homingcharge = 0
    

    if self.key["throw"] and not self.lastkey["throw"] and not supg:
        self.dropdashinit = 1
        
        
        
        
    
    diam = [400 + (abs(self.gp("act_vel",0)) + abs(self.gp("act_vel",1)))/2,200 + (abs(self.gp("act_vel",0)) + abs(self.gp("act_vel",1)))/1													]
    diams = [500,500]
    if self.flowstate:
        diam[0] *= 1.5
        diam[1] *= 1.5
        diams[0] *= 1.5
        diams[1] *= 1.5
    if self.lastdir == "r":
        dtg = 1
    else:
        dtg = -1
        
        
    if ground and self.isthere("spindash"):
        self.attackerbox = om.colliderect([om.objects["player"]["pos"][0]+(dtg * 200),om.objects["player"]["pos"][1] + (0 * -200)],diams,0,cam)
    else:
        self.attackerbox = om.colliderect([om.objects["player"]["pos"][0]+(dtg* 200),om.objects["player"]["pos"][1] + (self.key["y"] * -200)],diam,0,cam)






