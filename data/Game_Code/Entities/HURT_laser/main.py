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
    if om.get_value(id,"enid") in om.objects.keys():
        om.set_value(id,"time",om.get_value(id,"time") - st/60)
        # speed = om.get_value(id,"speed")

        # movec = pygame.Vector2()
        # movec.from_polar((speed,dir))


        if om.get_value(id,"time") < 0:
            om.removeid(id)
        else:
            movec = om.get_value(id,"movec")

            movecst = [movec.x*st * om.speed,movec.y*st * om.speed]
            om.translate(self,id,movecst,usedt=0)
    else:
        om.removeid(id)






self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)