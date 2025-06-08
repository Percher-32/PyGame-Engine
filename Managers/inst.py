import pygame
import funcs
import Cameramod
import univars
cam = Cameramod.cam
class inst(pygame.sprite.Sprite):
	def __init__(self,screen,grandim,name:str,x:int,y:int,rot:int,sizen:list,type:str):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.func = funcs.func(screen,grandim)
		self.sizen = sizen
		self.name = name
		self.type = type
		self.bart = self.func.getsprites(name)[0]
		self.image = self.func.getsprites(name)[0]
		self.rot = rot
		self.realpos = (x + (self.screen.get_width()/30 * (1- self.sizen[0])) ,y + (self.screen.get_width()/30 * (1- self.sizen[1])) )
		self.realestpos = (x,y)
		self.realsize = [self.func.getsprites(name)[0].get_width() * sizen[0],self.func.getsprites(name)[0].get_height() * sizen[1]]
		self.rect = self.image.get_rect(center = (x + cam.x,y + cam.y))

	def inchunk(self,cam,object,dim):
		dist = 1/cam.size * 9
		if cam.x - (dim * dist) - self.realsize[0] <= object[0] <= cam.x + (dim * dist) + self.realsize[0]:
			x = True
		else:
			x = False
		if cam.y - (dim * dist) - self.realsize[1] <= object[1] <= cam.y + (dim * dist) - self.realsize[1]:
			y = True
		else:
			y = False
		if x and y:
			return True
		else:
			return False

	def update(self, camera,fm,dim:int,alpha:int):
		if self.inchunk(camera,self.realestpos,dim):
			self.image =  pygame.transform.rotate(pygame.transform.scale(self.bart,  [self.realsize[0] * abs(camera.size),self.realsize[1] * abs(camera.size)]  ) ,self.rot)
			self.image.set_alpha(alpha)
			self.rect = self.image.get_rect(center = ((self.realpos[0] - camera.x - (self.screen.get_width()/30 * (1- self.sizen[0])) ) * camera.size + self.screen.get_width()//2    ,(self.realpos[1] - camera.y - (self.screen.get_width()/30 * (1- self.sizen[1])) ) * camera.size + self.screen.get_height()//2     ))
		else:
			self.image = pygame.Surface((0,0))

class obj(pygame.sprite.Sprite):
	def __init__(self,name:str,info:dict):
		#info has [
		# 0 = pos
		# 1 = name
		# 2 = type
		# 3 = rot
		# 4 = sn
		# 5 = gothru
		# 6 = rendercond
		# 7 = alpha
		# 8 = layer
		# 9 = type
		# 10 = animname]
		pygame.sprite.Sprite.__init__(self)
		screen = univars.screen
		grandim = univars.grandim
		self.func = funcs.func(screen,grandim)
		self.info = info
		self.sprites = self.func.getspritesscale(info["name"],info["size"])
		self.fakerect = pygame.Rect(info["pos"][0],info["pos"][1],info["size"][0],info["size"][1])
		self.name = name

	def inchunk(self,cam,dist,dim):
		if cam.x - (dim * dist) - self.info["size"][0] <= self.info["pos"][0] <= cam.x + (dim * dist) + self.info["size"][0]:
			x = True
		else:
			x = False
		if cam.y - (dim * dist) - self.info["size"][1] <= self.info["pos"][1] <= cam.y + (dim * dist) - self.info["size"][1]:
			y = True
		else:
			y = False
		if x and y:
			return True
		else:
			return False

	def update(self, camera,om,dim):
		self.info = om.objects[self.name]
		sprite = self.sprites[self.info["sn"]]
		pos = self.info["pos"]
		# if self.inchunk(camera,32,dim):
		if self.info["rendercond"]:
			# self.image =  pygame.transform.rotate(pygame.transform.scale(self.bart,  [self.realsize[0] * abs(camera.size),self.realsize[1] * abs(camera.size)]  ) ,self.rot)
			# self.image.set_alpha(alpha)
			b = sprite
			b = pygame.transform.rotate(b,self.info["rot"])
			b.set_alpha(self.info["alpha"])
			b = pygame.transform.scale(b,[self.info["size"][0] * camera.size,self.info["size"][1] * camera.size])
			self.image = b
			self.rect = self.image.get_rect(topleft = ( (pos[0] - camera.x) * round(camera.size,2) + univars.screen.get_width()//2 - b.get_width()/2 ,(pos[1] - camera.y) * round(camera.size,2) + univars.screen.get_height()//2 - b.get_height()/2))
		else:
			self.image = pygame.Surface((0,0))


		if self.name in om.toreinst:
			self.reinstsprite(om)

	def reinstsprite(self,om):
		info = om.objects[self.name]
		self.sprite = self.func.getspritesscale(info["sprite"],info["size"])[info["sn"]]
		self.fakerect = pygame.Rect(info["pos"][0],info["pos"][1],info["size"][0],info["size"][1])

	