import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math


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


	
class Game(Gamemananager.GameManager):	
	"""
		this class handles the actual game code and not the game engine code.\n
		it inherits the in-engine properties
	"""
	def __init__(self,screen,fm):
		super().__init__(screen,fm)
		self.typesofhoming = ["enemy-L","omnispring","goal","turret","rocket"]
		self.ingametime = 0
		self.boardoffset = [0,0]
		self.playeroffset = [0,0]
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
			# self.initialiseplayer([0,60])
			self.initialiseplayer([0,60])


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
		if "game" == self.states:
			self.initialiseplayer(cm.getcam("def","pos"))
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
		# print(self.dt * 60)
		self.println(self.actualwaterheight,2)
		# om.speed = 0.8
		# pm.particlespawn("circle",[0,0],[[-5,5],[-5,5]],(0,100,255),[0,0],[0,-1],5,0.001,alpha=300,alphadec=4,divergencepos=[[-1000,1000],[0,0]],ntimes=1)

		# cm.setcond("def","pos",[random.randint(-10000,10000),random.randint(-10000,10000)])


		if "game" == self.states:
			self.playercode()
			self.publicvariables["showater"] = True

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




		




		self.println(cam.size,1)
		self.actualwaterheight =(self.publicvariables["waterh"] - cam.y)/(univars.realscreeen.height / cam.size) * -1 - cam.size

		if self.publicvariables["showater"]:
			sd.program["waterlevel"] = self.actualwaterheight
		else:
			sd.program["waterlevel"] = -1
		

		
		sd.program["camx"] = cam.x/(univars.startdims[0] * univars.scaledown)

	def playercode(self):
		"""
			contins all the code that the player needs to function
		"""
		if "player" in om.objects.keys() and "skateboard" in om.objects.keys() and "playersprite" in om.objects.keys():



			#move player

			if not abs(self.key["x"]) > 0:
				om.playanim(self.dt,"playersprite","idle",forceplay=True)
			elif not abs(self.gp("des_vel")[0]  - self.key["x"] * 150) < 20:
				om.playanim(self.dt,"playersprite","moveidle",forceplay=True)
			else:
				om.playanim(self.dt,"playersprite","fastidle",forceplay=True)


			self.moveplayer()

			if em.controller["options"]:
				self.initialiseplayer([0,60])

			#move camera
			campos = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1]]
				

			
			
			
			campos[0] += self.lookahead
			campos[1] += self.lookaheady




			# if not self.gp("homing") > 0:
			cm.cam_focus_size("playercam",campos,4,0.3 / (univars.scaledown/2.5) * 15/7 )



			
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
				self.println(colb["obj"],6)
				for obj in colb["obj"]:
					
					id = obj.name
					if obj.info["type"] == "enemy-L":
						om.set_value(id,"flashtimer",1)
						om.set_value(id,"HP",om.get_value(id,"HP") - 120)
						om.set_value(id,"knock",4)
						om.set_value(id,"yeetvel",[self.key["x"] * 10,self.key["y"] * 10])
						om.set_value("player","dashmeter",om.get_value(id,"dashmeter") + 100)

						cm.setcond("playercam","shake",20)
			
			
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

	def initialiseplayer(self,pos):
		"""
		Initialises the players variables
		"""
		#create the cameras
		startpos = pos
		cm.addcam("playercam",startpos,univars.pixelscale/7 * 0.4)
		cm.setcam("playercam")  

		om.speed = 1


		#create player
		self.prevtricks = []
		
		om.adds(self,"player",startpos,"player","player",0,[1,1],400,5)
		self.sp("#DEBUG","HELLO WOLRD")
		om.objects["player"]["rendercond"] = False

		self.sp("dashmeter",0)
		
		self.sp("dashcooldown",0)
		self.sp("deshrem",0)
		sc = 1.4
		#creates the player sprite you actually see
		om.adds(self,"playersprite",[-1400,400],"player","player",0,[sc,sc],400,5)
		om.objects["playersprite"]["rendercond"] = True
		om.includeflipping("playersprite")

		#creates the skateboard
		om.adds(self,"skateboard",[-1400,400],"skateboard","skateboard",0,[sc,sc],400,5)
		om.objects["skateboard"]["rendercond"] = True

		#desired velocity


		self.sp("lastframewall",0)


		self.sp("slinging",0)

		self.lastrail = 0

		self.sp("des_vel",[0,0])

		self.sp("candj",0)

		self.dropdashinit = 0
		self.lastground = 0

		
		self.sp("exithm",0)

		#actual velocity
		self.sp("act_vel",[0,0])

		#smoothing
		self.sp("smoothing",2)

		self.sp("prevprevpos",om.objects["player"]["pos"])

		#modes
		self.sp("mode","grounded")

		#able to jump?
		self.sp("jumpamble",False)

		#fall speed smoothing
		self.sp("fss",8)

		self.lastframeslanted = False
		self.gate = "r"

		self.lastdirrail = 0
		self.sp("lastframeswing",0)


		self.lastdir = "r"

		self.lastdirslant = "r"

		#previous frames actual velocity
		self.sp("prev_act_vel",[0,0])

		#shidding?
		self.sp("skidding",False)

		self.reclock = 1

		self.sp("rot",0)


		#on skateboard?
		self.sp("onboard",True)

		self.sp("unboundrot",0)

		self.sp("rotoffset",0)
		self.sp("rotdes",0)

		self.sp("desrot",0)
		self.sp("desmooth",5)

		self.sp("machspeed",150)

		self.sp("lastwall","l")


		self.sp("slantdir","r")

		om.set_value("skateboard","fallvalue",5)

		self.sp("thickness",1)




		self.sp("homing",0)
		self.sp("target",None)

		self.joyaxis = pygame.math.Vector2(self.key["x"],self.key["y"])
		if self.joyaxis.length()> 0:
			self.joyaxis.normalize()
		else:
			self.joyaxis = pygame.math.Vector2(-1,0)




		#In_game_UI
		om.adds(self,"enemyzoom",[0,0],"enemyzoom","In_Game_UI",0,[1.6,1.6],255,5)
		om.objects["enemyzoom"]["rendercond"] = 0





		#UI
		um.changestate("maingame",None)
		um.addrect([6000,100 + 30 - 30],["maingame"],[(-0.5 + 0.02) - 0.5,0.8],"dashbarback",color=(0,0,0),fromstart=0,alpha = 200)
		um.addrect([(1000 -19)/2 + 20,100 + 30 - 30],["maingame"],[(-0.5 + 0.02) - 0.5,0.8],"dashbarback",color=(0,0,0),fromstart=1,alpha = 200)
		um.addrect([1000 - 30 - 20,90 - 30],["maingame"],[(-0.5 + 0.04/2 + 0.02) - 0.5,0.8],"dashbar",color=(225,100,100),fromstart=1,alpha = 200)



		um.addrect([1000 - 30 - 20 + 30,90 - 30 + 30],["maingame"],[(-0.5 + 0.04/2 + 0.02) - 0.5 -0.02,-0.8],"missiletimeback",color=(0,0,0),fromstart=1,alpha = 200)
		um.addrect([1000 - 30 - 20,90 - 30],["maingame"],[(-0.5 + 0.04/2 + 0.02) - 0.5,-0.8],"missiletime",color=(225,0,0),fromstart=1,alpha = 200)

		um.addtext("Speed-timer","0",univars.defont,[0,0.8],univars.theme["accent"],60,["maingame"])
		um.elements["Speed-timer"]["text"]  = str(0)

		um.addtext("attemps","0",univars.defont,[0.5,0.8],univars.theme["accent"],60,["maingame"])
		um.elements["attemps"]["text"]  = str(0)


	def moveplayer(self):
		um.elements["Speed-timer"]["text"]  = str(round(float(um.elements["Speed-timer"]["text"]) + (self.dt/60 *self.publicvariables["gamespeed"] ),2))
		um.elements["attemps"]["text"]  = str(self.timesdone)
		
		self.sp("wantime",self.publicvariables["gamespeed"])
		self.sp("dashmeter",min([300,self.gp("dashmeter")]))
		self.sp("dashmeter",max([0,self.gp("dashmeter")]))




		um.elements["dashbar"]["dimensions"][0] = self.unilerp( um.elements["dashbar"]["dimensions"][0] ,   max([((self.gp("dashmeter") * 10) - 50)/2,0])/3 ,4  )

		if self.gp("homing"):
			if self.gp("target").info["type"] == "rocket":
				um.elements["missiletime"]["dimensions"][0] = 950 * self.gp("MISSIILETIME")
				um.elements["missiletimeback"]["dimensions"][0] = 950
			else:
				um.elements["missiletime"]["dimensions"][0] = 0
				um.elements["missiletimeback"]["dimensions"][0] = 0
		else:
			um.elements["missiletime"]["dimensions"][0] = 0
			um.elements["missiletimeback"]["dimensions"][0] = 0

		if self.gp("dashmeter") <= 0:
			um.elements["dashbar"]["dimensions"][0] = 0
		um.elements["dashbar"]["color"] = (0,100,255)
		collision = om.collide9("player",0,cam,self.dim,ignore= ["playersprite","skateboard"])
		lonepoint1 = om.collidep([om.objects["player"]["pos"][0] + 60,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
		lonepoint2 = om.collidep([om.objects["player"]["pos"][0] - 50,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
		collisionbox = om.collide("player",0,cam,extra=20)
		bigcollisionbox = om.collide("player",0,cam,extra=600)
		attackbox = om.colliderect([cm.getcam("playercam","pos")[0] +(self.lookahead*0),cm.getcam("playercam","pos")[1] + (self.lookaheady*0)],[1300,700],0,cam)

		ground1 = len(collision["botmid"]["inst"]) > 0
		ground2 = len(collision["botleft"]["inst"]) > 0    and not (len(collision["topleft"]["inst"])  > 0  ) and not (len(collision["midleft"]["inst"])  > 0  )
		ground3 = len(collision["botright"]["inst"]) > 0   and not (len(collision["topright"]["inst"]) > 0  ) and not (len(collision["midright"]["inst"]) > 0  )
		ground = ground1 or ground2 or ground3
		instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"]
		collisionlisttype = [i.type for i in instlist]
		collisionboxtype = [i.type for i in collisionbox["inst"]] 

		
		if "HURT:laser" in [ i.info["type"] for i in collisionbox["obj"]]:
			if not self.isthere("dashrem") and not self.isthere("inv"):
				self.wait("BAIL",2)
			

		#TRAIL
		if self.gp("dashmeter") > 200:
			self.wait("dotrail",0.2)
			if self.ondone("dotrail"):
				colid = random.randint(6,11)
				if colid == 6:
					col = (255, 79, 0)
				elif colid == 7:
					col = (255, 225, 0)
				elif colid == 8:
					col = (26, 255, 0)
				elif colid == 9:
					col = (0, 255, 255)
				elif colid == 10:
					col = (0, 8, 255)
				elif colid == 11:
					col = (255, 0, 203)

				
				ltid = om.add(self,om.objects["player"]["pos"],"player",om.objects["playersprite"]["rot"],"RAINBOWTRAIL",[1.1,1.1],self.dim,layer=0,sn = colid ,keepprev=1,info={"col":col})

				

				


				om.lighttoenemy(ltid,"l1",color=col,colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=30)

		

		rail = False
		if len(collisionboxtype) > 0:
			rail = collisionboxtype[0] == "rail"
		
		if not rail:
			self.sp("dashmeter",self.gp("dashmeter") + (abs(self.gp("des_vel",0))/150 * self.dt))
		else:
			self.sp("dashmeter",self.gp("dashmeter") + (abs(self.gp("des_vel",0))/150 * self.dt))

		if abs(self.key["x"]) > 0:
			if self.key["x"] > 0:
				self.lastdirslant = "l"
			else:
				self.lastdirslant = "r"
	
		if self.dt == 0 or self.dt > 10:
			self.dt = 1

		if len(collisionboxtype) > 0:
			if "slantl"  in collisionboxtype or "slantr" in collisionboxtype:
				slanted = True
				if "slantr" in collisionboxtype:
					if self.lastdirslant == "r":
						if len(lonepoint2["inst"]) > 0:
							slanted = False
							om.objects["player"]["pos"] = [lonepoint2["inst"][0].realpos[0] + univars.grandim,lonepoint2["inst"][0].realpos[1] - 32]
				else:
					if self.lastdirslant == "l":
						if len(lonepoint1["inst"]) > 0:
							slanted = False
							om.objects["player"]["pos"] = [lonepoint2["inst"][0].realpos[0] + univars.grandim,lonepoint2["inst"][0].realpos[1] - 32]

				
			else:
				slanted = False	
		else: 
			slanted = False


		#Board projectile INITIATE THROW
		if not ground:
			if self.key["attack"] and not self.key["trick"]:
				self.sp("wantime",0.2)
			else:
				if self.lastkey["attack"] and not self.lastkey["trick"]:
					self.wait("skatego",0.5,barrier=1)
					self.spin(30,0.1)
					
					# self.bailable = 1
					if not self.key["tert"]:
						self.skatevel = [
											(self.key["x"] * 1000 )  + om.objects["player"]["pos"][0],
											(self.key["y"] * -500 )  + om.objects["player"]["pos"][1]
										]	
					else:
						self.skatevel = [
											(self.key["x"] * -1000 )  + om.objects["player"]["pos"][0],
											(self.key["y"] * 500 )  + om.objects["player"]["pos"][1]
										]	
					
					
		if self.key["x"] > 0:
			self.lastdir = "r"
		if self.key["x"] < 0:
			self.lastdir = "l"

		axis = [self.key["x"],self.key["y"] * 1]
		vecaxis = pygame.math.Vector2(axis[0],axis[1])
		if vecaxis.length()> 0:
			vecaxis.normalize()
			vecaxis.scale_to_length(1.2)
		axis = [vecaxis.x,vecaxis.y]
		axis[1] = round(axis[1],2)

		
		vec = None
		#HOMING ATTACK SELECT
		if len(attackbox["obj"]):
			om.objects["enemyzoom"]["rendercond"] = 1
			if pygame.math.Vector2(self.key["x"],self.key["y"] ).length() > 0:
				self.joyaxis = pygame.math.Vector2(-1 *self.key["x"],1 *self.key["y"] )
				self.joyaxis.normalize()
			enaxis = self.joyaxis
			vec = None
			closeness = None
			playervec = pygame.math.Vector2(om.objects["player"]["pos"])
			for obj in attackbox["obj"]:	
				if not obj == None:
					emvec = pygame.math.Vector2(obj.info["pos"])
					distvec = playervec - emvec
					if distvec.length() > 0:
						distvec.normalize()
						if obj.info["type"] in self.typesofhoming and om.get_value(obj.name,"canhome"):
							if vec == None:
								vec = obj
								closeness = 1 - distvec.dot(enaxis) 
							else:
								if 1-distvec.dot(enaxis) < closeness:
									vec = obj
									closeness = 1 - distvec.dot(enaxis) 
			if vec == None:
				om.objects["enemyzoom"]["rendercond"] = 0
			else:
				om.objects["enemyzoom"]["pos"] = vec.info["pos"]
				om.objects["enemyzoom"]["sizen"] = self.listadd((vec.info["sizen"],[0.5,0.5]))





			

		

			if self.gp("homing") == 2:
				vec = self.gp("target")



		else:
			om.objects["enemyzoom"]["rendercond"] = 0



		if ground and not rail:
			# self.sp("dashmeter",self.gp("dashmeter") - min([((40/(self.gp("dashmeter") + 2))*self.dt),2*self.dt]) - (0.5*self.dt))
			self.sp("dashmeter",self.gp("dashmeter") - (1.5 * self.dt * self.gp("dashmeter")/100  ))
		else:
			# self.sp("dashmeter",self.gp("dashmeter") - min([((50/(self.gp("dashmeter") + 2))*self.dt),2*self.dt])  - (0.5*self.dt))
			self.sp("dashmeter",self.gp("dashmeter") - (1.1 * self.dt * self.gp("dashmeter")/100  ))



		if len(collisionbox["inst"] ) >0:
			if self.isthere("VULNERABLE"):
				self.bailable = 1
				self.prevtricks = []
				self.deltimer("VULNERABLE")

		#MAIN
		
		if not slanted:
			if slanted == self.lastframeslanted or self.key["jump"]:
				#MAIN
				
				if not rail:
					if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ):
						#IN HERE IS EITHER [NO MIDMID] OR [Yes MIDMID AND GROUND]
						if self.key["trick"] and not len(collisionbox["inst"] ) >0:
							times = 0.7
							self.wait("inv",times)
							if not self.isthere("tcd"):
								if self.key["throw"] and not self.lastkey["throw"]:
									self.prevtricks.append(1)
									self.wait("tcd",0.2)
									self.wait("VULNERABLE",times,barrier=False)
									self.wait("trick1",times,barrier=False)
									self.spin(12,times,0.1)
									if self.prevtricks[-1] == 1:
										self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
									else:
										self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))
								elif self.key["secondary"] and not self.lastkey["secondary"]:
									self.prevtricks.append(2)
									self.wait("tcd",0.2)
									self.wait("VULNERABLE",times,barrier=False)
									self.wait("trick2",times,barrier=False)
									self.sp("dashmeter",self.gp("dashmeter") + 20)
									if self.prevtricks[-1] == 2:
										self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
									else:
										self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))
								elif self.key["attack"] and not self.lastkey["attack"]:
									self.prevtricks.append(3)
									self.wait("tcd",0.2)
									self.wait("VULNERABLE",times,barrier=False)
									self.wait("trick3",times,barrier=False)
									self.sp("dashmeter",self.gp("dashmeter") + 20)
									if self.prevtricks[-1] == 3:
										self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
									else:
										self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))


						if self.isthere("BAIL"):

							self.key["x"] = 0
							self.key["y"] = 0
							self.key["jump"] = 0
							if self.gp("leftwall") or self.gp("rightwall"):
								self.key["jump"] = 1
						if self.ondone("BAIL"):
							self.key["jump"] = 1
							self.sp("act_vel",100,1)
							self.sp("des_vel",100,1)
							

						self.sp("dashmeter",max([self.gp("dashmeter"),0])) 

						
						
						self.sp("dashmeter",max([self.gp("dashmeter"),0])) 


						# if self.key["attack"] and not self.lastkey["attack"]:
						# 	for i in range(int(self.gp("dashmeter"))):
						# 		pm.particlespawnbluprint(om.objects["player"]["pos"],"star")
						


						if self.lastrail:
							# self.spin(21,0.4,0.1)
							pass




						#TRICKS
						


						if abs(self.gp("des_vel",0)) > 250:
							self.sp("des_vel",250 * self.valsign(self.gp("des_vel",0)),0)
						if abs(self.gp("act_vel",0)) > 250:
							self.sp("act_vel",250 * self.valsign(self.gp("act_vel",0)),0)

						self.println(self.gp("act_vel"),17)
						self.println(self.gp("des_vel"),18)

						#x dir movement
						if abs(self.key["x"]) > 0:
							if self.isthere("leftjump"):
								self.key["x"] = 1
							if self.isthere("rightjump"):
								self.key["x"] = -1 * 1

							if self.gp("xinit"):
								self.sp("xinit",False)
								self.sp("des_vel",[self.key["x"] * 120,self.gp("des_vel")[1]])
								self.sp("act_vel",[self.key["x"] * 20,self.gp("act_vel")[1]])
							
							
							if ground:
								if self.key["throw"] and self.dropdashinit == 0:
									# self.sp("act_vel",self.gp("des_vel"))
									self.sp("des_vel",[        self.key["x"] * self.gp("machspeed")/10            ,    self.gp("des_vel")[1]   ])
								else:
									if abs(self.gp("des_vel",0)) < self.gp("machspeed"):
										self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * self.gp("machspeed"),30 )              ,    self.gp("des_vel")[1]   ])
									else:
										# self.print("WOO")
										pass
							else:
								if abs(self.gp("des_vel",0)) < self.gp("machspeed"):
									self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * self.gp("machspeed"),30 )              ,    self.gp("des_vel")[1]   ])
								else:
									# self.print("WOO")
									pass
						else:
							self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
							self.sp("xinit",True)



						self.sp("machspeed",150)



						#SPIN/DROP DASH
						self.println(self.dropdashinit,16)
						self.println(self.homingcharge,15)
						if ((not self.key["throw"] and self.lastkey["throw"] and ground) or (ground and self.dropdashinit==1)) and not self.dropdashinit==2:
								self.wait("dashrem",0.5)
								self.print("BOOOM")
								self.wait("spindash",1)
								# cm.setcond("playercam","shake",10)
								
								if self.dropdashinit:
									self.dropdashinit = 2
								else:
									
									self.dropdashinit = 0

								if self.lastdir == "r":
									self.sp("des_vel",self.homingcharge,0)
									self.sp("act_vel",self.homingcharge,0)
									self.sp("dashav",[self.homingcharge*1/2,0])
									self.sp("dashdv",[self.homingcharge*1/2,0])
								else:
									self.sp("des_vel",self.homingcharge * -1,0)
									self.sp("act_vel",self.homingcharge * -1,0)
									
									self.sp("dashav",[self.homingcharge*-1/2,0])
									self.sp("dashdv",[self.homingcharge*-1/2,0])

								
								pm.particlespawnbluprint(om.objects["player"]["pos"],"exp4",initvel=[self.gp("des_vel",0)/10,10])
								self.homingcharge = 0

						if (not ground or not self.key["throw"]) and self.dropdashinit == 2:
							self.dropdashinit = 0

						#BUILD-UP DASH
						if self.key["throw"] and not self.dropdashinit == 2:
							
							if ground:
								cm.setcond("playercam","shake",3)
							else:
								
								cm.setcond("playercam","shake",2)

							self.homingcharge += 10 * self.dt * om.speed
							if self.homingcharge > 260:
								self.homingcharge = 260


						if not self.key["throw"]:
							self.homingcharge = 0
						

						if self.key["throw"] and not self.lastkey["throw"] and not ground:
							self.dropdashinit = 1

						

						#Wall clinging
						if not collision["midmid"]["inst"]:
							if len(collision["midleft"]["inst"]) > 0 :
								if collision["midleft"]["inst"][0].type == "ground":
									self.sp("leftwall",True)
									self.sp("lastwall","l")
									self.sp("jumpable",True)	
									om.objects["player"]["pos"][0] = collision["midleft"]["inst"][0].realpos[0] + 32

									if not collision["botmid"]["inst"]:
										self.sp("des_vel",[0,self.gp("des_vel")[1]])
										self.sp("act_vel",[0,self.gp("act_vel")[1]])
									else:
										if self.gp("des_vel")[0] < 0:
											self.sp("des_vel",[0,0])
										if self.gp("act_vel")[0] < 0:
											self.sp("act_vel",[0,0])

								else:
									self.sp("leftwall",False)
							else:
								self.sp("leftwall",False)


							if len(collision["midright"]["inst"]) > 0 :
								if  collision["midright"]["inst"][0].type == "ground":
									self.sp("rightwall",True)
									self.sp("lastwall","r")
									self.sp("jumpable",True)	
									om.objects["player"]["pos"][0] = collision["midright"]["inst"][0].realpos[0] -32
									if not collision["botmid"]["inst"]:
										self.sp("des_vel",[0,self.gp("des_vel")[1]])
										self.sp("act_vel",[0,self.gp("act_vel")[1]])
									else:
										if self.gp("des_vel")[0] > 0:
											self.sp("des_vel",[0,0])
										if self.gp("act_vel")[0] > 0:
											self.sp("act_vel",[0,0])

								else:
									self.sp("rightwall",False)
							else:
								self.sp("rightwall",False)


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


							

						#Skid detection 
						if abs(self.gp("act_vel")[0]  - self.gp("des_vel")[0]) > 50:
							self.sp("skidding",True)
						else:
							self.sp("skidding",False)


						#rerout detection
						if not self.isthere("leftjump") or not self.isthere("rightjump"):
							if not self.sign(self.key["x"]) == self.sign(self.gp("lastx")):
								self.sp("xinit",True)
								if ground and abs(self.gp("act_vel")[0]) > 100:
									self.wait("skid",0.3)
									# self.print("shid")
							self.sp("lastx",self.key["x"])


						if self.isthere("skid"):
							if ground:
								pm.particlespawnbluprint(om.objects["player"]["pos"],"grind",initvel=[0,0])
						
						# if self.gp("dashmeter") > -100:
							# pm.particlespawnbluprint([om.objects["player"]["pos"][0] + (self.gp("act_vel")[0]/100) - 32/2,om.objects["player"]["pos"][1] + 10],"ultra",initvel=[self.gp("act_vel")[0]/10,self.gp("act_vel")[1]/10])

						#ground detection + falling
						if ground:
							if self.bailable:
								self.wait("BAIL",0.6)
								self.sp("dashmeter",0)
								self.bailable = 0
								# for i in range(10):
								# 	pm.particlespawnbluprint(om.objects["player"]["pos"],"dust",initvel=[0,5])
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


						#prevent rotation on walls
						if self.gp("leftwall") or self.gp("rightwall"):
							self.killtimer("rotate")
							self.sp("rotoffset",0)

						#AIR DASH
						if self.key["jump"] and not ground and not self.lastkey["jump"]:
							if not self.isthere("doublejumpcd") and self.gp("candj"):
								self.bailable = 0
								self.sp("candj",0)
								self.sp("dashmeter",self.gp("dashmeter") + 30)
								self.wait("dashrem",2)
								# cm.setcond("playercam","shake",6)
								actmult = [160,160]
								actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
								desmult = [160,160]
								desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]
								# self.spin(21,0.4,0.1)

								self.sp("dashav",self.listdiv(actvel,80))
								self.sp("dashdv",self.listdiv(desvel,80))

								self.sp("act_vel",0,1)
								self.sp("des_vel",0,1)
								self.sp("act_vel",0,0)
								self.sp("des_vel",0,0)
								self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
								self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))

						# self.println(collisionlisttype,4)
						if not self.gp("homing") == 0:
							if "ground" in collisionlisttype:							
								self.sp("homing",0)
								self.print("AAHHH")
								self.key["secondary"] = 0




						#INITIATE HOMING ATTACK
						if not self.gp("homing") == 1:
							if self.key["secondary"] and not self.key["trick"]:
								if not vec == None:
									if not self.isthere("homecooldown"):
										if not self.lastkey["secondary"]:
											self.wait("homecooldown",0.2)
											self.sp("homing",1)
											self.sp("target",vec)
											if ground:
												self.key["jump"] = 1
												self.sp("act_vel",40,index=1)


						#GOTO TARGET
						if self.gp("homing") == 1:
							# self.wait("teltimer",1)
							enposvec = pygame.math.Vector2(self.gp("target").info["pos"])
							playerposvec = pygame.math.Vector2(om.objects["player"]["pos"])

							envec = enposvec - playerposvec
							if envec.length() > 0:
								nenvec = envec.normalize()
								nenvec = [nenvec.x,nenvec.y * -1]
								ground = 0
								if self.gp("target").info["type"] in ["enemy-L","omnispring","goal","turret","rocket"]:
									if envec.length() > 40:
										a = (380 + (abs(envec.length()/3)))/2
										d = (380 + (abs(envec.length()/3)))/2
										
										if self.gp("target").info["type"] == "rocket":
											a += om.get_value(self.gp("target").name,"vel") * 4
											d += om.get_value(self.gp("target").name,"vel") * 4
										av = [a * nenvec[0] , a * nenvec[1]]
										dv = [d * nenvec[0] , d * nenvec[1]]
										self.sp("act_vel",av)
										self.sp("act_vel",dv)
										if self.gp("target").info["type"] == "enemy-L":
											om.set_value(self.gp("target").name,"des_vel",[0,0])
											om.set_value(self.gp("target").name,"act_vel",[0,0])
									else:
										self.sp("homing",2)
										# om.objects["player"]["pos"] = self.gp("target").info["pos"]
										self.sp("HOLD",self.gp("target").info["pos"])
										self.sp("act_vel",200,1)

						#DISMOUNT
						if self.gp("homing") == 2:
							if self.gp("target").info["type"] == "enemy-L":
								if self.key["secondary"]:
									# self.sp("des_vel",[0,0])
									self.sp("wantime",0.1)
									om.set_value(self.gp("target").name,"act_vel",[0,0])
									om.set_value(self.gp("target").name,"des_vel",[0,0])
									self.gp("target").info["pos"] = self.listadd((om.objects["player"]["pos"],[  self.valsign(self.gp("des_vel")[0]) * 40  ,  -30   ]))
								else:
									self.sp("homing",0)
									if self.lastkey["secondary"]:
										self.sp("dashmeter",self.gp("dashmeter") + 30)
										od = self.timers.copy()
										for timer in self.timers.keys():
											if "#Throwing" in timer:
												od.pop(timer)
										self.timers = od

										
										if round(axis[0]) == 0:
											if round(axis[1]) == 0:
												actmult = [0,100]
										actmult = [axis[0] * 100,axis[1] * 100]
										if actmult == [0,0]:
											actmult = [100,0]


										om.set_value(self.gp("target").name,"throwvel",actmult)
										self.wait("#Throwing" + self.gp("target").name,3,0)
										self.sp("dashmeter",self.gp("dashmeter") + 30)

										self.wait("dashrem",2)
										# cm.setcond("playercam","shake",6)
										actmult = [160,160]
										actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
										desmult = [160,160]
										desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]
										# self.spin(21,0.4,0.1)

										self.sp("dashav",self.listdiv(actvel,80))
										self.sp("dashdv",self.listdiv(desvel,80))

										self.sp("act_vel",0,1)
										self.sp("des_vel",0,1)
										self.sp("act_vel",0,0)
										self.sp("des_vel",0,0)
										self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))

										self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))
									else:
										
										self.sp("dashmeter",self.gp("dashmeter") + 30)
										self.wait("dashrem",2)
										# cm.setcond("playercam","shake",6)
										actmult = [160,160]
										actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
										desmult = [160,160]
										desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]

										if actmult == [0,0]:
											actmult = [160,50]
											desmult = [160,50]
										# self.spin(21,0.4,0.1)

										self.sp("dashav",self.listdiv(actvel,80))
										self.sp("dashdv",self.listdiv(desvel,80))

										self.sp("act_vel",0,1)
										self.sp("des_vel",0,1)
										self.sp("act_vel",0,0)
										self.sp("des_vel",0,0)
										self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
										self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))
							if self.gp("target").info["type"] == "goal":
								if not self.isthere("show-score"):
									# self.print(    "attempt" + str(self.timesdone) + ":" + um.elements["Speed-timer"]["text"]     )
									self.storedscore = "attempt" + " "+str(self.timesdone) +  " =" + " "+ um.elements["Speed-timer"]["text"] 
									self.scores[self.timesdone] = float(um.elements["Speed-timer"]["text"])
									self.timesdone += 1

									self.highest = 10000000000000000
									self.highestatt = 0
									for i in self.scores.keys():
										if self.scores[i] < self.highest:
											self.highest = self.scores[i]
											self.highestatt = i
									# print(self.highestatt)

									self.wait("show-score",7)
								self.sp("homing",0)
							if self.gp("target").info["type"] in ["omnispring","turret"]:
								if self.key["secondary"]:
									self.sp("des_vel",[0,0])
									self.sp("act_vel",[0,0])
									self.sp("wantime",0.5)
									om.objects["player"]["pos"] = self.gp("HOLD")
								else:
									self.sp("dashmeter",self.gp("dashmeter") + 30)
									self.sp("jumpable",1)
									self.sp("homing",0)
									self.wait("bouncerem",3)
									# cm.setcond("playercam","shake",6)
									actmult = [150,150]
									actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
									desmult = [150,150]
									desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]

									if actmult == [0,0]:
										actmult = [160,50]
										desmult = [160,50]
									# self.spin(23,0.4,0.1)

									self.sp("dashav",self.listdiv(actvel,16))
									self.sp("dashdv",self.listdiv(desvel,16))

									self.sp("act_vel",0,1)
									self.sp("des_vel",0,1)
									self.sp("act_vel",0,0)
									self.sp("des_vel",0,0)
									self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
									self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))
							if self.gp("target").info["type"] in ["rocket"]:
								if self.key["secondary"] and not self.gp("exithm"):
									self.sp("des_vel",[0,0])
									self.sp("act_vel",[0,0])
									self.sp("wantime",0.5)
									om.objects["player"]["pos"] = self.gp("target").info["pos"]
								else:
									
									self.sp("exithm",0)
									self.sp("dashmeter",self.gp("dashmeter") + 70)
									self.sp("jumpable",1)
									self.sp("homing",0)
									self.wait("bouncerem",3)
									# cm.setcond("playercam","shake",6)
									actmult = [150,150]
									# actvel = [  axis[0] * actmult[0], axis[1] * actmult[1]]
									actvel = [0,0]
									desmult = [150,150]
									desvel = [  axis[0] * desmult[0], axis[1] * desmult[1]]
									om.set_value(self.gp("target").name,"exp",1)
									actvel[0] = math.cos(self.gp("target").info["rot"]/180 * math.pi) * 12 * om.get_value(self.gp("target").name,"vel") + (axis[0]*50)
									actvel[1] = math.sin(self.gp("target").info["rot"]/180 * math.pi) * 12 * om.get_value(self.gp("target").name,"vel") + (axis[1]*50)

									if self.gp("exithm"):
										actvel[0] /= 3
										actvel[1] /= 3

									if actmult == [0,0]:
										actmult = [160,50]
										desmult = [160,50]
									# self.spin(23,0.4,0.1)

									self.sp("dashav",self.listdiv(actvel,16))
									self.sp("dashdv",self.listdiv(desvel,16))

									self.sp("act_vel",0,1)
									self.sp("des_vel",0,1)
									self.sp("act_vel",0,0)
									self.sp("des_vel",0,0)
									self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
									self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))



						if self.isthere("show-score"):
							um.state = "vic"
							um.addrect([6000,6000],["vic"],[(-0.5 + 0.02) - 0.5,0.8],"atnum",color=(0,0,0),fromstart=0,alpha = 200)
							um.addtext("Victory-lap","",univars.defont,[0,0],univars.theme["accent"],100,"vic")
							um.elements["Victory-lap"]["text"] = self.storedscore + "    " + str(int(self.timers["show-score"]/60) + 1) + "\n\n"  + f"Lowest - time:{self.highest}  on-attempt:{self.highestatt}"


					

						


								


						#jumping
						if self.key["jump"]:
							self.sp("fss",16)
							# self.sp("desmooth",5)
							if self.gp("jumpable"):
								self.sp("jumpable",0)
								self.deltimer("doublejumpcd")
								self.wait("doublejumpcd",0.2)
								self.sp("candj",1)
								#normal
								self.lastframejumped = 1
								self.sp("jumpable",False)
								self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
								self.sp("mode","in-air")



								#Wall jumping
								# if self.key["y"] > 0.4:
								a = 200
								# else:
								# 	a = 120
								if self.gp("leftwall") and not  len(collision["botmid"]["inst"]) > 0:
									self.sp("dashmeter",self.gp("dashmeter") + (30 * self.dt))
									self.deltimer("rightjump")
									self.wait("leftjump",0.1)
									
									self.spin(-7 ,1,spindec = 0)
									self.sp("jumpable",False)
									self.sp("des_vel",[ self.gp("des_vel",0)  , a     ])
									self.sp("act_vel",[  150 , self.gp("act_vel")[1]     ])
									self.sp("dashmeter",self.gp("dashmeter") + 15)
									self.sp("mode","in-air")
								if self.gp("rightwall") and not  len(collision["botmid"]["inst"]) > 0:
									self.sp("dashmeter",self.gp("dashmeter") + (30 * self.dt))
									self.deltimer("leftjump")
									
									self.spin(7 ,1,spindec = 0)
									self.wait("rightjump",0.1)
									self.sp("jumpable",False)
									self.sp("des_vel",[  self.gp("des_vel",0) , a     ])
									self.sp("act_vel",[  -150 , self.gp("act_vel")[1]     ])
									self.sp("dashmeter",self.gp("dashmeter") + 15)
									self.sp("mode","in-air")

						else:
							self.lastframejumped = 0
							self.sp("fss",8)

							if self.gp("leftwall") or self.gp("rightwall"):
								self.sp("des_vel",[self.gp("des_vel")[0],self.key["y"] * 200])
								# if self.gp("dashmeter") < 200:
								# 	if abs(self.key["y"]) > 0:
								# 		self.sp("dashmeter",self.gp("dashmeter")+ (self.dt * 3 * abs(self.key["y"])))

							if not ground:
								if self.gp("leftwall"):
									self.sp("desrot",-90)
									self.sp("desmooth",3)

								elif self.gp("rightwall"):
									self.sp("desrot",90)
									self.sp("desmooth",3)

							# else:
							# 	if not ground:


						#tilt when moving
						if not ground:
							if not self.gp("leftwall") and not self.gp("rightwall"):
								if abs(self.key["x"]) > 0:
									if not self.isthere("rotate"):
										# if not abs()
										
										if not self.bailable:
											self.sp("rotoffset",self.rotlerp(self.gp("rotoffset"),0,5))
											self.sp("desrot",self.rotlerp(self.gp("desrot"),self.gp("act_vel")[0]/4,5) )


						

						# #slingshot
						# if self.key["secondary"] and self.gp("dashmeter") > 0 and not ground:
						# 	self.sp("slinging",1)
						# 	self.sp("wantime",0.1)
						# 	self.sp("dashmeter",self.gp("dashmeter") - self.dt/10)
						# 	om.speed = self.unilerp(om.speed,0.1,5,roundto=2,useigt=0) 
						# 	self.sp("slomorot",vecaxis.angle)
						# else:
						# 	self.sp("slinging",0)


							if self.gp("lastframeswing"):
								self.sp("dashmeter",self.gp("dashmeter") - 10)
								self.wait("dashrem",2)
								# cm.setcond("playercam","shake",6)
								actmult = [190,190]
								actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
								desmult = [190,190]
								desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]
								# self.spin(20,0.7,0.1)

								self.sp("dashav",self.listdiv(actvel,40))
								self.sp("dashdv",self.listdiv(desvel,40))

								self.sp("act_vel",0,1)
								self.sp("des_vel",0,1)
								self.sp("act_vel",0,0)
								self.sp("des_vel",0,0)
								self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
								self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))	

						
						self.sp("lastframeswing",self.gp("slinging"))	

						

						
									


						if self.isthere("dashrem"):
							self.unilerp(self.gp("dashav"),[0,0],3)
							self.unilerp(self.gp("dashdv"),[0,0],3)
							self.sp("act_vel",self.listadd((self.gp("act_vel"),self.gp("dashav"))))
							self.sp("des_vel",self.listadd((self.gp("des_vel"),self.gp("dashdv"))))
							
							# cm.setcond("playercam","shake",0)

						if self.isthere("bouncerem"):
							self.unilerp(self.gp("dashav"),[0,0],7)
							self.unilerp(self.gp("dashdv"),[0,0],7)
							self.sp("act_vel",self.listadd((self.gp("act_vel"),self.gp("dashav"))))
							self.sp("des_vel",self.listadd((self.gp("des_vel"),self.gp("dashdv"))))
							
							# cm.setcond("playercam","shake",0)



						if ground:
								# self.print("AAAHHH")
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
					self.sp("homing",0)
					self.bailable = 0
					om.speed = univars.func.lerp(om.speed,1,5,roundto=2)
					self.sp("slinging",0)
					self.sp("jumpable",True)

					self.killtimer("rotate")
					self.sp("rotoffset",0)
					railpiece = collisionbox["inst"][0]
					if railpiece.name == "rail":
						railrot = railpiece.rot
					else:
						railrot = railpiece.rot + 45
					if not self.lastrail  == rail or not self.lastdirrail == railrot:
						self.sp("entervel",univars.func.dist([0,0],self.gp("act_vel")) )


						

						axisvec = pygame.math.Vector2(self.key["x"],self.key["y"])
						if axisvec.length() == 0:
							axisvec = pygame.math.Vector2(self.gp("des_vel",0),self.gp("des_vel",1))
						if axisvec.length() == 0:
							axisvec = pygame.math.Vector2(1,0)
						# print(axisvec.length())
						axisvec = axisvec.normalize()

						railvec = pygame.Vector2()
						railvec.from_polar((1,railrot))
						# print(railvec)
						# Vector2.from_polar((r, phi))

						if axisvec.dot(railvec) > 0:
							raildir = 1
							self.sp("dirforrail","l")
						else:
							raildir = -1
							self.sp("dirforrail","r")



						# self.sp("dirforrail",self.lastdirslant)
						# if self.gp("dirforrail") == "l":
						# 	raildir = 1
						# else:
						# 	raildir = -1



						if railpiece.name == "rail":
							om.objects["player"]["pos"] = [
															collisionbox["inst"][collisionboxtype.index("rail")].realpos[0]  -  (math.sin((railrot/180) * math.pi) * 5) ,
															collisionbox["inst"][collisionboxtype.index("rail")].realpos[1]  -  (math.cos((railrot/180) * math.pi) * 5) 
														]
						else:
							om.objects["player"]["pos"] = [
															collisionbox["inst"][collisionboxtype.index("rail")].realpos[0]  -  (math.sin((railrot/180) * math.pi) * 20) ,
															collisionbox["inst"][collisionboxtype.index("rail")].realpos[1]  -  (math.cos((railrot/180) * math.pi) * 20) 
														]
						motivate = [  300 * math.cos((railrot/180) * math.pi) * raildir,300   * math.sin((railrot/180) * math.pi) * raildir ]
						om.translate(self,"player",motivate,usedt=1)
						# if self.gp("entervel") < 1:
						# 	self.sp("entervel",1)

					
					# if abs(self.key["x"]) > 0.5 or abs(self.key["y"]) > 0.5 and not self.key["jump"]:
					self.sp("entervel",self.gp("entervel") + 2 )
					self.sp("entervel",self.gp("entervel") + 2 )

					axisvec = pygame.math.Vector2(self.key["x"],self.key["y"])
					if axisvec.length() == 0:
						axisvec = pygame.math.Vector2(self.gp("des_vel",0),self.gp("des_vel",1))
					if axisvec.length() == 0:
						axisvec = pygame.math.Vector2(1,0)
					# print(axisvec.length())
					axisvec = axisvec.normalize()

					railvec = pygame.Vector2()
					railvec.from_polar((1,railrot))
					# print(railvec)
					# Vector2.from_polar((r, phi))

					if axisvec.dot(railvec) > 0:
						raildir = 1
						self.sp("dirforrail","l")
					else:
						raildir = -1
						self.sp("dirforrail","r")


					if self.gp("entervel") > 220:
						self.sp("entervel",220)
					if self.gp("entervel") < -220:
						self.sp("entervel",-220)
	


				
					self.sp("desrot",railrot)
					
					railvel = [  self.gp("entervel") * math.cos((railrot/180) * math.pi) * raildir, self.gp("entervel")  * math.sin((railrot/180) * math.pi) * raildir ]
					self.sp("act_vel",railvel)
					self.sp("des_vel",railvel)
					self.lastdirrail = railrot

					
					
					# if railrot > 180:
					# 	railrot =  railrot -360

					if self.key["jump"]:
						if self.gp("jumpable"):
							newvec = railvec.rotate(90)
							# newvec = newvec + axisvec
							newvec.scale_to_length(100)
							self.sp("des_vel",[newvec.x + self.gp("des_vel",0),newvec.y + self.gp("des_vel",1)])
							self.sp("act_vel",[newvec.x + self.gp("act_vel",0),newvec.y + self.gp("act_vel",1)])
					parts = om.objects["player"]["pos"]
					vel = [self.gp("act_vel")[0]/7,self.gp("act_vel")[1]/7]
					pm.particlespawnbluprint(parts,"grind",initvel= vel)




						

				#UPDATE POSITIONS AND ROTATIONS
				if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ) or rail:
					self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
					om.translate(self,"player",self.gp("act_vel"),usedt=1)
					if self.isthere("BAIL"):
						self.sp("desrot",90)
					
					if self.isthere("trick3"):
						if self.key["x"] > 0:
							self.sp("desrot",-180)
						else:
							self.sp("desrot",180)

					# if round(self.gp("desrot")) == 270:
					# 	self.sp("desrot",-90)
						# print(self.gp("desrot"))
					# if self.gp("desrot") < 0:
					# 	self.sp("desrot",0 - self.gp("desrot"))
					if self.isthere("rotate"):
						self.sp("rotoffset",self.gp("rotoffset") + (self.gp("rot")*self.dt) )

						self.sp("rot",self.gp("rot") - (self.valsign(self.gp("rot")) * abs(self.gp("rotdes") * self.dt)       ) )
						
					# om.objects["playersprite"]["rot"] = a
					if abs(self.gp("unboundrot")) > 180 and abs(self.gp("rotoffset")) > 180 :
						min_value = -180
						max_value = 180
						range_size = max_value - min_value

						self.sp("rotoffset",((self.gp("rotoffset") - min_value) % range_size) + min_value)
						self.sp("unboundrot",((self.gp("unboundrot") - min_value) % range_size) + min_value)


					if self.gp("slinging"):
						if abs(self.gp("unboundrot")) > 180 :
							min_value = -180
							max_value = 180
							range_size = max_value - min_value

							self.sp("unboundrot",((self.gp("unboundrot") - min_value) % range_size) + min_value)
						

					# min_value = -180
					# max_value = 180
					# range_size = max_value - min_value
					# self.sp("rotoffset", ((self.gp("rotoffset") - min_value) % range_size) + min_value)
					# 	self.sp("rotoffset",self.gp("rotoffset") - 360)
					# if self.gp("rotoffset") < -180:
					# 	self.sp("rotoffset",self.gp("rotoffset") + 360)


					rot = self.gp("unboundrot")
					if not self.gp("slinging"):
						dest = self.gp("desrot")+ self.gp("rotoffset")
					else:
						dest = self.gp("slomorot")

					d1 = abs(rot - (dest - 360))
					d2 = abs(rot - (dest + 360))
					d3 = abs(rot - (dest + 0))
					
					destinations = {d1:dest-360,d2:dest+360,d3:dest}


					dest = destinations[min([d1,d2,d3])]


					# if path == d1: 
					# dest = fm.frame* 30
					# print(dest)
					# om.objects["playersprite"]["rot"]   +=  30
					sm = 5
					
					if self.isthere("trick3"):
						sm = 3
					# om.objects["playersprite"]["rot"]   =  
					if not self.gp("slinging"):
						self.sp("unboundrot",self.unilerp(rot,dest,sm,roundto=2))
						a = self.gp("unboundrot")
						min_value = -180
						max_value = 180
						range_size = max_value - min_value
						a = ((a - min_value) % range_size) + min_value
						if -5 < a < 5:
							om.objects["playersprite"]["rot"]  =  0
						else:
							om.objects["playersprite"]["rot"] = a
					else:
						self.sp("unboundrot",self.unilerp(rot,dest,sm,roundto=2,useigt=0))
						a = self.gp("unboundrot")
						min_value = -180
						max_value = 180
						range_size = max_value - min_value
						a = ((a - min_value) % range_size) + min_value
						om.objects["playersprite"]["rot"] = a
					

						
				
				

					if not rail:
						#prevent no-clip
						if self.gp("mode") == "grounded":
							if "ground" in collisionlisttype:
								self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
								self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
								om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32

						if not self.gp("onboard"):
							if om.get_value("skateboard","fallvalue")< 20:
								om.set_value("skateboard","fallvalue",om.get_value("skateboard","fallvalue") - 2* self.dt)
							om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 0]
							om.translate(self,"skateboard",[0,om.get_value("skateboard","fallvalue")])
						else:
							om.set_value("skateboard","fallvalue",5)

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
		else:                                                                                                                               
			
			
			self.sp("candj",1)
			self.sp("jumpable",1)
			if "slantr" in collisionboxtype:
				self.sp("slantdir","r")
				if not slanted == self.lastframeslanted:
					# if not ground:
					index = collisionboxtype.index("slantr")
					om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] - 20,collisionbox["inst"][index].realpos[1] - 20]
					self.sp("act_vel",[  self.gp("act_vel")[0]    ,    self.gp("act_vel")[0]   ])
					self.sp("des_vel",[  self.gp("des_vel")[0]    ,    self.gp("des_vel")[0]   ])
						# else:
						# 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
				else:
					if abs(self.key["x"]) > 0:
						self.sp("des_vel",[         self.key["x"] * 70             ,    self.gp("des_vel")[1]   ])
					else:
						self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
					self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
					if not self.key["jump"]:
						self.sp("act_vel",[self.gp("act_vel")[0],self.gp("act_vel")[0]])
					else:
						self.sp("act_vel",[self.gp("act_vel")[0],abs(self.gp("act_vel")[1])])
					om.translate(self,"player", self.gp("act_vel"),usedt=1)
					self.sp("desrot",45) 
			else:
				
				self.sp("slantdir","l")
				if not slanted == self.lastframeslanted:
					index = collisionboxtype.index("slantl")
					# if not ground2:
					om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] +16,collisionbox["inst"][index].realpos[1] -20]
					self.sp("act_vel",[  self.gp("act_vel")[0] * 1.1    ,    -1 * self.gp("act_vel")[0] * 1.1   ])
					self.sp("des_vel",[  self.gp("des_vel")[0] * 1.1    ,    -1 * self.gp("des_vel")[0] * 1.1   ])
						# else:
						# 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
				else:
					if abs(self.key["x"]) > 0:
						self.sp("des_vel",[         self.key["x"] * 70             ,    self.gp("des_vel")[1]   ])
					else:
						self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
					self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
					if not self.key["jump"]:
						self.sp("act_vel",[self.gp("act_vel")[0],-1 * self.gp("act_vel")[0]])
					else:
						self.sp("act_vel",[self.gp("act_vel")[0], self.gp("act_vel")[1]])
					om.translate(self,"player", self.gp("act_vel"),usedt=1)
					self.sp("desrot",-45)



		




			if -5 < self.gp("desrot") < 5:
				om.objects["playersprite"]["rot"]  =  0
			else:
				om.objects["playersprite"]["rot"]  =  self.unilerp(om.objects["playersprite"]["rot"],self.gp("desrot"),5,roundto=2) 

			if self.key["jump"]:
				self.sp("fss",16)
				self.sp("desmooth",5)
		
				#normal
				self.sp("jumpable",False)
				self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
				self.sp("mode","in-air")
				self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
				om.translate(self,"player",[0,self.gp("act_vel")[1]],usedt=1)
		


		














		#get out of wall
		if len(collision["midmid"]["inst"] )> 0 and not slanted and not rail :
			top = collision["topmid"]["inst"] or collision["topleft"]["inst"] or collision["topright"]["inst"]
			bot = collision["botmid"]["inst"] or collision["botleft"]["inst"] or collision["botright"]["inst"]
			left = collision["topleft"]["inst"] or collision["midleft"]["inst"] or collision["botleft"]["inst"]
			right = collision["topright"]["inst"] or collision["midright"]["inst"] or collision["botright"]["inst"]
			mip = collision["midmid"]["inst"][0].realpos
			if collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] :
				# self.publicvariables["shaderstate"] = not self.publicvariables["shaderstate"]
				om.translate(self,"player",[self.gp("act_vel")[0] * -1,self.gp("act_vel")[1] * -1],usedt=1)
				self.sp("des_vel",[0,0])
			elif top and not collision["botmid"]["inst"]:
				om.objects["player"]["pos"][1] =  mip[1] + 32
			elif bot and not collision["topmid"]["inst"]:
				om.objects["player"]["pos"][1] =  mip[1] - 32
			elif right and not collision["midleft"]["inst"]:
				om.objects["player"]["pos"][0] = mip[0] - 32
			elif left  and not collision["midright"]["inst"]:
				om.objects["player"]["pos"][0] = mip[0] + 32
		else:
			self.lastframeslanted = slanted
			self.sp("prev_act_vel",self.gp("act_vel"))
			self.sp("prev_des_vel",self.gp("des_vel"))
			self.sp("prevprevpos",om.objects["player"]["pos"])

		


								 

				
		


		#LOOK AHEAD

		if not rail:
			if self.gp("slinging"):
				self.lookaheady = self.unilerp(self.lookaheady,self.key["y"] * -20,4,roundto=2,useigt=0)
				self.lookahead = self.unilerp(self.lookahead,self.key["x"] * 20,4,roundto=2,useigt=0)
			elif self.gp("homing") == 2:
				self.lookaheady = self.unilerp(self.lookaheady,self.key["y"] * -200,4,roundto=2,useigt=0)
				self.lookahead = self.unilerp(self.lookahead,self.key["x"] * 200,4,roundto=2,useigt=0)
				# self.print("REXTRCTVBIUN")
			else:
				
				if self.gp("leftwall") or self.gp("rightwall"):
					self.lookahead = self.unilerp(self.lookahead,0,4,roundto=2,useigt=1)
					if self.key["y"] < 0:
						self.lookaheady = self.unilerp(self.lookaheady,200,8,roundto=2)
					elif self.key["y"] > 0:
						self.lookaheady = self.unilerp(self.lookaheady,-200,8,roundto=2)
					else:
						self.lookaheady = self.unilerp(self.lookaheady,0,20,roundto=2)
				else:
					self.lookaheady = self.unilerp(self.lookaheady,self.key["y"] * -100,4,roundto=2,useigt=1)
					if self.gp("xinit"):
						self.lookahead = 0
					if self.gp("des_vel")[0] > 0:
						self.lookahead = self.unilerp(self.lookahead,400,8,roundto=2)
					elif self.gp("des_vel")[0] < 0:
						self.lookahead = self.unilerp(self.lookahead,-400,8,roundto=2)
					else:
						self.lookahead = self.unilerp(self.lookahead,0,20,roundto=2)


					
					
				
				# self.println([self.lookahead,self.lookaheady],3)
		else:
			cm.setcond("playercam","shake",4)
			self.lookaheady = self.unilerp(self.lookaheady,-300 * math.sin((railrot/180) * math.pi) * raildir ,4,roundto=2,useigt=0)
			self.lookahead = self.unilerp(self.lookahead,300 * math.cos((railrot/180) * math.pi) * raildir,4,roundto=2,useigt=0)


		

		cm.setcond("playercam","shake",self.unilerp(cm.getcam("playercam","shake"),0,10)     )

		self.println(self.gp("candj"),4)
		self.println(self.gp("jumpable"),5)


			
		
		self.lastrail = rail
		self.lastground = ground
		self.sp("lastframewall",self.gp("leftwall") or self.gp("rightwall"))
		om.speed = univars.func.lerp(om.speed,self.gp("wantime"),5,roundto=2)
		if self.ondone("show-score"):
			um.state = "maingame"
			# self.wait()
			self.initialiseplayer([0,60])


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

	def sp(self,val:str,to,index=None):
		"""
		changes the value a players variable
		"""
		if index == None:
			om.set_value("player",val,to)
		else:
			change = to
			to = self.gp(val)
			to[index] = change
			om.set_value("player",val,to)

	def gp(self,val:str,index=None):
		"""
		gets the value a players variable
		"""
		if index == None:
			return om.get_value("player",val)
		else:
			return om.get_value("player",val)[index]
	

	

	# def qrcond(self, id, info):
	# 	om.set_value(id,"spawned",0)
		
	def qrcond(self, id, info):
		if info["type"] == "spawn-1":
			if not om.get_value(id,"sid") == 0:
				for i in om.get_value(id,"sid"):
					if i in om.objects.keys():
						om.removeid(i)
			om.set_value(id,"spawned",0)


		if info["type"] == "HURT:laser":
			om.removeid(id)

		if info["type"] == "HPBAR":
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


		
			
			
			
		if info["type"] == "bird":
			om.set_value(id,"active",0)
			om.set_value(id,"vel",[0,0])
			
			


	def cond(self,id,info,st):
		"""id -> the id   info -> the info for the id"""
		if info["type"] == "enemy-L" and "player" in om.values.keys():
			self.trianglebot(id,info,st)

		if info["type"] == "HURT:laser":
			self.laserbeam(id,info,st)

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
			
			self.print(om.get_value(master,"col"))
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
			om.set_value(id,"timeon",om.get_value(id,"timeon") + st)
			om.set_value(id,"timer",om.get_value(id,"timer") - st/20)
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
				
				self.sp("exithm",1)
				om.set_value(id,"canhome",0)

		if om.get_value(id,"exp"):
			if om.objects[id]["rendercond"]:
				pm.particlespawnbluprint([om.objects[id]["pos"][0],om.objects[id]["pos"][1] ],"exp3",initvel=[  math.cos(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel")  , math.sin(om.objects[id]["rot"]/180 * math.pi) * om.get_value(id,"vel")  ])
			om.objects[id]["rendercond"] = 0
			om.set_value(id,"canhome",0)
		

			
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


	def createhpbar(self,id,size,offset):
		"""
			offset has y up = +\n
			Y axis FIXED
		"""
		hpid = om.add(self,(0,0),"laser",0,"HPBAR",[size,size],univars.grandim,keepprev=1,layer=5)
		om.objects[hpid]["type"] = "HPBAR"
		om.set_value(hpid,"obj-id",id)
		om.set_value(hpid,"size",size)
		om.set_value(hpid,"offset",offset)

	def hpbar(self,id,info):
		try:
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

	def trianglebot(self,id,info,st):
		if id in om.values.keys() and "act_vel" in om.values["player"].keys():

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
