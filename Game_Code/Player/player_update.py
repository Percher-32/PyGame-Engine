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

def main(self,collision,collisionlisttype,instlist):
     #UPDATE POSITIONS AND ROTATIONS
    rail = self.rail
    if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ) or rail:
        self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
        om.translate(self,"player",self.gp("act_vel"),usedt=1)
        if self.isthere("BAIL"):
            self.sp("desrot",90)
        
        if self.isthere("trick3"):
            if self.key["x"] > 0:
                self.sp("desrot",-180)
            else:
                self.sp("desrot",180)

        # if round(self.gp("desrot")) == 270:
        # 	self.sp("desrot",-90)
            # print(self.gp("desrot"))
        # if self.gp("desrot") < 0:
        # 	self.sp("desrot",0 - self.gp("desrot"))
        if self.isthere("rotate"):
            self.sp("rotoffset",self.gp("rotoffset") + (self.gp("rot")*self.dt) )

            self.sp("rot",self.gp("rot") - (self.valsign(self.gp("rot")) * abs(self.gp("rotdes") * self.dt)       ) )
            
        # om.objects["playersprite"]["rot"] = a
        if abs(self.gp("unboundrot")) > 180 and abs(self.gp("rotoffset")) > 180 :
            min_value = -180
            max_value = 180
            range_size = max_value - min_value

            self.sp("rotoffset",((self.gp("rotoffset") - min_value) % range_size) + min_value)
            self.sp("unboundrot",((self.gp("unboundrot") - min_value) % range_size) + min_value)


        if self.gp("slinging"):
            if abs(self.gp("unboundrot")) > 180 :
                min_value = -180
                max_value = 180
                range_size = max_value - min_value

                self.sp("unboundrot",((self.gp("unboundrot") - min_value) % range_size) + min_value)
            

        # min_value = -180
        # max_value = 180
        # range_size = max_value - min_value
        # self.sp("rotoffset", ((self.gp("rotoffset") - min_value) % range_size) + min_value)
        # 	self.sp("rotoffset",self.gp("rotoffset") - 360)
        # if self.gp("rotoffset") < -180:
        # 	self.sp("rotoffset",self.gp("rotoffset") + 360)


        rot = self.gp("unboundrot")
        if not self.gp("slinging"):
            dest = self.gp("desrot")+ self.gp("rotoffset")
        else:
            dest = self.gp("slomorot")

        d1 = abs(rot - (dest - 360))
        d2 = abs(rot - (dest + 360))
        d3 = abs(rot - (dest + 0))
        
        destinations = {d1:dest-360,d2:dest+360,d3:dest}


        dest = destinations[min([d1,d2,d3])]


        # if path == d1: 
        # dest = fm.frame* 30
        # print(dest)
        # om.objects["playersprite"]["rot"]   +=  30
        sm = 5
        
        if self.isthere("trick3"):
            sm = 3
        # om.objects["playersprite"]["rot"]   =  
        if not self.gp("slinging"):
            self.sp("unboundrot",self.unilerp(rot,dest,sm,roundto=2))
            a = self.gp("unboundrot")
            min_value = -180
            max_value = 180
            range_size = max_value - min_value
            a = ((a - min_value) % range_size) + min_value
            if -5 < a < 5:
                om.objects["playersprite"]["rot"]  =  0
            else:
                om.objects["playersprite"]["rot"] = a
        else:
            self.sp("unboundrot",self.unilerp(rot,dest,sm,roundto=2,useigt=0))
            a = self.gp("unboundrot")
            min_value = -180
            max_value = 180
            range_size = max_value - min_value
            a = ((a - min_value) % range_size) + min_value
            om.objects["playersprite"]["rot"] = a
        

            
    
    

        if not rail:
            #prevent no-clip
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
                    
                    
                    
                    