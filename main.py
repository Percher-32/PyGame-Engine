import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import os
import pygame
import random
import math
import sys

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
import Game_Code.Player.util_gp
import Game_Code.Player.util_sp





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
		self.util_sp 				 = 		Game_Code.Player.util_sp.main
		self.util_gp 				 = 		Game_Code.Player.util_gp.main


Player = PlayerClass()


class Game(Gamemananager.GameManager):
	"""
		this class handles the actual game code and not the game engine code.\n
		it inherits the in-engine properties
	"""
	def __init__(self,screen,fm):
     
  
   
   
		
		super().__init__(screen,fm)
		self.publicvariables["mood"] = "sunset"
		self.attackerbox = {"obj":[]}
		self.typesofhoming = ["enemy-L","omnispring","goal","turret","rocket","easybot","HURT_biglaser","spring"]
		self.ingametime = 0
		self.boardoffset = [0,0]
		self.playeroffset = [0,0]
		self.camzoom = 0.3
		self.objrange = 6000
		self.bailable = 0
		self.skatedetach = 0
		self.publicvariables["gamespeed"] = 1
		self.publicvariables["showater"] = 1
		self.publicvariables["waterh"] = -(64 * 0.4)
		self.lookaheady = 0
		self.timesdone = 1
		self.scores = {}
		self.homingcharge = 0
		self.lookahead = 100
		self.lerpshake = 0
		self.actualwaterheight = 0
  
  
  
		self.sp = Player.util_sp
		self.gp = Player.util_gp
  
  
  
  




	def onreload(self):
     
		self.a = 0

		# bg.addbackground("night")
		# bg.addbackgrounditem("stars","night",[0,-70],layer=0.01,infiniscroll=True,dimensions=[300,300],zdep=-2,surf="stars")
		# bg.addbackgrounditem("moon","night",[200,-60]                ,surf = "moon",dimensions=[200,200],layer = 0.015,infiniscroll=False,zdep=-1)
		# bg.addbackgrounditem("mount1","night",[0, -140]                ,surf = "mount",dimensions=[2500, 1250],layer = 0.05,infiniscroll=True,zdep=0)
		# bg.addbackgrounditem("mount2","night",[0, -20]                ,surf = "mount",dimensions=[2000, 700],layer = 0.1,infiniscroll=True,zdep=1)


		# bg.addbackground("day")
		# bg.addbackgrounditem("sun","day",[200,10]                ,surf = "sun",dimensions=[200,200],layer = 0.015,infiniscroll=False,zdep=-1)
		# bg.addbackgrounditem("mount1","day",[0, -140]                ,surf = "mount",dimensions=[2500, 1250],layer = 0.05,infiniscroll=True,zdep=0)
		# bg.addbackgrounditem("mount2","day",[0, -20]                ,surf = "mount",dimensions=[2000, 700],layer = 0.1,infiniscroll=True,zdep=1)
		# bg.savebg()

		if "game" == self.states:
			# initialise player and all its variables
			Player.init(self,[0,60])


		if "veiw" == self.states:
			um.changestate("test1","but1")
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[-0.5,0],"but1",color=univars.theme["dark"],surf = "testbutton")
			# um.addglide("but1",univars.sizes["mediumbutton"],univars.sizes["largebutton"])
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0],"but2",color=univars.theme["dark"])
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[0.5,0],"but3",color=univars.theme["dark"])
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0.5],"but4",color=univars.theme["dark"])
			# um.savealluielements()


		if self.states == "test":
			om.add(self,(0,0),"player",0,"green",[1,1],self.dim)

		if sm.state == "game":
			om.BAKE()

	def quickrel(self):
		# self.qrcond()
		if "game" == self.states:
			Player.init(self,cm.getcam("def","pos"))
		if "Editor" == self.states:
			om.removeid("enemyzoom")
			cm.setcond("def","pos",cm.getcam("playercam","pos"))
			cm.setcond("def","size",cm.getcam("playercam","size"))




	def commence(self):
	 

		# for i in range(200):

			# om.createlight(i,color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),colorinc=(0,0,0),nits=20,sizeinc=20,size=50,alphadec=2,alpha=30,pos=[i * 64 * 10,0])
		pass

	def update(self):
		# self.print(self.reactions,20)
		bg.background = "test2"
  
		if self.dt == 0 or self.dt > 10:
			self.dt = 1
		# print/
		# print(self.dt * 60)
		# om.speed = 0.8
		# pm.particlespawn("circle",[0,0],[[-5,5],[-5,5]],(0,100,255),[0,0],[0,-1],5,0.001,alpha=300,alphadec=4,divergencepos=[[-1000,1000],[0,0]],ntimes=1)

		# cm.setcond("def","pos",[random.randint(-10000,10000),random.randint(-10000,10000)])


		if "game" == self.states:
			Player.main(self)
			self.publicvariables["showater"] = True
			


			if self.isthere("show-score"):
				um.state = "vic"
				um.addrect([6000,6000],["vic"],[(-0.5 + 0.02) - 0.5,0.8],"atnum",color=(0,0,0),fromstart=0,alpha = 200)
				um.addtext("Victory-lap","",univars.defont,[0,0],univars.theme["accent"],100,"vic")
				um.elements["Victory-lap"]["text"] = self.storedscore + "    " + str(int(self.timers["show-score"]/60) + 1) + "\n\n"  + f"Lowest - time:{self.highest}  on-attempt:{self.highestatt}"

			

		if "veiw" == self.states:
			if um.hover("but1"):
				um.elements["but1"]["color"] = univars.theme["bright"]
			else:
				um.elements["but1"]["color"] = univars.theme["dark"]

			if um.hover("but2"):
				um.elements["but2"]["color"] = univars.theme["bright"]
			else:
				um.elements["but2"]["color"] = univars.theme["dark"]

			if um.hover("but3"):
				um.elements["but3"]["color"] = univars.theme["bright"]
			else:
				um.elements["but3"]["color"] = univars.theme["dark"]

			if um.hover("but4"):
				um.elements["but4"]["color"] = univars.theme["bright"]
			else:
				um.elements["but4"]["color"] = univars.theme["dark"]



		mood = self.publicvariables["mood"]

		# self.publicvariables["waterh"] -= 0.002
		sd.program['time'] = fm.frame
		sd.program['state'] = self.publicvariables["shaderstate"]
		# univars.pixelscale = abs(math.sin(fm.frame/100) * 3) + 1




		if mood == "afternoon":
			bg.background = "day"
			self.publicvariables["screencol"] = (90-30 ,234 ,234 )
			sd.program["illuminace"] = 1
			sd.program["hurt"] = -0.4
			sd.program["sunpos"] = [0,0]
			sd.program["pacify"] = -0.7
			sd.program["night"] = 0

		if mood == "sunset":
			bg.background = "day"
			self.publicvariables["screencol"] = (174, 99, 142)
			sd.program["illuminace"] = 0.34

			sd.program["hurt"] = 3.4
			sd.program["sunpos"] = [0,-1 * self.actualwaterheight/20 + 0.5 ]
			sd.program["pacify"] = -0.2

			sd.program["night"] = 0


		if mood == "daybreak":

			bg.background = "day"
			self.publicvariables["screencol"] = (110 ,189 ,234 )
			sd.program["hurt"] = 0
			sd.program["illuminace"] = 0.5
			sd.program["sunpos"] = [0,0]
			sd.program["pacify"] = 0

			sd.program["night"] = 0

		if mood == "night":
			bg.background = "night"
			self.publicvariables["screencol"] = (20,0,30)
			sd.program["illuminace"] = 0.22
			sd.program["hurt"] = 1
			sd.program["sunpos"] = [0,0]
			sd.program["pacify"] = 0.2
			sd.program["night"] = 1









		self.actualwaterheight =(self.publicvariables["waterh"] - cam.y)/(univars.realscreeen.height / cam.size) * -1 - cam.size

		if self.publicvariables["showater"]:
			sd.program["waterlevel"] = self.actualwaterheight
		else:
			sd.program["waterlevel"] = -1



		sd.program["camx"] = cam.x/(univars.startdims[0] * univars.scaledown)

	def spin(self,angle,time,spindec = 0):
		"""
			rotates the player by (angle) for (time) seconds
		"""
		self.wait(f"rotate",time,barrier=False)
		self.sp("rotdes",spindec)
		self.sp("rot",angle)


	def rotlerp(self,rot,dest,sm,roundto = 2):
		"""
			a ROTATION lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int\n
			FINDS SHORTEST DISTANCE
		"""
		d1 = abs(rot - (dest - 360))
		d2 = abs(rot - (dest + 360))
		d3 = abs(rot - (dest + 0))

		destinations = {d1:dest-360,d2:dest+360,d3:dest}

		dest = destinations[min([d1,d2,d3])]

		rot = self.unilerp(rot,dest,sm,roundto=roundto)
		return rot

	def unilerp(self,val,max,sm,roundto = 2,useigt = True):
		"""
			a lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int
		"""
		if om.speed == 0:
			om.speed = 0.1
		if self.dt == 0:
			self.dt = 1

		if useigt:
			return univars.func.lerp(val,max,              (  (sm/om.speed) / self.dt)*1.5              ,roundto = roundto)
		else:
			return univars.func.lerp(val,max,              (  (sm) / self.dt)*1.5              ,roundto = roundto)

	def customunilerp(self,val,max,sm,gamespeed,deltatime,roundto = 2):
		"""
			a lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int
		"""
		return univars.func.lerp(val,max,              (  (sm/gamespeed) / deltatime)*1.5              ,roundto = roundto)

	def sign(self,value):
		"""
			 returns + or -
		"""
		if abs(value) == value:
			return "+"
		else:
			return "-"

	def valsign(self,value):
		"""
			 returns 1 or -1
		"""
		if abs(value) == value:
			return 1
		else:
			return -1

	def listadd(self,lists:tuple) -> list:
		"""
			lists = tuple of lists to add together
		"""
		# print(lists[0])
		mainlist = [0 for i in lists[0]]
		for lst in lists:
			for index in range(len(lst)):
				mainlist[index] += lst[index]
		return mainlist

	def listdiv(self,list,num):
		"""
			divides a list by single number
		"""
		return [i/num for i in list]

	

	




	def qrcond(self, id, info):

		if info["type"] == "HURT_biglaser":
			om.removeid(id)

		if info["type"] == "spawn-1":
			if not om.get_value(id,"sid") == 0:
				for i in om.get_value(id,"sid"):
					if i in om.objects.keys():
						om.removeid(i)
			om.set_value(id,"spawned",0)


		if info["type"] == "HURT_laser":
			om.removeid(id)

		if info["type"] == "rocket":
			om.objects[id]["pos"] = om.get_value(id,"sp")
			om.objects[id]["rot"] = om.get_value(id,"sr")
			om.set_value(id,"canhome",1)
			om.set_value(id,"timer",om.get_value(id,"maxtimer"))
			om.set_value(id,"timeon",0)
			om.set_value(id,"active",0)
			om.set_value(id,"exp",0)
			om.objects[id]["rendercond"] = 1

		if info["type"] == "bird":
			om.removeid(id)




		if info["type"] == "easybot":
			om.set_value(id,"HP",100)

			om.set_value(id,"canhome",1)
			om.objects[id]["rendercond"] = 1


			om.objects[id]["pos"] = om.get_value(id,"sp")

		if info["type"] == "cluster":
			birbs = []
			for i in range(om.get_value(id,"num")):
				bid = om.add(self,[info["pos"][0] + random.randint(-200,200),info["pos"][1]],"bird",0,"bird",[1.2,1.2],univars.grandim,keepprev=1,info={"master":id})
				birbs.append(bid)

			om.set_value(id,"birds",birbs)

	def parse_init(self,sr:str,id,info):
		sr = sr.replace('"<id>"',f"'{id}'")
		sr = sr.replace('"<info>"',str(info))
		sr = sr.replace('"<self>"',"self")
		return sr

	def parse_main(self,sr:str,id,info,st):
		sr = sr.replace('"<id>"',f"'{id}'")
		sr = sr.replace('"<info>"',str(info))
		sr = sr.replace('"<st>"',str(st))
		sr = sr.replace('"<self>"',"self")
		return sr

	def entity_list_create(self):
		
		self.entity_type = os.listdir("Game_Code/Entities")
		self.entity_type = [entity for entity in self.entity_type if not ".py" in entity]

  
		self.entity_codes = {}
		for entity in self.entity_type:
			init_code = None
			main_code = None
			with open(f"Game_Code/Entities/{entity}/init.py","r") as init:
				init_code = init.read()
			with open(f"Game_Code/Entities/{entity}/main.py","r") as main:
				main_code = main.read()
    
			init_code = init_code.replace('self = "<REMOVE>"'," ")
			init_code = init_code.replace('id = "<REMOVE>"'," ")
			init_code = init_code.replace('info = "<REMOVE>"'," ")
   
	
			main_code = main_code.replace('self = "<REMOVE>"'," ")
			main_code = main_code.replace('id = "<REMOVE>"'," ")
			main_code = main_code.replace('info = "<REMOVE>"'," ")
			main_code = main_code.replace('st = "<REMOVE>"'," ")


			self.entity_codes[entity] = {"init":   compile(init_code,f"Game_Code/Entities/{entity}/init.py","exec"),"main":     compile(main_code,f"Game_Code/Entities/{entity}/main.py","exec")}

   
			if 'FLAG = "<PASS>"' in init_code.strip():
				self.entity_codes[entity]["init"] = "<PASS>"
			if 'FLAG = "<PASS>"' in main_code.strip():
				self.entity_codes[entity]["main"] = "<PASS>"




	def oncreate(self,id,info):

		if not hasattr(self,"entity_type"):
			self.entity_list_create()
   
		if info["type"] in self.entity_type:
			code = self.entity_codes[info["type"]]["init"]
			if not code == "<PASS>":
				exec(code,{"self":self,"id":id,"info":info})

	def cond(self,id,info,st):
		"""id -> the id   info -> the info for the id"""
			
		if info["type"] in self.entity_type:
			code = self.entity_codes[info["type"]]["main"]
			if not code == "<PASS>":
				exec(code,{"self":self,"id":id,"info":info,"st":st})




	def spawnlaser(self,pos,speed,dir,enid,time,extraspeed=[0,0]):
		id = om.add(self,pos,"laser",dir,"HURT_laser",[1,1],univars.grandim,keepprev=1)
		om.objects[id]["type"] = "HURT_laser"
		movec = pygame.Vector2()
		movec.from_polar((speed,dir))
		movec +=  pygame.Vector2(extraspeed[0],extraspeed[1])
		om.set_value(id,"movec",movec)
		om.set_value(id,"speed",speed)
		om.set_value(id,"damage",5)
		om.set_value(id,"enid",enid)
		om.set_value(id,"extraspeed",extraspeed)
		om.set_value(id,"time",time)
		om.lighttoenemy(id,"l1",color=(255,0,20),colorinc=(0,0,0),nits=10,sizeinc=3,size=6,alphadec=6,alpha=60)


	def spawnbiglaser(self,pos,time,speed,topspeed):
		id = om.add(self,pos,"rocket",0,"HURT_biglaser",[1.2,1.2],univars.grandim,keepprev=1)
		om.objects[id]["type"] = "HURT_biglaser"
		om.set_value(id,"tr",random.randint(30,60)/10)

		om.set_value(id,"maxtimer",time)
		om.set_value(id,"time",time)
		om.set_value(id,"canhome",1)
		om.set_value(id,"speed",speed + random.randint(-20,20))
		om.set_value(id,"topspeed",topspeed + random.randint(-20,0))
		om.set_value(id,"rot",0)
		om.lighttoenemy(id,"l1",color=(255,0,20),colorinc=(0,0,0),nits=10,sizeinc=3,size=6,alphadec=6,alpha=20)


	def createhpbar(self,id,size,offset):
		"""
			offset has y up = +\n
			Y axis FIXED
		"""
		hpid = om.add(self,(0,0),"laser",0,"HPBAR",[size,size],univars.grandim,keepprev=1,layer=5)
		om.objects[hpid]["type"] = "HPBAR"
		om.objects[hpid]["rendercond"] = 0

		om.set_value(hpid,"obj-id",id)
		om.set_value(hpid,"size",size)
		om.set_value(hpid,"offset",offset)










	def damageable(self,id,dm,range = 200,functhrow = None,func = None):
		if self.flowstate:
			dm *= 2
		if len(self.attackerbox.keys()) > 0:
			if len(self.attackerbox["obj"]) > 0:
				if id in [i.name for i in self.attackerbox["obj"]]:
					if self.isthere("attack"):
						if not self.isthere("damf" + id):
							om.set_value(id,"HP",om.get_value(id,"HP") - dm)
							self.wait("damf" + id,1)
							om.set_value("player","dashmeter",om.get_value(id,"dashmeter") + 50)
							om.set_value(id,"flashtimer",1)
							if not func == None:
								func()

		if self.isthere("skatego"):
			rad = 700
			if self.flowstate:
				rad *= 2
			if univars.func.dist(om.objects[id]["pos"],om.objects["skateboard"]["pos"]) < rad :

				if not self.isthere("damfthrow" + id):
					om.set_value(id,"flashtimer",1)
					self.wait("damfthrow" + id,1)
					om.set_value(id,"HP",om.get_value(id,"HP") - (dm*2))
					om.set_value("player","dashmeter",om.get_value(id,"dashmeter") + 100)

					if not functhrow == None:
						functhrow()


					cm.setcond("playercam","shake",20)







rm = Game(univars.screencol,fm)

if univars.profile == 1:
	def main():
		rm = Game(univars.screencol,fm)
		if univars.safemode:
			try:
				rm.Run()
			except Exception as error:
				print(error)
				pygame.quit()
		else:
			rm.Run()
	if __name__ == "__main__":
		cProfile.run('main()', sort='cumtime')
else:
	if univars.safemode:
		try:
			rm.Run()
		except Exception as error:
			print(error)
			pygame.quit()
	else:
		rm.Run()