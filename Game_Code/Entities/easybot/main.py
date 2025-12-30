import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import pygame
import math
import random
import Utils.Entities as Entities




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

def main(self,id,info,st):
    

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


		Entities.damageable(id,100,self,func = hit,functhrow=skatehit)






self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)