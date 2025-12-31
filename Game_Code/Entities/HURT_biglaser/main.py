import Managers.Gamemanager as Gamemananager
import Managers.univars as univars 
import Game_Code.Utils.Entities as Entities
import math
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
    rot = om.get_value(id,"rot")
    speed = om.get_value(id,"speed")
    timer = om.get_value(id,"time")
    maxtimer = om.get_value(id,"maxtimer")
    if speed < om.get_value(id,"topspeed"):
        speed += 1*st*om.speed
    timer -= 0.1*st * om.speed
    om.set_value(id,"speed",speed)
    om.set_value(id,"time",timer)



    Entities.damageable(id,20,range=600,self=self)





    playervec = pygame.Vector2(om.objects["player"]["pos"])
    selfpos =  pygame.Vector2(info["pos"])
    vectoplayer = playervec-selfpos
    desrot = vectoplayer.angle * -1
    tr = om.get_value(id,"tr")
    if univars.func.dist(info["pos"],om.objects["player"]["pos"]) < 100:
        tr  = 1
    d1 = desrot
    d2 = desrot - 360
    d3 = desrot + 360

    rank = [abs(d-rot) for d in [d1,d2,d3]]

    first = min(rank)

    desrot = [d1,d2,d3][rank.index(first)]

    rot = self.unilerp(rot,desrot,tr)


    # rot = desrot
    # rot += (20*st)
    om.set_value(id,"rot",rot)

    vel = [ math.cos(rot/180 * math.pi) *  speed, math.sin(rot/180 * math.pi) *  speed  ]


    om.translate(self,id,vel,1)
    om.objects[id]["rot"] = rot




    shake = int((maxtimer - timer)/maxtimer * 20)

    om.objects[id]["pos"][0] += random.randint(-1 * shake,shake)
    om.objects[id]["pos"][1] += random.randint(-1 * shake,shake)
    addon = [(32 * math.sin(om.objects[id]["rot"]/180 * math.pi)) ,
            (32 * math.cos(om.objects[id]["rot"]/180 * math.pi)) ]
    addon = [0,0]
    # pm.particlespawnbluprint([om.objects[id]["pos"][0] + addon[0],om.objects[id]["pos"][1] + addon[1] ],"exp",initvel=[  math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 , math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 ])



    if univars.func.dist(info["pos"],om.objects["player"]["pos"]) < 20 or timer < 0 or om.get_value(id,"HP") < 0:
        if univars.func.dist(info["pos"],om.objects["player"]["pos"]) < 20:
            if self.gp("homing") == 0:
                if not self.isthere("inv"):
                    self.wait("BAIL",0.5)
        for _ in range(3):
            pm.particlespawnbluprint([om.objects[id]["pos"][0],om.objects[id]["pos"][1] ],"exp2",initvel=[vel[0]/20,vel[1]/20])
        om.removeid(id)





self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)