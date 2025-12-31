import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import os
import pygame
import random
import math
import sys
from functools import partial

sys.path.append("....")



import Game_Code.Player.state_rail
import Game_Code.Player.state_main
import Game_Code.Player.state_slope
import Game_Code.Player.logic_spindash
import Game_Code.Player.player_main
import Game_Code.Player.player_movement
import Game_Code.Player.logic_trick
import Game_Code.Player.player_movement_core
import Game_Code.Player.flare
import Game_Code.Player.logic_airdash
import Game_Code.Player.logic_col
import Game_Code.Player.logic_dashbar
import Game_Code.Player.logic_fallin
import Game_Code.Player.logic_homingattack
import Game_Code.Player.logic_jump
import Game_Code.Player.logic_wall
import Game_Code.Player.logic_x_cont
import Game_Code.Player.player_init
""""""



import Game_Code.Utils.Entities
import Game_Code.Utils.Player
import Game_Code.Utils.math
""""""






import Game_Code.Core.Game_start
import Game_Code.Core.quick_reload
import Game_Code.Core.reload
import Game_Code.Core.Update








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


class PlayerClass:
	def __init__(self):
		self.state_rail              =      Game_Code.Player.state_rail.main
		self.state_main              =      Game_Code.Player.state_main.main
		self.state_slope             =      Game_Code.Player.state_slope.main
		self.logic_spindash	         =	    Game_Code.Player.logic_spindash.main
		self.main                    =      Game_Code.Player.player_main.main
		self.movement                =      Game_Code.Player.player_movement.main
		self.logic_trick             =	    Game_Code.Player.logic_trick.main
		self.movement_core           = 	    Game_Code.Player.player_movement_core.main
		self.flare                   = 	    Game_Code.Player.flare.main
		self.logic_airdash           = 	    Game_Code.Player.logic_airdash.main
		self.logic_col               = 	    Game_Code.Player.logic_col.main
		self.logic_dashbar           = 	    Game_Code.Player.logic_dashbar.main
		self.logic_fallin            = 	    Game_Code.Player.logic_fallin.main
		self.logic_homingattack      = 	    Game_Code.Player.logic_homingattack.main
		self.logic_jump              = 	    Game_Code.Player.logic_jump.main
		self.logic_wall              = 	    Game_Code.Player.logic_wall.main
		self.logic_x_cont            = 	    Game_Code.Player.logic_x_cont.main
		self.init                    =      Game_Code.Player.player_init.main


Player = PlayerClass()


class Game(Gamemananager.GameManager):
	"""
		this class handles the actual game code and not the game engine code.\n
		it inherits the in-engine properties
	"""
	def __init__(self,screen,fm):
     
  
   
   
		self.spawnbiglaser        =   partial(Game_Code.Utils.Entities.spawnbiglaser       ,self = self)
		self.spawnlaser           =   partial(Game_Code.Utils.Entities.spawnlaser          ,self = self)
		self.entity_list_create   =   partial(Game_Code.Utils.Entities.entity_list_create  ,self = self)
		self.oncreate             =   partial(Game_Code.Utils.Entities.oncreate            ,self = self)
		self.cond                 =   partial(Game_Code.Utils.Entities.cond                ,self = self)
		self.qrcond               =   partial(Game_Code.Utils.Entities.qrcond              ,self = self)
  
  
	
         
		self.sp                   =   Game_Code.Utils.Player.sp
		self.gp                   =   Game_Code.Utils.Player.gp
		self.spin                 =   partial(Game_Code.Utils.Player.spin             ,self = self)
       
       
       
		self.valsign              =   Game_Code.Utils.math.valsign
		self.sign                 =   Game_Code.Utils.math.sign
		self.listadd              =   Game_Code.Utils.math.listadd
		self.listdiv              =   Game_Code.Utils.math.listdiv
		self.customunilerp        =   Game_Code.Utils.math.customunilerp
		self.unilerp              =   partial(Game_Code.Utils.math.unilerp             ,self = self)
		self.rotlerp              =   partial(Game_Code.Utils.math.rotlerp             ,self = self)
  

  
  
		
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
		Game_Code.Core.reload.main(self,Player)
     
	def quickrel(self):
		Game_Code.Core.quick_reload.main(self,Player)

	def commence(self):
		Game_Code.Core.Game_start.main(self)

	def update(self):
		Game_Code.Core.Update.main(self,Player)








rm = Game(univars.screencol,fm)
rm.Run()