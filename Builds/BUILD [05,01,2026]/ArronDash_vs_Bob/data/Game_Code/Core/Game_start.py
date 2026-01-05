import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Ui.Ui_class
import os




Ui = data.Game_Code.Ui.Ui_class.Uiclass()
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
    if "menu" in self.states:
        um.changestate("start_menu","start_button")
    self.playablelevels =   os.listdir("data/Saved/tilemaps")
    self.publicvariables["shaderstate"] = 1
    Ui.init_all(self)
    pass
