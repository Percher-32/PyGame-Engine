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

def main(self):
    rail = self.rail
    railrot = self.railrot
    raildir = self.raildir
    
    
    #POS
    if not rail:
        if self.gp("slinging"):
            self.lookaheady = self.unilerp(self.lookaheady,self.key["y"] * -20,4,roundto=2,useigt=0)
            self.lookahead = self.unilerp(self.lookahead,self.key["x"] * 20,4,roundto=2,useigt=0)
        elif self.gp("homing") == 2:
            self.lookaheady = self.unilerp(self.lookaheady,self.key["y"] * -200,4,roundto=2,useigt=0)
            self.lookahead = self.unilerp(self.lookahead,self.key["x"] * 200,4,roundto=2,useigt=0)
            # self.print("REXTRCTVBIUN")
        else:
            
            if self.gp("leftwall") or self.gp("rightwall"):
                self.lookahead = self.unilerp(self.lookahead,0,4,roundto=2,useigt=1)
                if self.key["y"] < 0:
                    self.lookaheady = self.unilerp(self.lookaheady,200,8,roundto=2)
                elif self.key["y"] > 0:
                    self.lookaheady = self.unilerp(self.lookaheady,-200,8,roundto=2)
                else:
                    self.lookaheady = self.unilerp(self.lookaheady,0,20,roundto=2)
            else:
                self.lookaheady = self.unilerp(self.lookaheady,self.key["y"] * -100,4,roundto=2,useigt=1)
                if self.gp("xinit"):
                    self.lookahead = 0
                if self.gp("des_vel")[0] > 0:
                    self.lookahead = self.unilerp(self.lookahead,400,8,roundto=2)
                elif self.gp("des_vel")[0] < 0:
                    self.lookahead = self.unilerp(self.lookahead,-400,8,roundto=2)
                else:
                    self.lookahead = self.unilerp(self.lookahead,0,20,roundto=2)


                
                
            
            # self.println([self.lookahead,self.lookaheady],3)
    else:
        cm.setcond("playercam","shake",4)
        self.lookaheady = self.unilerp(self.lookaheady,-300 * math.sin((railrot/180) * math.pi) * raildir ,4,roundto=2,useigt=0)
        self.lookahead = self.unilerp(self.lookahead,300 * math.cos((railrot/180) * math.pi) * raildir,4,roundto=2,useigt=0)

    campos = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1]]
    campos[0] += self.lookahead
    campos[1] += self.lookaheady




    #ZOOM
    self.cfcp = om.collide("player",0,cam,extra=3)
    types = [i.info["type"] for i in self.cfcp["obj"]]
    if "camz" in types:
        self.camzoom = om.get_value(    self.cfcp["obj"][types.index("camz")].name                  ,"zoom")
    else:
        self.camzoom = 0.3
    cm.cam_focus_size("playercam",campos,4,self.camzoom / (univars.scaledown/2.5) * 15/7 * (0.8) )
    
    
    
    
    
    #SHAKE
    cm.setcond("playercam","shake",self.unilerp(cm.getcam("playercam","shake"),0,10)     )
