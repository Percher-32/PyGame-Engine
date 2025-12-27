import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
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
		self.attackerbox = {"obj":[]}
		self.typesofhoming = ["enemy-L","omnispring","goal","turret","rocket","easybot","HURT:biglaser","spring"]
		self.ingametime = 0
		self.boardoffset = [0,0]
		self.playeroffset = [0,0]
		self.camzoom = 0.3
		self.objrange = 6000
		self.bailable = 0
		self.skatedetach = 0
		self.publicvariables["gamespeed"] = 1
		self.publicvariables["mood"] = "sunset"
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
		self.print(f"SPIN MESSAGE SENT   : TIME = {time}")
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

	

	




	# def qrcond(self, id, info):
 
	# 	om.set_value(id,"spawned",0)

	def qrcond(self, id, info):

		if info["type"] == "HURT:biglaser":
			om.removeid(id)

		if info["type"] == "spawn-1":
			if not om.get_value(id,"sid") == 0:
				for i in om.get_value(id,"sid"):
					if i in om.objects.keys():
						om.removeid(i)
			om.set_value(id,"spawned",0)


		if info["type"] == "HURT:laser":
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



	def oncreate(self,id,info):


		if info["name"] == "target":
			om.objects[id]["type"] = "omnispring"
			info["type"] = "omnispring"
			# om.set_value(id,"vel",[0,0])
			# om.set_value(id,"tarvel",[0,0])
			# om.set_value(id,"clipspeed",5)

		if info["name"] == "enemy":
			om.objects[id]["type"] = "enemy-L"
			info["type"] = "enemy-L"

		if info["type"] == "enemy-L":
			# om.objects["sizen"] = 0.5
			# om.rescale(id,sizen=[0.5,0.5])
			om.objects[id]["sizen"] = [0.8,0.8]

			om.set_value(id,"master_pos",info["pos"])
			om.set_value(id,"canhome",1)
			om.set_value(id,"state","idle")
			om.set_value(id,"HP",100)
			om.set_value(id,"des_vel",[0,0])
			om.set_value(id,"act_vel",[0,0])
			om.set_value(id,"rotspeed",random.randint(30,60))
			pl0 = random.randint(15,40)
			om.set_value(id,"pl0",pl0)
			om.set_value(id,"side",random.randint(0,1))
			om.set_value(id,"pl1",pl0 + random.randint(40,80) )
			om.set_value(id,"level",0 )
			om.set_value(id,"speed",random.randint(2,10))
			om.set_value(id,"superspeed",random.randint(5,5))
			om.set_value(id,"yfac",random.randint(-100,0))
			om.set_value(id,"spacing",random.randint(200,200))
			om.set_value(id,"orbitrot",0)
			om.set_value(id,"lasttogoto",info["pos"])
			om.set_value(id,"act_vel",[0,0])
			om.set_value(id,"vel",[0,0])
			om.set_value(id,"tarvel",[0,0])
			om.set_value(id,"clipspeed",5)
			om.set_value(id,"timer",5)
			om.set_value(id,"maxtimer",random.randint(10 * 2,15 * 2))
			om.set_value(id,"flashtimer",0)


			if self.publicvariables["mood"] == "night":
				om.lighttoenemy(id,"l1",color=(255,0,255),colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=20)
			elif self.publicvariables["mood"] == "sunset":
				om.lighttoenemy(id,"l1",color=(255,0,255),colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=10)


			self.createhpbar(id,1,[0,30])

		if info["type"] == "omnispring":
			om.set_value(id,"canhome",1)

		if info["type"] == "goal":
			om.set_value(id,"canhome",1)
			om.translate(self,id,[0,20],0)
			om.objects[id]["sizen"] = [1.4,1.4]

		if info["type"] == "spawn-1":
			om.objects[id]["type"]  = "spawn-1"
			om.set_value(id,"spawned",0)
			om.set_value(id,"sid",[])
			if om.get_value(id,"ir") == 0:
				om.set_value(id,"ir",500)
			if om.get_value(id,"mp") == 0:
				om.set_value(id,"mp",5)

		if info["type"] == "turret":
			om.objects[id]["type"]  = "turret"
			om.set_value(id,"shotimer",0)
			om.set_value(id,"maxtimer",2)
			om.objects[id]["sizen"] = [2,2]

		if info["type"] == "camz":
			om.objects[id]["layer"] = 0
			om.objects[id]["alpha"] = 100

		if info["type"] == "rocket":

			om.objects[id]["sizen"] = [2,2]

			if not id in om.values.keys():
				om.set_value(id,"vel",1)
				om.set_value(id,"accel",1)
				om.set_value(id,"top",40)

				om.set_value(id,"rad",-0.2)
				om.set_value(id,"maxtimer",20)



			om.set_value(id,"canhome",1)
			om.set_value(id,"timer",om.get_value(id,"maxtimer"))
			om.set_value(id,"timeon",0)
			om.set_value(id,"active",0)
			om.set_value(id,"exp",0)
			om.set_value(id,"sp",om.objects[id]["pos"])
			om.set_value(id,"sr",om.objects[id]["rot"])

		if info["type"] == "cluster":


			if not id in om.values.keys():
				om.set_value(id,"num",5)

		if info["type"] == "spring":
			om.set_value(id,"canhome",1)
			om.objects[id]["sizen"] = [2,2]
			if not "power" in om.values[id].keys():
				om.set_value(id,"power",150)


		if info["type"] == "easybot":
			om.set_value(id,"canhome",1)
			if not "frq" in om.values[id].keys():
				om.set_value(id,"frq",100)
				om.set_value(id,"speed",100)
				om.set_value(id,"time",20)
				om.set_value(id,"HP",100)
			if not "am" in om.values[id].keys():
				om.set_value(id,"am",1)
			if not "bs" in om.values[id].keys():
				om.set_value(id,"bs",40)


			om.objects[id]["sizen"] = [2,2]
			self.createhpbar(id,1.7,[0,80])
			om.set_value(id,"sp",om.objects[id]["pos"])
			om.set_value(id,"gotimer",0)
			om.set_value(id,"randpos",om.objects[id]["pos"])

		if info["type"] == "camz":
			om.set_value(id,"COOLGUY",True)
			if not "zoom" == om.values[id].keys():
				om.set_value(id,"zoom",0.2)

		if info["type"] == "bird":
			om.set_value(id,"active",0)
			om.set_value(id,"vel",[0,0])




	def cond(self,id,info,st):
		"""id -> the id   info -> the info for the id"""
		if info["type"] == "enemy-L" and "player" in om.values.keys():
			self.trianglebot(id,info,st)

		if info["type"] == "HURT:laser":
			self.laserbeam(id,info,st)

		if info["type"] == "HURT:biglaser":
			self.biglaserbeam(id,info,st)


		if info["type"] == "HPBAR":
			self.hpbar(id,info)

		if info["type"] == "spawn-1":
			if om.get_value(id,"spawned") < om.get_value(id,"mp"):
				if univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < om.get_value(id,"ir"):
					om.set_value(id,"spawned",om.get_value(id,"spawned") + 1)

					nid = om.add(self,info["pos"],"enemy",0,"enemy-L",[1,1],univars.grandim,keepprev=1,info={"masterange":om.get_value(id,"or")})

					om.set_value(id,"sid",om.get_value(id,"sid") + [nid] )

					om.set_value(nid,"masterange",om.get_value(id,"or"))
					# print("nid",nid)

					# print("nid",nid,om.get_value(nid,"master_pos"))
				# om.objects[id]["type"] = "HURT:laser"

		if info["type"] == "turret":
			self.turret(id,info,st)
			om.set_value(id,"canhome",1)

		if info["type"] == "RAINBOWTRAIL":
			# om.set_value(id,"canhome",1)
			# self.print("Dragt")
			if om.objects[id]["alpha"] < 10:
				om.removeid(id)
			else:
				om.objects[id]["alpha"] -= 5 * st
				# om.lights.pop(id + "[obj-light]"+ "FIREBALL")
				om.lighttoenemy(id,"l1",color=om.get_value(id,"col"),colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=om.objects[id]["alpha"]/10)

		if info["type"] == "rocket":
			self.rocket(id,info,st)

		if info["type"] == "easybot":
			self.easybot(id,info,st)



		if info["type"] == "cluster":
			self.cluster(id,info,st)

		if info["type"] == "bird":
			self.bird(id,info,st)
			# self.print("WERTYUI")


	def bird(self,id,info,st):
		if not om.get_value(id,"master") in om.objects:
			om.remove(id)
		else:
			master = om.get_value(id,"master")

			if om.get_value(master,"col") and not om.get_value(id,"active"):
				om.set_value(id,"active",1)
				om.set_value(id,"vel",[  self.gp("act_vel")[0]/10 + random.randint(-10,10) + 5 ,  random.randint(2,6)  ])
				# om.set_value(id,"vel",[  2 + random.randint(-4,4), 2 +   ])
			if om.get_value(id,"active"):
				om.playanim(self.dt,id,"fly")
				om.objects[id]["pos"][0] += om.get_value(id,"vel")[0] * st
				om.objects[id]["pos"][1] -= om.get_value(id,"vel")[1] * st



	def cluster(self,id,info,st):
		om.objects[id]["rendercond"] = 0
		col = om.collide(id,0,cam,extra=100)
		bo = 0
		if len(col["obj"]) > 2:
			if "player" in [obj.name for obj in col["obj"] if not obj == None]:
				bo = 1
				# self.print(bo)
			else:
				bo = 0
		else:
			bo = 0
		om.set_value(id,"col",bo)

	def rocket(self,id,info,st):
		col = om.collide(id,0,cam,extra=300)
		if not self.gp("target") == None:
			if self.gp("target").name == id:
				om.set_value(id,"active",1)
		if om.get_value(id,"active") and not  om.get_value(id,"exp"):
			self.sp("MISSIILETIME",om.get_value(id,"timer")/om.get_value(id,"maxtimer"))

			cm.setcond("playercam","shake",20)
			om.set_value(id,"timeon",om.get_value(id,"timeon") + (st* om.speed))
			om.set_value(id,"timer",om.get_value(id,"timer") - (st/20* om.speed))
			addon = [(64 * math.sin(om.objects[id]["rot"]/180 * math.pi)) ,
					 (64 * math.cos(om.objects[id]["rot"]/180 * math.pi)) ]

			addon = [-40,-40]
			# self.println(om.objects[id]["rot"],10)
			pm.particlespawnbluprint([om.objects[id]["pos"][0] + addon[0],om.objects[id]["pos"][1] + addon[1] ],"exp2",initvel=[  math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 , math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 ])
			om.objects[id]["rot"] += om.get_value(id,"rad")
			om.set_value(id,"vel",om.get_value(id,"vel") + (om.get_value(id,"accel")) * st)
			if om.get_value(id,"vel") > om.get_value(id,"top"):
				om.set_value(id,"vel",om.get_value(id,"top"))
			om.objects[id]["pos"][0] += math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * st
			om.objects[id]["pos"][1] -= math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * st


			if len(col["inst"]) > 0 and om.get_value(id,"timeon") > 50 or om.get_value(id,"timer") < 0:
				om.set_value(id,"exp",1)
				om.objects[id]["pos"] = om.get_value(id,"sp")
				self.sp("exithm",1)
				om.set_value(id,"canhome",0)

		if om.get_value(id,"exp"):
			if om.objects[id]["rendercond"]:
				pm.particlespawnbluprint([om.objects[id]["pos"][0],om.objects[id]["pos"][1] ],"exp3",initvel=[  math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel")  , math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel")  ])
			om.objects[id]["rendercond"] = 0
			om.set_value(id,"canhome",0)
			# self.qrcond(id,info) #MAGEBE



	# def createnemyl(self,pos)


	def spawnlaser(self,pos,speed,dir,enid,time,extraspeed=[0,0]):
		id = om.add(self,pos,"laser",dir,"HURT:laser",[1,1],univars.grandim,keepprev=1)
		om.objects[id]["type"] = "HURT:laser"
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
		id = om.add(self,pos,"rocket",0,"HURT:biglaser",[1.2,1.2],univars.grandim,keepprev=1)
		om.objects[id]["type"] = "HURT:biglaser"
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

	def hpbar(self,id,info):
		try:
			om.objects[id]["rendercond"] =  om.objects[om.get_value(id,"obj-id")]["rendercond"]
			om.objects[id]["sizen"][0] = abs(om.get_value(om.get_value(id,"obj-id"),"HP")/100 * om.get_value(id,"size"))
			om.objects[id]["pos"] = self.listadd((om.objects[om.get_value(id,"obj-id")]["pos"],[om.get_value(id,"offset")[0],om.get_value(id,"offset")[1] * -1]))
		except:
			om.removeid(id)



	def laserbeam(self,id,info,st):
		if om.get_value(id,"enid") in om.objects.keys():
			om.set_value(id,"time",om.get_value(id,"time") - st/60)
			# speed = om.get_value(id,"speed")

			# movec = pygame.Vector2()
			# movec.from_polar((speed,dir))


			if om.get_value(id,"time") < 0:
				om.removeid(id)
			else:
				movec = om.get_value(id,"movec")

				movecst = [movec.x*st * om.speed,movec.y*st * om.speed]
				om.translate(self,id,movecst,usedt=0)
		else:
			om.removeid(id)



	def biglaserbeam(self,id,info,st):
		rot = om.get_value(id,"rot")
		speed = om.get_value(id,"speed")
		timer = om.get_value(id,"time")
		maxtimer = om.get_value(id,"maxtimer")
		if speed < om.get_value(id,"topspeed"):
			speed += 1*st*om.speed
		timer -= 0.1*st * om.speed
		om.set_value(id,"speed",speed)
		om.set_value(id,"time",timer)



		self.damageable(id,20,range=600)





		playervec = pygame.Vector2(om.objects["player"]["pos"])
		selfpos =  pygame.Vector2(info["pos"])
		vectoplayer = playervec-selfpos
		desrot = vectoplayer.angle * -1
		tr = om.get_value(id,"tr")
		if univars.func.dist(info["pos"],om.objects["player"]["pos"]) < 100:
			tr  = 1
		d1 = desrot
		d2 = desrot - 360
		d3 = desrot + 360

		rank = [abs(d-rot) for d in [d1,d2,d3]]

		first = min(rank)

		desrot = [d1,d2,d3][rank.index(first)]

		rot = self.unilerp(rot,desrot,tr)


		# rot = desrot
		# rot += (20*st)
		om.set_value(id,"rot",rot)

		vel = [ math.cos(rot/180 * math.pi) *  speed, math.sin(rot/180 * math.pi) *  speed  ]


		om.translate(self,id,vel,1)
		om.objects[id]["rot"] = rot




		shake = int((maxtimer - timer)/maxtimer * 20)

		om.objects[id]["pos"][0] += random.randint(-1 * shake,shake)
		om.objects[id]["pos"][1] += random.randint(-1 * shake,shake)
		addon = [(32 * math.sin(om.objects[id]["rot"]/180 * math.pi)) ,
				(32 * math.cos(om.objects[id]["rot"]/180 * math.pi)) ]
		addon = [0,0]
		# pm.particlespawnbluprint([om.objects[id]["pos"][0] + addon[0],om.objects[id]["pos"][1] + addon[1] ],"exp",initvel=[  math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 , math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel") * 0 ])



		if univars.func.dist(info["pos"],om.objects["player"]["pos"]) < 20 or timer < 0 or om.get_value(id,"HP") < 0:
			if univars.func.dist(info["pos"],om.objects["player"]["pos"]) < 20:
				if self.gp("homing") == 0:
					if not self.isthere("inv"):
						self.wait("BAIL",0.5)
			for _ in range(3):
				pm.particlespawnbluprint([om.objects[id]["pos"][0],om.objects[id]["pos"][1] ],"exp2",initvel=[vel[0]/20,vel[1]/20])
			om.removeid(id)






	def trianglebot(self,id,info,st):
		if id in om.values.keys() and "act_vel" in om.values["player"].keys():
			def skated():
				om.set_value(id,"knock",4)
				om.set_value(id,"yeetvel",[self.key["x"] * 20,self.key["y"] * 10])
			def hit():
				om.set_value(id,"knock",3)
				om.set_value(id,"yeetvel",[self.key["x"] * 20,self.key["y"] * 20])
			self.damageable(id,20,functhrow=skated,func=hit)

			# print(om.get_value(id,"master_pos"),om.objects[id]["pos"])
			if univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < 1600:
				if om.objects[id]["pos"][1] > 64 * 10:
					om.objects[id]["pos"][1] = 64 * 10


				om.translate(self,id,[om.get_value(id,"act_vel")[0]*st * om.speed,om.get_value(id,"act_vel")[1]*st * om.speed],usedt=0)

				rotvec = pygame.Vector2()
				om.set_value(id,"orbitrot",om.get_value(id,"orbitrot") + om.get_value(id,"rotspeed")/20)
				rotvec.from_polar((om.get_value(id,"spacing"),om.get_value(id,"orbitrot")))
				# rotvec.y -= om.get_value(id,"spacing")/2
				# rotvec.y *= 0.3
				# rotvec.x *= 1.4
				# rotvec.y = abs(rotvec.y)* -1 * om.get_value(id,"yfac")/100
				# rotvec.y -=  om.get_value(id,"yfac")
				# rotvec = pygame.Vector2((0,0))


				playerpos = om.objects["player"]["pos"]
				togoto=  [ playerpos[0] + (self.gp("act_vel")[0]*om.get_value(id,"superspeed")) + rotvec.x  - (om.get_value(id,"side") * (self.gp("act_vel")[0] + 20) * 3), playerpos[1]  - (self.gp("act_vel")[1]*om.get_value(id,"superspeed")) + rotvec.y   ]
				ltogoto = om.get_value(id,"lasttogoto")
				# togoto[0] /= 2
				# togoto[1] /= 2
				# togoto[0]
				newvel = [ (togoto[0] - info["pos"][0])/5 , (togoto[1] - info["pos"][1])/-5    ]
				# togoto=[0,0]



				om.set_value(id,"des_vel",newvel)


				om.set_value(id,"lasttogoto",togoto)




				if self.isthere("#Throwing" + str(id)):
					if not id + "[obj-light]"+ "FIREBALL" in om.lights :
						om.lighttoenemy(id,"FIREBALL",color=(255,0,100),colorinc=(0,0,0),nits=20,sizeinc=5,size=30,alphadec=3,alpha=50)

					om.set_value(id,"fireball",1)
					om.set_value(id,"canhome",0)
					if not om.get_value(id,"throwvel") == 0:
						# print(self.gp("throwaxis"))
						om.set_value(id,"act_vel",om.get_value(id,"throwvel"))
						om.set_value(id,"HP",om.get_value(id,"HP") - (1*st)/10)
						om.set_value(id,"des_vel",om.get_value(id,"throwvel"))



						om.set_value(id,"throwvel",[om.get_value(id,"throwvel")[0]/1.0000005,om.get_value(id,"throwvel")[1]/1.0000005 - 1])


					col = om.collide(id,0,cam,extrax=500,extray=500)["obj"]
					if not None in col:
						for obj in col:
							om.set_value(obj.name,"flashtimer",2)
							om.set_value(obj.name,"HP",om.get_value(obj.name,"HP") - (1))



				else:
					if id + "[obj-light]"+ "FIREBALL" in om.lights :
						om.lights.pop(id + "[obj-light]"+ "FIREBALL")
					om.set_value(id,"fireball",0)
					om.set_value(id,"canhome",1)
					om.objects[id]["rot"] = 0

					# if len(collide) > 0:
					# 	om.set_value(id,"rotspeed",om.get_value(id,"rotspeed") * -1)


				# om.set_value(id,"HP",abs(math.sin(fm.frame/100) * 100))
				# if len(collide) > 0:
				# 	lt = om.get_value(id,"des_vel")

				# 	lt[0] *= -1
				# 	lt[1] *= -1
				# 	om.set_value(id,"act_vel",lt)
				# 	om.set_value(id,"des_vel",[0,0])
				# 	om.set_value(id,"throwvel",0)


				# om.translate(self,id,[0,20*st],usedt=0)

				if om.get_value(id,"gotoplay") > 0:
					om.set_value(id,"gotoplay",om.get_value(id,"gotoplay") - (1*st)/40)
					# om.set_value(id,"des_vel",[random.randint(-20,20),random.randint(-20,20)])
					om.set_value(id,"act_vel",[3*(om.objects["player"]["pos"][0] + self.gp("act_vel")[0] - info["pos"][0]),
											-3*(om.objects["player"]["pos"][1]  + self.gp("act_vel")[1] -  info["pos"][1])])

					om.set_value(id,"act_vel",[0,
											-0])

					om.set_value(id,"des_vel",[0,
											-0])

				if om.get_value(id,"knock") > 0:
					om.set_value(id,"knock",om.get_value(id,"knock") - (1*st)/40)
					om.set_value(id,"act_vel",  self.listadd((   self.listdiv(om.get_value(id,"yeetvel"),1/st)   ,om.get_value(id,"act_vel")))    )
					om.set_value(id,"des_vel",  self.listadd((   self.listdiv(om.get_value(id,"yeetvel"),1/st)     ,om.get_value(id,"des_vel")))       )
					# if om.get_value(id,"act_vel")[0] + om.get_value(id,"act_vel")[1] < 2:
					# 	om.set_value(id,"act_vel",om.get_value(id,"embedvel"))
					# 	om.set_value(id,"des_vel",om.get_value(id,"embedvel"))
					# 	om.set_value(id,"gotoplay",0)





				om.set_value(id,"act_vel",self.customunilerp(om.get_value(id,"act_vel"),om.get_value(id,"des_vel"),om.get_value(id,"speed"),om.speed,st))

				# a = pygame.math.Vector2( om.get_value(id,"act_vel"))
				# if a.length() > 0 and not self.isthere("#Throwing" + str(id)):
				# 	if om.get_value(id,"pl0") > pygame.math.Vector2( om.get_value(id,"act_vel")).length() < om.get_value(id,"pl1"):
				# 		a = pygame.math.Vector2( om.get_value(id,"act_vel"))
				# 		a.scale_to_length(self.valsign(a.length()) * om.get_value(id,"pl0"))
				# 		om.set_value(id,"act_vel",list(a))
				# 	elif om.get_value(id,"pl1") < pygame.math.Vector2( om.get_value(id,"act_vel")).length():
				# 		a = pygame.math.Vector2( om.get_value(id,"act_vel"))
				# 		a.scale_to_length(self.valsign(a.length()) * om.get_value(id,"pl1"))
				# 		om.set_value(id,"act_vel",list(a))

				if self.isthere("#Throwing" + str(id)):

						om.rotate(self,id,20)
						cm.setcond("playercam","shake",10)
						pm.particlespawnbluprint(self.listadd((om.objects[id]["pos"],(-32,-32))),"exp")

				# if not None in col["obj"]:
				# 	if  True in [ om.get_value(obj.name,"fireball") for obj in col["obj"] ]:
				# 		om.set_value(id,"HP",om.get_value(id,"HP") - (1*st))
				# 		# pm.particlespawnbluprint(self.listadd((om.objects[id]["pos"],(-32,-32))),"exp")
				# 		om.set_value(id,"flashtimer",2)
				# 		om.objects[id]["sn"] = 1


				if om.get_value(id,"flashtimer") > 0:
					om.set_value(id,"flashtimer",om.get_value(id,"flashtimer") - (1*st)/40)
					if round(om.get_value(id,"flashtimer") * 5)%2 == 0:
						om.objects[id]["sn"] = 1
					else:
						om.objects[id]["sn"] = 0
				else:
					om.objects[id]["sn"] = 0








				om.set_value(id,"timer",om.get_value(id,"timer") - (st * self.gp("wantime"))/10)


				playervec = pygame.Vector2(om.objects["player"]["pos"])
				selfpos =  pygame.Vector2(info["pos"])


				vectoplayer = playervec-selfpos

				if  abs(vectoplayer.length()) > 300:
					if om.get_value(id,"timer") < 0 :
						rot = vectoplayer.angle * -1 + random.randint(-1 * abs(int(self.gp("des_vel")[0]/100)),1 * abs(int(self.gp("des_vel")[0]/100)))
						self.spawnlaser(om.objects[id]["pos"],40,rot,id,3,extraspeed=self.listdiv(om.get_value("player","act_vel"),2))
						om.set_value(id,"timer",om.get_value(id,"maxtimer"))









				if om.get_value(id,"HP") <= 0:
					om.removeid(id)
					# if self.gp("target") == id:


			else:
				om.objects[id]["pos"] = om.get_value(id,"master_pos")

	def turret(self,id,info,st):
		om.set_value(id,"shotimer",om.get_value(id,"shotimer") - st/2)
		if om.get_value(id,"shotimer") < 0:
			playervec = pygame.Vector2(om.objects["player"]["pos"])
			selfpos =  pygame.Vector2(info["pos"])
			om.set_value(id,"maxtimer",5)


			vectoplayer = playervec-selfpos

			if  600 > abs(vectoplayer.length()) > 20:
				if om.get_value(id,"shotimer") < 0 :
					rot = vectoplayer.angle * -1 + random.randint(-50,50)
					om.set_value(id,"rot",om.get_value(id,"rot") - (10*st) )
					# om.translate(self,id,[math.sin(fm.frame/100) * 100,0],usedt=0)
					# rot = om.get_value(id,"rot")
					for i in range(1):
						for i in [0,90,180,-90]:
							rot = i + random.randint(0,0) + om.get_value(id,"rot")
							self.spawnlaser(om.objects[id]["pos"],40,rot,id,3,extraspeed=[self.gp("act_vel",0)/10,self.gp("act_vel",1)/10])
					om.set_value(id,"shotimer",om.get_value(id,"maxtimer"))

	def easybot(self,id,info,st):



		if om.get_value(id,"HP") <= 0:
			om.set_value(id,"canhome",0)
			om.objects[id]["rendercond"] = 0

		om.set_value(id,"randpos",[om.get_value(id,"sp")[0]  + math.sin(fm.frame/40) * 20,om.get_value(id,"sp")[1]  + math.cos(fm.frame/40) * 20 ])
		if self.isthere("easybotmove" + id):
			om.set_value(id,"randpos",[om.get_value(id,"randpos")[0] + om.get_value(id,"knock")[0],om.get_value(id,"randpos")[1] + om.get_value(id,"knock")[1]  ])


		if om.get_value(id,"HP") > 0:
			om.set_value(id,"timer",om.get_value(id,"timer") - (st*om.speed))
			if univars.func.dist(info["pos"],om.objects["player"]["pos"]) < 1000:
				if om.get_value(id,"timer") < 0:
					playervec = pygame.Vector2(om.objects["player"]["pos"])
					selfpos =  pygame.Vector2(info["pos"])
					vectoplayer = playervec-selfpos
					rot = vectoplayer.angle * -1
					if self.gp("homing") == 0:
						self.wait("charge" + id,0.5)
					om.set_value(id,"storedrot",rot)
					om.playanim(st,id,"charge",speed=2)
					if self.flowstate:
						om.set_value(id,"timer",om.get_value(id,"frq")/2)
					else:
						om.set_value(id,"timer",om.get_value(id,"frq"))


		om.objects[id]["pos"] = univars.func.lerp(om.objects[id]["pos"],om.get_value(id,"randpos"),10)

		if self.isthere("charge"+ id):
			range = int((45 - self.timers["charge" + id])/10)
			om.objects[id]["pos"][0] += random.randint(range * -1 ,range)
			om.objects[id]["pos"][1] +=  random.randint(range * -1 ,range)
			playervec = pygame.Vector2(om.objects["player"]["pos"])
			selfpos =  pygame.Vector2(info["pos"])
			vectoplayer = playervec-selfpos
			rot = vectoplayer.angle * -1
			om.set_value(id,"storedrot",rot)

		if self.ondone("charge" + id):

			if self.gp("homing") == 0:
				for i in [0]*om.get_value(id,"am"):
					self.spawnbiglaser(info["pos"],om.get_value(id,"time"),om.get_value(id,"bs"),om.get_value(id,"speed"))


		if om.get_value(id,"flashtimer") > 0:
			om.set_value(id,"flashtimer",om.get_value(id,"flashtimer") - (1*st*om.speed)/40)
			if round(om.get_value(id,"flashtimer") * 5)%2 == 0:
				om.objects[id]["sn"] = 5
			else:
				if not self.isthere("charge"+ id):
					om.objects[id]["sn"] = 0
		else:
			if not self.isthere("charge"+ id):
				om.objects[id]["sn"] = 0


		def hit():
			om.set_value(id,"knock",[(self.gp("act_vel",0)/200 + self.key["x"])  * 400  ,  (self.gp("act_vel",1)/200 + self.key["y"])  * -300])
			self.wait("easybotmove" + id,0.5)

		def skatehit():
			om.set_value(id,"knock",[(self.gp("act_vel",0)/200 + self.key["x"])  * 400   * 1.5,  (self.gp("act_vel",1)/200 + self.key["y"])  * -300 * 1.5])
			self.wait("easybotmove" + id,0.5)


		self.damageable(id,100,func = hit,functhrow=skatehit)






	def damageable(self,id,dm,range = 200,functhrow = None,func = None):
		# if univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < range:
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