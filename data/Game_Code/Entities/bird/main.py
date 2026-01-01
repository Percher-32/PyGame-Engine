import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
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
    if not om.get_value(id,"master") in om.objects:
        om.remove(id)
    else:
        master = om.get_value(id,"master")

        if om.get_value(master,"col") and not om.get_value(id,"active"):
            om.set_value(id,"active",1)
            om.set_value(id,"vel",[  self.gp("act_vel")[0]/10 + random.randint(-10,10) + 5 ,  random.randint(2,6)  ])
            # om.set_value(id,"vel",[  2 + random.randint(-4,4), 2 +   ])
        if om.get_value(id,"active"):
            om.playanim(self.dt,id,"fly")
            om.objects[id]["pos"][0] += om.get_value(id,"vel")[0] * st
            om.objects[id]["pos"][1] -= om.get_value(id,"vel")[1] * st






self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)