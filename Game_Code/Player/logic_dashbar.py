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
    
    
    
    
    #UI
    self.sp("dashmeter",min([300,self.gp("dashmeter")]))
    self.sp("dashmeter",max([0,self.gp("dashmeter")]))




    um.elements["dashbar"]["dimensions"][0] = self.unilerp( um.elements["dashbar"]["dimensions"][0] ,   max([((self.gp("dashmeter") * 10) - 50)/2,0])/3 ,4  )

    

    if self.gp("dashmeter") <= 0:
        um.elements["dashbar"]["dimensions"][0] = 0
    um.elements["dashbar"]["color"] = (0,100,255)



