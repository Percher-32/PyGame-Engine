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
    om.objects[id]["type"]  = "turret"
    om.set_value(id,"shotimer",0)
    om.set_value(id,"maxtimer",2)
    om.objects[id]["sizen"] = [2,2]
    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)