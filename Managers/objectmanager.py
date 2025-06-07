import pickle as pk
import json
import funcs
import pygame
import Textmanager
import itertools
import inst
import os

class object_manager: 
	def __init__(self,realscreeen,screen,grandim,alpha,rend):
		self.objects = {}
		self.values = {}
		self.func = funcs.func(screen,grandim)
		self.screen = screen
		self.realscreen = realscreeen
		self.grandim = grandim
		self.tm = Textmanager.Textmanager(realscreeen)
		self.loadingmap = False
		self.sprites = {}
		self.rects = {}
		self.instances = {}
		self.instables = []
		self.loadedmap = "Null"
		self.renderdist = 32
		self.dodist = 128
		self.tracker = 0
		self.tileup = 1
		self.showmap = 0
		self.loadedchunk = 0
		self.showcolist = []
		self.showall = False
		self.aplhainst = alpha
		self.renderinst = rend
		self.speed = 0

	def moveto(self,info,place):
		self.objects[info][8] = place

	def removecol(self,id):
		if id in self.rects.keys():
			self.rects.pop(id)

	def inchunk(self,campos,object,dim,dist):
		if campos[0] - (dim * dist) <= object[0] <= campos[0] + (dim * dist):
			x = True
		else:
			x = False
		if campos[1] - (dim * dist) <= object[1] <= campos[1] + (dim * dist):
			y = True
		else:
			y = False
		return (x,y)

	def default(self):
		self.objects = {}
		self.values = {}
		self.sprites = {}
		self.rects = {}
		self.loadedmap = "Null"
		self.renderdist = 32
		self.dodist = 128
		self.tracker = 0
		self.tileup = 1
		self.showmap = 0
		self.loadedchunk = 0
		self.showcolist = []
		self.showall = False

	def loadtilemap(self,name):
		# try:
		if not name == "null":
			self.loadedmap = name
			with open(f"Saved/tilemaps/{self.loadedmap}/datap.pickle","rb") as file:
				a = pk.load(file)
			self.objects = a["objects"]
			self.values = a["values"]
			self.rects = a["rects"]
			self.decodeinst(32)
			self.decodespr()
		else:
			self.default()
		# except:
		# 	self.default()

	def savetilemap(self,name):
		if os.path.exists(f"Saved/tilemaps/{name}"):
			return "No"
		else:
			os.mkdir(f"Saved/tilemaps/{name}")
			with open(f"Saved/tilemaps/{name}/datap.pickle","wb") as file:
				todump = {"objects":self.objects,"values":self.values,"rects":self.rects}
				pk.dump(todump,file)
			with open(f"Saved/tilemaps/{name}/dataj.json","w") as file:
				todump = {"names": [ [i,self.objects[i][1],self.sprites[i][0].get_size()] for i in self.objects.keys() ],"instvalues":[ [b.name,b.realpos,b.rot,b.type,b.sizen] for a in self.instances.values() for b in a ]}
				json.dump(todump,file)
			self.loadtilemap(name)
			return "True"
		
	def getcull(self,pos,grid_size,dim) -> list:
		patch = [i for i in list(self.objects.keys()) if (pos[0]) - (grid_size * dim) <= self.objects[i][0][0] <= (pos[0]) + (grid_size * dim)    and (pos[1]) - (grid_size * dim) <= self.objects[i][0][1] <= (pos[1]) + (grid_size * dim)]                                                  
		return patch

	def playanim(self,gm,i,anim,animname):
		if not gm == "none":
			if not self.objects[i][10] == animname:
				self.objects[i][5] = 0
				self.objects[i][10] = animname
			self.objects[i][5] += gm.frame_manager.dt * self.speed
			if round(self.objects[i][5]/5) < len(anim):
				self.objects[i][4] = anim[round(self.objects[i][5]/5)]
			else:
				self.objects[i][10] = "none"

	def decodeinst(self,dim):
		self.instances = {}
		folder = f"Saved/tilemaps/{self.loadedmap}/dataj.json"
		with open(folder,"r") as file:
			a = json.load(file)["instvalues"]
		for i in a:
			self.addinst(i[1],i[0],dim,i[2],i[3],i[4])

	def decodespr(self):
		folder = f"Saved/tilemaps/{self.loadedmap}/dataj.json"
		with open(folder,"r") as file:
			a = json.load(file)["names"]
		for i in a:
			self.sprites[i[0]] = self.func.getspritesscale(i[1],i[2])
		


	def cond(self,id:str,gm,cam):
		name = self.objects[id][1]
		if self.speed == 0:
			self.objects[id][0] = [ round( self.objects[id][0][0]/gm.dim ) * gm.dim      ,   round( self.objects[id][0][1]/gm.dim ) * gm.dim       ]
		if name == "bird":
			self.playanim(gm,id,[0,1,0,1,0],"flap")




	def tilemap(self,i,gm,a,uld,urd,ldr,ulr,lr,ud,n,dt,dl,ur,ul,dr,rt,lt,ut):
		if self.tileup:
			posl = [self.objects[i][0][0] - gm.dim,self.objects[i][0][1]]
			posr = [self.objects[i][0][0] + gm.dim,self.objects[i][0][1]]
			posu = [self.objects[i][0][0],self.objects[i][0][1] - gm.dim]
			posd = [self.objects[i][0][0],self.objects[i][0][1] + gm.dim]
			poslist = dict(zip(self.objects.keys(),(self.objects[i][0] for i in self.objects.keys())))
			l = self.func.getif(poslist,posl)
			r = self.func.getif(poslist,posr)
			u = self.func.getif(poslist,posu)
			d = self.func.getif(poslist,posd)
			if l:
				l = self.objects[self.func.get(poslist,posl)[0]][0] == self.objects[i][0]
			if r:
				r = self.objects[self.func.get(poslist,posr)[0]][0] == self.objects[i][0]
			if u:
				u = self.objects[self.func.get(poslist,posu)[0]][0] == self.objects[i][0]
			if d:
				d = self.objects[self.func.get(poslist,posd)[0]][0] == self.objects[i][0]
			if l and r and u and d:
				self.objects[i][4] = n
			elif l and r and not u and not d:
				self.objects[i][4] = ud
			elif l and r and u and not d:
				self.objects[i][4] = dt
			elif l and r and d and not u:
				self.objects[i][4] = ut
			elif u and l and d and not r:
				self.objects[i][4] = rt
			elif u and r and d and not l:
				self.objects[i][4] = lt
			elif u and d and not l and not r:
				self.objects[i][4] = lr
			elif not u and not d and not l and not r:
				self.objects[i][4] = a
			elif d and l and not u and not r:
				self.objects[i][4] = ur
			elif u and r and not d and not l:
				self.objects[i][4] = dl
			elif u and l and not d and not r:
				self.objects[i][4] = dr
			elif d and not l and not r and not u:
				self.objects[i][4] = ulr
			elif d and r and not l and not u:
				self.objects[i][4] = ul
			elif l and not d and not u and not r:
				self.objects[i][4] = urd
			elif r and not l and not u and not d:
				self.objects[i][4] = uld
			elif u and not d and not l and not r:
				self.objects[i][4] = ldr

	def translate(self,GameManager,id:str,sv:list):
		if not GameManager == "none":
			self.objects[id][0][0] += (sv[0] * GameManager.frame_manager.dt * self.speed) * self.screen.get_width()/self.realscreen.get_width()
			self.objects[id][0][1] -= (sv[1] * GameManager.frame_manager.dt * self.speed) * self.screen.get_width()/self.realscreen.get_width()
			if id in self.rects.keys():
				self.rects[id].center = self.objects[id][0]

	def rotate(self,GameManager,id,ang):
		if not GameManager == "none":
			self.objects[id][3] = self.objects[id][3] + (ang * GameManager.frame_manager.dt * self.speed)

	def scaleto(self,id,scale):
		self.sprites[id] = self.func.getspritesscale(self.objects[id][1],scale)

	def get_value(self,info,name):
		return self.values[info][name]
		
	def set_value(self,info,name,value):
		try:
			self.values[info][name] = value
		except:
			self.values[info] = {}
			self.values[info][name] = value

	def collide(self,id,type,dim):
		r1 = self.rects[id]
		typel = self.getcull(self.objects[id][0],1,dim)
		types = (self.objects[i][2] for i in self.objects.keys())
		typedict = zip(list(self.objects.keys()),types)
		typel2 = self.func.get(typedict,type)
		olist = []
		type3 = self.func.intersect(typel,typel2)
		for i in type3:
			r2 = self.rects[i] 
			if r1.colliderect(r2):
				olist.append(i)
		return olist
	
	def collidein(self,pos,width,type,show,camera,dim) -> list: 
		r1 = pygame.Rect(pos[0], pos[1], width[0],width[1])
		typel = self.getcull(pos,1,dim)
		types = ( i[2] for i in self.objects.values() )
		typedict = dict(zip(list(self.objects.keys()),types))
		typel2 = [self.func.get(typedict,i) for i in type]
		typel2 = list(itertools.chain.from_iterable(typel2))
		type3 = self.func.intersect(typel,typel2)
		type4 = self.func.intersect(type3,self.rects)
		olist = [ i for i in type4 if r1.colliderect(self.rects[i])]
		if show:
			if len(olist) > 0:
				self.func.rectblit([pos[0],pos[1]],width,(0,225,0),camera,dim)
			else:
				self.func.rectblit([pos[0],pos[1]],width,(225,0,0),camera,dim)
			
		return olist

	def collide4(self,posof,wid,i,type,show,camera,dim):
		if posof == "none":
			posof = [[0,0],[0,0],[0,0],[0,0]]
		if not self.showcolist == "all":
			if self.objects[i][0] in self.showcolist:
				show = True
		else:
			show = True

		
		if isinstance(wid[0], int):
			nop = [wid[0],self.sprites[i][int(self.objects[i][4])].get_width()]
			wid[0] = nop
		if isinstance(wid[1], int):
			nop = [wid[1],self.sprites[i][int(self.objects[i][4])].get_width()]
			wid[1] = nop
		if isinstance(wid[2], int):
			nop = [wid[2],self.sprites[i][int(self.objects[i][4])].get_height()]
			wid[2] = nop
		if isinstance(wid[3], int):
			nop = [wid[3],self.sprites[i][int(self.objects[i][4])].get_height()]
			wid[3] = nop

		if wid[0][1] == "none":
			wid[0][1] = self.sprites[i][int(self.objects[i][4])].get_width()
		if wid[1][1] == "none":
			wid[1][1] = self.sprites[i][int(self.objects[i][4])].get_width()
		if wid[2][1] == "none":
			wid[2][1] = self.sprites[i][int(self.objects[i][4])].get_height()
		if wid[3][1] == "none":
			wid[3][1] = self.sprites[i][int(self.objects[i][4])].get_height()

		wid[0][0] *= dim/64
		wid[1][0] *= dim/64
		wid[2][0] *= dim/64
		wid[3][0] *= dim/64

		a = self.collidein( (self.objects[i][0][0] + posof[0][0] + self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[0][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[0][0],wid[0][1]) , type , show , camera ,dim)
		b = self.collidein( (self.objects[i][0][0] + posof[1][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2 - wid[1][0],self.objects[i][0][1] + posof[1][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2) , (wid[1][0],wid[1][1]) , type , show , camera ,dim)
		c = self.collidein( (self.objects[i][0][0] + posof[2][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[2][1]- self.sprites[i][int(self.objects[i][4])].get_height()/2  - wid[2][0]) , (wid[2][1],wid[2][0]) , type , show , camera ,dim)
		d = self.collidein( (self.objects[i][0][0] + posof[3][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[3][1] + self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[3][1],wid[3][0]) , type , show , camera,dim )
		return (a,b,c,d)

	def collideinst4(self,posof,wid,i,type,show,camera,dim):
		if posof == "none":
			posof = [[0,0],[0,0],[0,0],[0,0]]
		if not self.showcolist == "all":
			if self.objects[i][0] in self.showcolist:
				show = True
		else:
			show = True

		
		if isinstance(wid[0], int):
			nop = [wid[0],self.sprites[i][int(self.objects[i][4])].get_width()]
			wid[0] = nop
		if isinstance(wid[1], int):
			nop = [wid[1],self.sprites[i][int(self.objects[i][4])].get_width()]
			wid[1] = nop
		if isinstance(wid[2], int):
			nop = [wid[2],self.sprites[i][int(self.objects[i][4])].get_height()]
			wid[2] = nop
		if isinstance(wid[3], int):
			nop = [wid[3],self.sprites[i][int(self.objects[i][4])].get_height()]
			wid[3] = nop

		if wid[0][1] == "none":
			wid[0][1] = self.sprites[i][int(self.objects[i][4])].get_width()
		if wid[1][1] == "none":
			wid[1][1] = self.sprites[i][int(self.objects[i][4])].get_width()
		if wid[2][1] == "none":
			wid[2][1] = self.sprites[i][int(self.objects[i][4])].get_height()
		if wid[3][1] == "none":
			wid[3][1] = self.sprites[i][int(self.objects[i][4])].get_height()

		wid[0][0] *= dim/64
		wid[1][0] *= dim/64
		wid[2][0] *= dim/64
		wid[3][0] *= dim/64

		a = self.collideinst( (self.objects[i][0][0] + posof[0][0] + self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[0][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[0][0],wid[0][1]) , type , show , camera ,dim)
		b = self.collideinst( (self.objects[i][0][0] + posof[1][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2 - wid[1][0],self.objects[i][0][1] + posof[1][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2) , (wid[1][0],wid[1][1]) , type , show , camera ,dim)
		c = self.collideinst( (self.objects[i][0][0] + posof[2][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[2][1]- self.sprites[i][int(self.objects[i][4])].get_height()/2  - wid[2][0]) , (wid[2][1],wid[2][0]) , type , show , camera ,dim)
		d = self.collideinst( (self.objects[i][0][0] + posof[3][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[3][1] + self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[3][1],wid[3][0]) , type , show , camera,dim )
		return (a,b,c,d)

	def collideinst(self,pos,width,type,show,camera,dim) -> list: 
		r1 = pygame.Rect(pos[0], pos[1], width[0],width[1])
		inpos = (round(pos[0]/(dim * self.renderdist)),round(pos[1]/(dim * self.renderdist)))
		typel = [self.instances.get((inpos,i),"none") for i in type]
		typel = list(itertools.chain.from_iterable(typel))
		if not typel == "none":
			typel2 = [pygame.Rect(sprite.realpos[0]- dim/2,sprite.realpos[1]- dim/2,sprite.realsize[0],sprite.realsize[1]) for sprite in typel]
			if not r1.collidelist(typel2) == -1:
				olist = True
			else:
				olist = False
		else:
			olist = False

		if show:
			if olist:
				self.func.rectblit([pos[0],pos[1]],width,(0,225,0),camera,dim)
			else:
				self.func.rectblit([pos[0],pos[1]],width,(225,0,0),camera,dim)
			
		return olist

	def collidepb(self,pos,type,show,camera,size,dim) -> list: 
		typel = self.getcull(pos,1,dim)
		types = ( i[2] for i in self.objects.values() )
		typedict = dict(zip(list(self.objects.keys()),types))
		typel2 = [self.func.get(typedict,i) for i in type]
		typel2 = list(itertools.chain.from_iterable(typel2))
		type3 = self.func.intersect(typel,typel2)
		type4 = self.func.intersect(type3,self.rects)
		olist = [ i for i in type4 if self.rects[i].collidepoint(pos)]
		if show:
			if len(olist) > 0:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(0,225,0),camera,dim)
			else:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(225,0,0),camera,dim)
		if len(olist) > 0:
			return True
		else:
			return False
		
	def collidep(self,pos,type,show,camera,size,dim) -> list: 
		typel = self.getcull(pos,1,dim)
		types = ( i[2] for i in self.objects.values() )
		typedict = dict(zip(list(self.objects.keys()),types))
		typel2 = [self.func.get(typedict,i) for i in type]
		typel2 = list(itertools.chain.from_iterable(typel2))
		type3 = self.func.intersect(typel,typel2)
		type4 = self.func.intersect(type3,self.rects)
		olist = [ i for i in type4 if self.rects[i].collidepoint(pos)]
		if show:
			if len(olist) > 0:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(0,225,0),camera,dim)
			else:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(225,0,0),camera,dim)
		return olist
		
	def collidepinstb(self,pos,type,show,camera,size,dim) -> bool: 
		inpos = (round(pos[0]/(dim * self.renderdist)),round(pos[1]/(dim * self.renderdist)))
		typel = [self.instances.get((inpos,i),"none") for i in type ]
		olist = []
		for a in typel:
			if not a == "none":
				typel2 = [pygame.Rect(sprite.realpos[0]- dim/2,sprite.realpos[1]- dim/2,sprite.realsize[0],sprite.realsize[1]) for sprite in a  ]
				for i in typel2:
					if i.collidepoint(pos):
						olist.append(i)
		
		if len(olist) > 0:
			if show:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(0,225,0),camera,dim)
			return True
		else:
			if show:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(225,0,0),camera,dim)
			return False
			
	def collidepinst(self,pos,type,show,camera,size,dim) -> bool: 
		inpos = (round(pos[0]/(dim * self.renderdist)),round(pos[1]/(dim * self.renderdist)))
		typel = [self.instances.get((inpos,i),"none") for i in type ]
		olist = []
		for a in typel:
			if not a == "none":
				typel2 = [  [pygame.Rect(sprite.realpos[0]- dim/2,sprite.realpos[1]- dim/2,sprite.realsize[0],sprite.realsize[1]),sprite] for sprite in a  ]
				for i in typel2:
					# self.func.rectblit([i[0].x,i[0].y],[i[0].width,i[0].height],(0,225,0),camera,dim)
					if i[0].collidepoint(pos):
						olist.append(i[1])


		if len(olist) > 0:
			if show:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(0,225,0),camera,dim)
		else:
			if show:
				self.func.rectblit([pos[0],pos[1]],[(1/camera.size) * size,(1/camera.size) * size],(225,0,0),camera,dim)
				
		return olist

	def collide9(self,i,type,show,camera,point_size,dim) -> dict:
		x = self.objects[i][0][0]
		y = self.objects[i][0][1]
		w = self.sprites[i][0].get_width()/2
		h = self.sprites[i][0].get_height()/2
		a = self.collidep((x - w,y - w),type,show,camera,point_size,dim)
		b = self.collidep((x  ,  y - w),type,show,camera,point_size,dim)
		c = self.collidep((x + w,y - w),type,show,camera,point_size,dim)
		d = self.collidep((x - w,  y  ),type,show,camera,point_size,dim)
		e = self.collidep((x    ,  y  ),type,show,camera,point_size,dim)
		f = self.collidep((x + w,  y  ),type,show,camera,point_size,dim)
		g = self.collidep((x - w,y + w),type,show,camera,point_size,dim)
		j = self.collidep((x  ,  y + w),type,show,camera,point_size,dim)
		k = self.collidep((x + w,y + w),type,show,camera,point_size,dim)
		ans = { "topleft":a,"topmid":b,"topright":c,"midleft":d,"midmid":e,"midright":f,"botleft":g,"botmid":j,"botright":k}
		return ans

	def collideinst9(self,i,type,show,camera,point_size,dim) -> dict:
		x = self.objects[i][0][0]
		y = self.objects[i][0][1]
		w = self.sprites[i][0].get_width()/2
		h = self.sprites[i][0].get_height()/2
		a = self.collidepinst((x - w,y - h),type,show,camera,point_size,dim)
		b = self.collidepinst((x  ,  y - h),type,show,camera,point_size,dim)
		c = self.collidepinst((x + w,y - h),type,show,camera,point_size,dim)
		d = self.collidepinst((x - w,  y  ),type,show,camera,point_size,dim)
		e = self.collidepinst((x    ,  y  ),type,show,camera,point_size,dim)
		f = self.collidepinst((x + w,  y  ),type,show,camera,point_size,dim)
		g = self.collidepinst((x - w,y + h),type,show,camera,point_size,dim)
		j = self.collidepinst((x  ,  y + h),type,show,camera,point_size,dim)
		k = self.collidepinst((x + w,y + h),type,show,camera,point_size,dim)
		l = a or d or g
		u = a or b or c
		r = c or f or k
		p = g or j or k
		ans = { "topleft":a,"topmid":b,"topright":c,"midleft":d,"midmid":e,"midright":f,"botleft":g,"botmid":j,"botright":k,"left":l,"up":u,"right":r,"down":p}
		return ans

	def collide9b(self,i,type,show,camera,point_size,dim) -> dict:
		x = self.objects[i][0][0]
		y = self.objects[i][0][1]
		w = self.sprites[i][0].get_width()/2
		h = self.sprites[i][0].get_height()/2
		a = self.collidep((x - w,y - w),type,show,camera,point_size,dim)
		b = self.collidep((x  ,  y - w),type,show,camera,point_size,dim)
		c = self.collidep((x + w,y - w),type,show,camera,point_size,dim)
		d = self.collidep((x - w,  y  ),type,show,camera,point_size,dim)
		e = self.collidep((x    ,  y  ),type,show,camera,point_size,dim)
		f = self.collidep((x + w,  y  ),type,show,camera,point_size,dim)
		g = self.collidep((x - w,y + w),type,show,camera,point_size,dim)
		j = self.collidep((x  ,  y + w),type,show,camera,point_size,dim)
		k = self.collidep((x + w,y + w),type,show,camera,point_size,dim)
		ans = { "topleft":a,"topmid":b,"topright":c,"midleft":d,"midmid":e,"midright":f,"botleft":g,"botmid":j,"botright":k}
		return ans

	def collideinst9b(self,i,type,show,camera,point_size,dim) -> dict:
		x = self.objects[i][0][0]
		y = self.objects[i][0][1]
		w = self.sprites[i][0].get_width()/2
		h = self.sprites[i][0].get_height()/2
		a = self.collidepinstb((x - w,y - h),type,show,camera,point_size,dim)
		b = self.collidepinstb((x  ,  y - h),type,show,camera,point_size,dim)
		c = self.collidepinstb((x + w,y - h),type,show,camera,point_size,dim)
		d = self.collidepinstb((x - w,  y  ),type,show,camera,point_size,dim)
		e = self.collidepinstb((x    ,  y  ),type,show,camera,point_size,dim)
		f = self.collidepinstb((x + w,  y  ),type,show,camera,point_size,dim)
		g = self.collidepinstb((x - w,y + h),type,show,camera,point_size,dim)
		j = self.collidepinstb((x  ,  y + h),type,show,camera,point_size,dim)
		k = self.collidepinstb((x + w,y + h),type,show,camera,point_size,dim)
		l = a or d or g
		u = a or b or c
		r = c or f or k
		p = g or j or k
		ans = { "topleft":a,"topmid":b,"topright":c,"midleft":d,"midmid":e,"midright":f,"botleft":g,"botmid":j,"botright":k,"left":l,"up":u,"right":r,"down":p}
		return ans


	def remove(self,pos:list,dim:int):
		poslist = dict(zip(self.objects.keys(),(self.objects[i][0] for i in self.objects.keys())))
		postodel = self.func.get(poslist,[pos[0],pos[1]])
		if not postodel == []:
			self.objects.pop(postodel[0])
			if postodel[0] in self.sprites.keys():
				self.sprites.pop(postodel[0])
			if postodel[0] in self.rects.keys():
				self.rects.pop(postodel[0])
		lof = [  b   for b in self.instances.keys() if b[0] == ( round(pos[0]/(dim * self.renderdist)),round(pos[1]/(dim * self.renderdist))   )]
		if len(lof) > 0:
			rems = [(i,b) for i in lof for b in self.instances[i] if b.realestpos == pos ]
			for i in rems:
				self.instances[i[0]].remove(i[1])

	def addinst(self,pos:tuple,name:str,dim:int,rot:int,type:str,sizen):
		self.remove(pos,dim)
		newt = inst.inst(self.screen,self.grandim,name,pos[0],pos[1],rot,sizen,type)
		name = ((round(pos[0]/(dim * self.renderdist)),round(pos[1]/(dim * self.renderdist))),type)
		try:
			self.instances[name].add(newt)
		except:
			self.instances[name] = pygame.sprite.Group()
			self.instances[name].add(newt)

	def add(self,pos:tuple,sprites:str,rot:int,type,sizen,dim:int):
		if not sprites in self.instables:
			self.remove(pos,dim)
			self.tracker += 1
			dummy  = self.func.getsprites(sprites)[0]
			size = [dummy.get_width() * sizen[0],dummy.get_height() * sizen[1]]
			realsprite = self.func.getspritesscale(sprites,size)
			rect = pygame.Surface.get_rect(realsprite[0])
			rect.center = (pos[0],pos[1])
			add = [list(pos),sprites,type,rot,0,0,1,1000,0,sprites,"none"]
			self.objects.update({str(self.tracker):add})
			self.sprites.update({str(self.tracker):realsprite})
			self.rects.update({str(self.tracker):rect})
		else:
			self.addinst(pos,sprites,dim,rot,type,sizen)

	def adds(self,pos,sprites,type,info,rot,size,alpha,layer):
		dummy  = self.func.getsprites(sprites)[0]
		if size == "none":
			size = [dummy.get_width(),dummy.get_height()]
		realsprite = self.func.getspritesscale(sprites,size)
		rect = pygame.Surface.get_rect(realsprite[0])
		rect.center = (pos[0],pos[1])
		add = [list(pos),sprites,type,rot,0,0,1,alpha,layer,type,"none"]
		self.objects[info] = add
		self.sprites[info] = realsprite
		self.rects[info] = rect

	def tile(self):
		speed = self.speed
		self.speed = 0
		self.tileup = 1
		for i in self.objects.keys():
			self.cond(i,"none","none")
		self.tileup = 0
		self.speed = speed

	def render(self,camera,GameManager,dim:int):
		campos = [round(camera.x),round(camera.y)]
		camposdim = [round(camera.x/(dim * self.renderdist)),round(camera.y/(dim * self.renderdist))]
		ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
		layerlike = [self.objects[i][8] for i in self.objects.keys()   if not self.objects[i][1] == "inst"]
		lof = [  b   for b in self.instances.keys() for i in ranges   if b[0] == ( i[0]  + camposdim[0],i[1] + camposdim[1]   )]
		if len(lof) > 0:
			for i in lof:
				# print(self.renderinst)
				# print(i[1])
				if not i[1] in self.renderinst:
					alpha = 400
					if i[1] in self.aplhainst.keys():
						alpha = self.aplhainst[i[1]]
					self.instances[i].update(camera,GameManager.frame_manager,GameManager.dim,alpha)
					self.instances[i].draw(self.screen)
				elif self.showall:
					self.instances[i].update(camera,GameManager.frame_manager,GameManager.dim,100)
					self.instances[i].draw(self.screen)



		if len(layerlike) > 0:
			for a in sorted(set(layerlike)):
				layerdict = dict(zip(self.objects.keys(),layerlike))
				newval = self.func.get(layerdict,a)
				newpos = self.getcull(campos,(1/camera.size) * 64/3,dim)
				for i in self.func.intersect(newval,newpos):
					temp_surf = self.sprites[i][self.objects[i][4]]
					if self.objects[i][6]:
						temp_surf.set_alpha(self.objects[i][7])
						GameManager.blitsurf(temp_surf,self.objects[i][0],self.objects[i][3],camera)
					else:
						if self.showall:
							temp_surf.set_alpha(70)
							GameManager.blitsurf(temp_surf,self.objects[i][0],self.objects[i][3],camera)


		for i in self.getcull(campos,(1/camera.size) * 128,dim):
			self.cond(i,GameManager,camera)
		if self.showmap:
			self.tm.drawtext2(f"Map : {self.loadedmap}","pixel2.ttf",40,0,0,0,(50,50,50),-0.97,0.75)
		self.tileup = 0
