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

def main(self,ground,collision):
               
    #wall ledge spin
    if self.gp("des_vel",1) > 0:
        if self.gp("lastframewall") and not self.gp("leftwall") and not self.gp("rightwall") and not (collision["botmid"]["inst"] and collision["botleft"]["inst"] and collision["botright"]["inst"]):
            self.sp("xinit",False)
            self.sp("mode","in-air")
            ground = False
            if not abs(self.key["x"]):
                if not self.key["jump"]:
                    if self.gp("lastwall") == "r":
                        self.spin(11 ,1,spindec = 0.2)
                        self.sp("des_vel",[0,200])
                        self.print("PRET")
                    else:
                        self.spin(-11 ,1,spindec = 0.2)
                        self.sp("des_vel",[0,200])
                        self.print("PRET")
            else:
                
                if not self.key["jump"]:
                    self.spin(self.valsign(self.key["x"]) * -11 ,1,spindec = 0.2)
                    self.sp("des_vel",[self.key["x"] * 150,200])

    if self.isthere("skid"):
        if ground:
            pm.particlespawnbluprint(om.objects["player"]["pos"],"grind",initvel=[0,0])
    
    #prevent rotation on walls
    if self.gp("leftwall") or self.gp("rightwall") and not self.key["jump"] :
        self.killtimer("rotate")
        self.sp("rotoffset",0)

    #tilt when moving
    if not ground:
        if not self.gp("leftwall") and not self.gp("rightwall"):
            if abs(self.key["x"]) > 0:
                if not self.isthere("rotate"):
                    # if not abs()
                    
                    if not self.bailable:
                        self.sp("rotoffset",self.rotlerp(self.gp("rotoffset"),0,5))
                        self.sp("desrot",self.rotlerp(self.gp("desrot"),self.gp("act_vel")[0]/4,5) )


    if not self.key["jump"]:
        if not ground:
            if self.gp("leftwall"):
                self.sp("desrot",-90)
                self.sp("desmooth",3)

            elif self.gp("rightwall"):
                self.sp("desrot",90)
                self.sp("desmooth",3)

    if not ground:
        if not self.key["jump"] and not self.isthere("rotate"):
            if  not self.gp("leftwall") and not  self.gp("rightwall"):
                if not self.bailable and not self.isthere("rotate"):
                    self.sp("desrot",self.key["x"] * 20)
                    # pass
        
    
    if self.flowstate:
        self.wait("dotrail",0.2)
        if self.ondone("dotrail"):
            colid = random.randint(6,11)
            if colid == 6:
                col = (255, 79, 0)
            elif colid == 7:
                col = (255, 225, 0)
            elif colid == 8:
                col = (26, 255, 0)
            elif colid == 9:
                col = (0, 255, 255)
            elif colid == 10:
                col = (0, 8, 255)
            elif colid == 11:
                col = (255, 0, 203)

            
            ltid = om.add(self,om.objects["player"]["pos"],"player",om.objects["playersprite"]["rot"],"RAINBOWTRAIL",[1.1,1.1],self.dim,layer=0,sn = colid ,keepprev=1,info={"col":col})

            

            


            om.lighttoenemy(ltid,"l1",color=col,colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=30)

    
