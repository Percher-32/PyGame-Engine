import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
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

def main(self,id,info):
    birbs = []
    for _ in range(om.get_value(id,"num")):
        bid = om.add(self,[info["pos"][0] + random.randint(-200,200),info["pos"][1]],"bird",0,"bird",[1.2,1.2],univars.grandim,keepprev=1,info={"master":id})
        birbs.append(bid)

    om.set_value(id,"birds",birbs)
        
    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)

