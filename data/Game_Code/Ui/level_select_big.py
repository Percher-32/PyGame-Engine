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
    um.addtext("level_name","NONE",univars.defont,[0,0.8],col=univars.theme["bright"],size=80,states=["level_select_big"])

def main(self):
    um.elements["level_name"]["text"] = self.leveldo
    buttonid = self.leveldo + "button"
    if not "level_select_big" in um.elements[buttonid]["states"]:
        um.elements[buttonid]["states"].append("level_select_big")
    # um.d
    um.lerpval(buttonid,"pos",[-0.3,-0.1],4)
    um.lerpval(buttonid,"dimensions",[750,750/2],4)
    # um.addglide(buttonid,[750,750/2],[750,750/2])
    
    if self.key["back"] and not self.lastkey["back"]:
        um.changestate("level_select",None)
        
    
