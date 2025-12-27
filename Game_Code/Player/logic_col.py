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

def main(self,ground,instlist,collision,collisionlisttype,slanted):
    if not self.rail:
        if slanted == self.lastframeslanted or self.key["jump"] and not slanted:
            #MAIN
            rail = self.rail
            if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ):
                
                #Ground detection
                if ground and self.gp("mode") == "grounded":
                    self.sp("desrot",0)
                    self.sp("onboard",True)
                    self.killtimer("rotate")
                    self.sp("rotoffset",0)
                    if not self.lastframejumped and not self.gp("lastframewall"):
                        if not self.bailable:
                            self.sp("desrot",0)
                        self.sp("mode","grounded")
                        self.sp("jumpable",True)
                        self.sp("onboard",True)
                        self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
                        self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
                        om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32
                    else:
                        self.lastframejumped = 0


                #head bump detection
                if collision["topmid"]["inst"] and not collision["midmid"]["inst"] :
                    self.sp("act_vel",[   self.gp("act_vel")[0] * 1  , -10 ])
                    om.objects["player"]["pos"][1] =  collision["topmid"]["inst"][0].realpos[1] + 40
                    # self.sp("des_vel",[  self.gp("des_vel")[0] * 1   ,  abs(self.gp("des_vel")[1]) * -1 ])
                    self.sp("jumpable",False)
                    
                    
                
                #Smooth ground clipping
                if self.gp("mode") == "grounded":
                    if "ground" in collisionlisttype:
                        self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
                        self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
                        om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32



                if not self.gp("onboard"):
                    if om.get_value("skateboard","fallvalue")< 20:
                        om.set_value("skateboard","fallvalue",om.get_value("skateboard","fallvalue") - 2* self.dt)
                    om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 0]
                    om.translate(self,"skateboard",[0,om.get_value("skateboard","fallvalue")])
                else:
                    om.set_value("skateboard","fallvalue",5)
                    
        
        #get out of wall
        if len(collision["midmid"]["inst"] )> 0 and not slanted and not self.rail :
            top = collision["topmid"]["inst"] or collision["topleft"]["inst"] or collision["topright"]["inst"]
            bot = collision["botmid"]["inst"] or collision["botleft"]["inst"] or collision["botright"]["inst"]
            left = collision["topleft"]["inst"] or collision["midleft"]["inst"] or collision["botleft"]["inst"]
            right = collision["topright"]["inst"] or collision["midright"]["inst"] or collision["botright"]["inst"]
            mip = collision["midmid"]["inst"][0].realpos
            if collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] :
                # self.publicvariables["shaderstate"] = not self.publicvariables["shaderstate"]
                om.translate(self,"player",[self.gp("act_vel")[0] * -1,self.gp("act_vel")[1] * -1],usedt=1)
                self.sp("des_vel",[0,0])
            elif top and not collision["botmid"]["inst"]:
                om.objects["player"]["pos"][1] =  mip[1] + 32
            elif bot and not collision["topmid"]["inst"]:
                om.objects["player"]["pos"][1] =  mip[1] - 32
            elif right and not collision["midleft"]["inst"]:
                om.objects["player"]["pos"][0] = mip[0] - 32
            elif left  and not collision["midright"]["inst"]:
                om.objects["player"]["pos"][0] = mip[0] + 32
        else:
            self.sp("prev_act_vel",self.gp("act_vel"))
            self.sp("prev_des_vel",self.gp("des_vel"))
            self.sp("prevprevpos",om.objects["player"]["pos"])

    
