import pygame
import Managers.Cameramod as Cameramod
import  Managers.univars as univars
import random
import json
import os
spritecache = {}

class Particlemanager:
	def __init__(self):
		self.particlelist = []
		"""
			list ot particles\n:
				particle  = {pos:list,"vel":list,"force":tuple   ...}


		"""
		self.screen = pygame.Surface((univars.screen_w,univars.screen_h))
		self.bluprints = {}



	def savebluprint(self,name,type,divergence,color,initvel,force,size,sizedec,dim = None,alpha=1000,alphadec=0,colordec = 0,quality = 1,divergenceforce = [[0,0],[0,0]],divergencepos = [[0,0],[0,0]],ntimes =1,speed = 1):
		"""
			Save particle bluprint\n

			name:\n
				name for the preset

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
		tosave = {"type":type,"divergence":divergence,"color":color,"initvel":initvel,"force":force,"size":size,"sizedec":sizedec,"dim":dim,"alpha":alpha,"alphadec":alphadec,"colordec":colordec,"quality":quality,"divergenceforce":divergenceforce,"divergencepos":divergencepos,"ntimes":ntimes,"speed":speed}
		with open(f"Saved/particles/{name}.json","w") as file:
			json.dump(tosave,file)
		self.bluprints[name] = tosave


	def loadallbluprints(self):
		"""
			loads all saved particle bluprints
		"""
		for i in os.listdir("Saved/particles"):
			with open(f"Saved/particles/{i}") as file:
				self.bluprints[i.replace(".json","")] = json.load(file)


	def particlespawnbluprint(self,pos,name,initvel = None):
		use = self.bluprints[name]
		if initvel == None:
			initvel = use["force"]
		self.particlespawn(use["type"],pos,use["divergence"],
							use["color"],initvel,use["force"],
							use["size"],use["sizedec"],dim = use["dim"],
							alpha = use["alpha"],alphadec=use["alphadec"],
							colordec=use["colordec"],quality=use["quality"],
							divergenceforce=use["divergenceforce"],
							divergencepos=use["divergencepos"],
							ntimes=use["ntimes"],
       						speed=use["speed"])
		
				




	def particlespawn(self,type,pos,divergence,color,initvel,force,size,sizedec,dim = None,alpha=1000,alphadec=0,colordec = 0,quality = 1,divergenceforce = [[0,0],[0,0]],divergencepos = [[0,0],[0,0]],ntimes =1,speed = 1):
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
		for _ in range(ntimes):
			newinitvel = list([initvel[0],initvel[1]])
			newforce = list([force[0],force[1]])
			newpos = list([pos[0],pos[1]])
			newinitvel[0] += random.randint(divergence[0][0],divergence[0][1])
			newinitvel[1] += random.randint(divergence[1][0],divergence[1][1])
			newforce[0] += random.randint(divergenceforce[0][0],divergenceforce[0][1])
			newforce[1] += random.randint(divergenceforce[1][0],divergenceforce[1][1])
			newpos[0] += random.randint(divergencepos[0][0],divergencepos[0][1])
			newpos[1] += random.randint(divergencepos[1][0],divergencepos[1][1])
			particle = {
						"pos":newpos,
						"vel":newinitvel,
						"force":newforce,
						"size":size,
						"initsize":size,
						"type":type,
						"sizedec":sizedec,
						"alpha":alpha,
						"alphadec":alphadec,
						"color":color,
						"dim":dim,
						"quality":quality,
    					"speed":speed
						}
			self.particlelist.append(particle)


	
	def circlesurf(self,col,rad,qual):
		"""
			allows circles to have alpha
		"""
		surf = pygame.Surface((rad * 2,rad * 2))
		pygame.draw.circle(surf,col,(rad,rad),rad)
		surf = pygame.transform.scale_by(surf,qual)
		surf = pygame.transform.scale(surf,(rad * 2,rad * 2))
		surf.set_colorkey((0,0,0))
		return surf

	def updateparticles(self,dt):
		"""
			updates all particles based on forces and velocities
		"""
		

		for particle in self.particlelist:
			particle["vel"][0] += particle["force"][0] * dt /2 * particle["speed"]
			particle["vel"][1] += particle["force"][1] * dt/2 * particle["speed"]
			particle["pos"][0] += particle["vel"][0] * dt/2 * particle["speed"]
			particle["pos"][1] -= particle["vel"][1] * dt/2 * particle["speed"]
			particle["size"] -= particle["sizedec"] * dt/2 * particle["speed"]
			particle["alpha"] -= particle["alphadec"] * dt/2 * particle["speed"]
			postodraw = [int(round(particle["pos"][0] - Cameramod.cam.x) * Cameramod.cam.size + univars.screen.get_width()//2),int(round((particle["pos"][1] - Cameramod.cam.y) * Cameramod.cam.size + univars.screen.get_height()//2 ))]
			if not particle["size"] <= 0:
				if particle["type"] == "circle":
					surf = self.circlesurf(particle["color"],particle["size"] * Cameramod.cam.size,particle["quality"])
					surf.set_alpha(particle["alpha"])
					univars.screen.blit(surf,postodraw)
				if particle["type"] == "rect":
					# if particle.get("rect",None) == None:
					size = [ particle["dim"][0] * particle["size"] * Cameramod.cam.size ,  particle["dim"][1] * particle["size"] * Cameramod.cam.size ]
					rect = pygame.Rect((postodraw[0],postodraw[1],size[0],size[1]))
					particle["rect"] = rect
					# else:
					# 	rect = particle["rect"].move(postodraw)
					pygame.draw.rect(univars.screen,particle["color"],rect)
			else:
				self.particlelist.remove(particle)


pm = Particlemanager()