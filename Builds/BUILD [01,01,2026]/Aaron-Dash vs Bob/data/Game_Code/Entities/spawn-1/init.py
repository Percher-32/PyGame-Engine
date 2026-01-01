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
    om.objects[id]["type"]  = "spawn-1"
    om.set_value(id,"spawned",0)
    om.set_value(id,"sid",[])
    if om.get_value(id,"ir") == 0:
        om.set_value(id,"ir",500)
    if om.get_value(id,"mp") == 0:
        om.set_value(id,"mp",5)

    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)