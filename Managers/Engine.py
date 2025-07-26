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
			om.speed = 1
			self.playercode()





	def initialiseplayer(self):
		#create player
		om.adds("player",[0,-400],"enemy","player",0,[1,1],400,5)

		#desired velocity
		self.sp("des_vel",[0,0])

		#actual velocity
		self.sp("act_vel",[0,0])

		#smoothing
		self.sp("smoothing",2)

		#modes
		self.sp("mode","grounded")

			
	def playercode(self):
		"""
			contins all the code that the player needs to function
		"""
		if "player" in om.objects.keys():
			
			cm.cam_focus_size("playercam",om.objects["player"]["pos"],4,0.4)
			self.moveplayer()


	def moveplayer(self):
		collision = om.collide9("player",1,cam,self.dim)
		ground1 = len(collision["botmid"]["inst"]) > 0
		ground2 = len(collision["botleft"]["inst"]) > 0 and not (len(collision["midleft"]["inst"]) > 0)
		ground3 = len(collision["botright"]["inst"]) > 0 and not (len(collision["midright"]["inst"]) > 0)
		ground = ground1 or ground2 or ground3
		instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"] 

		#show the mode
		um.showvar("mode",self.gp("mode"),[-0.8,-0.7])

		#show the desvel
		um.showvar("desvel",self.gp("des_vel"),[-0.4,-0.7])

		#show the ground cond
		um.showvar("1,2,3",str(ground1) +  " " + str(ground2) + " " +  str(ground3) ,[0,-0.7])


		#show the ground cond
		um.showvar("array", [self.key["x"] , self.key["y"]] ,[0.4,-0.7])

		if not (len(collision["midleft"]["inst"]) > 0) or (len(collision["midright"]["inst"]) > 0):
			if abs(self.key["x"]) > 0:
				self.sp("des_vel",[  self.key["x"] * 100    ,    self.gp("des_vel")[1]   ])
			else:
				self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])

		else:
			if abs(self.key["x"]) > 0:
				self.sp("act_vel",[   self.gp("act_vel")[0] , self.key["y"] * 100       ])
			else:
				self.sp("act_vel",[ self.gp("act_vel")[1] ,  0       ])


			if len(collision["midleft"]["inst"]) > 0 :
				om.objects["player"]["pos"][1] = collision["midleft"]["inst"][0].realpos[0] + 32
				self.sp("act_vel",[  0    ,    self.gp("act_vel")[1]   ])
				if self.gp("des_vel")[0] < 0:
					self.sp("des_vel",[0,0])
				if self.gp("act_vel")[0] < 0:
					self.sp("act_vel",[0,0])


		
		if "x" in self.lastkey.keys():
			if abs(self.gp("act_vel")[0]  - self.gp("des_vel")[0]) > 50:
				print("sskidd")




		

		
		if ground:
			self.sp("mode","grounded")
			if self.key["action"]:
				self.sp("des_vel",[  self.gp("des_vel")[0] , 200     ])
				self.sp("mode","in-air")
		else:
			if not self.gp("mode") == "jumping":
				self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    univars.func.lerp(self.gp("des_vel")[1],-70,10,roundto = 0)   ]     )
				self.sp("mode","in-air")





		#move
		univars.func.lerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
		om.translate(self,"player",self.gp("act_vel"))

		if self.gp("mode") == "grounded":
			self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
			self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
			while om.collide9("player",0,cam,self.dim)["midmid"]["inst"]:
				om.objects["player"]["pos"][1] -= 64

			om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32



		





	# def playermovex(self,c):
	# 	a = c["botmid"]["inst"]
	# 	b = c["botleft"]["inst"]
	# 	d = c["botright"]["inst"]

	# 	if len(a) > 0:
	# 		normt = True
	# 		norm = a
	# 	elif len(d) > 0:
	# 		normt = True
	# 		norm = d
	# 	elif len(b) > 0:
	# 		normt = True
	# 		norm = b
	# 	else:
	# 		normt = False
	# 		norm = None
	# 	self.sp("maxx",self.key["x"] * 40)
	# 	if normt:
	# 		self.sp("speedup",12)
	# 	else:
	# 		self.sp("speedup",16)
		
	# 	if normt:
	# 		if self.key["x"] == 0:
	# 			if self.key["y"] == -1:
	# 				self.sp("speedup",7)
	# 	if abs(self.gp("velx")) < 2:
	# 		self.sp("velx",0)
			
	# 	self.sp("velx",int(round(univars.func.lerp(self.gp("velx"),self.gp("maxx"),self.gp("speedup")))))
	# 	om.objects["player"]["pos"][0] += self.gp("velx")

	# def gravity(self,c):
	# 	if self.key["action"]:
	# 		if self.gp("jump"):
	# 			self.sp("mode","jumping")
	# 			self.sp("speedjump",10)
	# 			self.sp("jumph",10)
	# 			self.sp("jumpd",1)
	# 			self.sp("maxh",30)

	# 	a = c["botmid"]["inst"]
	# 	b = c["botleft"]["inst"]
	# 	d = c["botright"]["inst"]

	# 	if len(a) > 0:
	# 		normt = True
	# 		norm = a
	# 	elif len(d) > 0:
	# 		normt = True
	# 		norm = d
	# 	elif len(b) > 0:
	# 		normt = True
	# 		norm = b
	# 	else:
	# 		normt = False
	# 		norm = None

	# 	if self.gp("mode") == "falling or stat":
	# 		if normt:
	# 			self.sp("maxy",0)
	# 			self.sp("vely",0)
	# 			# if not len(c["midleft"]["inst"]) or not len(c["midright"]["inst"]):
	# 			om.objects["player"]["pos"][1] = norm[0].realpos[1] - self.dim
	# 			if len(c["midmid"]["inst"]):
	# 				om.objects["player"]["pos"][1] -= self.dim
	# 			self.sp("jump",1)
	# 		else:
	# 			self.sp("maxy",-40)
	# 			self.sp("vely",univars.func.lerp(self.gp("vely"),self.gp("maxy"),self.gp("speedupy")))
	# 			om.objects["player"]["pos"][1] -= self.gp("vely")
	# 	elif self.gp("mode") == "jumping":
	# 		if not self.gp("vely") > self.gp("maxh") and not self.gp("jumph") < 0:
	# 			self.sp("vely",self.gp("vely") + self.gp("jumph"))
	# 			self.sp("maxy",-20)
	# 			if self.key["action"]:
	# 				self.sp("vely",self.gp("vely") + 90)
	# 				self.sp("maxh",self.gp("vely"))
	# 				self.sp("jumph",20)
	# 			self.sp("vely",univars.func.lerp(self.gp("vely"),self.gp("maxy"),self.gp("speedupy")))
	# 			om.objects["player"]["pos"][1] -= self.gp("vely")
	# 			self.sp("jumph",self.gp("jumph") - self.gp("jumpd"))

	# 		else:
	# 			self.sp("jump",0)
	# 			self.sp("mode","falling or stat")
















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
