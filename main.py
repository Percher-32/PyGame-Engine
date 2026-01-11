import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import cProfile
import os
import pygame
import random
import math
import sys
from functools import partial

sys.path.append("....")



import data.Game_Code.Player.state_rail
import data.Game_Code.Player.state_main
import data.Game_Code.Player.state_slope
import data.Game_Code.Player.logic_spindash
import data.Game_Code.Player.player_main
import data.Game_Code.Player.player_movement
import data.Game_Code.Player.logic_trick
import data.Game_Code.Player.player_movement_core
import data.Game_Code.Player.flare
import data.Game_Code.Player.logic_airdash
import data.Game_Code.Player.logic_col
import data.Game_Code.Player.logic_dashbar
import data.Game_Code.Player.logic_fallin
import data.Game_Code.Player.logic_homingattack
import data.Game_Code.Player.logic_jump
import data.Game_Code.Player.logic_wall
import data.Game_Code.Player.logic_x_cont
import data.Game_Code.Player.player_init
""""""



import data.Game_Code.Utils.Entities
import data.Game_Code.Utils.Player
import data.Game_Code.Utils.math
""""""






import data.Game_Code.Core.Game_start
import data.Game_Code.Core.quick_reload
import data.Game_Code.Core.reload
import data.Game_Code.Core.Update








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
am = Gamemananager.am
pm = Gamemananager.pm


class PlayerClass:
	def __init__(self):
		self.state_rail              =      data.Game_Code.Player.state_rail.main
		self.state_main              =      data.Game_Code.Player.state_main.main
		self.state_slope             =      data.Game_Code.Player.state_slope.main
		self.logic_spindash	         =	    data.Game_Code.Player.logic_spindash.main
		self.main                    =      data.Game_Code.Player.player_main.main
		self.movement                =      data.Game_Code.Player.player_movement.main
		self.logic_trick             =	    data.Game_Code.Player.logic_trick.main
		self.movement_core           = 	    data.Game_Code.Player.player_movement_core.main
		self.flare                   = 	    data.Game_Code.Player.flare.main
		self.logic_airdash           = 	    data.Game_Code.Player.logic_airdash.main
		self.logic_col               = 	    data.Game_Code.Player.logic_col.main
		self.logic_dashbar           = 	    data.Game_Code.Player.logic_dashbar.main
		self.logic_fallin            = 	    data.Game_Code.Player.logic_fallin.main
		self.logic_homingattack      = 	    data.Game_Code.Player.logic_homingattack.main
		self.logic_jump              = 	    data.Game_Code.Player.logic_jump.main
		self.logic_wall              = 	    data.Game_Code.Player.logic_wall.main
		self.logic_x_cont            = 	    data.Game_Code.Player.logic_x_cont.main
		self.init                    =      data.Game_Code.Player.player_init.main


Player = PlayerClass()



class Game(Gamemananager.GameManager):
    
    
    
	"""
		this class handles the actual game code and not the game engine code.\n
		it inherits the in-engine properties
	"""
	def __init__(self,screen,fm):
     
  
   
   
		self.spawnbiglaser        =   partial(data.Game_Code.Utils.Entities.spawnbiglaser       ,self = self)
		self.spawnlaser           =   partial(data.Game_Code.Utils.Entities.spawnlaser          ,self = self)
		self.entity_list_create   =   partial(data.Game_Code.Utils.Entities.entity_list_create  ,self = self)
		self.oncreate             =   partial(data.Game_Code.Utils.Entities.oncreate            ,self = self)
		self.cond                 =   partial(data.Game_Code.Utils.Entities.cond                ,self = self)
		self.qrcond               =   partial(data.Game_Code.Utils.Entities.qrcond              ,self = self)
  
  
	
         
		self.sp                   =   data.Game_Code.Utils.Player.sp
		self.gp                   =   data.Game_Code.Utils.Player.gp
		self.spin                 =   partial(data.Game_Code.Utils.Player.spin             ,self = self)
       
       
       
		self.valsign              =   data.Game_Code.Utils.math.valsign
		self.sign                 =   data.Game_Code.Utils.math.sign
		self.listadd              =   data.Game_Code.Utils.math.listadd
		self.listdiv              =   data.Game_Code.Utils.math.listdiv
		self.customunilerp        =   data.Game_Code.Utils.math.customunilerp
		self.unilerp              =   partial(data.Game_Code.Utils.math.unilerp             ,self = self)
		self.rotlerp              =   partial(data.Game_Code.Utils.math.rotlerp             ,self = self)
  

  
  
		
		self.attackerbox = {"obj":[]}
		self.typesofhoming = ["enemy-L","omnispring","goal","turret","rocket","easybot","HURT_biglaser","spring","rolly"]
		self.ingametime = 0
		self.boardoffset = [0,0]
		self.playeroffset = [0,0]
		self.camzoom = 0.3
		self.objrange = 1000
		self.bailable = 0
		self.skatedetach = 0
		self.lookaheady = 0
		self.timesdone = 1
		self.scores = {}
		self.homingcharge = 0
		self.lookahead = 100
		self.lerpshake = 0
		self.actualwaterheight = 0
  
  
		super().__init__(screen,fm)
		self.publicvariables["mood"] = "sunset"
		self.publicvariables["gamespeed"] = 1
		self.publicvariables["showater"] = 1
		self.publicvariables["waterh"] = -(64 * 0.4)
  
  
  
  
  
  
  



	#CORE FUNCTIONS
	def onreload(self):
		am.play_song("debug3")
		data.Game_Code.Core.reload.main(self,Player)
     
	def quickrel(self):
		data.Game_Code.Core.quick_reload.main(self,Player)

	def commence(self):
		data.Game_Code.Core.Game_start.main(self)

	def update(self):
		self.wait("switchsong",1)

		if self.ondone("switchsong"):
			if am.current_song == "debug3":
				am.swapcont("debug4")
			else:
				am.swapcont("debug3")
				
		data.Game_Code.Core.Update.main(self,Player)








rm = Game(univars.screencol,fm )
rm.Run()