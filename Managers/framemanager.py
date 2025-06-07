#framemanager
import time
import pygame
class frame_manager:
	def __init__(self,event_manager,tm):
		self.frame = 0
		self.event_manager = event_manager
		self.tm = tm
		self.lasttime = time.time()
		self.dt = 0
		self.open = True
		self.showfps = True

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
			self.tm.drawtext(f"fps = {round(60/ self.dt)}","pixel2.ttf",40,0,0,0,(50,50,50),-0.9,-0.9)
		pygame.display.update()

	def On(self,frame):
		if round(self.frame) % frame == 0:
			return True
		else:
			return False
