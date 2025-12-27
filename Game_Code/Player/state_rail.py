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

def main(self,collisionbox,rail,collisionboxtype) :
    """
    Returns [railrot and raildir]
    """
    railrot = 0
    raildir = "r"
    rail = 0
    if "rail" in collisionboxtype:
        # self.sp("homing",0)
        self.bailable = 0
        om.speed = univars.func.lerp(om.speed,1,5,roundto=2)
        self.sp("slinging",0)
        self.sp("jumpable",True)
        self.killtimer("rotate")
        self.sp("rotoffset",0)
        
        
        
        
        
        
        railpiece = collisionbox["inst"][0]
        
        
        if railpiece.name == "rail":
            railrot = railpiece.rot
        else:
            railrot = railpiece.rot + 45
            
            
        if not self.gp("lastontherail"):
            # print()
            self.sp("entervel",univars.func.dist([0,0],self.gp("act_vel")))
        
        
        #increase speed
        self.sp("entervel",abs(self.gp("entervel") + (2*self.dt) ))

        
        playerpos = om.objects["player"]["pos"]
        
        


        #Get joystick rot  VECTOR2
        axisvec = pygame.math.Vector2(self.key["x"],self.key["y"])
        if axisvec.length() == 0:
            axisvec = pygame.math.Vector2(self.lastaxis)
        if axisvec.length() == 0:
            axisvec = pygame.math.Vector2(self.gp("des_vel",0),self.gp("des_vel",1))
        if axisvec.length() == 0:
            axisvec = pygame.math.Vector2(0,1)
        axisvec = axisvec.normalize()

        #Get rail rot  VECTOR2
        railvec = pygame.Vector2()
        railvec.from_polar((1,railrot))

        if axisvec.dot(railvec) > 0:
            raildir = 1
            self.sp("dirforrail","l")
        else:
            raildir = -1
            self.sp("dirforrail","r")

        #LIMIT THE SPEED
        if self.gp("entervel") > 220:
            self.sp("entervel",220)



        #Player rotate in rail direction
        self.sp("desrot",railrot)
        
        
        
        #set railvelocity
        railvel = [  self.gp("entervel") * math.cos((railrot/180) * math.pi) * raildir, self.gp("entervel")  * math.sin((railrot/180) * math.pi) * raildir ]
        self.println(railvel,13)
        self.sp("act_vel",railvel)
        self.sp("des_vel",railvel)

        
        
        if not self.key["jump"]:
            if not (railrot == 0 or railrot == 90 or railrot == -90 or railrot == 180 or railrot == -180):
                playerpos[1] = -1 * (     ( (railrot/45)*playerpos[0] )  + (   (-1* railpiece.realpos[1]) -    (railpiece.realpos[0]*(railrot/45))       )                      )
            elif railrot == 0:
                playerpos[1] = railpiece.realpos[1]
            elif railrot == 90:
                playerpos[0] = railpiece.realpos[0]
            elif railrot == -90:
                playerpos[0] = railpiece.realpos[0]
            elif railrot == 180:
                playerpos[1] = railpiece.realpos[1]
            elif railrot == -180:
                playerpos[1] = railpiece.realpos[1]
                
                
                
            
                
            om.objects["player"]["pos"] = playerpos
            
            
            if railpiece.name == "rail":
                om.translate(
                        self,"player",vector=
                                            [
                                                  -1 * (math.sin((railrot/180) * math.pi) * 5) ,
                                                  -1 * (math.cos((railrot/180) * math.pi) * 5) 
                                            ],
                                            usedt=0
                            )
                
            elif railpiece.name == "rail-diag":
                om.translate(
                        self,"player",vector=
                                            [
                                                  -1 * (math.sin((railrot/180) * math.pi) * 50) ,
                                                  1 * (math.cos((railrot/180) * math.pi) * 50) 
                                            ],
                                            usedt=0
                            )


        if self.key["jump"]:
            # if self.gp("jumpable"):
            jumpvec = railvec.rotate(90)
            # newvec = newvec + axisvec
            jumpvec.scale_to_length(100)
            self.sp("des_vel",[jumpvec.x + self.gp("des_vel",0),jumpvec.y + self.gp("des_vel",1)])
            self.sp("act_vel",[jumpvec.x + self.gp("act_vel",0),jumpvec.y + self.gp("act_vel",1)])
        
        
        
        
        
        
        
        
        #PREVENT NO_CLIP
                

        
        
        
        
        
        #particles
        parts = om.objects["player"]["pos"]
        vel = [self.gp("act_vel")[0]/7,self.gp("act_vel")[1]/7]
        pm.particlespawnbluprint(parts,"grind",initvel= vel)
        
        
        
        
        self.lastdirrail = railrot
        
        
        if abs(self.key["x"]) > 0 or abs(self.key["y"]) > 0:
            self.lastaxis = (self.key["x"],self.key["y"])
        
        
        self.railrot = railrot
        self.lastrail = rail
        self.raildir = raildir
        