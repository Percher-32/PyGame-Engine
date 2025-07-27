import pygame
import Cameramod as Cameramod
import Textmanager as Textmanager
import Cammanager as Cammanager
import event_manager as event_manager
import funcs as funcs
import framemanager as framemanager
import objectmanager as objectmanager
import Tiled as Tiled
import univars as univars
import statemanager as statemanager
import Uimanager
import copy
import backgroundmanager
import os
import threading
import time
pygame.init()
pygame.joystick.init()

em = event_manager.event_manager()
tm = Textmanager.Textmanager(univars.realscreeen)
fm = framemanager.frame_manager(em,tm)
om = objectmanager.om
Tiled = Tiled.TiledSoftwre(univars.realscreeen,univars.theme,univars.grandim,univars.screen,om)
cam = Cameramod.cam
cm = Cammanager.camager
sm = statemanager.sm(univars.startstate)
um = Uimanager.ingame
bg = backgroundmanager.bg

class GameManager():
	def __init__(self,screen_colour,frame_manager):
		self.screen_colour = screen_colour
		self.frame_manager = frame_manager
		self.event_manager = self.frame_manager.event_manager
		self.timers = {}
		self.dt = 1
		self.running = True
		self.lastkey = {}
		self.dons = []
		self.ids = []
		self.states = []
		self.key = {}
		self.dim = univars.grandim
		self.fpsmax = univars.maxfps
		self.work = True
		self.leveledit = True
		Tiled.extra(univars.extras)
		om.loadtilemap(univars.map)

	def keybind(self):
		if em.x or self.event_manager.key[pygame.K_SPACE]:
			self.key["action"] = True
		else:
			self.key["action"] = False
		if em.tri or self.event_manager.key[pygame.K_z]:
			self.key["a2"] = True
		else:
			self.key["a2"] = False
		if abs(event_manager.analog_keys[0]) > 0.3:
			self.key["x"] = event_manager.analog_keys[0]
		elif self.event_manager.key[pygame.K_RIGHT]:
			self.key["x"] = 1
		elif self.event_manager.key[pygame.K_LEFT]:
			self.key["x"] = -1
		else:
			self.key["x"] = 0
		if abs(event_manager.analog_keys[1]) > 0.3:
			self.key["y"] = -1 * event_manager.analog_keys[1]
		elif self.event_manager.key[pygame.K_UP]:
			self.key["y"] = 1
		elif self.event_manager.key[pygame.K_DOWN]:
			self.key["y"] = -1
		else:
			self.key["y"] = 0

	def blit(self,surf,rect,rot,camera):
		a = surf
		a = pygame.transform.scale_by(a,abs(camera.size))
		a = pygame.transform.rotate(a,rot)
		univars.screen.blit(a,((rect.x - camera.x) * camera.size + univars.screen.get_width()//2 ,(rect.y - camera.y) * camera.size + univars.screen.get_height()//2 ))

	def blitsurf(self,surf,pos,rot,camera):
		a = surf
		a = pygame.transform.scale_by(a,abs(camera.size))
		b = pygame.transform.rotate(a,rot)
		univars.screen.blit(b,((pos[0] - camera.x) * round(camera.size,2) + univars.screen.get_width()//2 - b.get_width()/2 ,(pos[1] - camera.y) * round(camera.size,2) + univars.screen.get_height()//2 - b.get_height()/2))

	def blitrect(self,surf,pos,rot,camera):
		a = surf
		a = pygame.transform.scale_by(a,abs(camera.size))
		b = pygame.transform.rotate(a,rot)
		univars.screen.blit(b,((pos[0] - camera.x) * round(camera.size,2) + univars.screen.get_width()//2 - b.get_width()/2 ,(pos[1] - camera.y) * round(camera.size,2) + univars.screen.get_height()//2 - b.get_height()/2))

	def realblit(self,surf,rect,rot,camera):
		a = surf
		a = pygame.transform.scale_by(a,abs(camera.size))
		a = pygame.transform.rotate(a,rot)
		univars.realscreeen.blit(a,((rect.x - camera.x) * camera.size + univars.realscreeen.get_width()//2 ,(rect.y - camera.y) * camera.size + univars.realscreeen.get_height()//2 ))

	def blitui(self,surf,pos,size):
		a = surf
		a = pygame.transform.scale(a,(abs(size[0]),abs(size[1])))
		univars.realscreeen.blit(a,(pos[0]  * univars.realscreeen.get_width()//2 - (a.get_width()/2)  + univars.realscreeen.get_width()//2  ,-1 * pos[1]  * univars.realscreeen.get_width()//2 - (a.get_height()/2)  + univars.realscreeen.get_height()//2 ))

	def blitui2(self,surf,pos):
		a = surf
		univars.realscreeen.blit(a,(pos[0]  * univars.realscreeen.get_width()//2 - (a.get_width()/2)  + univars.realscreeen.get_width()//2  ,-1 * pos[1]  * univars.realscreeen.get_width()//2 - (a.get_height()/2)  + univars.realscreeen.get_height()//2 ))

	def blituis(self,surf,pos,size,rot,alpha):
		a = surf
		a = pygame.transform.scale(a,(abs(size[0]),abs(size[1])))
		a = pygame.transform.rotate(a,rot)
		a.set_alpha(alpha)
		univars.realscreeen.blit(a,(pos[0]  * univars.realscreeen.get_width()//2 - (a.get_width()/2)  + univars.realscreeen.get_width()//2  ,-1 * pos[1]  * univars.realscreeen.get_height()//2 - (a.get_height()/2)  + univars.realscreeen.get_height()//2 ))

	def blituis2(self,surf,pos,size,rot,alpha):
		
		a = surf
		a = pygame.transform.scale(a,(abs(size[0]),abs(size[1])))
		a = pygame.transform.rotate(a,rot)
		a.set_alpha(alpha)
		univars.realscreeen.blit(a,(pos[0],pos[1]))

	def uibox(self,wh,pos,col,alpha):
		a = pygame.Surface((wh[0],wh[1]))
		a.fill(col)
		a.set_alpha(alpha)
		univars.realscreeen.blit(a,(pos[0] * univars.realscreeen.get_width()//2 - (wh[0]/2) + univars.realscreeen.get_width()//2 ,-1 * pos[1] * univars.realscreeen.get_height()//2 -  (wh[1]/2)  + univars.realscreeen.get_height()//2 ))

	def Gotomousepos(self,surf,id,size,rot):
		a = univars.func.getsprites(surf)[id]
		a = pygame.transform.scale_by(a,abs(size))
		a = pygame.transform.rotate(a,rot)
		univars.screen.blit(a,(self.event_manager.mousepos[0] ,self.event_manager.mousepos[1]))
	
	def Gotomousepos2(self,surf):
		univars.realscreeen.blit(surf,(self.event_manager.mousepos[0] ,self.event_manager.mousepos[1]))

	def Gotomouseposgrid(self,surface,camera,rot,dim):
		upscale = univars.realscreeen.get_width() / univars.screen.get_width()
		translation = univars.realscreeen.get_width()//4
		newsurface = pygame.transform.scale_by	(surface[0],(upscale,upscale))
		mousepos = (  (self.event_manager.mousepos[0]  - univars.realscreeen.get_width()//2) / camera.size) + camera.x, (( (self.event_manager.mousepos[1]  - univars.realscreeen.get_height()//2) / camera.size) + camera.y)
		size = camera.size
		gridpos = (round(mousepos[0]/(dim * upscale)) * dim * upscale , round(mousepos[1]/(dim * upscale)) * dim * upscale )
		newsurface.set_alpha(100)


		temp_rect = newsurface.get_rect(center = gridpos)

		self.realblit(newsurface,temp_rect,rot,camera)

	def on(self,frame):
		if round(self.frame_manager.frame) % frame == 0:
			return True
		else:
			return False

	def click(self,rect):
		if rect.collidepoint(self.frame_manager.event_manager.mousepos):
			return True
		else:
			return False

	def inum(self):
		while em.running:
			if len(om.objects.keys()) > 0:
				stabledict = om.objects
				for obj in stabledict.keys():
					range =  2000
					if univars.func.dist(stabledict[obj]["pos"],[Cameramod.cam.x,Cameramod.cam.y]) < range:
						self.cond(obj,stabledict[obj])
			time.sleep(0.01)


	def cond(self,obj,info):
		pass

	def wait(self,name:str,time:float):
		if not name in self.timers.keys():
			self.timers[name] = time * 45

	def updatetime(self):
		self.dons = []
		for i in self.timers.keys():
			self.timers[i] = self.timers[i] - self.frame_manager.dt
			if self.timers[i] < 0:
				self.dons.append(i)

		timer_copy = copy.copy(self.timers)
		for i in timer_copy.keys():
			if i in self.dons:
				self.timers.pop(i)

	def ondone(self,name:str) -> bool:
		if name in self.dons:
			return True
		else:
			return False

	def defs(self):
		sm.update()
		self.bosh()
		om.instables = univars.instables
		cm.setcam("def")
		self.debug = True

	def bosh(self):
		self.leveledit = sm.leveledit
		self.work = sm.work
		om.speed = sm.speed
		self.states = sm.states
		Tiled.showdata = sm.showui
		om.showall = sm.showall

	def sp(self,val:str,to):
		"""
		changes the value a players variable
		"""
		om.set_value("player",val,to)

	def gp(self,val:str):
		"""
		gets the value a players variable
		"""
		return om.get_value("player",val)

	def Run(self):
		self.commence()
		self.initial()
		inumthread = threading.Thread(target=self.inum)
		inumthread.start()
		while(1): 
			self.start()   
			if not Tiled.loadingmap:
				self.update()
			self.end()
		self.running = False


	def defs(self):
		sm.update()
		self.bosh()
		bg.loadbg()
		om.instables = univars.instables
		cm.setcam("def")
		self.debug = True
		self.loadanims()

		


	def start(self):
		"""run at the start of every frame"""
		if Tiled.comm:
			sm.state = Tiled.cht
			self.initial()
		if Tiled.loadingmap:
			self.initial()
		renderwid = max([univars.screen_w,univars.screen_h])
		univars.realscreeen.blit(pygame.transform.scale(univars.screen,(renderwid ,renderwid )),(0,-1 * renderwid//4))
		univars.screen.fill((self.screen_colour))
		bg.update()
		self.dt = fm.dt
		om.render(cam,self,self.dim)
		um.update(em)
		# self.inum()
		if self.work:
			Tiled.Run(self.work,univars.camspeeed,self,cam,self.dim,self.leveledit,cm,sm.state)
		self.keybind()
		cm.update()
		self.updatetime()
		univars.update()
		cam.update()


	def loadanims(self):
		for filename in os.listdir("Saved/animations"):
			if  not filename ==  "None":
				objfile = "Saved/animations" + "/" + filename
				for anim in os.listdir(objfile):
					anim = anim.replace(".json","")
					om.loadanim(filename,anim)

	def update(self):			
		pass
				
	def end(self):
		self.lastkey = self.key
		self.frame_manager.next(self.fpsmax)

	def initial(self):
		self.defs()
		self.onreload()
		


	def onreload(self):
		pass

