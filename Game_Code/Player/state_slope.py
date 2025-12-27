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





def main(self,collisionboxtype,collisionbox,slanted):
    self.sp("candj",1)
    self.sp("jumpable",1)
    if "slantr" in collisionboxtype:
        self.sp("slantdir","r")
        if not slanted == self.lastframeslanted:
            # if not ground:
            index = collisionboxtype.index("slantr")
            om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] - 20,collisionbox["inst"][index].realpos[1] - 20]
            self.sp("act_vel",[  self.gp("act_vel")[0]    ,    self.gp("act_vel")[0]   ])
            self.sp("des_vel",[  self.gp("des_vel")[0]    ,    self.gp("des_vel")[0]   ])
            self.slantspeed = abs(self.gp("des_vel",0))
                # else:
                # 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
        else:
            if abs(self.key["x"]) > 0:
                self.sp("des_vel",[         self.key["x"] * self.slantspeed             ,    self.gp("des_vel")[1]   ])
                if  self.slantspeed < 200:
                    self.slantspeed += (1  * self.dt)
                
            elif self.gp("des_vel",0) > -100:
                self.sp("des_vel",[  self.gp("des_vel",0) - (1*self.dt)    ,    self.gp("des_vel")[1]   ])
                if  self.slantspeed > 40 :
                    self.slantspeed -= (0.5  * self.dt)
                else:
                    self.slantspeed = 40
                    
                
                
            self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
            if not self.key["jump"]:
                self.sp("act_vel",[self.gp("act_vel")[0],self.gp("act_vel")[0]])
            else:
                self.sp("act_vel",[self.gp("act_vel")[0],abs(self.gp("act_vel")[1])])
            om.translate(self,"player", self.gp("act_vel"),usedt=1)
            self.sp("desrot",45) 
    else:
        
        self.sp("slantdir","l")
        if not slanted == self.lastframeslanted:
            index = collisionboxtype.index("slantl")
            # if not ground2:
            om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] +16,collisionbox["inst"][index].realpos[1] -20]
            self.sp("act_vel",[  self.gp("act_vel")[0] * 1.1    ,    -1 * self.gp("act_vel")[0] * 1.1   ])
            self.sp("des_vel",[  self.gp("des_vel")[0] * 1.1    ,    -1 * self.gp("des_vel")[0] * 1.1   ])
            self.slantspeed = abs(self.gp("des_vel",0))
                # else:
                # 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
        else:
            if abs(self.key["x"]) > 0:
                self.sp("des_vel",[         self.key["x"] * self.slantspeed             ,    self.gp("des_vel")[1]   ])
                
                if self.slantspeed < 200:
                    self.slantspeed += (1  * self.dt)
                    
                    
            elif self.gp("des_vel",0) > -100:
                self.sp("des_vel",[  self.gp("des_vel",0) + (1*self.dt)    ,    self.gp("des_vel")[1]   ])
                if  self.slantspeed > 40 :
                    self.slantspeed -= (0.5  * self.dt)
                else:
                    self.slantspeed = 40
                    
                    
                    
                    
                    
            self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
            if not self.key["jump"]:
                self.sp("act_vel",[self.gp("act_vel")[0],-1 * self.gp("act_vel")[0]])
            else:
                self.sp("act_vel",[self.gp("act_vel")[0], self.gp("act_vel")[1]])
            om.translate(self,"player", self.gp("act_vel"),usedt=1)
            self.sp("desrot",-45)








    if -5 < self.gp("desrot") < 5:
        om.objects["playersprite"]["rot"]  =  0
    else:
        om.objects["playersprite"]["rot"]  =  self.unilerp(om.objects["playersprite"]["rot"],self.gp("desrot"),5,roundto=2) 

    if self.key["jump"]:
        self.sp("fss",16)
        self.sp("desmooth",5)

        #normal
        self.sp("jumpable",False)
        self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
        self.sp("mode","in-air")
        self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
        om.translate(self,"player",[0,self.gp("act_vel")[1]],usedt=1)
        
        