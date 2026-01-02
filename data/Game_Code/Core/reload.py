import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Ui.start_menu




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


class Uiclass:
    def __init__(self):
        self.start_menu = data.Game_Code.Ui.start_menu

Ui = Uiclass()

def main(self,Player):
    
    self.a = 0
    
    Player.init(self,[0,60])
    Ui.start_menu.init(self)
    
    if sm.state == "debugame":
        um.changestate("maingame",None)
    

    if sm.state == "game":
        om.BAKE()
