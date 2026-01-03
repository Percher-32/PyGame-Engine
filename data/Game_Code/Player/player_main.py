import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import math


import data.Game_Code.Player.player_movement as player_movement
import data.Game_Code.Player.player_init as player_init
import data.Game_Code.Player.player_anim as player_anim
import data.Game_Code.Player.logic_skateboard as logic_skateboard



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



import data.Game_Code.Camera.player_cam_cont as player_cam_cont





def main(self):
    """
        contins all the code that the player needs to function
    """
    if "player" in om.objects.keys() and "skateboard" in om.objects.keys() and "playersprite" in om.objects.keys():
    # self.println(self.gp("dashmeter") > 0,20)
        #move player
        um.changestate("maingame",None)
        player_anim.main(self)
        
        logic_skateboard.main(self)
        
        player_movement.main(self)

        player_cam_cont.main(self)
        
        
        if em.controller["OPT"]:
            player_init.main(self,[0,60])
            self.qrcondHL()

        
        
