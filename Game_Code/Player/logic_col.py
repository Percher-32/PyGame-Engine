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

def main(self,ground,instlist,collision):
    if ground:
        self.sp("mode","grounded")
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

    if collision["topmid"]["inst"] and not collision["midmid"]["inst"]:
        self.sp("act_vel",[   self.gp("act_vel")[0] * 1  , -10 ])
        om.objects["player"]["pos"][1] =  collision["topmid"]["inst"][0].realpos[1] + 40
        # self.sp("des_vel",[  self.gp("des_vel")[0] * 1   ,  abs(self.gp("des_vel")[1]) * -1 ])
        self.sp("jumpable",False)
        
        
