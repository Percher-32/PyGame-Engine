import Gamemanager as Gamemananager
import univars as univars
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



class Runchinld(Gamemananager.GameManager):	
	def __init__(self,screen,fm):
		super().__init__(screen,fm)

	def initial(self):
		self.defs()
		om.adds("player",[0,0],"enemy","player",0,[1,1],400,5)
		if "test" in self.states:
			cm.addcam("playercam",[0,0],0.4)
			cm.setcam("playercam")
			om.adds((cam.x,cam.y),"enemy","player","player",0,[32,32],1000,1)
			om.objects["player"][8] = 4
			self.sp("velx",0)
			self.sp("vely",0)
			self.sp("speedupy",14)
			self.sp("jump",0)
			self.sp("mode","norm")

	def update(self):
		om.collide("player",True,cam)
		if "test" in self.states:
			ib = om.collideinst9b("player",univars.instables,0,cam,4,self.dim)
			i = om.collideinst9("player",univars.instables,  0,cam,4,self.dim)
			cb = om.collide9b("player",["grass","dirt"],     0,cam,4,self.dim)
			c = om.collide9("player",["grass","dirt"],       0,cam,4,self.dim)
			self.camfoc()
			self.gravity(ib,i,cb,c)
			self.playermovex(ib,i,cb,c)

	def camfoc(self):
		cm.cam_focus_size("playercam",om.objects["player"][0],4,0.3)
			
	def playermovex(self,ib,i,cb,c):
		self.sp("maxx",self.key["x"] * 40)
		if ib["botmid"]:
			self.sp("speedup",10)
		else:
			self.sp("speedup",25)
		self.sp("velx",univars.func.lerp(self.gp("velx"),self.gp("maxx"),self.gp("speedup")))
		om.objects["player"][0][0] += self.gp("velx")

	def gravity(self,ib,i,cb,c):
		if self.key["action"]:
			if self.gp("jump"):
				self.sp("mode","jumping")
				self.sp("speedjump",5)
				self.sp("jumph",20)
				self.sp("jumpd",1)
				self.sp("maxh",50)
		if self.gp("mode") == "norm":
			if ib["botmid"]:
				self.sp("maxy",0)
				self.sp("vely",0)
				if not ib["midleft"] or not ib["midright"]:
					om.objects["player"][0][1] = i["botmid"][0].realestpos[1] - self.dim
				if ib["midmid"]:
					om.objects["player"][0][1] -= self.dim
				self.sp("jump",1)
			else:
				self.sp("maxy",-40)
				self.sp("vely",univars.func.lerp(self.gp("vely"),self.gp("maxy"),self.gp("speedupy")))
				om.objects["player"][0][1] -= self.gp("vely")
		elif self.gp("mode") == "jumping":
			if not self.gp("vely") > self.gp("maxh") and not self.gp("jumph") < 0:
				self.sp("vely",self.gp("vely") + self.gp("jumph"))
				self.sp("maxy",-20)
				self.sp("vely",univars.func.lerp(self.gp("vely"),self.gp("maxy"),self.gp("speedupy")))
				om.objects["player"][0][1] -= self.gp("vely")
				self.sp("jumph",self.gp("jumph") - self.gp("jumpd"))
			else:
				self.sp("jump",0)
				self.sp("mode","norm")

	def cond(self,obj,info):
		if info["name"] == "enemy":
			om.translate(self,obj,[1,1])



rm = Runchinld((univars.screencol),fm)
rm.Run()