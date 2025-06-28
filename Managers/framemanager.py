#framemanager
import time
import pygame
import univars
import Textmanager

tm = Textmanager.tm
class frame_manager:
	def __init__(self,event_manager):
		self.frame = 0
		self.realfont = pygame.font.Font(f"Graphics/Fonts/pixel2.ttf",40)
		
		self.event_manager = event_manager
		self.lasttime = time.time()
		self.dt = 0
		self.open = True
		self.showfps = True
		self.theme = univars.theme["semibright"]

	def next(self,fps):
		self.fps = fps
		self.event_manager.next()
		self.dt = time.time() - self.lasttime
		self.dt *= 60
		self.lasttime = time.time()
		clock = pygame.time.Clock()
		self.frame += 1
		clock.tick(self.fps)
		if self.showfps:
			self.prednder = self.realfont.render(f"fps = {round(60/ self.dt)}",0,0)
			y = x = 0.9
			univars.realscreeen.blit(self.prednder,(x * univars.realscreeen.get_width()//2 - (self.prednder.get_width()/2) + univars.realscreeen.get_width()//2 ,-1 * y * univars.realscreeen.get_height()//2  - (self.prednder.get_height()/2)  + univars.realscreeen.get_height()//2 ))
			# tm.drawtext(f"fps = {round(60/ self.dt)}","pixel2.ttf",40,0,0,0,self.theme,-0.9,-0.9)
		pygame.display.update()
		if self.frame > 10000:
			self.frame = 0

	def On(self,frame):
		if round(self.frame) % frame == 0:
			return True
		else:
			return False
