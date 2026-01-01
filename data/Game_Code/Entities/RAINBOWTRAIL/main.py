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

def main(self,id,info,st):
    if om.objects[id]["alpha"] < 10:
        om.removeid(id)
    else:
        om.objects[id]["alpha"] -= 5 * st
        # om.lights.pop(id + "[obj-light]"+ "FIREBALL")
        om.lighttoenemy(id,"l1",color=om.get_value(id,"col"),colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=om.objects[id]["alpha"]/10)




self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)