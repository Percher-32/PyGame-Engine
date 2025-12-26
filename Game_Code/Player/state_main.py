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
import Game_Code.Player.logic_jump as logic_jump


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
    if slanted == self.lastframeslanted or self.key["jump"]:
        #MAIN
        rail = self.rail
        if not rail and not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ):
            #IN HERE IS EITHER [NO MIDMID] OR [Yes MIDMID AND GROUND]


            logic_x_cont.main(self,ground)





           
            #wall ledge spin
            if self.gp("des_vel",1) > 0:
                if self.gp("lastframewall") and not self.gp("leftwall") and not self.gp("rightwall") and not (collision["botmid"]["inst"] and collision["botleft"]["inst"] and collision["botright"]["inst"]):
                    self.sp("xinit",False)
                    self.sp("mode","in-air")
                    ground = False
                    if not abs(self.key["x"]):
                        if not self.key["jump"]:
                            if self.gp("lastwall") == "r":
                                self.spin(11 ,1,spindec = 0.2)
                                self.sp("des_vel",[0,200])
                            else:
                                self.spin(-11 ,1,spindec = 0.2)
                                self.sp("des_vel",[0,200])
                    else:
                        
                        if not self.key["jump"]:
                            self.spin(self.valsign(self.key["x"]) * -11 ,1,spindec = 0.2)
                            self.sp("des_vel",[self.key["x"] * 150,200])

            if self.isthere("skid"):
                if ground:
                    pm.particlespawnbluprint(om.objects["player"]["pos"],"grind",initvel=[0,0])
            
            #prevent rotation on walls
            if self.gp("leftwall") or self.gp("rightwall"):
                self.killtimer("rotate")
                self.sp("rotoffset",0)

            #tilt when moving
            if not ground:
                if not self.gp("leftwall") and not self.gp("rightwall"):
                    if abs(self.key["x"]) > 0:
                        if not self.isthere("rotate"):
                            # if not abs()
                            
                            if not self.bailable:
                                self.sp("rotoffset",self.rotlerp(self.gp("rotoffset"),0,5))
                                self.sp("desrot",self.rotlerp(self.gp("desrot"),self.gp("act_vel")[0]/4,5) )


            
            
            
            
            if ground:
                self.sp("desrot",0)
                self.sp("mode","grounded")
                self.sp("jumpable",True)
                self.sp("onboard",True)
            else:
                if self.key["jump"]:
                    self.sp("onboard",True)
                if not self.gp("leftwall") or not self.gp("rightwall"):
                    self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    self.unilerp(self.gp("des_vel")[1],-130,self.gp("fss"),roundto = 0)   ]     )
                    self.sp("mode","in-air")
                # else:
                # 	self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    self.unilerp(self.gp("des_vel")[1],-130,8,roundto = 0)   ]     )
                # 	self.sp("mode","in-air")

                if not self.key["jump"] and not self.isthere("rotate"):
                    if  self.gp("leftwall") or  self.gp("rightwall"):
                        self.sp("onboard",True)
                    else:
                        if not self.bailable:
                            self.sp("desrot",self.key["x"] * 20)




            


            #jumping


            if not self.key["jump"]:
                if not ground:
                    if self.gp("leftwall"):
                        self.sp("desrot",-90)
                        self.sp("desmooth",3)

                    elif self.gp("rightwall"):
                        self.sp("desrot",90)
                        self.sp("desmooth",3)

                # else:
                # 	if not ground:

            logic_airdash.main(self,ground,axis)
            logic_jump.main(self)
            logic_wall.main(self,collision)




            
            self.sp("lastframeswing",self.gp("slinging"))	

            

            
                        
            
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



            if ground:
                self.killtimer("rotate")
                self.sp("rotoffset",0)
                if not self.lastframejumped and not self.gp("lastframewall"):
                    if not self.bailable:
                        self.sp("desrot",0)
                    self.sp("mode","grounded")
                    self.sp("jumpable",True)
                    self.sp("onboard",True)
                    self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
                    self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
                    om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32
                else:
                    self.lastframejumped = 0


        
            
            if collision["topmid"]["inst"] and not collision["midmid"]["inst"]:
                self.sp("act_vel",[   self.gp("act_vel")[0] * 1  , -10 ])
                om.objects["player"]["pos"][1] =  collision["topmid"]["inst"][0].realpos[1] + 40
                # self.sp("des_vel",[  self.gp("des_vel")[0] * 1   ,  abs(self.gp("des_vel")[1]) * -1 ])
                self.sp("jumpable",False)

            
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
            state_rail.main(self,collisionbox,rail,collisionboxtype)
            
            
            




        for ty in ["HURT:laser"]:
            if ty in [ i.info["type"] for i in smallcollisionbox["obj"]]:
                if self.gp("homing") == 0:
                    if not self.isthere("inv"):
                        self.wait("BAIL",0.5)
                    
                    # self.sp("act_vel",[0,0])
                    # self.sp("des_vel",[0,0])

                

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
