import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math

import Game_Code.Player.state_rail as state_rail
import Game_Code.Player.player_update as player_update
import Game_Code.Player.logic_homingattack as logic_homingattack
import Game_Code.Player.logic_wall as logic_wall
import Game_Code.Player.logic_airdash as logic_airdash
import Game_Code.Player.logic_x_cont as logic_x_cont
import Game_Code.Player.logic_fallin as logic_fallin
import Game_Code.Player.logic_col as logic_col
import Game_Code.Player.logic_jump as logic_jump

import Game_Code.Player.flare as flare


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

def main(self,slanted,collision,collisionbox,axis,collisionlisttype,vec,instlist,collisionboxtype,smallcollisionbox,ground):
    """
        STATE:
            -when the player is iether on ground or in air
            -not on slope or on rails
    """
    if slanted == self.lastframeslanted or self.key["jump"]:
        #MAIN
        rail = self.rail
        if not rail and not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ):
            #X dir logic
            logic_x_cont.main(self,ground)
            
            #Wall logic
            logic_wall.main(self,collision)
            
            
            #Style logic
            flare.main(self,ground,collision)
            
            #Gravity logic
            logic_fallin.main(self,ground)
            
            
            if self.isthere("dashrem"):
                # print(self.gp("dashav"))
                if not type(self.gp("dashav")) == list:
                    self.sp("dashav",[0,0])

                self.unilerp(self.gp("dashav"),[0,0],3)
                self.unilerp(self.gp("dashdv"),[0,0],3)
                self.sp("act_vel",self.listadd((self.gp("act_vel"),self.gp("dashav"))))
                self.sp("des_vel",self.listadd((self.gp("des_vel"),self.gp("dashdv"))))
                
                # cm.setcond("playercam","shake",0)

            if self.isthere("bouncerem"):
                # if not type(self.gp("dashav")) == list:
                # 	self.sp("dashav",[0,0])
                # print(self.gp("dashav"))
                self.sp("dashav",self.unilerp(self.gp("dashav"),[0,0],7))
                self.sp("dashdv",self.unilerp(self.gp("dashdv"),[0,0],7))
                self.sp("act_vel",self.listadd((self.gp("act_vel"),self.gp("dashav"))))
                self.sp("des_vel",self.listadd((self.gp("des_vel"),self.gp("dashdv"))))
                
                # cm.setcond("playercam","shake",0)


            #water skid
            if  800 > om.objects["player"]["pos"][1] > 700 and not (self.key["jump"] and self.gp("act_vel")[1] >= 0) :
                if abs(self.gp("act_vel")[0]) >= 120:
                    if self.gp("act_vel")[0] > 100:
                        parts = [om.objects["player"]["pos"][0] -5,om.objects["player"]["pos"][1] + 9]
                    else:
                        parts = [om.objects["player"]["pos"][0] -5,om.objects["player"]["pos"][1] + 9]
                    vel = [self.gp("act_vel")[0]/self.dim * 4,4]
                    pm.particlespawnbluprint(parts,"water",initvel= vel)
                    self.sp("act_vel",[   self.gp("act_vel")[0] , 0  ]  ) 
                    self.sp("des_vel",[   self.gp("des_vel")[0] , 0  ]  ) 
                    om.objects["player"]["pos"][1] = 768

                    self.sp("jumpable",1)
                    self.sp("candj",0)


        else:
            #RAIL
            if rail:
                state_rail.main(self,collisionbox,rail,collisionboxtype)
            



        #UPDATE POSITIONS AND ROTATIONS
        player_update.main(self,collision,collisionlisttype,instlist)           
    else:

        if self.gp("slantdir") == "r":
            if self.lastdirslant == "l":
                om.translate(self,"player",[100,40])
                if abs(self.gp("act_vel",0)) > 30:
                    self.sp("act_vel",[self.gp("act_vel",0) + (200) ,self.gp("act_vel",0) + (110) ])
            if self.lastdirslant == "r":
                om.translate(self,"player",[-100,0])
        if self.gp("slantdir") == "l":
            if self.lastdirslant == "r":
                if abs(self.gp("act_vel",0)) > 30:
                    self.sp("act_vel",[self.gp("act_vel",0) - (200) ,self.gp("act_vel",0) + (110) ])
                om.translate(self,"player",[-100,40])
            if self.lastdirslant == "l":
                om.translate(self,"player",[300,0])



    #Jump logic
    logic_jump.main(self,ground)
    
    #Collision logic
    logic_col.main(self,ground,instlist,collision,collisionlisttype,slanted)