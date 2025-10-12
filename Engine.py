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
		self.ingametime = 0
		self.bailable = 0
		self.skatedetach = 0
		self.publicvariables["gamespeed"] = 1
		self.publicvariables["mood"] = "afternoon"
		self.publicvariables["showater"] = 1
		self.publicvariables["waterh"] = -(64 * 0.4)
		self.lookaheady = 0
		self.timesdone = 1
		self.scores = {}
		self.lookahead = 100
		self.lerpshake = 0
		self.actualwaterheight = 0


	def onreload(self):
		self.a = 0

		# bg.addbackground("test2")
		# bg.addbackgrounditem("black2","test2",[0,-40]                ,surf = "mount",dimensions=[500*5,250*5],layer = 0.15,infiniscroll=True)
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
			self.publicvariables["screencol"] = (70 ,189 ,234 )
			sd.program["illuminace"] = 0.5
			sd.program["sunpos"] = [0,0]
			sd.program["pacify"] = -0.5

		if mood == "sunset":
			self.publicvariables["screencol"] = (110 ,189 ,234 )
			sd.program["illuminace"] = 0.34
			sd.program["sunpos"] = [0,-1 * self.actualwaterheight/20 + 0.5]
			sd.program["pacify"] = -0.4


		if mood == "daybreak":
			self.publicvariables["screencol"] = (110 ,189 ,234 )
			sd.program["illuminace"] = 0.5
			sd.program["sunpos"] = [0,0]
			sd.program["pacify"] = 0

		if mood == "night":
			self.publicvariables["screencol"] = (0,0,50)
			sd.program["illuminace"] = 0.22
			sd.program["sunpos"] = [0,0]
			sd.program["pacify"] = 0.2




		




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
			om.objects["playersprite"]["pos"][0] = om.objects["player"]["pos"][0] - math.sin((rot/180) * math.pi) * 11
			om.objects["playersprite"]["pos"][1] = om.objects["player"]["pos"][1] - math.cos((rot/180) * math.pi) * 11
			if self.gp("des_vel")[0] > 0:
					om.flip("playersprite","right")
			if self.gp("des_vel")[0] < 0:
					om.flip("playersprite","left")


				

			if not self.isthere("skatego"):
				om.endanim("skateboard",0)
				if self.isthere("BAIL"):
					om.objects["skateboard"]["rot"] = 0
					
					om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0] -10,om.objects["player"]["pos"][1] - 0]
				else:
					
					om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 0]
					om.objects["skateboard"]["rot"] = rot
			
			else:
				om.playanim(self.dt,"skateboard","kickflip",1)
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
			


			if not abs(self.key["x"]) > 0:
				om.playanim(self.dt,"playersprite","idle",forceplay=True)
			elif not abs(self.gp("des_vel")[0]  - self.key["x"] * 150) < 20:
				om.playanim(self.dt,"playersprite","moveidle",forceplay=True)
			else:
				om.playanim(self.dt,"playersprite","fastidle",forceplay=True)

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
		
		om.adds(self,"player",startpos,"player","player",0,[1,1],400,5)
		self.sp("#DEBUG","HELLO WOLRD")
		om.objects["player"]["rendercond"] = False

		self.sp("dashmeter",0)
		
		self.sp("dashcooldown",0)
		self.sp("deshrem",0)

		#creates the player sprite you actually see
		om.adds(self,"playersprite",[-1400,400],"player","player",0,[1,1],400,5)
		om.objects["playersprite"]["rendercond"] = True
		om.includeflipping("playersprite")

		#creates the skateboard
		om.adds(self,"skateboard",[-1400,400],"skateboard","skateboard",0,[1,1],400,5)
		om.objects["skateboard"]["rendercond"] = True

		#desired velocity


		self.sp("lastframewall",0)


		self.sp("slinging",0)

		self.lastrail = 0

		self.sp("des_vel",[0,0])

		self.sp("candj",0)

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

		um.addtext("Speed-timer","0",univars.defont,[0,0.8],univars.theme["accent"],60,["maingame"])
		um.elements["Speed-timer"]["text"]  = str(0)

		um.addtext("attemps","0",univars.defont,[0.5,0.8],univars.theme["accent"],60,["maingame"])
		um.elements["attemps"]["text"]  = str(0)

	def moveplayer(self):
		# self.println(self.key["axis"],5)
		# om.speed = 0.4
		# self.println(self.gp("dashmeter"),2)
		# self.println(em.controller,10)
		# self.println(em.analog_keys[5],10)
		um.elements["Speed-timer"]["text"]  = str(round(float(um.elements["Speed-timer"]["text"]) + (self.dt/60 *self.publicvariables["gamespeed"] ),2))
		um.elements["attemps"]["text"]  = str(self.timesdone)
		
		self.sp("wantime",self.publicvariables["gamespeed"])
		# self.sp("dashmeter",abs(math.sin(fm.frame/100) * 100)
		self.sp("dashmeter",min([100,self.gp("dashmeter")]))
		self.sp("dashmeter",max([0,self.gp("dashmeter")]))
		# print(self.gp("dashmeter"))




		um.elements["dashbar"]["dimensions"][0] = self.unilerp( um.elements["dashbar"]["dimensions"][0] ,   max([((self.gp("dashmeter") * 10) - 50)/2,0]) ,4  )
		if self.gp("dashmeter") <= 0:
			um.elements["dashbar"]["dimensions"][0] = 0
		um.elements["dashbar"]["color"] = (0,100,255)
		# um.elements["dashbar"]["pos"][0] = self.gp("dashmeter")
		# um.showvar("pos",om.objects["player"]["pos"],[0,0])
		collision = om.collide9("player",0,cam,self.dim,ignore= ["playersprite","skateboard"])
		lonepoint1 = om.collidep([om.objects["player"]["pos"][0] + 60,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
		lonepoint2 = om.collidep([om.objects["player"]["pos"][0] - 50,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
		collisionbox = om.collide("player",0,cam,extra=20)
		bigcollisionbox = om.collide("player",0,cam,extra=600)
		# attackbox = om.collide("player",1,cam,extrax=1000,extray=500)
		attackbox = om.colliderect([cm.getcam("playercam","pos")[0] +(self.lookahead*0),cm.getcam("playercam","pos")[1] + (self.lookaheady*0)],[1300,700],0,cam)

		ground1 = len(collision["botmid"]["inst"]) > 0
		ground2 = len(collision["botleft"]["inst"]) > 0    and not (len(collision["topleft"]["inst"])  > 0  ) and not (len(collision["midleft"]["inst"])  > 0  )
		ground3 = len(collision["botright"]["inst"]) > 0   and not (len(collision["topright"]["inst"]) > 0  ) and not (len(collision["midright"]["inst"]) > 0  )
		ground = ground1 or ground2 or ground3
		instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"]
		collisionlisttype = [i.type for i in instlist]
		collisionboxtype = [i.type for i in collisionbox["inst"]] 
		# collisionlisttype.append("ground")

		self.println(collisionlisttype,7)
		if "HURT:laser" in [ i.info["type"] for i in collisionbox["obj"]]:
			if not self.isthere("dashrem") and not self.isthere("inv"):
				self.wait("BAIL",2)
			

		

		rail = False
		if len(collisionboxtype) > 0:
			rail = collisionboxtype[0] == "rail"
			

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
			if self.key["attack"]:
				self.sp("wantime",0.2)
			else:
				if self.lastkey["attack"]:
					self.wait("skatego",0.5,barrier=1)
					self.spin(30,0.1)
					
					self.bailable = 1
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
					
					


		axis = [self.key["x"],self.key["y"] * 1]
		vecaxis = pygame.math.Vector2(axis[0],axis[1])
		if vecaxis.length()> 0:
			vecaxis.normalize()
			vecaxis.scale_to_length(1.2)
		axis = [vecaxis.x,vecaxis.y]
		axis[1] = round(axis[1],2)

		
		vec = None
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
						if obj.info["type"] in ["enemy-L","omnispring","goal"] and om.get_value(obj.name,"canhome"):
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



			

		

			if self.gp("homing") == 2:
				vec = self.gp("target")



		else:
			om.objects["enemyzoom"]["rendercond"] = 0



		if ground and not rail:
			self.sp("dashmeter",self.gp("dashmeter") - min([((40/(self.gp("dashmeter") + 2))*self.dt),2*self.dt]) - (0.2*self.dt))
		else:
			self.sp("dashmeter",self.gp("dashmeter") - min([((5/(self.gp("dashmeter") + 2))*self.dt),2*self.dt])  - (0.2*self.dt))




		#Main movement

		if not slanted:
			if slanted == self.lastframeslanted or self.key["jump"]:
				#MAIN
				
				if not rail:
					if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ):
						#IN HERE IS EITHER [NO MIDMID] OR [Yes MIDMID AND GROUND]
						if self.isthere("BAIL"):
							self.key["x"] = 0
							self.key["y"] = 0
							self.key["jump"] = 0
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


						if self.key["throw"] and not self.lastkey["throw"]:
							
							self.spin(21,0.4,0.1)
							self.wait("inv",0.4)
							
							self.bailable = 0
							self.sp("dashmeter",self.gp("dashmeter") + 20)



						#x dir movement
						if abs(self.key["x"]) > 0:
							if self.isthere("leftjump"):
								self.key["x"] = 1
							if self.isthere("rightjump"):
								self.key["x"] = -1 * 1

							if self.gp("xinit"):
								self.sp("xinit",False)
								self.sp("des_vel",[self.key["x"] * 120,self.gp("des_vel")[1]])
							
							


							self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * 150,30 )              ,    self.gp("des_vel")[1]   ])
						else:
							self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
							self.sp("xinit",True)



						

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
									if self.gp("lastwall") == "r":
										# self.spin(16 ,1,spindec = 0.4)
										self.sp("des_vel",[0,200])
									else:
										# self.spin(-16 ,1,spindec = 0.4)
										self.sp("des_vel",[0,200])
								else:
									# self.spin(self.valsign(self.key["x"]) * -23 ,1,spindec = 0.5)
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

						#ground detection + falling
						if ground:
							if self.bailable:
								self.wait("BAIL",0.6)
								self.sp("dashmeter",0)
								self.bailable = 0
								for i in range(10):
									pm.particlespawnbluprint(om.objects["player"]["pos"],"dust",initvel=[0,5])
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
							if self.key["secondary"]:
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
							enposvec = pygame.math.Vector2(self.gp("target").info["pos"])
							playerposvec = pygame.math.Vector2(om.objects["player"]["pos"])

							envec = enposvec - playerposvec
							if envec.length() > 0:
								nenvec = envec.normalize()
								nenvec = [nenvec.x,nenvec.y * -1]
								ground = 0
								if self.gp("target").info["type"] in ["enemy-L","omnispring","goal"]:
									if envec.length() > 40:
										a = (380 + (abs(envec.length()/3)))/2
										d = (380 + (abs(envec.length()/3)))/2
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
							if self.gp("target").info["type"] == "omnispring":
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
								if self.key["y"] > 0.4:
									a = 200
								else:
									a = 120
								if self.gp("leftwall") and not  len(collision["botmid"]["inst"]) > 0:
									self.deltimer("rightjump")
									self.wait("leftjump",0.1)
									self.sp("jumpable",False)
									self.sp("des_vel",[  self.gp("des_vel")[0] , a     ])
									self.sp("act_vel",[  120 , self.gp("act_vel")[1]     ])
									self.sp("mode","in-air")
								if self.gp("rightwall") and not  len(collision["botmid"]["inst"]) > 0:
									self.deltimer("leftjump")
									self.wait("rightjump",0.1)
									self.sp("jumpable",False)
									self.sp("des_vel",[  self.gp("des_vel")[0] , a     ])
									self.sp("act_vel",[  -120 , self.gp("act_vel")[1]     ])
									self.sp("mode","in-air")

						else:
							self.lastframejumped = 0
							self.sp("fss",8)

							if self.gp("leftwall") or self.gp("rightwall"):
								self.sp("des_vel",[self.gp("des_vel")[0],self.key["y"] * 200])

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


					if self.gp("entervel") > 200:
						self.sp("entervel",200)
					if self.gp("entervel") < -200:
						self.sp("entervel",-200)
	


				
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
					
					# if round(self.gp("desrot")) == 270:
					# 	self.sp("desrot",-90)
						# print(self.gp("desrot"))
					# if self.gp("desrot") < 0:
					# 	self.sp("desrot",0 - self.gp("desrot"))
					if self.isthere("rotate"):
						self.sp("rotoffset",self.gp("rotoffset") + self.gp("rot"))

						self.sp("rot",self.gp("rot") - (self.valsign(self.gp("rot")) * abs(self.gp("rotdes")) ) )
						
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
					 
					# om.objects["playersprite"]["rot"]   =  
					if not self.gp("slinging"):
						self.sp("unboundrot",self.unilerp(rot,dest,5,roundto=2))
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
						self.sp("unboundrot",self.unilerp(rot,dest,5,roundto=2,useigt=0))
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
				if self.gp("slantdir") == "l":
					if self.lastdirslant == "r":
						om.translate(self,"player",[-100,40])
		else:                                                                                                                               
			
			
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
					self.sp("act_vel",[  self.gp("act_vel")[0]    ,    -1 * self.gp("act_vel")[0]   ])
					self.sp("des_vel",[  self.gp("des_vel")[0]    ,    -1 * self.gp("des_vel")[0]   ])
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

			
		
		self.lastrail = rail
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
			om.set_value(id,"canhome",1)
			om.set_value(id,"state","idle")
			om.set_value(id,"HP",100)
			om.set_value(id,"des_vel",[0,0])
			om.set_value(id,"act_vel",[0,0])
			om.set_value(id,"rotspeed",random.randint(1,30))
			pl0 = random.randint(15,30)
			om.set_value(id,"pl0",pl0) 

			om.set_value(id,"pl1",pl0 + random.randint(40,80) ) 
			om.set_value(id,"level",0 )
			om.set_value(id,"speed",random.randint(10 + 20,15 + 20))
			om.set_value(id,"superspeed",random.randint(10,10))
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
			
			om.lighttoenemy(id,"l1",color=(255,0,255),colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=20)


			self.createhpbar(id,1,[0,30])
			



		if info["type"] == "omnispring":
			om.set_value(id,"canhome",1)

		if info["type"] == "goal":
			om.set_value(id,"canhome",1)
			om.translate(self,id,[0,20],0)
			om.objects[id]["sizen"] = [1.4,1.4]

		# if info["type"] == "enemy":
		# 	om.set_value(id,"vel",[0,0])
		# 	om.set_value(id,"tarvel",[0,0])
		# 	om.set_value(id,"clipspeed",5)



	def cond(self,id,info,st):
		"""id -> the id   info -> the info for the id"""
		if info["type"] == "enemy-L" and "player" in om.values.keys():
			self.trianglebot(id,info,st)

		if info["type"] == "HURT:laser":
			self.laserbeam(id,info,st)

		if info["type"] == "HPBAR":
			self.hpbar(id,info)

	def spawnlaser(self,pos,speed,dir,time,extraspeed=[0,0]):
		id = om.add(self,pos,"laser",dir,"HURT:laser",[1,1],univars.grandim,keepprev=1)
		om.objects[id]["type"] = "HURT:laser"
		movec = pygame.Vector2()
		movec.from_polar((speed,dir))
		movec +=  pygame.Vector2(extraspeed[0],extraspeed[1])
		om.set_value(id,"movec",movec)
		om.set_value(id,"speed",speed)
		om.set_value(id,"damage",5)
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


	def trianglebot(self,id,info,st):
		if id in om.values.keys() and "act_vel" in om.values["player"].keys():
	

			if univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < 6000:
				
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
				togoto=  [ playerpos[0] + (self.gp("act_vel")[0]*om.get_value(id,"superspeed")) + rotvec.x , playerpos[1]  - (self.gp("act_vel")[1]*om.get_value(id,"superspeed")) + rotvec.y   ]
				ltogoto = om.get_value(id,"lasttogoto")
				# togoto[0] /= 2
				# togoto[1] /= 2
				# togoto[0]
				newvel = [ (togoto[0] - info["pos"][0])/5 , (togoto[1] - info["pos"][1])/-5    ]



				om.set_value(id,"des_vel",newvel)


				om.set_value(id,"lasttogoto",togoto)
				if univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < 6000:
					om.set_value(id,"state","hover")

				else:
					om.set_value(id,"state","sprint")
			else:
				om.set_value(id,"state","idle")



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
			
			a = pygame.math.Vector2( om.get_value(id,"act_vel"))
			if a.length() > 0 and not self.isthere("#Throwing" + str(id)):
				if om.get_value(id,"pl0") > pygame.math.Vector2( om.get_value(id,"act_vel")).length() < om.get_value(id,"pl1"):
					a = pygame.math.Vector2( om.get_value(id,"act_vel"))
					a.scale_to_length(self.valsign(a.length()) * om.get_value(id,"pl0"))
					om.set_value(id,"act_vel",list(a))
				elif om.get_value(id,"pl1") < pygame.math.Vector2( om.get_value(id,"act_vel")).length():
					a = pygame.math.Vector2( om.get_value(id,"act_vel"))
					a.scale_to_length(self.valsign(a.length()) * om.get_value(id,"pl1"))
					om.set_value(id,"act_vel",list(a))
			
			if self.isthere("#Throwing" + str(id)):
					
					om.rotate(self,id,20)
					cm.setcond("playercam","shake",20)
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
					rot = vectoplayer.angle * -1 + random.randint(-1 * abs(int(self.gp("des_vel")[0]/10)),1 * abs(int(self.gp("des_vel")[0]/10)))
					self.spawnlaser(om.objects[id]["pos"],40,rot,3,extraspeed=self.listdiv(om.get_value("player","act_vel"),2))
					om.set_value(id,"timer",om.get_value(id,"maxtimer"))


			






			if om.get_value(id,"HP") <= 0:
				om.removeid(id)
				# if self.gp("target") == id:


		













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