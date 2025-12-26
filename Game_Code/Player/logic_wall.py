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

def main(self,collision):
    #Wall clinging
    if not collision["midmid"]["inst"]:
        
        #LEFTWALL
        if len(collision["midleft"]["inst"]) > 0 :
            if collision["midleft"]["inst"][0].type == "ground":
                self.sp("leftwall",True)
                self.sp("lastwall","l")
                self.sp("jumpable",True)	
                om.objects["player"]["pos"][0] = collision["midleft"]["inst"][0].realpos[0] + 32

                if not collision["botmid"]["inst"]:
                    self.sp("des_vel",[0,self.gp("des_vel")[1]])
                    self.sp("act_vel",[0,self.gp("act_vel")[1]])
                else:
                    if self.gp("des_vel")[0] < 0:
                        self.sp("des_vel",[0,0])
                    if self.gp("act_vel")[0] < 0:
                        self.sp("act_vel",[0,0])

            else:
                self.sp("leftwall",False)
        else:
            self.sp("leftwall",False)


        #RIGHTWALL
        if len(collision["midright"]["inst"]) > 0 :
            if  collision["midright"]["inst"][0].type == "ground":
                self.sp("rightwall",True)
                self.sp("lastwall","r")
                self.sp("jumpable",True)	
                om.objects["player"]["pos"][0] = collision["midright"]["inst"][0].realpos[0] -32
                if not collision["botmid"]["inst"]:
                    self.sp("des_vel",[0,self.gp("des_vel")[1]])
                    self.sp("act_vel",[0,self.gp("act_vel")[1]])
                else:
                    if self.gp("des_vel")[0] > 0:
                        self.sp("des_vel",[0,0])
                    if self.gp("act_vel")[0] > 0:
                        self.sp("act_vel",[0,0])

            else:
                self.sp("rightwall",False)
        else:
            self.sp("rightwall",False)
            
            
    
    #Wall running
    if self.gp("leftwall") or self.gp("rightwall") and not self.key["jump"]:
        self.sp("des_vel",[self.gp("des_vel")[0],self.key["y"] * 200])
        
     
     
        
    #Wall jumping
    if self.key["jump"]:
        a = 200
        if self.gp("leftwall") and not  len(collision["botmid"]["inst"]) > 0:
            self.sp("dashmeter",self.gp("dashmeter") + (30 * self.dt))
            self.deltimer("rightjump")
            self.wait("leftjump",0.1)
            
            self.spin(-7 ,1,spindec = 0)
            self.sp("jumpable",False)
            self.sp("des_vel",[ self.key["x"] * self.gp("machspeed")  , a     ])
            self.sp("act_vel",[  120 , self.gp("act_vel")[1]     ])
            self.sp("dashmeter",self.gp("dashmeter") + 15)
            self.sp("mode","in-air")
        if self.gp("rightwall") and not  len(collision["botmid"]["inst"]) > 0:
            self.sp("dashmeter",self.gp("dashmeter") + (30 * self.dt))
            self.deltimer("leftjump")
            
            self.spin(7 ,1,spindec = 0)
            self.wait("rightjump",0.1)
            self.sp("jumpable",False)
            self.sp("des_vel",[  self.key["x"] * self.gp("machspeed") , a     ])
            self.sp("act_vel",[  -120 , self.gp("act_vel")[1]     ])
            self.sp("dashmeter",self.gp("dashmeter") + 15)
            self.sp("mode","in-air")


