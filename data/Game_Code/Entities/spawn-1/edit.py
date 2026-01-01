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
    if not om.get_value(id,"sid") == 0:
        for i in om.get_value(id,"sid"):
            if i in om.objects.keys():
                om.removeid(i)
    om.set_value(id,"spawned",0)
    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)


