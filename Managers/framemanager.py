#framemanager
import time
import pygame
import Managers.univars as univars
class frame_manager:
	def __init__(self,tm):
		self.frame = 0
		self.tm = tm
		self.lasttime = time.time()
		self.dt = 0
		self.lastdt = 1
		self.open = True
		self.showfps = False
		self.theme = univars.theme["semibright"]
		self.lastdts = []

	def next(self,fps):
		self.fps = fps
		# self.lastdts.append()
		self.dt = (time.time() - self.lasttime) * 60
		# if len(self.lastdts) > univars.maxfpsbuffersize:
		# 	self.lastdts.pop(0)

		if self.dt > 3:
			self.dt = 3
		if self.dt < 0.5:
			self.dt = 0.5

		self.lasttime = time.time()
		clock = pygame.time.Clock()
		self.frame += 1
		clock.tick(self.fps)
		if self.showfps:
			self.tm.drawtext(f"fps = {round(60/ self.dt)}","pixel2.ttf",40,0,0,0,self.theme,-0.9,-0.9)
		pygame.display.update()
		if self.frame > 10000:
			self.frame = 0

	def On(self,frame):
		if round(self.frame) % frame == 0:
			return True
		else:
			return False
