import pickle as pk
import json
import funcs
import pygame
import Textmanager
import itertools
import inst
import time
import univars
import os
# from render import render

class object_manager: 
	def __init__(self,realscreeen,screen,grandim,alpha,rend):
		self.objects = {}
		self.values = {}
		self.layers = {}
		self.func = funcs.func(screen,grandim)
		self.screen = screen
		self.realscreen = realscreeen
		self.grandim = grandim
		self.tm = Textmanager.Textmanager(realscreeen)
		self.loadingmap = False
		#chunk id stored in a tuple "(x,y)"
		self.instances = {}
		self.instables = []
		self.toreinst = []
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
		patch = [i for i in list(self.objects.keys()) if (pos[0]) - (grid_size * dim) <= self.objects[i]["pos"][0] <= (pos[0]) + (grid_size * dim)    and (pos[1]) - (grid_size * dim) <= self.objects[i]["pos"][1] <= (pos[1]) + (grid_size * dim)]                                                  
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
			self.objects[id]["pos"][0] += (sv[0] * GameManager.frame_manager.dt * self.speed) * self.screen.get_width()/self.realscreen.get_width()
			self.objects[id]["pos"][1] -= (sv[1] * GameManager.frame_manager.dt * self.speed) * self.screen.get_width()/self.realscreen.get_width()
			if id in self.rects.keys():
				self.rects[id].center = self.objects[id][0]

	def rotate(self,GameManager,id,ang):
		if not GameManager == "none":
			self.objects[id]["rot"] += (ang * GameManager.frame_manager.dt * self.speed)

	def scaleto(self,id,scale):
		self.sprites[id] = self.func.getspritesscale(self.objects[id][1],scale)

	def get_value(self,info,name):
		return self.values[info][name]
		
	def set_value(self,id,name,value):
		try:
			self.values[id][name] = value
		except:
			self.values[id] = {}
			self.values[id][name] = value

	def objfromid(self,id):
		for a in self.layers.keys():
			layer = self.layers[a]
			for b in layer:
				if str(b.name) == str(id):
					return b

	def collide(self,id,show,camera) -> dict:
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" """
		if not self.objfromid(id) == None:
			#coll for non-inst
			dim = univars.grandim
			id = str(id)
			r1 = self.objfromid(id).fakerect
			typel = self.getcull(self.objects[id]["pos"],1,dim)
			typel.remove(id)
			noninst = []
			[noninst.append(self.objfromid(i)) for i in typel if r1.colliderect(self.objfromid(i).fakerect) ]

			#coll for inst
			camchunk = (int(round(r1.x/(dim * self.renderdist))),int(round(r1.y/(dim * self.renderdist))))
			inst = []
			if camchunk in self.instances.keys():
				inst = [ i for i in self.instances[camchunk] if r1.colliderect(i.fakerect)]

			#render the collbox
			if show:
				if len(inst or noninst) > 0:
					col = (0,225,0)
				else:
					col = (225,0,0)
				self.func.ssblitrect(r1,col,camera,5)


			return {"noninst":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}

	def colliderect(self,pos,dimensions,show,camera) -> dict:
		"""return noninst:obj[]   return inst:inst[]"""
		#coll for non-inst
		dim = univars.grandim
		id = str(id)
		r1 = pygame.Rect(pos[0],pos[1],dimensions[0],dimensions[1])
		typel = self.getcull(pos,1,dim)
		noninst = []
		[noninst.append(self.objfromid(i)) for i in typel if r1.colliderect(self.objfromid(i).fakerect) ]

		#coll for inst
		camchunk = (int(round(pos[0]/(dim * self.renderdist))),int(round(pos[1]/(dim * self.renderdist))))
		inst = []
		if camchunk in self.instances.keys():
			inst = [ i for i in self.instances[camchunk] if r1.colliderect(i.fakerect)]

		#render the collbox
		if show:
			if len(inst or noninst) > 0:
				col = (0,225,0)
			else:
				col = (225,0,0)
			self.func.ssblitrect(r1,col,camera,5)


		return {"noninst":noninst,"inst":inst}


	# def tempcollide4(self,posof,wid,i,type,show,camera,dim):
	# 	if posof == "none":
	# 		posof = [[0,0],[0,0],[0,0],[0,0]]
	# 	if not self.showcolist == "all":
	# 		if self.objects[i][0] in self.showcolist:
	# 			show = True
	# 	else:
	# 		show = True

		
	# 	if isinstance(wid[0], int):
	# 		nop = [wid[0],self.sprites[i][int(self.objects[i][4])].get_width()]
	# 		wid[0] = nop
	# 	if isinstance(wid[1], int):
	# 		nop = [wid[1],self.sprites[i][int(self.objects[i][4])].get_width()]
	# 		wid[1] = nop
	# 	if isinstance(wid[2], int):
	# 		nop = [wid[2],self.sprites[i][int(self.objects[i][4])].get_height()]
	# 		wid[2] = nop
	# 	if isinstance(wid[3], int):
	# 		nop = [wid[3],self.sprites[i][int(self.objects[i][4])].get_height()]
	# 		wid[3] = nop

	# 	if wid[0][1] == "none":
	# 		wid[0][1] = self.sprites[i][int(self.objects[i][4])].get_width()
	# 	if wid[1][1] == "none":
	# 		wid[1][1] = self.sprites[i][int(self.objects[i][4])].get_width()
	# 	if wid[2][1] == "none":
	# 		wid[2][1] = self.sprites[i][int(self.objects[i][4])].get_height()
	# 	if wid[3][1] == "none":
	# 		wid[3][1] = self.sprites[i][int(self.objects[i][4])].get_height()

	# 	wid[0][0] *= dim/64
	# 	wid[1][0] *= dim/64
	# 	wid[2][0] *= dim/64
	# 	wid[3][0] *= dim/64

	# 	a = self.collidein( (self.objects[i][0][0] + posof[0][0] + self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[0][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[0][0],wid[0][1]) , type , show , camera ,dim)
	# 	b = self.collidein( (self.objects[i][0][0] + posof[1][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2 - wid[1][0],self.objects[i][0][1] + posof[1][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2) , (wid[1][0],wid[1][1]) , type , show , camera ,dim)
	# 	c = self.collidein( (self.objects[i][0][0] + posof[2][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[2][1]- self.sprites[i][int(self.objects[i][4])].get_height()/2  - wid[2][0]) , (wid[2][1],wid[2][0]) , type , show , camera ,dim)
	# 	d = self.collidein( (self.objects[i][0][0] + posof[3][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[3][1] + self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[3][1],wid[3][0]) , type , show , camera,dim )
	# 	return (a,b,c,d)
	


	# # def collideinst4(self,posof,wid,i,type,show,camera,dim):
	# # 	if posof == "none":
	# # 		posof = [[0,0],[0,0],[0,0],[0,0]]
	# # 	if not self.showcolist == "all":
	# # 		if self.objects[i][0] in self.showcolist:
	# # 			show = True
	# # 	else:
	# # 		show = True

		
	# # 	if isinstance(wid[0], int):
	# # 		nop = [wid[0],self.sprites[i][int(self.objects[i][4])].get_width()]
	# # 		wid[0] = nop
	# # 	if isinstance(wid[1], int):
	# # 		nop = [wid[1],self.sprites[i][int(self.objects[i][4])].get_width()]
	# # 		wid[1] = nop
	# # 	if isinstance(wid[2], int):
	# # 		nop = [wid[2],self.sprites[i][int(self.objects[i][4])].get_height()]
	# # 		wid[2] = nop
	# # 	if isinstance(wid[3], int):
	# # 		nop = [wid[3],self.sprites[i][int(self.objects[i][4])].get_height()]
	# # 		wid[3] = nop

	# # 	if wid[0][1] == "none":
	# # 		wid[0][1] = self.sprites[i][int(self.objects[i][4])].get_width()
	# # 	if wid[1][1] == "none":
	# # 		wid[1][1] = self.sprites[i][int(self.objects[i][4])].get_width()
	# # 	if wid[2][1] == "none":
	# # 		wid[2][1] = self.sprites[i][int(self.objects[i][4])].get_height()
	# # 	if wid[3][1] == "none":
	# # 		wid[3][1] = self.sprites[i][int(self.objects[i][4])].get_height()

	# # 	wid[0][0] *= dim/64
	# # 	wid[1][0] *= dim/64
	# # 	wid[2][0] *= dim/64
	# # 	wid[3][0] *= dim/64

	# # 	a = self.collideinst( (self.objects[i][0][0] + posof[0][0] + self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[0][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[0][0],wid[0][1]) , type , show , camera ,dim)
	# # 	b = self.collideinst( (self.objects[i][0][0] + posof[1][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2 - wid[1][0],self.objects[i][0][1] + posof[1][1] - self.sprites[i][int(self.objects[i][4])].get_height()/2) , (wid[1][0],wid[1][1]) , type , show , camera ,dim)
	# # 	c = self.collideinst( (self.objects[i][0][0] + posof[2][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[2][1]- self.sprites[i][int(self.objects[i][4])].get_height()/2  - wid[2][0]) , (wid[2][1],wid[2][0]) , type , show , camera ,dim)
	# # 	d = self.collideinst( (self.objects[i][0][0] + posof[3][0] - self.sprites[i][int(self.objects[i][4])].get_width()/2,self.objects[i][0][1] + posof[3][1] + self.sprites[i][int(self.objects[i][4])].get_height()/2)             , (wid[3][1],wid[3][0]) , type , show , camera,dim )
	# # 	return (a,b,c,d)

	# # def collideinst(self,pos,width,type,show,camera,dim) -> list: 
	# 	r1 = pygame.Rect(pos[0], pos[1], width[0],width[1])
	# 	inpos = (round(pos[0]/(dim * self.renderdist)),round(pos[1]/(dim * self.renderdist)))
	# 	typel = [self.instances.get((inpos,i),"none") for i in type]
	# 	typel = list(itertools.chain.from_iterable(typel))
	# 	if not typel == "none":
	# 		typel2 = [pygame.Rect(sprite.realpos[0]- dim/2,sprite.realpos[1]- dim/2,sprite.realsize[0],sprite.realsize[1]) for sprite in typel]
	# 		if not r1.collidelist(typel2) == -1:
	# 			olist = True
	# 		else:
	# 			olist = False
	# 	else:
	# 		olist = False

	# 	if show:
	# 		if olist:
	# 			self.func.rectblit([pos[0],pos[1]],width,(0,225,0),camera,dim)
	# 		else:
	# 			self.func.rectblit([pos[0],pos[1]],width,(225,0,0),camera,dim)
			
	# 	return olist

	def collidep(self,pos,show,camera,dim,pointsize=5,instcol = (0,225,0),noninstcol=(0,225,150),ignore_id = None) -> dict: 
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" """
		#coll for non-inst
		dim = univars.grandim
		typel = self.getcull(pos,1,dim)
		noninst = []
		[noninst.append(self.objfromid(i)) for i in typel if self.objfromid(i).fakerect.collidepoint(pos)  and not self.objfromid(i).name == ignore_id ]

		#coll for inst
		camchunk = (int(round(pos[0]/(dim * self.renderdist))),int(round(pos[1]/(dim * self.renderdist))))
		inst = []
		if camchunk in self.instances.keys():
			inst = [ i for i in self.instances[camchunk] if i.fakerect.collidepoint(pos)]

		#render the collpoint
		r1 = pygame.Rect(pos[0],pos[1],(1/camera.size) * pointsize,(1/camera.size) * pointsize)
		if show:
			if len(inst) > 0:
				col = instcol
			elif len(noninst) > 0:
				col = noninstcol
			else:
				col = (225,0,0)
			self.func.ssblitrect(r1,col,camera,0)


		
		return {"obj":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}


	def collide9(self,id,show,camera,dim,pointsize = 5,offsets = { "topleft":[0,0],"topmid":[0,0],"topright":[0,0],"midleft":[0,0],"midmid":[0,0],"midright":[0,0],"botleft":[0,0],"botmid":[0,0],"botright":[0,0]}) -> dict:
		"""points ->  [topleft , topmid , topright  , midleft  , midmid  ,  midright  ,  botleft  , botmid  , botleft] . for each point ( collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if")   """
		if id in self.objects.keys():
			x = self.objects[id]["pos"][0]
			y = self.objects[id]["pos"][1]
			w = self.objects[id]["size"][0]/2
			h = self.objects[id]["size"][1]/2
			
			topleft  = self.collidep((x - w +  offsets["topleft"][0]  ,  y - h +  offsets["topleft"][1]),show,camera,dim,pointsize,ignore_id=id)
			topmid   = self.collidep((x     +   offsets["topmid"][0]  ,  y - h +   offsets["topmid"][1]),show,camera,dim,pointsize,ignore_id=id)
			topright = self.collidep((x + w + offsets["topright"][0]  ,  y - h + offsets["topright"][1]),show,camera,dim,pointsize,ignore_id=id)
			midleft  = self.collidep((x - w +  offsets["midleft"][0]  ,    y   +  offsets["midleft"][1]),show,camera,dim,pointsize,ignore_id=id)
			midmid   = self.collidep((x     +   offsets["midmid"][0]  ,    y   +   offsets["midmid"][1]),show,camera,dim,pointsize,ignore_id=id)
			midright = self.collidep((x + w + offsets["midright"][0]  ,    y   + offsets["midright"][1]),show,camera,dim,pointsize,ignore_id=id)
			botleft  = self.collidep((x - w +  offsets["botleft"][0]  ,  y + h +  offsets["botleft"][1]),show,camera,dim,pointsize,ignore_id=id)
			botmid   = self.collidep((x     +   offsets["botmid"][0]  ,  y + h +   offsets["botmid"][1]),show,camera,dim,pointsize,ignore_id=id)
			botright = self.collidep((x + w + offsets["botright"][0]  ,  y + h + offsets["botright"][1]),show,camera,dim,pointsize,ignore_id=id)
			ans = { "topleft":topleft,"topmid":topmid,"topright":topright,"midleft":midleft,"midmid":midmid,"midright":midright,"botleft":botleft,"botmid":botmid,"botright":botright}
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

	def remove(self,pos):
		postodel = self.func.get(dict(zip(self.objects.keys(),(self.objects[i]["pos"] for i in self.objects.keys()))),[pos[0],pos[1]])


		#deleting non-instances
		if not postodel == []:
			self.objects.pop(postodel[0])
			for a in self.layers.keys():
				layer = self.layers[a]
				for b in layer:
					if b.name == postodel[0]:
						self.layers[a].remove(b)


		#deleting instances
		for a in self.instances.keys():
			for inst in self.instances[a]:
				if int(round(inst.realpos[0])) == int(pos[0]) and int(round(inst.realpos[1])) == int(pos[1]):
					self.instances[a].remove(inst)

	def addinst(self,pos:tuple,name:str,dim:int,rot:int,type:str,sizen):
		self.remove(list(pos))
		if not type in self.renderinst:
			if not type in self.aplhainst.keys():
				alp = 400
			else:
				alp = self.aplhainst[type]
		else:
			alp = 0
		newt = inst.inst(self.screen,self.grandim,name,pos[0],pos[1],rot,sizen,type,alp)
		name = (int(round(pos[0]/(dim * self.renderdist))),int(round(pos[1]/(dim * self.renderdist))))
		if name in self.instances.keys():
			self.instances[name].add(newt)
		else:
			self.instances[name] = pygame.sprite.Group()
			self.instances[name].add(newt)

	def add(self,pos:tuple,sprites:str,rot:int,type,sizen,dim:int):
		if not sprites in self.instables:
			layer = 0
			self.remove(pos)
			self.tracker += 1
			dummy  = self.func.getsprites(sprites)[0]
			size = [dummy.get_width() * sizen[0],dummy.get_height() * sizen[1]]
			realsprite = self.func.getspritesscale(sprites,size)
			rect = pygame.Surface.get_rect(realsprite[0])
			rect.center = (pos[0],pos[1])
			add = {"pos":list(pos),"name":sprites,"type":sprites,"rot":rot,"sn":0,"gothru":0,"rendercond":1,"alpha":1000,"layer":0,"animname":"none","size":size}
			self.objects.update({str(self.tracker):add})
			finalobj = inst.obj(str(self.tracker),add)
			if not layer in self.layers.keys():
				self.layers[layer] = pygame.sprite.Group()
			self.layers[layer].add(finalobj)
			# self.sprites.update({str(self.tracker):realsprite})
			# self.rects.update({str(self.tracker):rect})
		else:
			self.addinst(pos,sprites,dim,rot,type,sizen)

	def adds(self,name,pos,sprites,type,rot,size,alpha,layer):
		"""add special for more unique items"""
		dummy  = self.func.getsprites(sprites)[0]
		size = [dummy.get_width() * size[0],dummy.get_height() * size[1]]
		realsprite = self.func.getspritesscale(sprites,size)
		rect = pygame.Surface.get_rect(realsprite[0])
		rect.center = (pos[0],pos[1])
		add = {"pos":list(pos),"name":sprites,"type":type,"rot":rot,"sn":0,"gothru":0,"rendercond":1,"alpha":alpha,"layer":layer,"animname":"none","size":size}
		self.objects.update({str(name):add})
		finalobj = inst.obj(str(name),add)
		if not layer in self.layers.keys():
			self.layers[layer] = pygame.sprite.Group()
		self.layers[layer].add(finalobj)

	def tile(self):
		speed = self.speed
		self.speed = 0
		self.tileup = 1
		for i in self.objects.keys():
			self.cond(i,"none","none")
		self.tileup = 0
		self.speed = speed

	def render(self,camera,GameManager,dim:int):
		# start_time = time.time()
		#camera-chunk
		camposdim = [round(camera.x/(dim * self.renderdist)),round(camera.y/(dim * self.renderdist))]
		#availabe chunks
		ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
		#the instanciate chunks to be rendered
		lof = [  b   for b in self.instances.keys() for i in ranges   if b == ( i[0]  + camposdim[0],i[1] + camposdim[1]   )]

		#rendering the instanciates
		if len(lof) > 0:
			for i in lof:
				self.instances[i].update(camera,GameManager.dim,self.showall)
				self.instances[i].draw(self.screen)

		#rendering the non-instanciates
		for groupid in sorted(self.layers.keys()):
			self.layers[groupid].update(camera,self,dim)
			self.layers[groupid].draw(self.screen)

		if self.showmap:
			self.tm.drawtext2(f"Map : {self.loadedmap}","pixel2.ttf",40,0,0,0,(50,50,50),-0.97,0.75)
		# end_time = time.time()

