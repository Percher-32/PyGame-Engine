import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import math
import random





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
    col = om.collide(id,0,cam,extra=300)
    if not self.gp("target") == None:
        if self.gp("target").name == id:
            om.set_value(id,"active",1)
    if om.get_value(id,"active") and not  om.get_value(id,"exp"):
        self.sp("MISSIILETIME",om.get_value(id,"timer")/om.get_value(id,"maxtimer"))

        cm.setcond("playercam","shake",20)
        om.set_value(id,"timeon",om.get_value(id,"timeon") + (st* om.speed))
        om.set_value(id,"timer",om.get_value(id,"timer") - (st/20* om.speed))
        addon = [(64 * math.sin(om.objects[id]["rot"]/180 * math.pi)) ,
                    (64 * math.cos(om.objects[id]["rot"]/180 * math.pi)) ]

        addon = [-40,-40]
        pm.particlespawnbluprint([om.objects[id]["pos"][0] + addon[0],om.objects[id]["pos"][1] + addon[1] ],"exp2",initvel=[  math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 , math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 ])
        om.objects[id]["rot"] += om.get_value(id,"rad")
        om.set_value(id,"vel",om.get_value(id,"vel") + (om.get_value(id,"accel")) * st)
        if om.get_value(id,"vel") > om.get_value(id,"top"):
            om.set_value(id,"vel",om.get_value(id,"top"))
        om.objects[id]["pos"][0] += math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * st + random.randint(-20,20)
        om.objects[id]["pos"][1] -= math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * st + random.randint(-20,20)


        if len(col["inst"]) > 0 and om.get_value(id,"timeon") > 50 or om.get_value(id,"timer") < 0:
            om.set_value(id,"exp",1)
            om.objects[id]["pos"] = om.get_value(id,"sp")
            self.sp("exithm",1)
            om.set_value(id,"canhome",0)

    if om.get_value(id,"exp"):
        if om.objects[id]["rendercond"]:
            pm.particlespawnbluprint([om.objects[id]["pos"][0],om.objects[id]["pos"][1] ],"exp3",initvel=[  math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel")  , math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel")  ])
        om.objects[id]["rendercond"] = 0
        om.set_value(id,"canhome",0)
        # self.qrcond(id,info) #MAGEBE







self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)