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

def main(self,collisionbox):
    
    #styles
    if self.key["trick"] and not len(collisionbox["inst"] ) >0:
        times = 0.7
        self.wait("inv",times)
        if not self.isthere("tcd"):
            if self.key["throw"] and not self.lastkey["throw"]:
                self.prevtricks.append(1)
                self.wait("tcd",0.2)
                self.wait("VULNERABLE",times,barrier=False)
                self.wait("trick1",times,barrier=False)
                self.spin(12,times,0.1)
                if self.prevtricks[-1] == 1:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
                else:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))
            elif self.key["secondary"] and not self.lastkey["secondary"]:
                self.prevtricks.append(2)
                self.wait("tcd",0.2)
                self.wait("VULNERABLE",times,barrier=False)
                self.wait("trick2",times,barrier=False)
                self.sp("dashmeter",self.gp("dashmeter") + 20)
                if self.prevtricks[-1] == 2:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
                else:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))
            elif self.key["attack"] and not self.lastkey["attack"]:
                self.prevtricks.append(3)
                self.wait("tcd",0.2)
                self.wait("VULNERABLE",times,barrier=False)
                self.wait("trick3",times,barrier=False)
                self.sp("dashmeter",self.gp("dashmeter") + 20)
                if self.prevtricks[-1] == 3:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
                else:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))


    #Bail timer
    if self.isthere("BAIL"):

        self.key["x"] = 0
        self.key["y"] = 0
        self.key["jump"] = 0
        if self.gp("leftwall") or self.gp("rightwall"):
            self.key["jump"] = 1
    if self.ondone("BAIL"):
        self.key["jump"] = 1
        self.sp("act_vel",100,1)
        self.sp("des_vel",100,1)
        
        
        
    

