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
    om.set_value(id,"canhome",1)
    if not "frq" in om.values[id].keys():
        om.set_value(id,"frq",100)
        om.set_value(id,"speed",100)
        om.set_value(id,"time",20)
        om.set_value(id,"HP",100)
    if not "am" in om.values[id].keys():
        om.set_value(id,"am",1)
    if not "bs" in om.values[id].keys():
        om.set_value(id,"bs",40)


    om.objects[id]["sizen"] = [2,2]
    self.createhpbar(id,1.7,[0,80])
    om.set_value(id,"sp",om.objects[id]["pos"])
    om.set_value(id,"gotimer",0)
    om.set_value(id,"randpos",om.objects[id]["pos"])

  
    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)