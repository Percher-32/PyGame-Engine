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

def init(self):
    inc = 0
    um.addrect([univars.ui_screen_size[0],univars.ui_screen_size[1]],["level_select"],pos = [0,0],name="background2",color=(0,0,0),layer=0)
    for level in self.playablelevels:
        inc += 1
        
        um.addbutton([400,200],["level_select"],[-1.3 + (inc*0.7),0],level + "button",color=univars.theme["dark"],layer=1)
        um.addtext(level + "text",level,univars.defont,[0,-0.5],col=univars.theme["bright"],states=["level_select"],layer = 2,size=50)
        um.bindtobutton(level + "text",level + "button",offset=[0,-0.5])
        um.addglide(level + "button",univars.sizes["display"],univars.sizes["display_select"])

def main(self):
    pass
