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

def main(self,ground,rail):
    """
        Handeles all the logic for the dashbar.
    """
    
 
        
    #AUTOFILLBAR
    if ground and not rail:
        # self.sp("dashmeter",self.gp("dashmeter") - min([((40/(self.gp("dashmeter") + 2))*self.dt),2*self.dt]) - (0.5*self.dt))
        self.sp("dashmeter",self.gp("dashmeter") - (1.5 * self.dt * self.gp("dashmeter")/100  ))
    else:
        # self.sp("dashmeter",self.gp("dashmeter") - min([((50/(self.gp("dashmeter") + 2))*self.dt),2*self.dt])  - (0.5*self.dt))
        self.sp("dashmeter",self.gp("dashmeter") - (1.1 * self.dt * self.gp("dashmeter")/100  ))
        
    
    
    #DETERMINES BAR FOR FLOWSTATE    
    self.flowstate =self.gp("dashmeter") > 170



    #CLAMPING
    self.sp("dashmeter",max([self.gp("dashmeter"),0])) 
    self.sp("dashmeter",min([self.gp("dashmeter"),100])) 



