import pygame
import Managers.Cameramod as Cameramod
import Managers.Textmanager as Textmanager
import Managers.Cammanager as Cammanager
import Managers.event_manager as event_manager
import Managers.funcs as funcs
import math
import Managers.framemanager as framemanager
import Managers.objectmanager as objectmanager
import Managers.Tiled as Tiled
import copy
import Managers.univars as univars
import Managers.statemanager as statemanager
import Managers.Uimanager as Uimanager
import Managers.inst as inst
import copy
import moderngl
import Managers.backgroundmanager as backgroundmanager
import os
import Managers.Shader as shader
import threading
import multiprocessing
import json
import time
import random
import Managers.Particlesytem
pygame.init()
pygame.joystick.init()

em = event_manager.event_manager()
tm = Textmanager.Textmanager(univars.realscreeen)
fm = framemanager.frame_manager(tm)
om = objectmanager.om
Tiled = Tiled.TiledSoftwre(univars.realscreeen,univars.theme,univars.grandim,univars.screen,om)
cam = Cameramod.cam
cm = Cammanager.camager
sm = statemanager.sm(univars.startstate)
um = Uimanager.ingame
bg = backgroundmanager.bg
sd = shader
pm = Managers.Particlesytem.pm


class GameManager():
	def __init__(self,screen_colour,frame_manager):
		self.output = []
		self.screen_colour = screen_colour
		self.frame_manager = frame_manager
		self.event_manager = em
		self.objrange = 2000
		self.em = em
		self.publicvariables = {"showinput":univars.showinput,"leveledit":True,"showdata":True,"debug-mode":False,"showfps":True,"maxfps":univars.maxfps,"printdebug":True,    "screencol":univars.screencol   ,"cammove":False  ,"shaderstate":univars.startshaderstate ,"showallhidden":1 }
		self.timers = {}
		self.timerswdt = []
		self.dt = 1
		self.abttodo = []
		self.messages = {}
		self.running = True
		self.lastkey = {}
		self.dons = []
		self.ids = []
		self.fm = fm
		self.states = []
		self.pausebackground = False
		self.pauseui = False
		self.key = {"x":0,"y":0,"jump":0,"secondary":0,"attack":0,"throw":0,"axis":[0,0],"option":0,"alt-x":0,"tert":0,"trick":0}
		self.dim = univars.grandim
		self.fpsmax = univars.maxfps
		self.leveledit = True
		self.previousbacklayer = pygame.Surface((0,0))
		self.smstate = sm.state
		self.boxes = []
		Tiled.extra(univars.extras)
		om.loadtilemap(self,univars.map)
		self.clock = pygame.time.Clock()


	def print(self,string):
		"""
			prints a string in game in the debug menu
		"""
		univars.output.append(str(string))
		if len(univars.output) > univars.buffersize:
			univars.output.pop(0)

	def println(self,string,line):
		"""
			prints onto a specific line if it exists\n
			if not it just adds it on the next line
		"""
		while len(univars.output) <= line:
			univars.output.append("")
		univars.output[line] = str(string)
		
	

	def console(self):
		"""
			returns a string all printed items
		"""
		out = ""
		for i in univars.output:
			out += i + "\n"
		return out

		

	def debug(self,message,sep = 0):
		if self.publicvariables["printdebug"]:
			print(message)
			for i in range(sep):
				print()

	def keybind(self):
		self.lastkey = self.key.copy()
		#main 5 inputs
		if em.controller["x"] or em.key[pygame.K_SPACE] or em.key[pygame.K_RETURN]:
			self.key["jump"] = True
		else:
			self.key["jump"] = False
		if em.controller["triangle"] or em.controller["R1"] or em.key[pygame.K_z] or em.key[pygame.K_p]:
			self.key["secondary"] = True
		else:
			self.key["secondary"] = False
		if em.controller["square"] or em.key[pygame.K_o] or em.key[pygame.K_x]:
			self.key["attack"] = True
		else:
			self.key["attack"] = False
		if em.controller["circle"] or em.key[pygame.K_i] or em.key[pygame.K_c]:
			self.key["throw"] = True
		else:
			self.key["throw"] = False
		if em.controller["options"] or em.key[pygame.K_ESCAPE]:
			self.key["option"] = True
		else:
			self.key["option"] = False
		# if em.controller["L1"] or em.key[pygame.K_LCTRL] or em.key[pygame.K_RCTRL]:
		# 	self.key["tert"] = True
		# else:
		# 	self.key["tert"] = False
		if em.controller["L1"] or em.key[pygame.K_LCTRL] or em.key[pygame.K_RCTRL]:
			self.key["trick"] = True
		else:
			self.key["trick"] = False


		#joyaxis
		if abs(em.analog_keys[0]) > 0.3:
			self.key["x"] = round(em.analog_keys[0],2)
		elif em.key[pygame.K_RIGHT] or em.key[pygame.K_d] or em.controller["right_arrow"]:
			self.key["x"] = 1
		elif em.key[pygame.K_LEFT] or em.key[pygame.K_a] or em.controller["left_arrow"]:
			self.key["x"] = -1
		else:
			self.key["x"] = 0
		if abs(em.analog_keys[1]) > 0.3:
			self.key["y"] = round(-1 * em.analog_keys[1],2)
		elif em.key[pygame.K_UP] or em.key[pygame.K_w] or em.controller["up_arrow"]:
			self.key["y"] = 1
		elif em.key[pygame.K_DOWN] or em.key[pygame.K_s] or em.controller["down_arrow"]:
			self.key["y"] = -1
		else:
			self.key["y"] = 0

		if em.key[pygame.K_RIGHT] or em.controller["right_arrow"]:
			self.key["alt - x"] = 1
		if em.key[pygame.K_LEFT] or em.controller["left_arrow"]:
			self.key["alt - x"] = -1


		#ui axis
		if abs(em.analog_keys[0]) > 0.3:
			self.key["axis"][0] = round(em.analog_keys[0])
		elif em.key[pygame.K_RIGHT] or em.key[pygame.K_d] or em.controller["right_arrow"]:
			self.key["axis"][0] = 1
		elif em.key[pygame.K_LEFT] or em.key[pygame.K_a] or em.controller["left_arrow"]:
			self.key["axis"][0] = -1
		else:
			self.key["axis"][0] = 0
		if abs(em.analog_keys[1]) > 0.3:
			self.key["axis"][1] = round(-1 * em.analog_keys[1])
		elif em.key[pygame.K_UP] or em.key[pygame.K_w] or em.controller["up_arrow"]:
			self.key["axis"][1] = 1
		elif em.key[pygame.K_DOWN] or em.key[pygame.K_s] or em.controller["down_arrow"]:
			self.key["axis"][1] = -1
		else:
			self.key["axis"][1] = 0




	def blit(self,surf,rect,rot,camera):
		a = surf
		a = pygame.transform.scale_by(a,abs(camera.size)* (((((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983)) * 1980))
		a = pygame.transform.rotate(a,rot)
		univars.screen.blit(a,((rect.x - camera.x) * camera.size + univars.screen.get_width()//2 (((((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983)) * 1980) ,(rect.y - camera.y) * camera.size + univars.screen.get_height()//2 ))

	def blitsurf(self,surf,pos,rot,camera):
		a = surf
		a = pygame.transform.scale_by(a,abs(camera.size))
		b = pygame.transform.rotate(a,rot)
		self.abttodo.append([b,pos])

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
		a = pygame.transform.scale(a,(abs(size[0])  ,abs(size[1])))
		univars.realscreeen.blit(a,(pos[0]  * univars.realscreeen.get_width()//2 - (a.get_width()/2)  + univars.realscreeen.get_width()//2  ,-1 * pos[1]  * univars.realscreeen.get_width()//2 - (a.get_height()/2)  + univars.realscreeen.get_height()//2 ))

	def blitui2(self,surf,pos):
		a = surf
		univars.realscreeen.blit(a,(pos[0]  * univars.realscreeen.get_width()//2 - (a.get_width()/2)  + univars.realscreeen.get_width()//2  ,-1 * pos[1]  * univars.realscreeen.get_width()//2 - (a.get_height()/2)  + univars.realscreeen.get_height()//2 ))

	def blituis(self,surf,pos,size,rot,alpha):
		a = surf
		a = pygame.transform.scale(a,(round(abs(size[0]) * ((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983),round(abs(size[1])) * ((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983))
		a = pygame.transform.rotate(a,rot)
		a.set_alpha(alpha)
		univars.realscreeen.blit(a,(pos[0]  * univars.realscreeen.get_width()//2 - (a.get_width()/2)  + univars.realscreeen.get_width()//2  ,-1 * pos[1]  * univars.realscreeen.get_height()//2 - (a.get_height()/2)  + univars.realscreeen.get_height()//2 ))

	def blituis2(self,surf,pos,size,rot,alpha):
		
		a = surf
		a = pygame.transform.scale(a,(abs(size[0])  * round(((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983),abs(size[1])) * round(((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983))
		a = pygame.transform.rotate(a,rot)
		a.set_alpha(alpha)
		univars.realscreeen.blit(a,(pos[0],pos[1]))

	def uibox(self,wh,pos,col,alpha):
		wh = list(wh)
		wh[0] *= ((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983
		wh[1] *= ((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983
		a = pygame.Surface((round(wh[0]),round(wh[1])))
		a.fill(col)
		a.set_alpha(alpha)
		univars.realscreeen.blit(a,(pos[0] * univars.realscreeen.get_width()//2 - (wh[0]/2) + univars.realscreeen.get_width()//2 ,-1 * pos[1] * univars.realscreeen.get_height()//2 -  (wh[1]/2)  + univars.realscreeen.get_height()//2 ))

	def Gotomousepos(self,surf,id,size,rot):
		a = univars.func.getsprites(surf)[id]
		a = pygame.transform.scale_by(a,abs(size))
		a = pygame.transform.rotate(a,rot)
		univars.screen.blit(a,(em.mousepos[0] ,em.mousepos[1]))
	
	def Gotomousepos2(self,surf):
		univars.realscreeen.blit(surf,(em.mousepos[0] ,em.mousepos[1]))

	def Gotomouseposgrid(self,surface,camera,rot,dim):
		upscale = univars.realscreeen.get_width() / univars.screen.get_width()
		translation = univars.realscreeen.get_width()//4
		newsurface = pygame.transform.scale_by	(surface[0],(upscale,upscale))
		mousepos = (  (em.mousepos[0]  - univars.realscreeen.get_width()//2) / camera.size) + camera.x, (( (em.mousepos[1]  - univars.realscreeen.get_height()//2) / camera.size) + camera.y)
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
		if rect.collidepoint(self.frame_manager.em.mousepos):
			return True
		else:
			return False

	def inum(self):
		lastime = 1
		dt = self.dt
		lastime = time.time()
		if len(om.objects.keys()) > 0:
			stabledict = copy.copy(om.objects)
			for obj in stabledict.keys():
				range =  self.objrange
				if om.speed > 0:
					if univars.func.dist(stabledict[obj]["pos"],[Cameramod.cam.x,Cameramod.cam.y]) < range:
						
						self.cond(obj,stabledict[obj],dt)
			# pass


			# time.sleep(0.0000001)

	def cond(self,obj,info):
		pass

	def wait(self,name:str,time:float,barrier=True,useigt = 1):
		"""
			creates a timer that will elapse in (time) seconds.\n
			check if done with ondone.\n
			barier:True = only works if there isn't a timer with that name already\n
		"""
		if not name in self.timers.keys() or not barrier:
			self.timers[name] = time * 45

		if useigt == 1:
			self.timerswdt.append(name)

	def updatetime(self):
		self.dons = []
		for i in self.timers.keys():
			if i in self.timerswdt:
				self.timers[i] = self.timers[i] - (self.frame_manager.dt * om.speed)
			else:
				self.timers[i] = self.timers[i] - self.frame_manager.dt
			if self.timers[i] < 0:
				self.dons.append(i)

		timer_copy = copy.copy(self.timers)
		for i in timer_copy.keys():
			if i in self.dons:
				self.timers.pop(i)

	def ondone(self,name:str) -> bool:
		return name in self.dons

	def killtimer(self,name):
		"""
			removes a timer if it exists
		"""
		if name in self.timers.keys():
			self.timers.pop(name)

	def bosh(self):
		"""
			update all variables to be intouch with state manager
		"""
		self.publicvariables["leveledit"] = sm.leveledit
		self.publicvariables["debug-mode"] = sm.work
		om.speed = sm.speed
		self.states = sm.states
		self.publicvariables["showdata"] = sm.showui
		self.publicvariables["cammove"] = sm.cammove
		self.publicvariables["showallhidden"] = sm.showall
		self.smstate = sm.state

	def send(self,header,message):
		"""
			sends a message only lasts on that frame
      	"""
		self.messages[header] = message
  
  
	def message(self,header):
		"""
			returns dict:
			{
					"SENT" : BOOL
					"MESSAGE" : ANY
	
			}
		"""

		message = None
		sent = False
		if header in self.messages:
			sent = True

			message = self.messages[header] 
   
   
   
		
		return {sent,message}





	def Run(self):
		self.commence()
		self.initial()
		# inumthread = threading.Process(target=self.inum)
		# backgroundthread = threading.Thread(target=self.backgroundupdate)
		# uithread = threading.Thread(target=self.uiunpdate)
		# backgroundthread.start()
		# uithread.start()
		self.dt = 1
		
		# inumthread.start()
		while em.running: 
			self.start()   
			if not Tiled.loadingmap:
				self.update()
			self.end()
		self.running = False
		em.running = False

	def defs(self):
		"""
			automatically happens on reload
		"""
		sm.update()
		self.bosh()
		bg.loadbg()
		om.instables = univars.instables
		
		cm.setcam("def")
		self.debug = True
		cm.setcond(cm.currentcam,"size",1)
		# self.loadanims()
		
		self.roster()
		# um.loadalluielements()
		pm.loadallbluprints()

	def setbosh(self,state):
		sm.state = state
		sm.update()
		self.bosh()
		self.smstate = sm.state
		# print(f"bosh to {state}")
		self.quickrel()
		self.qrcondHL()

	def quickrel(self):
		pass

	def qrcondHL(self):
		if len(om.objects.keys()) > 0:
			stabledict = copy.deepcopy(om.objects)
			for obj in stabledict.keys():
				self.qrcond(obj,stabledict[obj])

	def qrcond(self,id,info):
		pass

	def inputdetect(self):
		em.next()

	def uiunpdate(self):
		while em.running:
			if not self.pauseui:
				um.update(em,self.publicvariables,self.key["axis"],self.dt)
				time.sleep(0.05)

	# def broadcast(self,message):


	def start(self):
		"""run at the start of every frame"""
		if self.dt == 0:
			self.dt = 1
		self.inum()
		self.fps = round(60/ self.dt,3)
		if Tiled.comm:
			sm.state = Tiled.cht
			self.initial()
		if Tiled.loadingmap:
			self.initial()

		#render background
		# if len(om.objects.keys()) > 0:
		# 	stabledict = om.objects
		# 	for obj in stabledict.keys():
		# 		range =  2000
		# 		if univars.func.dist(stabledict[obj]["pos"],[Cameramod.cam.x,Cameramod.cam.y]) < range:
		# 			self.cond(obj,stabledict[obj])
		
			
		bg.update(self.publicvariables["screencol"])
		univars.screen.blit(bg.backlayer,(0,0))



		#renders objects
		om.render(cam,self,self.dim,self.publicvariables["showallhidden"])


		
		#renders blits
		camera = Cameramod.cam
		for i in self.abttodo:
			b = i[0]
			pos = i[1]
			univars.screen.blit(b,(            (             ( (int(round(pos[0] - camera.x) * camera.size + univars.screen.get_width()//2 - b.get_width()/2)),int(round((pos[1] - camera.y) * camera.size + univars.screen.get_height()//2 - b.get_height()/2)))            )         )                  )
			self.abttodo.remove(i)

		
		#render onto screen
		renderwid = (((((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983)) * 1980) + 200
		renderwid = 0
		# renderwid = min([univars.realscreeen.width,univars.realscreeen.height])
		# renderwid = 1980
		# realwid = round(renderwid)
		# renderwid /= 2
		# univars.screen.blit(pm.screen,(univars.screen_w/2,univars.screen_h/2))
		pm.updateparticles(self.dt)
		univars.realscreeen.blit(pygame.transform.scale_by(univars.screen,univars.pixelscale),(univars.realscreeen.width//2 - (univars.pixelscale * univars.screen.size[0])//2,univars.realscreeen.height//2 - (univars.pixelscale * univars.screen.size[1])//2))
		

		#runs editor
		Tiled.Run(self.publicvariables["debug-mode"],univars.camspeeed,self,cam,self.dim,self.publicvariables["leveledit"],cm,sm.state)

		
		if fm.showfps:
			if self.dt > 0:
				tm.drawtext(f"fps = {round(60/ self.dt)}","pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.9,-0.9)


		#renders ui
		self.pauseui = True
		um.update(em,self.publicvariables,self.key["axis"],self.dt)
		um.sprites.draw(univars.realscreeen)
		self.pauseui = False






		self.keybind()
		self.updatetime()
		cm.update()
		cam.update()
		univars.update()

	def loadanims(self):
		for filename in os.listdir("Saved/animations"):
			if  not filename ==  "None":
				objfile = "Saved/animations" + "/" + filename
				for anim in os.listdir(objfile):
					anim = anim.replace(".json","")
					om.loadanim(filename,anim)


	def oncreate(self,id,info):
		pass

	def roster(self):
		"""
			goes through all sprites on reload
		"""
		if len(om.objects.keys()) > 0:
			stabledict = copy.deepcopy(om.objects)
			
			for obj in stabledict.keys():
				self.oncreate(obj,stabledict[obj])
			

	def update(self):			
		pass
				
	def end(self):
		renderwid = (((((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983)) * 1980) + 200
		self.messages = {}
		
		self.clock.tick(self.publicvariables["maxfps"])
		# univars.screen.blit(pm.screen,(univars.screen_w/2,univars.screen_h/2))
		pm.updateparticles(self.dt)
		# univars.realscreeen.blit(pygame.transform.scale(univars.fakescreen,(renderwid ,renderwid )),(univars.realscreeen.width//2 - renderwid//2,univars.realscreeen.height//2 - renderwid//2))
		univars.realscreeen.blit(pygame.transform.scale_by(univars.fakescreen,univars.pixelscale),(univars.realscreeen.width//2 - (univars.pixelscale * univars.screen.size[0])//2,univars.realscreeen.height//2 - (univars.pixelscale * univars.screen.size[1])//2))
		
		univars.fakescreen.fill((0,0,0))



		# univars.finalscreen.blit(univars.realscreeen,)
		# print(pygame.display.get_window_size())
		# univars.realscreeen = pygame.transform.scale(univars.realscreeen,[pygame.display.get_window_size()[0]/univars.startdims[0] * univars.startdims[0],pygame.display.get_window_size()[1]/univars.startdims[1] * univars.startdims[1]])
		# # univars.realscreeen = pygame.transform.scale_by(univars.realscreeen,(pygame.display.get_window_size()[0]/univars.startdims[0]))
		# print((pygame.display.get_window_size()[0]/univars.startdims[0]) ** 2)


		# bgframe_tex = shader.bg_surf_to_texture(bg.backlayer)
		# bgframe_tex.use(0)
		# shader.bgprogram['tex'] = 0
		# shader.bgprogram['time'] = fm.frame
		# shader.bgprogram['state'] = self.publicvariables["shaderstate"]
		# shader.bgrender_object.render(mode=moderngl.TRIANGLE_STRIP)


		frame_tex = shader.surf_to_texture(univars.realscreeen)
		frame_tex.use(0)
		shader.program['tex'] = 0
		shader.render_object.render(mode=moderngl.TRIANGLE_STRIP)

		


		self.dt = fm.dt
		
		self.inputdetect()
		self.frame_manager.next(self.publicvariables["maxfps"])
		
		# bgframe_tex.release()

	def initial(self):
		"""
			calles the in - engine and in game reload funcions
		"""
		self.defs()
		
		self.onreload()
		
	def isthere(self,name):
		"""
			if timer is currently there
		"""
		return name in self.timers.keys()

	def deltimer(self,name):
		"""
			removes a timer if it exists
		"""
		if name in self.timers.keys():
			self.timers.pop(name)

	def onreload(self):
		pass

