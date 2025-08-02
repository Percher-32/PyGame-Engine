import pygame
import Managers.Cameramod as Cameramod
import  Managers.univars as univars
import random

spritecache = {}

class Particlemanager:
	def __init__(self):
		self.particlelist = []
		self.screen = pygame.Surface((univars.screen_w,univars.screen_h))
		"""
			list ot particles\n:
				particle  = {pos:list,"vel":list,"force":tuple   ...}


		"""


	def particlespawn(self,type,pos,divergence,color,initvel,force,size,sizedec,dim = None,alpha=1000,alphadec=0,colordec = 0):
		"""
			spawns particles\n

			type:\n 
				"rect" or "circle"\n

			if using type == "rect":
				dim = dimensions

			

			divergence = range for randomness in initialvelocity:\n
				[ 
				  [ minx,maxx ] ,
				  [ miny,maxy ]
				]\n

			Particles are killed once size = 0\n
			
			nitems = number of particles to spawn\n
			force = force it's under\n
			initvel = initialvelocity\n
			pos = where to spawn  [x,y]\n
			
		"""
		initvel[0] += random.randint(divergence[0][0],divergence[0][1])
		initvel[1] += random.randint(divergence[1][0],divergence[1][1])
		particle = {
					"pos":pos,
					"vel":initvel,
					"force":force,
					"size":size,
					"initsize":size,
					"type":type,
					"sizedec":sizedec,
					"alpha":alpha,
					"alphadec":alphadec,
					"color":color,
					"dim":dim
					}
		self.particlelist.append(particle)


	


	def updateparticles(self,dt):
		"""
			updates all particles based on forces
		"""
		campos =  [Cameramod.cam.x,Cameramod.cam.y]
		def circlesurf(col,rad):
			surf = pygame.Surface((rad * 2,rad * 2))
			pygame.draw.circle(surf,col,(rad,rad),rad)
			surf.set_colorkey((0,0,0))
			return surf

		for particle in self.particlelist:
			particle["vel"][0] += particle["force"][0] * dt /2
			particle["vel"][1] += particle["force"][1] * dt/2
			particle["pos"][0] += particle["vel"][0] * dt/2
			particle["pos"][1] -= particle["vel"][1] * dt/2
			particle["size"] -= particle["sizedec"] * dt/2
			particle["alpha"] -= particle["alphadec"] * dt/2
			postodraw = [int(round(particle["pos"][0] - Cameramod.cam.x) * Cameramod.cam.size + univars.screen.get_width()//2),int(round((particle["pos"][1] - Cameramod.cam.y) * Cameramod.cam.size + univars.screen.get_height()//2 ))]
			if not particle["size"] <= 0:
				if particle["type"] == "circle":
					surf = circlesurf(particle["color"],particle["size"] * Cameramod.cam.size)
					surf.set_alpha(particle["alpha"])
					univars.screen.blit(surf,postodraw)
				if particle["type"] == "rect":
					if particle.get("rect",None) == None:
						size = [ particle["dim"][0] * particle["size"] ,  particle["dim"][1] * particle["size"] ]
						rect = pygame.Rect((postodraw[0],postodraw[1],size))
						particle["rect"] = rect
					else:
						rect = particle["rect"].move(postodraw)
					pygame.draw.rect(univars.screen,particle["color"],rect)
			else:
				self.particlelist.remove(particle)


pm = Particlemanager()