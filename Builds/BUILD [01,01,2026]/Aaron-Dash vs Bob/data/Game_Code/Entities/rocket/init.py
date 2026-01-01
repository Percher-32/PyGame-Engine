import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars





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

def main(self,id,info):
    om.objects[id]["sizen"] = [2,2]

    if not id in om.values.keys():
        om.set_value(id,"vel",1)
        om.set_value(id,"accel",1)
        om.set_value(id,"top",40)

        om.set_value(id,"rad",-0.2)
        om.set_value(id,"maxtimer",20)



    om.set_value(id,"canhome",1)
    om.set_value(id,"timer",om.get_value(id,"maxtimer"))
    om.set_value(id,"timeon",0)
    om.set_value(id,"active",0)
    om.set_value(id,"exp",0)
    om.set_value(id,"sp",om.objects[id]["pos"])
    om.set_value(id,"sr",om.objects[id]["rot"])
    
    
    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)