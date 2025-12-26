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
    if not self.gp("leftwall") or not self.gp("rightwall") and not ground:
        self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    self.unilerp(self.gp("des_vel")[1],-130,self.gp("fss"),roundto = 0)   ]     )
        self.sp("mode","in-air")