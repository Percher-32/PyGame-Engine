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


def main(self):
    if self.isthere("attack"):
        diam = [400 + (abs(self.gp("act_vel",0)) + abs(self.gp("act_vel",1)))/2 + 200                                                ,
                200 + (abs(self.gp("act_vel",0)) + abs(self.gp("act_vel",1)))/1	+ 200												]
        diams = [500,500]
        if self.flowstate:
            diam[0] *= 1.5
            diam[1] *= 1.5
            diams[0] *= 1.5
            diams[1] *= 1.5
        if self.lastdir == "r":
            dtg = 1
        else:
            dtg = -1
            
            
        self.attackerbox = om.colliderect([om.objects["player"]["pos"][0],om.objects["player"]["pos"][1]],diam,0,cam)
