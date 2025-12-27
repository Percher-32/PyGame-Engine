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

def main(self,ground):
    #x dir movement
    self.sp("machspeed",150)
    
    if self.gp("homing") == 0:
        
        if abs(self.gp("des_vel",0)) > 250:
            self.sp("des_vel",250 * self.valsign(self.gp("des_vel",0)),0)
        if abs(self.gp("act_vel",0)) > 250:
            self.sp("act_vel",250 * self.valsign(self.gp("act_vel",0)),0)

        if abs(self.key["x"]) > 0:
            if self.isthere("leftjump"):
                self.key["x"] = 1
            if self.isthere("rightjump"):
                self.key["x"] = -1 * 1

            if self.gp("xinit") or not self.valsign(self.gp("act_vel",0)) == self.valsign(self.key["x"]):
                self.sp("xinit",False)
                self.sp("des_vel",[self.key["x"] * 120,self.gp("des_vel")[1]])
                self.sp("act_vel",[self.key["x"] * 20,self.gp("act_vel")[1]])
            
            
            if ground:
                if self.key["throw"] and self.dropdashinit == 0:
                    # self.sp("act_vel",self.gp("des_vel"))
                    self.sp("des_vel",[        self.key["x"] * self.gp("machspeed")/10            ,    self.gp("des_vel")[1]   ])
                else:
                    if abs(self.gp("des_vel",0)) < self.gp("machspeed") or not self.valsign(self.gp("act_vel",0)) == self.valsign(self.key["x"]):
                        self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * self.gp("machspeed"),30 )              ,    self.gp("des_vel")[1]   ])
                    else:
                        pass
            else:
                if abs(self.gp("des_vel",0)) < self.gp("machspeed") or not self.valsign(self.gp("act_vel",0)) == self.valsign(self.key["x"]):
                    self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * self.gp("machspeed"),30 )              ,    self.gp("des_vel")[1]   ])
                else:
                    pass
        else:
            self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
            self.sp("xinit",True)

    
    #rerout detection
    if not self.isthere("leftjump") or not self.isthere("rightjump"):
        if not self.sign(self.key["x"]) == self.sign(self.gp("lastx")):
            self.sp("xinit",True)
            if ground and abs(self.gp("act_vel")[0]) > 100:
                self.wait("skid",0.3)
                # self.print("shid")
        self.sp("lastx",self.key["x"])
        
        
    

    #Skid detection 
    if abs(self.gp("act_vel")[0]  - self.gp("des_vel")[0]) > 50:
        self.sp("skidding",True)
    else:
        self.sp("skidding",False)

