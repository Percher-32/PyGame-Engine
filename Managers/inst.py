import pygame
import Managers.funcs as funcs
import Managers.Cameramod as Cameramod
import Managers.univars as univars
import json
import math
cam = Cameramod.cam


spritecache = {}
dataspritecache = []
with open("Saved/Spritecache.json") as file:
	fakespritecache = json.load(file)
dataspritecache = fakespritecache
for i in fakespritecache:
	spritecache[str(i)] = pygame.transform.scale(univars.func.getsprites(i[0])[0],i[1])

nullsurf = pygame.Surface((0,0))



class inst(pygame.sprite.Sprite):
	__slots__ = ["screen","grandim","name","x","y","rot","sizen","type","alpha"]


	def __init__(self,screen,grandim,name,x,y,rot,sizen,type,alpha,sprites,size):
		pygame.sprite.Sprite.__init__(self)
		
		camera = Cameramod.cam
		realestsize = [round(size[0] * abs(camera.size),1),round(size[1] * abs(camera.size),1)]
		self.sizen = list(sizen)
		self.name = str(name)
		self.type = type
		self.bart = sprites[0]
		self.newbie = True
		self.image =  nullsurf
		self.rot = int(rot)
		self.realpos = (int(x),int(y))
		self.size = size
		self.rect = self.image.get_rect(topleft = ( (int(round(self.realpos[0] - camera.x) * camera.size + univars.screen.get_width()//2 - self.image.get_width()/2)),int(round((self.realpos[1] - camera.y) * camera.size + univars.screen.get_height()//2 - self.image.get_height()/2))))
		self.fakerect = pygame.Rect(x - self.size[0]//2,y - self.size[1]//2,self.size[0] + 10,self.size[1] + 10)
		self.alpha = alpha

	# def inchunk(self,cam,object,dim):
	# 	dist = 1/cam.size * 9
	# 	if cam.x - (dim * dist) - (self.size[0] * dim) <= object[0] <= cam.x + (dim * dist) + (self.size[0] * dim):
	# 		x = True
	# 	else:
	# 		x = False
	# 	if cam.y - (dim * dist) - (self.size[1] * dim) <= object[1] <= cam.y + (dim * dist) + (self.size[1] * dim):
	# 		y = True
	# 	else:
	# 		y = False
	# 	if x and y:
	# 		return True
	# 	else:
	# 		return False

	def update(self,showall):
		camera = Cameramod.cam
		if univars.camchange or univars.poschange or self.newbie:
			self.newbie = False
			realestsize = [math.ceil((self.size[0] * abs(camera.size))/2)*2,math.ceil((self.size[1] * abs(camera.size))/2)*2]
			if not str([self.name,realestsize]) in spritecache.keys():
				self.image =  pygame.transform.scale(self.bart,  realestsize )
				spritecache[str([self.name,realestsize])] = self.image
				dataspritecache.append([self.name,realestsize])
			else:
				self.image = spritecache[str([self.name,realestsize])]
			self.image = pygame.transform.rotate(self.image,self.rot)


		if showall:
			if self.alpha == 0:
				alpha = 170
				self.image.set_alpha(alpha)



		self.rect = self.image.get_rect(
										topleft = 
												(   
													int((round((self.realpos[0] - camera.x)/1) * 1 * camera.size + univars.screen.get_width()//2  - self.image.get_width()/2 ))      ,
													int((round((self.realpos[1] - camera.y)/1) * 1 * camera.size + univars.screen.get_height()//2 - self.image.get_height()/2))  
												)   
													
										)
		



objcache = {}


class obj(pygame.sprite.Sprite):
	def __init__(self,name:str,info:dict,sprites):
		pygame.sprite.Sprite.__init__(self)
		screen = univars.screen
		grandim = univars.grandim
		self.fliped = 0
		self.func = funcs.func(screen,grandim)
		self.info = info
		self.sprites = sprites
		self.fakerect = pygame.Rect(info["pos"][0] - info["size"][0]//2,info["pos"][1] - info["size"][1]//2,info["size"][0],info["size"][1])
		self.name = name

	def supvar(self,lg,lh):
		lst = [(0,0),(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),]	

		for i in lst:
			if lg == [lh[0] + i[0] , lh[1] + i[1]]:
				return True
		return False

	def update(self, camera,om,dim,showall):
		self.info = om.objects[self.name]
		sprite = self.sprites[self.info["sn"]]
		pos = self.info["pos"]
		pos = [int(round(pos[0])),int(round(pos[1]))]
		self.info["pos"] = pos
		self.fakerect = pygame.Rect(self.info["pos"][0] - self.info["size"][0]//2,self.info["pos"][1] - self.info["size"][1]//2,self.info["size"][0],self.info["size"][1])
		if self.info["rendercond"] or showall:
			g = [round(self.info["pos"][0]),round(self.info["pos"][1])]
			h = [round(camera.x),round(camera.y)]
			if univars.func.dist(g,h) < 2000:


				scale = [round(camera.size * self.info["sizen"][0] ,1)* self.info["size"][0],round(camera.size * self.info["sizen"][1],1 )* self.info["size"][1]]

				if not str((self.name,scale,self.info["sn"],self.fliped)) in objcache: 
					b = sprite
					b = pygame.transform.scale(b,scale)
					objcache[str((self.name,scale,self.info["sn"],self.fliped))] = b

				else:
					b = objcache[str((self.name,scale,self.info["sn"],self.fliped))]

				


				
				b.set_alpha(self.info["alpha"])
				b = pygame.transform.rotate(b,self.info["rot"])
				self.image = b
				self.rect = self.image.get_rect(topleft = ( ((pos[0] - camera.x) * round(camera.size,2)) + univars.screen.get_width()//2 - b.get_width()/2 ,(    ((pos[1] - camera.y) * round(camera.size,2)))        + univars.screen.get_height()//2 - b.get_height()/2))
			else:
				self.image = pygame.Surface((0,0))
				self.rect = pygame.Rect(0,0,0,0)
		else:
			self.image = pygame.Surface((0,0))
			self.rect = pygame.Rect(0,0,0,0)


		if self.name in om.toreinst:
			self.reinstsprite(om)

	def reinstsprite(self,om):
		info = om.objects[self.name]
		self.sprites = self.func.getspritesscale(info["sprite"],info["size"])

	def flip(self):
		self.fliped = not self.fliped
		self.sprites = [pygame.transform.flip(i,True,False) for i in self.sprites ]

	