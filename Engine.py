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

	def onreload(self):
		self.a = 0
		# bg.addbackground("test2")
		# bg.addbackgrounditem("black","test2",[0,-40]                ,surf = "mount",dimensions=[500*4,250*4],layer = 0.2,infiniscroll=True)
		
		if "game" == self.states:

			#create the cameras
			cm.addcam("playercam",[0,0],0.4)
			cm.setcam("playercam")  

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
		# pm.particlespawn("circle",[0,0],[[-5,5],[-5,5]],(0,100,255),[0,0],[0,-1],5,0.001,alpha=300,alphadec=4,divergencepos=[[-1000,1000],[0,0]],ntimes=1)
		# cm.setcond("def","pos",[random.randint(-10000,10000),random.randint(-10000,10000)])


		if "game" == self.states:
			self.playercode()

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
			# if self.gp("des_vel")[1] > 0:
			# 	campos[1] += self.lookahead
			# elif self.gp("des_vel")[1] < 0:
			# 	campos[1] -= self.lookahead



			# cm.cam_focus_size("playercam",campos,4,univars.pixelscale/7 * ((-0.001 *      univars.func.dist([0,0],self.gp("act_vel"))                 ) + 0.5) )
			cm.cam_focus_size("playercam",campos,4,univars.pixelscale/7 * 0.5 )
			# cm.setcond("playercam","pos",[cm.getcam("playercam","pos")[0] + (self.key["x"] * 20) , cm.getcam("playercam","pos")[1] ])

			

			#update player sprite ansd skateboards position
			# particlepos = [om.objects["player"]["pos"][0] - 15,om.objects["player"]["pos"][1]]
			# pm.particlespawnbluprint(particlepos,"grind")
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

		self.lookahead = 100
		om.speed = 1

		#create player
		om.adds("player",[0,250],"player","player",0,[1,1],400,5)
		om.objects["player"]["rendercond"] = False

		#creates the player sprite you actually see
		om.adds("playersprite",[-1400,400],"player","player",0,[1,1],400,5)
		om.objects["playersprite"]["rendercond"] = True
		om.includeflipping("playersprite")

		#creates the skateboard
		om.adds("skateboard",[-1400,400],"skateboard","skateboard",0,[1,1],400,5)
		om.objects["skateboard"]["rendercond"] = True

		#desired velocity

		self.sp("des_vel",[0,0])

		#actual velocity
		self.sp("act_vel",[0,0])

		#smoothing
		self.sp("smoothing",2)

		#modes
		self.sp("mode","grounded")

		#able to jump?
		self.sp("jumpamble",False)

		#fall speed smoothing
		self.sp("fss",8)

		self.lastframeslanted = False
		self.gate = "r"

		self.lastdirslant = "r"

		#previous frames actual velocity
		self.sp("prev_act_vel",[0,0])

		#shidding?
		self.sp("skidding",False)


		#on skateboard?
		self.sp("onboard",True)


		self.sp("desrot",0)
		self.sp("desmooth",5)


		self.sp("slantdir","r")

		om.set_value("skateboard","fallvalue",5)

       
	def sign(self,value):
		"""
		 	returns + or -
		"""
		if abs(value) == value:
			return "+"
		else:
			return "-"

	def moveplayer(self):
		# om.speed = 0.4
		collision = om.collide9("player",1,cam,self.dim)
		lonepoint = om.collidep([om.objects["player"]["pos"][0] + 40,om.objects["player"]["pos"][1] - 32 ],0,32)
		collisionbox = om.collide("player",1,cam,extra=10)
		ground1 = len(collision["botmid"]["inst"]) > 0
		ground2 = len(collision["botleft"]["inst"]) > 0 and not (len(collision["midleft"]["inst"]) > 0)   and not (len(collision["topleft"]["inst"]) > 0)
		ground3 = len(collision["botright"]["inst"]) > 0 and not (len(collision["midright"]["inst"]) > 0)  and not (len(collision["topright"]["inst"]) > 0)
		ground = ground1 or ground2 or ground3
		instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"] 
		collisionlisttype = [i.type for i in instlist] 
		collisionboxtype = [i.type for i in collisionbox["inst"]] 
		# collisionlisttype.append(None)
	
		# show the mode
		# um.showvar("des_vel",self.gp("des_vel"),[0,-0.7])
		if self.dt == 0 or self.dt > 10:
			self.dt = 1

		# print(collisionboxtype)
		if len(collisionboxtype) > 0:
			if "slantl"  in collisionboxtype or "slantr" in collisionboxtype:
				slanted = True
				if "slantr" in collisionboxtype:
					if self.gp("act_vel")[0] < 0:
						if ground2:
							slanted = False
				else:
					if self.gp("act_vel")[0] > 0:
						if len(lonepoint["inst"]) > 0:
							slanted = False
							print("back")
				# if self.gp("act_vel")[0] > 0 :
				# 	if ground2:
				# 		slanted = False
				
			else:
				slanted = False	
		else:
			slanted = False

		um.showvar("slanted",slanted,[0,-0.5])

		#Main movement
		if not slanted:
			if not len(collision["midmid"]["inst"]) > 0:
				if slanted == self.lastframeslanted or self.key["jump"]:
					#IN HERE IS EITHER [NO MIDMID] OR [Yes MIDMID AND GROUND]

					#x dir movement
					if abs(self.key["x"]) > 0:
						if self.isthere("leftjump"):
							self.key["x"] = 1
						if self.isthere("rightjump"):
							self.key["x"] = -1 * 1

						if self.gp("xinit"):
							self.sp("xinit",False)
							self.sp("des_vel",[self.key["x"] * 100,self.gp("des_vel")[1]])

						


						self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * 120,30 )              ,    self.gp("des_vel")[1]   ])
					else:
						self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
						self.sp("xinit",True)



				

					#Wall clinging
					if len(collision["topleft"]["inst"]) > 0 :
						if  collision["topleft"]["inst"][0].type == "ground":
							self.sp("leftwall",True)
							self.sp("jumpable",True)	
							om.objects["player"]["pos"][0] = collision["topleft"]["inst"][0].realpos[0] + 30

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


					if len(collision["topright"]["inst"]) > 0 :
						if  collision["topright"]["inst"][0].type == "ground":
							self.sp("rightwall",True)
							self.sp("jumpable",True)	
							om.objects["player"]["pos"][0] = collision["topright"]["inst"][0].realpos[0] -32
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
							elif self.key["y"] < -0.2:
								a = -150
							else:
								a = 120
							if self.gp("leftwall"):
								self.deltimer("rightjump")
								self.wait("leftjump",0.1)
								self.sp("jumpable",False)
								self.sp("des_vel",[  self.gp("des_vel")[0] , a     ])
								self.sp("act_vel",[  100 , self.gp("act_vel")[1]     ])
								self.sp("mode","in-air")
							if self.gp("rightwall"):
								self.deltimer("leftjump")
								self.wait("rightjump",0.1)
								self.sp("jumpable",False)
								self.sp("des_vel",[  self.gp("des_vel")[0] , a     ])
								self.sp("act_vel",[  -100 , self.gp("act_vel")[1]     ])
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


					


				
					
					if collision["topmid"]["inst"]:
						if self.gp("leftwall"):
							om.objects["player"]["pos"][0] += 30
							om.objects["player"]["pos"][1] += abs(self.gp("act_vel")[1])
						elif self.gp("rightwall"):
							om.objects["player"]["pos"][0] -= 35
							om.objects["player"]["pos"][1] += abs(self.gp("act_vel")[1])
						else:
							om.objects["player"]["pos"][1] += 35 + abs(self.gp("act_vel")[1])
							self.sp("des_vel",[self.gp("des_vel")[0],20 + abs(self.gp("act_vel")[1])])
							self.sp("jumpable",False)
					else:
						#move
						
						om.objects["playersprite"]["rot"]  =  self.unilerp(om.objects["playersprite"]["rot"],self.gp("desrot"),5,roundto=2) 
						self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
						om.translate(self,"player",self.gp("act_vel"),usedt=1)
						self.sp("prev_act_vel",self.gp("act_vel"))
						self.sp("prev_des_vel",self.gp("des_vel"))
						if not self.gp("onboard"):
							if om.get_value("skateboard","fallvalue")< 20:
								om.set_value("skateboard","fallvalue",om.get_value("skateboard","fallvalue") - 2* self.dt)
							om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 0]
							om.translate(self,"skateboard",[0,om.get_value("skateboard","fallvalue")])
						else:
							om.set_value("skateboard","fallvalue",5)

					


					
						#prevent no-clip
						if self.gp("mode") == "grounded":
							if "ground" in collisionlisttype:
								self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
								self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
								om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32

				else:
					if self.gp("slantdir") == "r":
						if self.lastdirslant == "r":
							om.translate(self,"player",[100,40])
					if self.gp("slantdir") == "l":
						if self.lastdirslant == "r":
							om.translate(self,"player",[-100,40])




			else:
				if len(collision["midmid"]["inst"]) > 0:
					if len(collision["topleft"]["inst"]) > 0 or len(collision["topright"]["inst"]) > 0:
						self.sp("act_vel",[   self.gp("prev_act_vel")[0] * -1  ,  self.gp("prev_act_vel")[1] * -1 ])
					else:
						self.sp("act_vel",[   self.gp("prev_act_vel")[0] * 1  ,  self.gp("prev_act_vel")[1] * -1 ])
					self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
					om.translate(self,"player",self.gp("act_vel"))
		else:
			if abs(self.key["x"]) > 0:
				if self.key["x"] > 0:
					self.lastdirslant = "l"
				else:
					self.lastdirslant = "r"
			if self.key["jump"]:
				self.sp("fss",16)
				self.sp("desmooth",5)
		
				#normal
				self.sp("jumpable",False)
				self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
				self.sp("mode","in-air")
				self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
				om.translate(self,"player",self.gp("act_vel"),usedt=1)
			
			if "slantr" in collisionboxtype:
				self.sp("slantdir","r")
				if not slanted == self.lastframeslanted:
					# if not ground:
					index = collisionboxtype.index("slantr")
					om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] - 20,collisionbox["inst"][index].realpos[1] - 20]
						# else:
						# 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
				else:
					if abs(self.key["x"]) > 0:
						if self.key["x"] > 0:
							self.lastdirslant = "r"
						else:
							self.lastdirslant = "l"
						self.sp("des_vel",[         self.key["x"] * 70             ,    self.gp("des_vel")[1]   ])
					else:
						self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
					self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
					if not self.key["jump"]:
						actvel = [self.gp("act_vel")[0],self.gp("act_vel")[0]]
					else:
						actvel = [-1 * self.gp("act_vel")[0],abs(self.gp("act_vel")[1])]
					om.translate(self,"player",actvel,usedt=1)
					self.sp("desrot",45) 
			else:
				self.sp("slantdir","l")
				if not slanted == self.lastframeslanted:
					index = collisionboxtype.index("slantl")
					# if not ground2:
					om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] +16,collisionbox["inst"][index].realpos[1] -20]
						# else:
						# 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
				else:
					if abs(self.key["x"]) > 0:
						self.sp("des_vel",[         self.key["x"] * 70             ,    self.gp("des_vel")[1]   ])
					else:
						self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
					self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
					if not self.key["jump"]:
						actvel = [self.gp("act_vel")[0],-1 * self.gp("act_vel")[0]]
					else:
						actvel = [self.gp("act_vel")[0], self.gp("act_vel")[1]]
					om.translate(self,"player",actvel,usedt=1)
					self.sp("desrot",-45)
			om.objects["playersprite"]["rot"]  =  self.unilerp(om.objects["playersprite"]["rot"],self.gp("desrot"),5,roundto=2) 
			
			



		if  -5 > self.gp("desrot") > 5:
			self.sp("desrot",0)

		self.lastframeslanted = slanted


	
	def unilerp(self,val,max,sm,roundto = None):
		"""
			a lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int
		"""
		return univars.func.lerp(val,max,              (  (sm/om.speed) / self.dt)*1.5              ,roundto = roundto)
	


















	def cond(self,id,info):
		"""id -> the id   info -> the info for the id"""
		if info["name"] == "player":
			om.playanim(self.dt,id,"fastidle",1)












rm = Game(univars.screencol,fm)
if univars.mode == "opt":
	def main():
		rm = Game(univars.screencol,fm)
		rm.Run()

	if __name__ == "__main__":
		cProfile.run('main()', sort='cumtime')
else:
	rm.Run()
 