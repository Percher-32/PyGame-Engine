import Gamemanager as Gamemananager
import univars as univars
import cProfile
import sys


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


class Runchinld(Gamemananager.GameManager):	
	def __init__(self,screen,fm):
		super().__init__(screen,fm)

	def onreload(self):
		self.a = 0
		# bg.background = "test1"
		bg.addbackground("test2")
		bg.addbackgrounditem("black","test2",[0,-40],surf = "mount",dimensions=[500*2.3,250*2.3],layer = 20)
		
		
		if "test" in self.states:

			#create the cameras
			cm.addcam("playercam",[0,0],0.4)
			cm.setcam("playercam")  

			#initialise player and all its variables
			self.initialiseplayer()

			


			


	def commence(self):
		# self.wait("intro",1)
		# self.maxbg = [univars.realscreeen.get_width(),univars.realscreeen.get_height()]
		# um.addrect(self.maxbg,["default","test2","gameplay"],(0,0),"bg2",univars.theme["dark"],255)
		# um.addrect([univars.realscreeen.get_width() - 200,0],["default","test2","gameplay"],(0,0),"bg",univars.theme["mid"],100)
		# um.addbutton((100,50),["default","test2","gameplay"],(0,-2),"playbutton",univars.theme["dark"],255)
		# um.addtext("playtext","play",univars.defont,(0,-1),univars.theme["semibright"],40,["default"])
		# um.bindtobutton("playtext","playbutton")
		# um.addglide("playbutton",univars.sizes["mediumbutton"],univars.sizes["largebutton"])
		# self.enppos = [0,-0.5]
		pass

	def update(self):
		bg.background = "test2"

		if "test" in self.states:
			self.playercode()




			
	def playercode(self):
		"""
			contins all the code that the player needs to function
		"""
		if "player" in om.objects.keys() and "skateboard" in om.objects.keys() and "playersprite" in om.objects.keys():
			#move camera
			cm.cam_focus_size("playercam",om.objects["player"]["pos"],4,univars.pixelscale/7 * ((-0.001 * abs(self.gp("act_vel")[0])) + 0.5) )

			um.showvar("av0",self.gp("act_vel")[0],[0,-0.7])


			#move player
			self.moveplayer()

			#update player sprite ansd skateboards position
			if self.gp("onboard"):
				om.objects["playersprite"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 11]
				om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 0]


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

		
		om.speed = 1

		#create player
		om.adds("player",[0,-400],"player","player",0,[1,1],400,5)
		om.objects["player"]["rendercond"] = False

		#creates the player sprite you actually see
		om.adds("playersprite",[0,-400],"player","player",0,[1,1],400,5)
		om.objects["playersprite"]["rendercond"] = True
		om.includeflipping("playersprite")

		#creates the skateboard
		om.adds("skateboard",[0,-400],"skateboard","skateboard",0,[1,1],400,5)
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


		#previous frames actual velocity
		self.sp("prev_act_vel",[0,0])

		#shidding?
		self.sp("skidding",False)


		#on skateboard?
		self.sp("onboard",True)


	def moveplayer(self):
		collision = om.collide9("player",0,cam,self.dim)
		ground1 = len(collision["botmid"]["inst"]) > 0
		ground2 = len(collision["botleft"]["inst"]) > 0 and not (len(collision["midleft"]["inst"]) > 0)
		ground3 = len(collision["botright"]["inst"]) > 0 and not (len(collision["midright"]["inst"]) > 0)
		ground = ground1 or ground2 or ground3
		instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"] 

		# show the mode
		# um.showvar("des_vel",self.gp("des_vel"),[0,-0.7])
		
		#get out of being stuck
		if not  om.collide9("player",0,cam,self.dim)["midmid"]["inst"]:
			#IN HERE IS EITHER NO MIDMID OR MIDMID AND GROUND




			#x dir movement
			if abs(self.key["x"]) > 0:
				if self.gp("xinit"):
					self.sp("xinit",False)
					self.sp("des_vel",[self.key["x"] * 100,self.gp("des_vel")[1]])
				self.sp("des_vel",[  univars.func.lerp(self.gp("des_vel")[0],self.key["x"] * 150,(30/om.speed))    ,    self.gp("des_vel")[1]   ])
			else:
				self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
				self.sp("xinit",True)



		

			#Wall clinging
			if len(collision["topleft"]["inst"]) > 0 :
				self.sp("jumpable",True)	
				om.objects["player"]["pos"][0] = collision["topleft"]["inst"][0].realpos[0] + 32
				if self.gp("des_vel")[0] < 0:
					self.sp("des_vel",[0,0])
				if self.gp("act_vel")[0] < 0:
					self.sp("act_vel",[0,0])
			if len(collision["topright"]["inst"]) > 0 :
				self.sp("jumpable",True)	
				om.objects["player"]["pos"][0] = collision["topright"]["inst"][0].realpos[0] - 32
				if self.gp("des_vel")[0] > 0:
					self.sp("des_vel",[0,0])
				if self.gp("act_vel")[0] > 0:
					self.sp("act_vel",[0,0])
				

			#Skid detection
			if abs(self.gp("act_vel")[0]  - self.gp("des_vel")[0]) > 50:
				self.sp("skidding",True)
			else:
				self.sp("skidding",False)


			#rerout detection
			if abs(self.key["x"] * 100  - self.gp("des_vel")[0]) > 200:
				self.sp("xinit",True)

			#ground detection + falling
			if ground:
				self.sp("mode","grounded")
				self.sp("jumpable",True)	
			else:
				if not len(collision["midright"]["inst"]) > 0  or len(collision["midleft"]["inst"]) > 0:
					self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    univars.func.lerp(self.gp("des_vel")[1],-130,(self.gp("fss")/om.speed),roundto = 0)   ]     )
					self.sp("mode","in-air")
				else:
					self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    univars.func.lerp(self.gp("des_vel")[1],-60,(self.gp("fss")/om.speed),roundto = 0)   ]     )
					self.sp("mode","in-air")


			#jumping
			if self.key["action"]:
				self.sp("fss",16)
				if self.gp("jumpable"):
					#normal
					self.sp("jumpable",False)
					self.sp("des_vel",[  self.gp("des_vel")[0] , 200     ])
					self.sp("mode","in-air")



					#Wall jumping
					if len(collision["midleft"]["inst"]) > 0 :
						self.sp("jumpable",True)
						self.sp("des_vel",[  self.gp("des_vel")[0] , 300     ])
						self.sp("act_vel",[  100 , self.gp("act_vel")[1]     ])
						self.sp("mode","in-air")
					if len(collision["midright"]["inst"]) > 0 :
						self.sp("jumpable",True)
						self.sp("des_vel",[  self.gp("des_vel")[0] , 300     ])
						self.sp("act_vel",[  -100 , self.gp("act_vel")[1]     ])
						self.sp("mode","in-air")
			else:
				self.sp("fss",8)


		


					

			#move
			univars.func.lerp(self.gp("act_vel"),self.gp("des_vel"),(8/om.speed),roundto = 2)
			om.translate(self,"player",self.gp("act_vel"))
			self.sp("prev_act_vel",self.gp("act_vel"))
			self.sp("prev_des_vel",self.gp("des_vel"))


			
			#prevent no-clip
			if self.gp("mode") == "grounded":
				self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
				self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])

				om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32

			collision = om.collide9("player",0,cam,self.dim)["midmid"]["inst"]
		else:
			if len(collision["topleft"]["inst"]) > 0 or len(collision["topright"]["inst"]) > 0:
				self.sp("act_vel",[   self.gp("prev_act_vel")[0] * -1  ,  self.gp("prev_act_vel")[1] * -1 ])
			else:
				self.sp("act_vel",[   self.gp("prev_act_vel")[0] * 1  ,  self.gp("prev_act_vel")[1] * -1 ])
			# self.sp("des_vel",[   self.gp("prev_des_vel")[0] * -1  ,  self.gp("prev_des_vel")[1] * -1 ])
			#move
			univars.func.lerp(self.gp("act_vel"),self.gp("des_vel"),(8/om.speed),roundto = 2)
			om.translate(self,"player",self.gp("act_vel"))


		


















	def cond(self,obj,info):
		"""obj -> the id   info -> the info for the id"""
		if info["name"] == "bird":
			om.translate(self,obj,[5,5])
			om.playanim(self.dt,obj,"fly")















rm = Runchinld(univars.screencol,fm)
if univars.mode == 0:
	def main():
		rm = Runchinld(univars.screencol,fm)
		rm.Run()

	if __name__ == "__main__":
		cProfile.run('main()', sort='cumtime')
else:
	rm.Run()
