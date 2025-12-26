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
    self.sp("homing",0)
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
    if not self.lastrail  == rail or not self.lastdirrail == railrot:
        self.sp("entervel",univars.func.dist([0,0],self.gp("act_vel")) )


        

        axisvec = pygame.math.Vector2(self.key["x"],self.key["y"])
        if axisvec.length() == 0:
            axisvec = pygame.math.Vector2(self.gp("des_vel",0),self.gp("des_vel",1))
        if axisvec.length() == 0:
            axisvec = pygame.math.Vector2(1,0)
        # print(axisvec.length())
        axisvec = axisvec.normalize()

        railvec = pygame.Vector2()
        railvec.from_polar((1,railrot))
        # print(railvec)
        # Vector2.from_polar((r, phi))

        if axisvec.dot(railvec) > 0:
            raildir = 1
            self.sp("dirforrail","l")
        else:
            raildir = -1
            self.sp("dirforrail","r")



        # self.sp("dirforrail",self.lastdirslant)
        # if self.gp("dirforrail") == "l":
        # 	raildir = 1
        # else:
        # 	raildir = -1



        if railpiece.name == "rail":
            om.objects["player"]["pos"] = [
                                            collisionbox["inst"][collisionboxtype.index("rail")].realpos[0]  -  (math.sin((railrot/180) * math.pi) * 5) ,
                                            collisionbox["inst"][collisionboxtype.index("rail")].realpos[1]  -  (math.cos((railrot/180) * math.pi) * 5) 
                                        ]
        else:
            om.objects["player"]["pos"] = [
                                            collisionbox["inst"][collisionboxtype.index("rail")].realpos[0]  -  (math.sin((railrot/180) * math.pi) * 20) ,
                                            collisionbox["inst"][collisionboxtype.index("rail")].realpos[1]  -  (math.cos((railrot/180) * math.pi) * 20) 
                                        ]
        motivate = [  300 * math.cos((railrot/180) * math.pi) * raildir,300   * math.sin((railrot/180) * math.pi) * raildir ]
        om.translate(self,"player",motivate,usedt=1)
        # if self.gp("entervel") < 1:
        # 	self.sp("entervel",1)

    
    # if abs(self.key["x"]) > 0.5 or abs(self.key["y"]) > 0.5 and not self.key["jump"]:
    self.sp("entervel",self.gp("entervel") + 2 )
    self.sp("entervel",self.gp("entervel") + 2 )

    axisvec = pygame.math.Vector2(self.key["x"],self.key["y"])
    if axisvec.length() == 0:
        axisvec = pygame.math.Vector2(self.gp("des_vel",0),self.gp("des_vel",1))
    if axisvec.length() == 0:
        axisvec = pygame.math.Vector2(1,0)
    # print(axisvec.length())
    axisvec = axisvec.normalize()

    railvec = pygame.Vector2()
    railvec.from_polar((1,railrot))
    # print(railvec)
    # Vector2.from_polar((r, phi))

    if axisvec.dot(railvec) > 0:
        raildir = 1
        self.sp("dirforrail","l")
    else:
        raildir = -1
        self.sp("dirforrail","r")


    if self.gp("entervel") > 220:
        self.sp("entervel",220)
    if self.gp("entervel") < -220:
        self.sp("entervel",-220)




    self.sp("desrot",railrot)
    
    railvel = [  self.gp("entervel") * math.cos((railrot/180) * math.pi) * raildir, self.gp("entervel")  * math.sin((railrot/180) * math.pi) * raildir ]
    self.sp("act_vel",railvel)
    self.sp("des_vel",railvel)
    self.lastdirrail = railrot

    
    
    # if railrot > 180:
    # 	railrot =  railrot -360

    if self.key["jump"]:
        if self.gp("jumpable"):
            newvec = railvec.rotate(90)
            # newvec = newvec + axisvec
            newvec.scale_to_length(100)
            self.sp("des_vel",[newvec.x + self.gp("des_vel",0),newvec.y + self.gp("des_vel",1)])
            self.sp("act_vel",[newvec.x + self.gp("act_vel",0),newvec.y + self.gp("act_vel",1)])
    parts = om.objects["player"]["pos"]
    vel = [self.gp("act_vel")[0]/7,self.gp("act_vel")[1]/7]
    pm.particlespawnbluprint(parts,"grind",initvel= vel)
    
        
    self.railrot = railrot
    self.raildir = raildir
    self.rail = rail