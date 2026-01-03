import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Ui.Ui_class




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



Ui = data.Game_Code.Ui.Ui_class.Uiclass()

def main(self,Player):
    
    self.a = 0
    
    
    # Ui.init_all(self)
    Player.init(self,[0,60])
    
    if "game" in self.states:
        um.changestate("maingame",None)
    
    if "menu" in self.states:
        um.changestate("start_menu","start_button")
        
    if "test" in self.states:
        um.changestate("level_select",None)
    

    if sm.state == "game":
        om.BAKE()
