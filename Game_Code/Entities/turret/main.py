import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import random
import pygame





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

def main(self,id,info,st):
    om.set_value(id,"canhome",1)
    om.set_value(id,"shotimer",om.get_value(id,"shotimer") - st/2)
    if om.get_value(id,"shotimer") < 0:
        playervec = pygame.Vector2(om.objects["player"]["pos"])
        selfpos =  pygame.Vector2(info["pos"])
        om.set_value(id,"maxtimer",5)


        vectoplayer = playervec-selfpos

        if  600 > abs(vectoplayer.length()) > 20:
            if om.get_value(id,"shotimer") < 0 :
                rot = vectoplayer.angle * -1 + random.randint(-50,50)
                om.set_value(id,"rot",om.get_value(id,"rot") - (10*st) )
                # om.translate(self,id,[math.sin(fm.frame/100) * 100,0],usedt=0)
                # rot = om.get_value(id,"rot")
                for i in range(1):
                    for i in [0,90,180,-90]:
                        rot = i + random.randint(0,0) + om.get_value(id,"rot")
                        self.spawnlaser(om.objects[id]["pos"],40,rot,id,3,extraspeed=[self.gp("act_vel",0)/10,self.gp("act_vel",1)/10])
                om.set_value(id,"shotimer",om.get_value(id,"maxtimer"))




self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)