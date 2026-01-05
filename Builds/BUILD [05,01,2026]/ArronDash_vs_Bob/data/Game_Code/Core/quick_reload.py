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


def main(self,Player):
    # self.qrcond()
    if "game" == self.states:
        Player.init(self,cm.getcam("def","pos"))
    if "Editor" == self.states:
        om.removeid("enemyzoom")
        cm.setcond("def","pos",cm.getcam("playercam","pos"))
        cm.setcond("def","size",cm.getcam("playercam","size"))

