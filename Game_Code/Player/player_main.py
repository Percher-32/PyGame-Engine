import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import math


import Game_Code.Player.player_movement as player_movement
import Game_Code.Player.player_init as player_init
import Game_Code.Player.player_anim as player_anim
import Game_Code.Player.logic_skateboard as logic_skateboard



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



import Game_Code.Camera.player_cam_cont as player_cam_cont





def main(self):
    """
        contins all the code that the player needs to function
    """
    if "player" in om.objects.keys() and "skateboard" in om.objects.keys() and "playersprite" in om.objects.keys():
    # self.println(self.gp("dashmeter") > 0,20)
        #move player
        player_anim.main(self)
        
        logic_skateboard.main(self)
        
        player_movement.main(self)

        player_cam_cont.main(self)
        
        
        if em.controller["options"]:
            player_init.main(self,[0,60])
            self.qrcondHL()

        
        
