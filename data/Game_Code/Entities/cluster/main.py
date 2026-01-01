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

def main(self,id,info,st):
    om.objects[id]["rendercond"] = 0
    col = om.collide(id,0,cam,extra=100)
    bo = 0
    if len(col["obj"]) > 2:
        if "player" in [obj.name for obj in col["obj"] if not obj == None]:
            bo = 1
            # self.print(bo)
        else:
            bo = 0
    else:
        bo = 0
    om.set_value(id,"col",bo)





self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)