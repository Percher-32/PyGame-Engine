import Managers.Gamemanager as Gamemananager
import Managers.univars as univars





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
    om.objects[id]["pos"] = om.get_value(id,"sp")
    om.objects[id]["rot"] = om.get_value(id,"sr")
    om.set_value(id,"canhome",1)
    om.set_value(id,"timer",om.get_value(id,"maxtimer"))
    om.set_value(id,"timeon",0)
    om.set_value(id,"active",0)
    om.set_value(id,"exp",0)
    om.objects[id]["rendercond"] = 1
    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)


