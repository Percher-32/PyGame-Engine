import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math


import Game_Code.Player.state_rail as state_rail
import Game_Code.Player.state_slope as state_slope
import Game_Code.Player.state_main as state_main



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



def main(self,collisionbox,slanted,rail,collision,collisionlisttype,axis,vec,instlist,collisionboxtype,smallcollisionbox,ground):
    raildir = None
    railrot = None
    ground = ground
    
    
    
    if "spring" in [i.info["type"] for i in collisionbox["obj"]]:
        ground = 0
        self.sp("dashmeter",self.gp("dashmeter") + 30)
        self.sp("jumpable",1)
        self.wait("bouncerem",3)
        self.sp("homing",0)
        info = collisionbox["obj"][[i.info["type"] for i in collisionbox["obj"]].index("spring")].info
        sid = collisionbox["obj"][[i.info["type"] for i in collisionbox["obj"]].index("spring")].name
        # cm.setcond("playercam","shake",6)
        actmult = [1,1]
        actvel = [  math.sin(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * actmult[0] * -1.5 , math.cos(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * actmult[1] ]
        desmult = [1,1]
        desvel = [  math.sin(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * desmult[0] * -1.5 , math.cos(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * desmult[1] ]


        self.sp("dashav",self.listdiv(actvel,5))
        self.sp("dashdv",self.listdiv(desvel,5))

        self.sp("act_vel",0,1)
        self.sp("des_vel",0,1)
        self.sp("act_vel",0,0)
        self.sp("des_vel",0,0)
        self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
        self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))




    if not slanted:
        state_main.main(self,slanted,collision,collisionbox,axis,collisionlisttype,vec,instlist,collisionboxtype,smallcollisionbox,ground)
    else:                                                                                                                               
        state_slope.main(self,collisionboxtype,collisionbox,slanted)
            
    return {"railrot":railrot,"raildir":raildir}
