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

def main(self,ground,axis):
     #AIR DASH
    if self.key["jump"] and not ground and not self.lastkey["jump"]:
        if not self.isthere("doublejumpcd") and self.gp("candj"):
            self.bailable = 0
            self.sp("candj",0)
            self.wait("inv",0.3,0)
            self.sp("dashmeter",self.gp("dashmeter") + 30)
            self.wait("dashrem",2)
            # cm.setcond("playercam","shake",6)
            actmult = [160,160]
            actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
            desmult = [160,160]
            desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]
            # self.spin(21,0.4,0.1)

            self.sp("dashav",self.listdiv(actvel,80))
            self.sp("dashdv",self.listdiv(desvel,80))

            self.sp("act_vel",0,1)
            self.sp("des_vel",0,1)
            self.sp("act_vel",0,0)
            self.sp("des_vel",0,0)
            self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
            self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))