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
    if self.key["jump"]:
        self.sp("fss",16)
        # self.sp("desmooth",5)
        if self.gp("jumpable") or ground:
            self.sp("jumpable",0)
            self.deltimer("doublejumpcd")
            self.wait("doublejumpcd",0.2)
            self.sp("candj",1)
            #normal
            self.lastframejumped = 1
            self.sp("jumpable",False)
            self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
            self.sp("mode","in-air")
    else:
        self.lastframejumped = 0
        self.sp("fss",8)