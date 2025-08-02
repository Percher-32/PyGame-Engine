import pygame
import Cameramod
import univars
import random

spritecache = {}

class Particlemanager:
	def __init__(self):
		self.flamelist = []
		"""
			list of particleobjects

		"""


	def flame(self,nitems,force,pos,type,dim):
		"""
			a particle effect that draws the type and moves it based on force\n
			nitems = number of particles to spawn\n
			force = force it's under\n
			pos = where to spawn  [x,y]\n
			type:\n 
				"rect"   : dim = [width,height]
				"circle" : dim = radius
		"""
		id = str((nitems,force,pos,type,dim))
		campos =  [Cameramod.cam.x,Cameramod.cam.y]
		if not id in self.flamedict.keys():
			self.flamedict[id] = []
			for i in range




class Particle(pygame.sprite.Sprite):
	def __init__(self,surf,type,pos,force,initvel,dim,time,diversion):
		self.type = type
		self.image = surf
		self.rect((0,0,0,0))
		self.pos = pos
		self.dim = dim
		self.startpos = pos
		self.force = force
		self.initvel = initvel
		self.vel = initvel
		self.tottime = time
		self.time = time

	
	def update(self,campos):
		self.vel[0] += self.force[0] 
		self.vel[1] += self.force[1]
		self.pos[0] += self.vel[0]
		self.pos[1] -= self.vel[1]

		if univars.camchange or univars.poschange:
			realestsize = [int(round(self.size[0] * abs(camera.size))),int(round(self.size[1] * abs(camera.size)))]
			if not str([type,dim]) in spritecache.keys():
				self.image =  pygame.transform.scale(self.bart,  realestsize )
				spritecache[str([self.name,realestsize])] = self.image
			else:
				self.image = spritecache[str([self.name,realestsize])]
		else:
			self.image = self.lastframe



		self.rect = 
		


			
		
		
		



