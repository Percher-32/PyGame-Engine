import data.Game_Code.Ui.start_menu
import data.Game_Code.Ui.level_select
import data.Managers.Gamemanager as Gamemananager
um = Gamemananager.um



class Uiclass:
    """
        contains all the ui state files
    """
    def __init__(self):
        self.start_menu = data.Game_Code.Ui.start_menu
        self.level_select = data.Game_Code.Ui.level_select
        
        
    def main(self,GM):
        if um.state == "start_menu":
            GM.publicvariables["shaderstate"] = 1
            self.start_menu.main(GM)
        if um.state == "level_select":
            GM.publicvariables["shaderstate"] = 1
            self.level_select.main(GM)
            
        if um.state == "maingame":
            GM.publicvariables["shaderstate"] = 0
            
    def init_all(self,GM):
        self.start_menu.init(GM)
        self.level_select.init(GM)
            
    
        
        
# Ui = Uiclass()
# """
#     an instance of the Uiclass class
# """