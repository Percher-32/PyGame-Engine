import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Player.player_init as player_init




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
    pass

def main(self):
    buttonid = self.leveldo + "button"
    if not "level_select_big" in um.elements[buttonid]["states"]:
        um.elements[buttonid]["states"].append("level_select_big")
    # um.d
    um.lerpval(buttonid,"pos",[-0.4,0],4)
    um.lerpval(buttonid,"dimensions",[750,750/2],2)
    # um.addglide(buttonid,[750,750/2],[750,750/2])
    
    if self.key["back"] and not self.lastkey["back"]:
        um.changestate("level_select",None)
        
    
