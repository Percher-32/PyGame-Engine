import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.day_night_cycle.update as day_night_cycle
import data.Game_Code.Ui.Ui_class





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



def main(self,Player):
    # if um.state == "#
    Ui.main(self)
   

    if "game" == self.states:
        bg.background = "test2"
        Player.main(self)
        self.publicvariables["showater"] = True
        if self.isthere("show-score"):
            um.state = "vic"
            um.addrect([6000,6000],["vic"],[(-0.5 + 0.02) - 0.5,0.8],"atnum",color=(0,0,0),fromstart=0,alpha = 200)
            um.addtext("Victory-lap","",univars.defont,[0,0],univars.theme["accent"],100,"vic")
            um.elements["Victory-lap"]["text"] = self.storedscore + "    " + str(int(self.timers["show-score"]/60) + 1) + "\n\n"  + f"Lowest - time:{self.highest}  on-attempt:{self.highestatt}"

    day_night_cycle.main(self)