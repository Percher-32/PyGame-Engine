import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import math




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


def main(self):
    rot = om.objects["playersprite"]["rot"]
    om.objects["playersprite"]["pos"][0] = om.objects["player"]["pos"][0] - math.sin((rot/180) * math.pi) * 40
    om.objects["playersprite"]["pos"][1] = om.objects["player"]["pos"][1] - math.cos((rot/180) * math.pi) * 40
    
    if self.gp("des_vel")[0] > 0:
            om.flip("playersprite","right")
    if self.gp("des_vel")[0] < 0:
            om.flip("playersprite","left")
    if not abs(self.key["x"]) > 0:
        om.playanim(self.dt,"playersprite","idle",forceplay=True)
    elif not abs(self.gp("des_vel")[0]  - self.key["x"] * 150) < 20:
        om.playanim(self.dt,"playersprite","moveidle",forceplay=True)
    else:
        om.playanim(self.dt,"playersprite","fastidle",forceplay=True)
        
        
    
    if self.isthere("BAIL"):
        om.objects["playersprite"]["sn"] = 0
        om.objects["skateboard"]["sn"] = 0

        


