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


def main(self,collisionbox):
    objs = collisionbox["obj"]
    
    
    for obj in objs:
        if obj.name in om.values.keys():
            if obj.info["type"] == "hurt_area":
                self.wait("BAIL",1)
                self.sp("HP",self.gp("HP") - om.get_value(obj.name,"damage"))
                om.removeid(obj.name)
                
                
