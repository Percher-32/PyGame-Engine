import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math


import Game_Code.Player.player_movement as player_movement
import Game_Code.Player.player_init as player_init



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
                    

        if not abs(self.key["x"]) > 0:
            om.playanim(self.dt,"playersprite","idle",forceplay=True)
        elif not abs(self.gp("des_vel")[0]  - self.key["x"] * 150) < 20:
            om.playanim(self.dt,"playersprite","moveidle",forceplay=True)
        else:
            om.playanim(self.dt,"playersprite","fastidle",forceplay=True)


        player_movement.main(self)

        if em.controller["options"]:
            player_init.main(self,[0,60])
            self.qrcondHL()

 


        
        rot = om.objects["playersprite"]["rot"]
        om.objects["playersprite"]["pos"][0] = om.objects["player"]["pos"][0] - math.sin((rot/180) * math.pi) * 20
        om.objects["playersprite"]["pos"][1] = om.objects["player"]["pos"][1] - math.cos((rot/180) * math.pi) * 20
        if self.gp("des_vel")[0] > 0:
                om.flip("playersprite","right")
        if self.gp("des_vel")[0] < 0:
                om.flip("playersprite","left")


            

        if not self.isthere("skatego"):
            if self.isthere("BAIL"):
                om.objects["skateboard"]["rot"] = 0
                
                om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0] -10,om.objects["player"]["pos"][1] - 0]
            else:
                
                om.objects["skateboard"]["pos"][0] = om.objects["player"]["pos"][0] - math.sin((rot/180) * math.pi) * 5
                om.objects["skateboard"]["pos"][1] = om.objects["player"]["pos"][1] - math.cos((rot/180) * math.pi) * 5
                om.objects["skateboard"]["rot"] = rot
        
        else:
            if self.timers["skatego"] >= 20/2 :
                pm.particlespawnbluprint(om.objects["skateboard"]["pos"],"star",initvel=[self.key["x"] * 10,self.key["y"] * 10])
                # om.translate(self,"skateboard",self.skatevel,1)
                om.objects["skateboard"]["pos"] = self.unilerp(om.objects["skateboard"]["pos"],self.skatevel,3)
                om.rotate(self,"skateboard",40)
            else:
                om.objects["skateboard"]["pos"] = self.unilerp(om.objects["skateboard"]["pos"],om.objects["player"]["pos"],2)
                om.objects["skateboard"]["rot"] = self.unilerp(om.objects["skateboard"]["rot"],rot,2)


            colb = om.collide("skateboard",0,cam,extra=300)
        
        
        
        # if self.isthere("trick2")and self.isthere("VULNERABLE"):
        # 	om.objects["playersprite"]["sn"] = 12
        # 	self.boardoffset[1] = self.unilerp(self.boardoffset[1],100,5)
        # 	self.playeroffset[1] = self.unilerp(self.playeroffset[1],-100,5)
        # 	om.objects["skateboard"]["rot"] = 0
        # 	om.playanim(self.dt,"skateboard","kickflip",1,speed=3)


        if self.isthere("BAIL"):
            om.objects["playersprite"]["sn"] = 0
            om.objects["skateboard"]["sn"] = 0

        if self.isthere("trick1")and self.isthere("VULNERABLE"):
            om.objects["playersprite"]["sn"] = 12
            # self.boardoffset[0] = self.unilerp(self.boardoffset[0],math.sin((rot/180) * math.pi) * 0,4)
            self.boardoffset[1] += 10 * self.dt
            self.playeroffset[1] -= 10 * self.dt
            om.objects["skateboard"]["rot"] = 0
        if self.isthere("trick2")and self.isthere("VULNERABLE"):
            om.objects["playersprite"]["sn"] = 0
            
            self.playeroffset[1] = self.unilerp(self.playeroffset[1],-40,8)
            om.objects["playersprite"]["sn"] = 13
            
            if self.key["x"] > 0:
                om.objects["skateboard"]["rot"] = 45
                self.boardoffset[0] = self.unilerp(self.boardoffset[0],10,3)
            elif self.key["x"] < 0:
                om.objects["skateboard"]["rot"] = -45
                self.boardoffset[0] = self.unilerp(self.boardoffset[0],-10,3)
            else:
                self.boardoffset[1] = self.unilerp(self.boardoffset[1],10,5)
                self.playeroffset[1] = self.unilerp(self.playeroffset[1],-10,5)

            om.playanim(self.dt,"skateboard","kickflip",1,speed=3)
            # om.objects["playersprite"]["rot"] = 180
        elif self.isthere("trick3")and self.isthere("VULNERABLE"):
            
            om.playanim(self.dt,"skateboard","kickflip",1,speed=3)
            om.objects["playersprite"]["sn"] = 13
            
            self.playeroffset[1] = self.unilerp(self.playeroffset[1],-50,8)
            self.boardoffset[1] = self.unilerp(self.boardoffset[1],50,8)
            
            if self.key["x"] > 0:
                om.objects["skateboard"]["rot"] = 0
                # self.playeroffset[0] = self.unilerp(self.playeroffset[0],30,3)
                
                # self.boardoffset[0] = self.unilerp(self.boardoffset[0],30,3)
            else :
                om.objects["skateboard"]["rot"] =0
                # self.playeroffset[0] = self.unilerp(self.playeroffset[0],-30,3)
                
                # self.boardoffset[0] = self.unilerp(self.playeroffset[0],-30,3)

            # om.playanim(self.dt,"skateboard","kickflip",1,speed=3)
            # om.objects["playersprite"]["rot"] = 180
        else:
            
            self.boardoffset[0] = self.unilerp(self.boardoffset[0],0,4)
            self.boardoffset[1] = self.unilerp(self.boardoffset[1],0,4)
            self.playeroffset[0] = self.unilerp(self.playeroffset[0],0,4)
            self.playeroffset[1] = self.unilerp(self.playeroffset[1],0,4)

        

            
        self.boardoffset[1] = min([self.boardoffset[1],100])
        om.objects["skateboard"]["pos"][0] += self.boardoffset[0]
        om.objects["skateboard"]["pos"][1] += self.boardoffset[1]

        om.objects["playersprite"]["pos"][0] += self.playeroffset[0]
        om.objects["playersprite"]["pos"][1] += self.playeroffset[1]			
        
        
        
        
        
        player_cam_cont.main(self)
        
        
