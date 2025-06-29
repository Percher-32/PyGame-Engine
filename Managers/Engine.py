import Gamemanager as Gamemananager
import univars as univars




em = Gamemananager.em
tm = Gamemananager.tm
fm = Gamemananager.fm
om = Gamemananager.om
Tiled = Gamemananager.Tiled
cam =Gamemananager.cam
cm = Gamemananager.cm
sm = Gamemananager.sm
um = Gamemananager.um





class Runchinld(Gamemananager.GameManager):	
	def __init__(self,screen,fm):
		super().__init__(screen,fm)

	def initial(self):
		self.defs()
		self.a = 0
		
		
		# om.saveanim("bird","fly",[{"0":0,"10":1,"19":0},False])
		# om.loadanim("bird","fly")
		# om.saveanim("bird","fly2",[{"0":0,"1":1,"2":0,"3":1,"5":0,"6":1,"7":0,"8":1},False])
		# om.loadanim("bird","fly2")
		if "test" in self.states:
			cm.addcam("playercam",[0,0],0.4)
			cm.setcam("playercam")
			om.adds("player",[0,0],"enemy","player",0,[1,1],400,5)
			self.sp("velx",0)
			self.sp("vely",0)
			self.sp("speedupy",14)
			self.sp("jump",0)
			self.sp("mode","falling or stat")

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
		om.speed = 1
		# fm.showfps = 0
		# self.maxbg = [univars.realscreeen.get_width(),univars.realscreeen.get_height()]
		# if um == "default" or "test2":
		# 	um.elements["bg2"]["dimension"] = univars.func.lerp(um.elements["bg2"]["dimensions"],self.maxbg,1)

		# if self.ondone("intro"):
		# 	um.state = "test2"
		# if um.state == "test2":
		# 	um.elements["playbutton"]["pos"] = univars.func.lerp(um.elements["playbutton"]["pos"],self.enppos,4)
		# 	um.elements["bg"]["dimension"] = univars.func.lerp(um.elements["bg"]["dimensions"],[univars.realscreeen.get_width() - 200,univars.realscreeen.get_height() - 200],4)
		# if um.elements["playbutton"]["click"]:
		# 	um.state = "gameplay"
		# if  um.state == "gameplay":
		# 	um.elements["playbutton"]["pos"] = univars.func.lerp(um.elements["playbutton"]["pos"],[0,-2],4)
		# 	um.elements["bg"]["dimension"] = univars.func.lerp(um.elements["bg"]["dimensions"],[univars.realscreeen.get_width() - 200,0],2)
		# 	um.elements["bg2"]["dimension"] = univars.func.lerp(um.elements["bg2"]["dimensions"],[0,0],1)
		

		if "test" in self.states:
			c = om.collide9("player",0,cam,self.dim)
			self.camfoc()
			self.gravity(c)
			self.playermovex(c)

	def camfoc(self):
		cm.cam_focus_size("playercam",om.objects["player"]["pos"],4,0.4)
			
	def playermovex(self,c):
		a = c["botmid"]["inst"]
		b = c["botleft"]["inst"]
		d = c["botright"]["inst"]

		if len(a) > 0:
			normt = True
			norm = a
		elif len(d) > 0:
			normt = True
			norm = d
		elif len(b) > 0:
			normt = True
			norm = b
		else:
			normt = False
			norm = None
		self.sp("maxx",self.key["x"] * 40)
		if normt:
			self.sp("speedup",12)
		else:
			self.sp("speedup",16)
		
		if normt:
			if self.key["x"] == 0:
				if self.key["y"] == -1:
					self.sp("speedup",7)
		if abs(self.gp("velx")) < 2:
			self.sp("velx",0)
			
		self.sp("velx",int(round(univars.func.lerp(self.gp("velx"),self.gp("maxx"),self.gp("speedup")))))
		om.objects["player"]["pos"][0] += self.gp("velx")

	def gravity(self,c):
		if self.key["action"]:
			if self.gp("jump"):
				self.sp("mode","jumping")
				self.sp("speedjump",10)
				self.sp("jumph",10)
				self.sp("jumpd",1)
				self.sp("maxh",30)

		a = c["botmid"]["inst"]
		b = c["botleft"]["inst"]
		d = c["botright"]["inst"]

		if len(a) > 0:
			normt = True
			norm = a
		elif len(d) > 0:
			normt = True
			norm = d
		elif len(b) > 0:
			normt = True
			norm = b
		else:
			normt = False
			norm = None

		if self.gp("mode") == "falling or stat":
			if normt:
				self.sp("maxy",0)
				self.sp("vely",0)
				# if not len(c["midleft"]["inst"]) or not len(c["midright"]["inst"]):
				om.objects["player"]["pos"][1] = norm[0].realpos[1] - self.dim
				if len(c["midmid"]["inst"]):
					om.objects["player"]["pos"][1] -= self.dim
				self.sp("jump",1)
			else:
				self.sp("maxy",-40)
				self.sp("vely",univars.func.lerp(self.gp("vely"),self.gp("maxy"),self.gp("speedupy")))
				om.objects["player"]["pos"][1] -= self.gp("vely")
		elif self.gp("mode") == "jumping":
			if not self.gp("vely") > self.gp("maxh") and not self.gp("jumph") < 0:
				self.sp("vely",self.gp("vely") + self.gp("jumph"))
				self.sp("maxy",-20)
				if self.key["action"]:
					self.sp("vely",self.gp("vely") + 90)
					self.sp("maxh",self.gp("vely"))
					self.sp("jumph",20)
				self.sp("vely",univars.func.lerp(self.gp("vely"),self.gp("maxy"),self.gp("speedupy")))
				om.objects["player"]["pos"][1] -= self.gp("vely")
				self.sp("jumph",self.gp("jumph") - self.gp("jumpd"))

			else:
				self.sp("jump",0)
				self.sp("mode","falling or stat")

	def cond(self,obj,info):
		"""obj -> the id   info -> the info for the id"""
		if info["name"] == "bird":
			om.playanim(fm.dt,obj,"fly2")
			om.translate(self,obj,[4,4])




rm = Runchinld((univars.screencol),fm)
rm.Run()