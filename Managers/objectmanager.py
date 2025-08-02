import pickle as pk
import json
import Managers.funcs as funcs
import pygame
import Managers.Textmanager as Textmanager
import itertools
import Managers.inst as inst
import time
import Managers.univars as univars
import os
import math
# from render import render



class object_manager: 
	def __init__(self,realscreeen,screen,grandim,alpha,rend):
		self.objects = {}
		self.values = {}
		self.layers = {}
		self.anims = {}
		self.forceplay = {}
		self.func = funcs.func(screen,grandim)
		self.screen = screen
		self.realscreen = realscreeen
		self.grandim = univars.grandim
		self.tm = Textmanager.Textmanager(realscreeen)
		self.loadingmap = False
		#chunk id stored in a tuple "(x,y)"
		self.instances = {}
		self.instables = []
		self.toreinst = []
		self.loadedmap = "Null"
		self.renderdist = univars.renderdist
		self.dodist = 128
		self.tracker = 0
		self.tileup = 1
		self.showmap = 0
		self.loadedchunk = 0
		self.showcolist = []
		self.showall = False
		self.aplhainst = alpha
		self.renderinst = rend
		self.spritecache = {"hi":"hello"}
		self.speed = 0
		self.animations = {}

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
		self.layers = {}
		self.loadingmap = False
		#chunk id stored in a tuple "(x,y)"
		self.instances = {}
		self.instables = []
		self.toreinst = []
		self.loadedmap = "Null"
		self.renderdist = univars.renderdist
		self.dodist = 128
		self.tracker = 0
		self.tileup = 1
		self.showmap = 0
		self.loadedchunk = 0
		self.showcolist = []
		self.showall = False
		self.speed = 0

	def loadtilemap(self,name):
		if not name == "null" and os.path.exists(f"Saved/tilemaps/{name}"):
			self.default()
			self.loadedmap = name
			self.decodeinst()
			self.decodeobj()
		else:
			self.default()

	def savetilemap(self,name,check = False):
		if os.path.exists(f"Saved/tilemaps/{name}") and not check:
			return "No"
		else:
			if not check:
				os.mkdir(f"Saved/tilemaps/{name}")
			with open(f"Saved/tilemaps/{name}/inst.json","w") as file:
				todump = self.encodeinst()
				json.dump(todump,file)
			with open(f"Saved/tilemaps/{name}/non-inst.json","w") as file:
				todump = self.objects
				json.dump(todump,file)
			self.loadtilemap(name)
			return "True"
		
	def forcesavetilemap(self,name):
		self.savetilemap(name,check=True)
		

	def getcull(self,pos,grid_size,dim) -> list:
		return [i for i in list(self.objects.keys()) if pos[0] - grid_size * dim <= self.objects[i]["pos"][0] <= pos[0] + grid_size * dim  and pos[1] - grid_size * dim <= self.objects[i]["pos"][1] <= (pos[1]) + grid_size * dim]                                                  





	def playanim(self,dt,id,name,forceplay = False):
		a = name
		if not self.objects[id]["animname"] == name:
			if forceplay:
				self.objects[id]["animname"] = name
				self.objects[id]["gothru"] = 0
			else:
				if self.objects[id]["gothru"] == 0:
					self.objects[id]["animname"] = name
		
		
		frame = int(round(self.objects[id]["gothru"]))
		g = self.animations[self.objects[id]['name']][a].keys()
		g = [int(i) for i in g]
		if not frame >= max(g):
			self.objects[id]["gothru"] += dt/10
			if frame in g:
				self.objects[id]["sn"] = self.animations[self.objects[id]['name']][a][str(frame)]
		else:
			self.objects[id]["gothru"] = 0
		


	def saveanim(self,name:str,animname:str,anim:dict):
		""""obj -> name of object   animname -> animation name  , anim -> actual animation"""
		if not os.path.exists(f"Saved/animations/{name}"):
			os.mkdir(f"Saved/animations/{name}")
		with open(f"Saved/animations/{name}/{animname}.json","w") as file:
			json.dump(anim,file)
			


	def loadanim(self,name,animname):
		"""obj -> name   , animname -> animation name"""
		with open(f"Saved/animations/{name}/{animname}.json","r") as file:
			anim = json.load(file)
		
		if name in self.animations.keys():
			self.animations[name][animname] = anim
		else:
			self.animations[name] = {}
			self.animations[name][animname] = anim




	def deleteanim(self,obj,animname):
		anim = f"Saved/animations/{obj}/{animname}.json"
		if os.path.exists(anim):
			os.remove(anim)



	def encodeinst(self):
		insts = []
		for chunk in self.instances.keys():
			for inst in self.instances[chunk]:
				insts.append([{"pos":inst.realpos,"name":inst.name,"rot":inst.rot,"type":inst.type,"sizen":inst.sizen,"alpha":inst.alpha},chunk])
		return [insts,self.tracker]

	def decodeinst(self):
		with open(f"Saved/tilemaps/{self.loadedmap}/inst.json","r") as file:
			allinst = json.load(file)
			for inst in allinst[0]:
				self.datatoinst(inst[1],inst[0])
		self.tracker = allinst[1] + 1
		
	def decodeobj(self):
		with open(f"Saved/tilemaps/{self.loadedmap}/non-inst.json","r") as file:
			allobj = json.load(file)
			for obj in allobj.keys():
				self.datatoobj(obj,allobj[obj])

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

	def translate(self,GameManager,id:str,vector:list,usedt = False):
		"""
		y-axis is fixed to be + up , - down
		"""
		if not GameManager == "none":
			if usedt:
				self.objects[id]["pos"][0] += int(round((vector[0] * 0.2 * GameManager.dt * self.speed)))
				self.objects[id]["pos"][1] -= int(round((vector[1] * 0.2 * GameManager.dt * self.speed)))
			else:
				self.objects[id]["pos"][0] += int(round((vector[0] * 0.3)))
				self.objects[id]["pos"][1] -= int(round((vector[1] * 0.3)))


	def rotate(self,GameManager,id,ang):
		if not GameManager == "none":
			self.objects[id]["rot"] += (ang * GameManager.frame_manager.dt * self.speed)
			if self.objects[id]["rot"] > 360:
				self.objects[id]["rot"] = self.objects[id]["rot"] - 360

	def scaleto(self,id,scale):
		self.sprites[id] = univars.func.getspritesscale(self.objects[id][1],scale)

	def get_value(self,info,name):
		"""
			returns value in sprite
			returns None if not found
		"""
		if name in self.values[info].keys():
			return self.values[info].get(name,None)
		else:
			return 0
		
	def set_value(self,id,name,value):
		"""
			creates a value in a sprite
		"""
		if id in self.values.keys():
			self.values[id][name] = value
		else:
			self.values[id] = {}
			self.values[id][name] = value

	def objfromid(self,id):
		"""returns an object class with an id of the input "id" """
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
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" """
		#coll for non-inst
		dim = univars.grandim
		id = str(id)
		r1 = pygame.Rect(pos[0],pos[1],dimensions[0],dimensions[1])
		typel = self.getcull(pos,1,dim)
		noninst = [self.objfromid(i) for i in typel if r1.colliderect(self.objfromid(i).fakerect) ]

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


		return {"noninst":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}

	def collidep(self,pos,show,dim,pointsize=5,instcol = (0,225,0),noninstcol=(0,225,150),ignore_id = None,camera = None) -> dict: 
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" """
		#coll for non-inst
		dim = univars.grandim
		typel = self.getcull(pos,1,dim)
		noninst = [self.objfromid(i) for i in typel if self.objfromid(i).fakerect.collidepoint(pos) ]

		#coll for inst
		camchunk = (int(round(pos[0]/(dim * self.renderdist))),int(round(pos[1]/(dim * self.renderdist))))
		inst = []
		r1 = pygame.Rect(pos[0],pos[1],1,1)
		if camchunk in self.instances.keys():
			inst = [ i for i in self.instances[camchunk] if i.fakerect.collidepoint(pos)]

		#render the collpoint
		if show:
			num = max(0.6,1/camera.size)
			if len(inst) > 0:
				col = instcol
			elif len(noninst) > 0:
				col = noninstcol
			else:
				col = (225,0,0)
			self.func.ssblitrect(pygame.Rect(pos[0],pos[1],num * pointsize,num * pointsize),col,camera,0)
			# self.func.ssblitrect(r1,col,camera,5)


		
		return {"obj":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}

	def collide9(self,id,show,camera,dim,pointsize = 5,offsets = { "topleft":[0,0],"topmid":[0,0],"topright":[0,0],"midleft":[0,0],"midmid":[0,0],"midright":[0,0],"botleft":[0,0],"botmid":[0,0],"botright":[0,0]}) -> dict:
		"""points ->  [topleft , topmid , topright  , midleft  , midmid  ,  midright  ,  botleft  , botmid  , botleft] . for each point ( collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if")   """
		if id in self.objects.keys():
			x = self.objects[id]["pos"][0]
			y = self.objects[id]["pos"][1]
			w = self.objects[id]["size"][0]/2
			h = self.objects[id]["size"][1]/2
			
			topleft  = self.collidep((x - w +  offsets["topleft"][0]  ,  y - h +  offsets["topleft"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			topmid   = self.collidep((x     +   offsets["topmid"][0]  ,  y - h +   offsets["topmid"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			topright = self.collidep((x + w + offsets["topright"][0]  ,  y - h + offsets["topright"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			midleft  = self.collidep((x - w +  offsets["midleft"][0]  ,    y   +  offsets["midleft"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			midmid   = self.collidep((x     +   offsets["midmid"][0]  ,    y   +   offsets["midmid"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			midright = self.collidep((x + w + offsets["midright"][0]  ,    y   + offsets["midright"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			botleft  = self.collidep((x - w +  offsets["botleft"][0]  ,  y + h +  offsets["botleft"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			botmid   = self.collidep((x     +   offsets["botmid"][0]  ,  y + h +   offsets["botmid"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			botright = self.collidep((x + w + offsets["botright"][0]  ,  y + h + offsets["botright"][1]),show,dim,pointsize,ignore_id=id,camera=camera)
			ans = { "topleft":topleft,"topmid":topmid,"topright":topright,"midleft":midleft,"midmid":midmid,"midright":midright,"botleft":botleft,"botmid":botmid,"botright":botright}
			return ans

	def remove(self,pos):
		# postodel = self.func.get(dict(zip(self.objects.keys(),(self.objects[i]["pos"] for i in self.objects.keys()))),[pos[0],pos[1]])
		poscol = self.collidep(pos,0,univars.grandim)
		postodel = [i.name for i in poscol["obj"]]
		instpostodel = poscol["inst"]

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
				if inst in instpostodel:
					self.instances[a].remove(inst)

	def removeid(self,id):
		"""removes an object and its class"""
		postodel = id
		self.objects.pop(postodel)
		for a in self.layers.keys():
			layer = self.layers[a]
			for b in layer:
				if b.name == postodel:
					self.layers[a].remove(b)

	def includeflipping(self,id):
		"""
			allows the sprite to be flipped with the flip command
		"""
		self.set_value(id,"#flipped","right")

	def flip(self,id,dir):
		"""
			'right' = flip to right
			'left' = flip to left
		"""

		if  not self.get_value(id,"#flipped")  == None:
			if not self.get_value(id,"#flipped") == dir:
				self.objfromid(id).flip()
				self.set_value(id,"#flipped",dir)

	def addinst(self,pos:tuple,name:str,dim:int,rot:int,type:str,sizen , keepprev = False):
		if not keepprev:
			self.remove(list(pos))
		if not type in self.renderinst:
			if not type in self.aplhainst.keys():
				alp = 400
			else:
				alp = self.aplhainst[type]
		else:
			alp = 0
		if str([name,sizen]) in list(self.spritecache.keys()):
			spritelist = self.spritecache[str([name,sizen])]
		else:
			temp = univars.func.getsprites(name)[0]
			spritelist = univars.func.getspritesscale(name,[temp.get_width() * sizen[0],temp.get_height() * sizen[1]])
			self.spritecache[str([name,sizen])] = spritelist
		newt = inst.inst(self.screen,self.grandim,name,pos[0],pos[1],rot,sizen,univars.lumptype.get(name,name),alp,spritelist,[spritelist[0].get_width() * sizen[0],spritelist[0].get_height() * sizen[1]])
		name = (int(round(pos[0]/(dim * self.renderdist))),int(round(pos[1]/(dim * self.renderdist))))
		if name in self.instances.keys():
			self.instances[name].add(newt)
		else:
			self.instances[name] = pygame.sprite.Group()
			self.instances[name].add(newt)

	def add(self,pos:tuple,sprites:str,rot:int,type,sizen,dim:int , keepprev = False):
		"""adds an object to the manager  , gives an id of type str"""
		
		pos = list(pos)
		if sprites in univars.offsets.keys():
			pos[0] += univars.offsets[sprites][0]
			pos[1] -= univars.offsets[sprites][1]
		pos = tuple(pos)

		if not sprites in self.instables:
			layer = 0


			


			if not keepprev:
				self.remove(pos)
			self.tracker += 1
			if str([sprites,sizen]) in list(self.spritecache.keys()):
				spritelist = self.spritecache[str([sprites,sizen])]
				size = [self.spritecache[str([sprites,sizen])][0].get_width() * sizen[0],self.spritecache[str([sprites,sizen])][0].get_height() * sizen[1]]
			else:
				dummy  = univars.func.getsprites(sprites)[0]
				size = [dummy.get_width() * sizen[0],dummy.get_height() * sizen[1]]
				spritelist = univars.func.getspritesscale(sprites,size)
				self.spritecache[str([sprites,sizen])] = spritelist
			add = {"pos":list(pos),"name":sprites,"type":sprites,"rot":rot,"sn":0,"gothru":0,"rendercond":1,"alpha":1000,"layer":layer,"animname":"none","size":size,"sizen":sizen}
			self.objects.update({str(self.tracker):add})
			finalobj = inst.obj(str(self.tracker),add,spritelist)
			if not layer in self.layers.keys():
				self.layers[layer] = pygame.sprite.Group()
			self.layers[layer].add(finalobj)
		else:
			self.addinst(pos,sprites,dim,rot,type,sizen)

	def datatoobj(self,id,data):
		add = data
		self.objects.update({id:add})
		name = add["name"]
		sizen = add.get("sizen",[  data["size"][0] /univars.grandim ,  data["size"][1] /univars.grandim ])

		if str([name,sizen]) in list(self.spritecache.keys()):
			spritelist = self.spritecache[str([name,sizen])]
		else:
			spritelist = univars.func.getspritesscale(name,add["size"])
			self.spritecache[str([name,sizen])] = spritelist
		finalobj = inst.obj(id,add,spritelist)
		if not data["layer"] in self.layers.keys():
			self.layers[data["layer"]] = pygame.sprite.Group()
		self.layers[data["layer"]].add(finalobj)

	def datatoinst(self,chunk,data):
		sizen = data.get("sizen",[1,1])
		name = data["name"]
		if str([name,sizen]) in list(self.spritecache.keys()):
			spritelist = self.spritecache[str([name,sizen])]
		else:
			temp = univars.func.getsprites(name)[0]
			spritelist = univars.func.getspritesscale(name,[temp.get_width() * sizen[0],temp.get_height() * sizen[1]])
			self.spritecache[str([name,sizen])] = spritelist
		newt = inst.inst(self.screen,self.grandim,data["name"],data["pos"][0],data["pos"][1],data["rot"],data["sizen"],univars.lumptype.get(data["name"],data["name"]),data["alpha"],spritelist,[spritelist[0].get_width() * sizen[0],spritelist[0].get_height() * sizen[1]])
		name = (int(round(data["pos"][0]/(univars.grandim * self.renderdist))),int(round(data["pos"][1]/(univars.grandim * self.renderdist))))
		if name in list(self.instances.keys()):
			self.instances[name].add(newt)
		else:
			self.instances[name] = pygame.sprite.Group()
			self.instances[name].add(newt)

	def adds(self,name,pos,sprites,type,rot,size,alpha,layer):
		"""add special for more unique items"""
		dummy  = univars.func.getsprites(sprites)[0]
		size = [dummy.get_width() * size[0],dummy.get_height() * size[1]]
		realsprite = univars.func.getspritesscale(sprites,size)
		rect = pygame.Surface.get_rect(realsprite[0])
		rect.center = (pos[0],pos[1])
		if str([sprites,size]) in list(self.spritecache.keys()):
			spritelist = self.spritecache[str([sprites,size])]
		else:
			spritelist = univars.func.getspritesscale(sprites,size)
			self.spritecache[str([sprites,size])] = spritelist
		add = {"pos":list(pos),"name":sprites,"type":type,"rot":rot,"sn":0,"gothru":0,"rendercond":1,"alpha":alpha,"layer":layer,"animname":"none","size":size}
		self.objects.update({str(name):add})
		finalobj = inst.obj(str(name),add,spritelist)
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

	def render(self,camera,GameManager,dim:int,showall):
		#camera-chunk
		camposdim = [int(round(camera.x/(dim * self.renderdist))),int(round(camera.y/(dim * self.renderdist)))]
		#availabe chunks
		ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
		#the instanciate chunks to be rendered
		lof = [  b   for b in self.instances.keys() for i in ranges   if b == ( i[0]  + camposdim[0],i[1] + camposdim[1]   )]

		

		

		#rendering the instanciates
		if len(lof) > 0:
			for i in lof:
				self.instances[i].update(camera,GameManager.dim,showall)
				self.instances[i].draw(self.screen)

		#rendering the non-instanciates
		for groupid in sorted(self.layers.keys()):
			self.layers[groupid].update(camera,self,dim,showall)
			self.layers[groupid].draw(self.screen)



om = object_manager(univars.realscreeen,univars.screen,univars.grandim,univars.aplhatypes,univars.hideentypes)