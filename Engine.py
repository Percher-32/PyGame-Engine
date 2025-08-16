import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
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
		self.publicvariables["showater"] = False
		self.publicvariables["waterh"] = 0.9
		self.actualwaterheight = 0

	def onreload(self):
		self.a = 0
		# bg.addbackground("test2")
		# bg.addbackgrounditem("black2","test2",[0,-40]                ,surf = "mount",dimensions=[500*5,250*5],layer = 0.15,infiniscroll=True)
		# bg.savebg()
		
		if "game" == self.states:

			

			#initialise player and all its variables
			self.initialiseplayer()

		if "veiw" == self.states:
			um.changestate("test1","but1")
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[-0.5,0],"but1",color=univars.theme["dark"],surf = "testbutton")
			# um.addglide("but1",univars.sizes["mediumbutton"],univars.sizes["largebutton"])
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0],"but2",color=univars.theme["dark"])
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[0.5,0],"but3",color=univars.theme["dark"])
			# um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0.5],"but4",color=univars.theme["dark"])
			# um.savealluielements()


		if self.states == "test":
			om.add((0,0),"player",0,"green",[1,1],self.dim)


	def commence(self):
		pass

	def update(self):
		bg.background = "test2"
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


	
		# self.ingametime += self.dt/300 * om.speed
		self.ingametime = -1

		# self.publicvariables["waterh"] -= 0.002
		sd.program['time'] = fm.frame
		sd.program['state'] = self.publicvariables["shaderstate"]
		sd.program["illuminace"] = (math.cos(self.ingametime) + 2)/2
		if self.publicvariables["showater"]:
			sd.program["waterlevel"] = (cam.y/univars.screen.get_height() * 1.7  * cam.size)-( self.publicvariables["waterh"]) + ((1-cam.size)* 1.46)
		else:
			sd.program["waterlevel"] = -1
		sd.program["sunpos"] = [math.sin(self.ingametime) * -1.3,math.cos(self.ingametime) * -1.5 ]
		self.actualwaterheight = (cam.y/univars.screen.get_height() * 1.7  * cam.size)-( + self.publicvariables["waterh"]) + ((1-cam.size)* 1.46)
		# sd.program["sunpos"] = [0,0]
		sd.program["camx"] = cam.x/univars.startdims[0]

			
	def playercode(self):
		"""
			contins all the code that the player needs to function
		"""
		if "player" in om.objects.keys() and "skateboard" in om.objects.keys() and "playersprite" in om.objects.keys():



			#move player
			self.moveplayer()

			#move camera
			campos = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1]]
				

			

			if self.gp("des_vel")[0] > 0:
				self.lookahead = self.unilerp(self.lookahead,200,8,roundto=2)
			elif self.gp("des_vel")[0] < 0:
				self.lookahead = self.unilerp(self.lookahead,-200,8,roundto=2)
			else:
				self.lookahead = self.unilerp(self.lookahead,0,20,roundto=2)

			campos[0] += self.lookahead



			cm.cam_focus_size("playercam",campos,4,univars.pixelscale/7 * 0.5 )

			
			rot = om.objects["playersprite"]["rot"]
			if self.gp("onboard"):
				om.objects["playersprite"]["pos"][0] = om.objects["player"]["pos"][0] - math.sin((rot/180) * math.pi) * 11
				om.objects["playersprite"]["pos"][1] = om.objects["player"]["pos"][1] - math.cos((rot/180) * math.pi) * 11
				if self.gp("des_vel")[0] > 0:
					om.flip("playersprite","right")
				if self.gp("des_vel")[0] < 0:
					om.flip("playersprite","left")



				om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 0]
				om.objects["skateboard"]["rot"] = rot
			else:
				om.objects["playersprite"]["pos"][0] = om.objects["player"]["pos"][0] - math.sin((rot/180) * math.pi) * 0
				om.objects["playersprite"]["pos"][1] = om.objects["player"]["pos"][1] - math.cos((rot/180) * math.pi) * 0
				if self.gp("des_vel")[0] > 0:
					om.flip("playersprite","right")
				if self.gp("des_vel")[0] < 0:
					om.flip("playersprite","left")




			if not abs(self.key["x"]) > 0:
				om.playanim(self.dt,"playersprite","idle",forceplay=True)
			elif not abs(self.gp("des_vel")[0]  - self.key["x"] * 150) < 20:
				om.playanim(self.dt,"playersprite","moveidle",forceplay=True)
			else:
				om.playanim(self.dt,"playersprite","fastidle",forceplay=True)

	def initialiseplayer(self):
		"""
		Initialises the players variables
		"""
		#create the cameras
		cm.addcam("playercam",[8500,608],0.4)
		cm.setcam("playercam")  

		self.lookahead = 100
		om.speed = 1

		#create player
		om.adds("player",[8500,128],"player","player",0,[1,1],400,5)
		om.objects["player"]["rendercond"] = False

		#creates the player sprite you actually see
		om.adds("playersprite",[-1400,400],"player","player",0,[1,1],400,5)
		om.objects["playersprite"]["rendercond"] = True
		om.includeflipping("playersprite")

		#creates the skateboard
		om.adds("skateboard",[-1400,400],"skateboard","skateboard",0,[1,1],400,5)
		om.objects["skateboard"]["rendercond"] = True

		#desired velocity



		self.lastrail = 0

		self.sp("des_vel",[0,0])

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

		self.lastdirslant = "r"

		#previous frames actual velocity
		self.sp("prev_act_vel",[0,0])

		#shidding?
		self.sp("skidding",False)

		self.reclock = 1


		#on skateboard?
		self.sp("onboard",True)


		self.sp("desrot",0)
		self.sp("desmooth",5)


		self.sp("slantdir","r")

		om.set_value("skateboard","fallvalue",5)

		self.sp("thickness",1)

	def moveplayer(self):
		# om.speed = 0.4
		
		# um.showvar("pos",om.objects["player"]["pos"],[0,0])
		collision = om.collide9("player",0,cam,self.dim,ignore= ["playersprite","skateboard"])
		lonepoint1 = om.collidep([om.objects["player"]["pos"][0] + 50,om.objects["player"]["pos"][1] + 10 ],1,32,camera=cam,basecolor=(0,1,0))
		lonepoint2 = om.collidep([om.objects["player"]["pos"][0] - 50,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
		collisionbox = om.collide("player",0,cam,extra=20)
		ground1 = len(collision["botmid"]["inst"]) > 0
		ground2 = len(collision["botleft"]["inst"]) > 0    and not (len(collision["topleft"]["inst"])  > 0  ) and not (len(collision["midleft"]["inst"])  > 0  )
		ground3 = len(collision["botright"]["inst"]) > 0   and not (len(collision["topright"]["inst"]) > 0  ) and not (len(collision["midright"]["inst"]) > 0  )
		ground = ground1 or ground2 or ground3
		instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"] 
		collisionlisttype = [i.type for i in instlist] 
		collisionboxtype = [i.type for i in collisionbox["inst"]] 
		collisionlisttype.append("ground")

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

	


		#Main movement
		if not slanted:
			if slanted == self.lastframeslanted or self.key["jump"]:
				if not rail:
					if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ):
						#IN HERE IS EITHER [NO MIDMID] OR [Yes MIDMID AND GROUND]

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



						


							

						#Skid detection 
						if abs(self.gp("act_vel")[0]  - self.gp("des_vel")[0]) > 50:
							self.sp("skidding",True)
						else:
							self.sp("skidding",False)


						#rerout detection
						if not self.isthere("leftjump") or not self.isthere("rightjump"):
							if not self.sign(self.key["x"]) == self.sign(self.gp("lastx")):
								self.sp("xinit",True)
							self.sp("lastx",self.key["x"])

						#ground detection + falling
						if ground:
							
							self.sp("desrot",0)
							self.sp("mode","grounded")
							self.sp("jumpable",True)
							self.sp("onboard",True)
							self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
							self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
							om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32
						else:
							if self.key["jump"]:
								self.sp("onboard",True)
							if not self.gp("leftwall") or not self.gp("rightwall"):
								self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    self.unilerp(self.gp("des_vel")[1],-130,self.gp("fss"),roundto = 0)   ]     )
								self.sp("mode","in-air")
							else:
								self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    self.unilerp(self.gp("des_vel")[1],-130,8,roundto = 0)   ]     )
								self.sp("mode","in-air")

							if  self.gp("leftwall") or  self.gp("rightwall"):
								self.sp("onboard",True)
							else:
								self.sp("desrot",self.key["x"] * 20)





						#jumping
						if self.key["jump"]:
							self.sp("fss",16)
							self.sp("desmooth",5)
							
							if self.gp("jumpable"):
								#normal
								
								self.sp("jumpable",False)
								self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
								self.sp("mode","in-air")



								#Wall jumping
								if self.key["y"] > 0.4:
									a = 200
								else:
									a = 120
								if self.gp("leftwall"):
									self.deltimer("rightjump")
									self.wait("leftjump",0.1)
									self.sp("jumpable",False)
									self.sp("des_vel",[  self.gp("des_vel")[0] , a     ])
									self.sp("act_vel",[  120 , self.gp("act_vel")[1]     ])
									self.sp("mode","in-air")
								if self.gp("rightwall"):
									self.deltimer("leftjump")
									self.wait("rightjump",0.1)
									self.sp("jumpable",False)
									self.sp("des_vel",[  self.gp("des_vel")[0] , a     ])
									self.sp("act_vel",[  -120 , self.gp("act_vel")[1]     ])
									self.sp("mode","in-air")

						else:
							self.sp("fss",8)

							if self.gp("leftwall") or self.gp("rightwall"):
								self.sp("des_vel",[self.gp("des_vel")[0],self.key["y"] * 100])

							if not ground:
								if self.gp("leftwall"):
									self.sp("desrot",-90)
									self.sp("desmooth",3)

								elif self.gp("rightwall"):
									self.sp("desrot",90)
									self.sp("desmooth",3)

							# else:
							# 	if not ground:
							# 		self.sp("desrot",self.gp("desrot") - self.gp("act_vel")[1]/20 )


						


					
						
						if collision["topmid"]["inst"] and not collision["midmid"]["inst"]:
							self.sp("act_vel",[   self.gp("act_vel")[0] * 1  , -10 ])
							om.objects["player"]["pos"][1] =  collision["topmid"]["inst"][0].realpos[1] + 40
							# self.sp("des_vel",[  self.gp("des_vel")[0] * 1   ,  abs(self.gp("des_vel")[1]) * -1 ])
							self.sp("jumpable",False)

						
						#water skid
						if 0.7 > self.actualwaterheight > 0.5 and not self.key["jump"]:
							if abs(self.gp("act_vel")[0]) >= 110:
								if self.gp("act_vel")[0] > 100:
									parts = [om.objects["player"]["pos"][0] -5,om.objects["player"]["pos"][1] + 9]
								else:
									parts = [om.objects["player"]["pos"][0] -5,om.objects["player"]["pos"][1] + 9]
								vel = [self.gp("act_vel")[0]/self.dim * 4,4]
								pm.particlespawnbluprint(parts,"water",initvel= vel)
								self.sp("act_vel",[   self.gp("act_vel")[0] , 0  ]  ) 
								self.sp("des_vel",[   self.gp("des_vel")[0] , 0  ]  ) 
								om.objects["player"]["pos"][1] = (510.11583 * self.publicvariables["waterh"])+343.6834
								self.sp("jumpable",1)


				else:
					self.sp("jumpable",True)
					railpiece = collisionbox["inst"][0]
					if railpiece.name == "rail":
						railrot = railpiece.rot
					else:
						railrot = railpiece.rot + 45
					if not self.lastrail  == rail or not self.lastdirrail == railrot:
						self.sp("entervel",univars.func.dist([0,0],self.gp("act_vel")) )
						self.sp("dirforrail",self.lastdirslant)
						if self.gp("dirforrail") == "l":
							raildir = 1
						else:
							raildir = -1



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

					# um.showvar("",self.gp("dirforslant"),[0,0])

					if abs(self.key["x"]) > 0.5:
						if self.key["x"] > 0:
							self.sp("dirforrail","l")
							self.sp("entervel",self.gp("entervel") + abs(self.key["x"]/2 ))
						else:
							self.sp("dirforrail","r")
							self.sp("entervel",self.gp("entervel") + abs(self.key["x"]/2 ))

					if self.gp("entervel") > 130:
						self.sp("entervel",130)
					if self.gp("entervel") < -130:
						self.sp("entervel",-130)
	


					if self.gp("dirforrail") == "l":
						raildir = 1
					else:
						raildir = -1

					self.sp("desrot",railrot)
					
					railvel = [  self.gp("entervel") * math.cos((railrot/180) * math.pi) * raildir, self.gp("entervel")  * math.sin((railrot/180) * math.pi) * raildir ]
					self.sp("act_vel",railvel)
					self.sp("des_vel",railvel)
					self.lastdirrail = railrot

					if self.key["jump"]:
						if self.gp("jumpable"):
							if railrot in [0] :
								self.sp("act_vel",[self.gp("act_vel")[0],40])
								self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
								self.sp("mode","in-air")
							if railrot in [45,-45] :
								if raildir == -1:
									self.sp("act_vel",[  self.gp("act_vel")[0] *   self.valsign(railrot)  * 1   ,   40      ])
									self.sp("des_vel",[  self.gp("des_vel")[0] *   self.valsign(railrot)  * 1   ,   150     ])
								else:
									self.sp("act_vel",[  self.gp("act_vel")[0] *   self.valsign(railrot)  * 1   ,   150      ])
									self.sp("des_vel",[  self.gp("des_vel")[0] *   self.valsign(railrot)  * 1   ,   300     ])
							elif railrot in [90,-90] :
								self.sp("act_vel",[  self.valsign(railrot) * self.gp("entervel")* -1 ,self.gp("act_vel")[1]   ] )
								self.sp("des_vel",[  self.valsign(railrot) * self.gp("entervel")* -1,self.gp("des_vel")[1]   ])
								self.sp("mode","in-air")

					parts = om.objects["player"]["pos"]
					vel = [self.gp("act_vel")[0]/7,self.gp("act_vel")[1]/7]
					pm.particlespawnbluprint(parts,"grind",initvel= vel)




						


				if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ) or rail:
					self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
					om.translate(self,"player",self.gp("act_vel"),usedt=1)
					om.objects["playersprite"]["rot"]  =  self.unilerp(om.objects["playersprite"]["rot"],self.gp("desrot"),5,roundto=2) 
						
				


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

		# um.showvar("prevprevpos",self.gp("prevprevpos"),[0,-0.2])
			# if len(collision["topleft"]["inst"]) > 0 or len(collision["topright"]["inst"]) > 0 or len(collision["midleft"]["inst"]) > 0 or len(collision["midright"]["inst"]) > 0:
			# 	self.sp("act_vel",[   self.gp("prev_act_vel")[0] * -1  ,  self.gp("prev_act_vel")[1] * -1 ])
			# 	self.sp("des_vel",[   self.gp("prev_des_vel")[0] * -1  ,  self.gp("prev_des_vel")[1] * -1 ])
			# else:
			# 	self.sp("act_vel",[   self.gp("prev_act_vel")[0] * 1  ,  self.gp("prev_act_vel")[1] * -1 ])
			# 	self.sp("des_vel",[   self.gp("prev_des_vel")[0] * 1  ,  self.gp("prev_des_vel")[1] * -1 ])
			# self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
			# om.translate(self,"player",self.gp("act_vel"),usedt=1)
				
		


		if  -5 > self.gp("desrot") > 5:
			self.sp("desrot",0)

		
		self.lastrail = rail

	



	def unilerp(self,val,max,sm,roundto = None):
		"""
			a lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int
		"""
		return univars.func.lerp(val,max,              (  (sm/om.speed) / self.dt)*1.5              ,roundto = roundto)
	
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












	def cond(self,id,info):
		"""id -> the id   info -> the info for the id"""
		# if info["name"] == "player":
		# 	om.playanim(self.dt,id,"fastidle",1)












rm = Game(univars.screencol,fm)
if univars.mode == "opt":
	def main():
		rm = Game(univars.screencol,fm)
		rm.Run()

	if __name__ == "__main__":
		cProfile.run('main()', sort='cumtime')
else:
	rm.Run()
 