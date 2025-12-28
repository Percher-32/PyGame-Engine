import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
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



        

    if not self.isthere("skatego"):
        if self.isthere("BAIL"):
            om.objects["skateboard"]["rot"] = 0
            
            om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0] -10,om.objects["player"]["pos"][1] - 0]
        else:
            
            om.objects["skateboard"]["pos"][0] = om.objects["player"]["pos"][0] - math.sin((rot/180) * math.pi) * 5
            om.objects["skateboard"]["pos"][1] = om.objects["player"]["pos"][1] - math.cos((rot/180) * math.pi) * 5
            om.objects["skateboard"]["rot"] = rot
    
    else:
        if self.timers["skatego"] >= 20/2 :
            pm.particlespawnbluprint(om.objects["skateboard"]["pos"],"star",initvel=[self.key["x"] * 10,self.key["y"] * 10])
            # om.translate(self,"skateboard",self.skatevel,1)
            om.objects["skateboard"]["pos"] = self.unilerp(om.objects["skateboard"]["pos"],self.skatevel,3)
            om.rotate(self,"skateboard",40)
        else:
            om.objects["skateboard"]["pos"] = self.unilerp(om.objects["skateboard"]["pos"],om.objects["player"]["pos"],2)
            om.objects["skateboard"]["rot"] = self.unilerp(om.objects["skateboard"]["rot"],rot,2)


        # colb = om.collide("skateboard",0,cam,extra=300)
    
    
        
    self.boardoffset[1] = min([self.boardoffset[1],100])
    om.objects["skateboard"]["pos"][0] += self.boardoffset[0]
    om.objects["skateboard"]["pos"][1] += self.boardoffset[1]

    om.objects["playersprite"]["pos"][0] += self.playeroffset[0]
    om.objects["playersprite"]["pos"][1] += self.playeroffset[1]			
    
