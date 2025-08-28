import pickle as pk
import json
import Managers.funcs as funcs
import pygame
import Managers.Textmanager as Textmanager
import random
import itertools
import Managers.inst as inst
import time
import Managers.Cameramod as Cameramod
import Managers.univars as univars
import os
import math


# from render import render




class collinst(pygame.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((100,100))
		self.pos = (x,y)
		self.size = (w,h)
		self.rect = pygame.Rect((x,y,w,h))
		self.fakerect = self.rect
		
		self.rect = pygame.Rect( (self.fakerect.x - Cameramod.cam.x) * Cameramod.cam.size + univars.screen.get_width()//2
						  		,(self.fakerect.y - Cameramod.cam.y) * Cameramod.cam.size + univars.screen.get_height()//2 
								, self.fakerect.width * abs(Cameramod.cam.size)
								, self.fakerect.height * abs(Cameramod.cam.size))
		
class Ghostcollinst(pygame.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((100,100))
		self.pos = (x,y)
		self.size = (w,h)
		self.rect = pygame.Rect((x,y,w,h))
		


class Ghost(pygame.sprite.Sprite):
	def __init__(self,inst):
		pygame.sprite.Sprite.__init__(self)
		self.inst = inst
		self.rect = inst.fakerect
		self.image = pygame.Surface((0,0))






class object_manager: 
	def __init__(self,realscreeen,screen,grandim,alpha,rend):
		self.objects = {}
		self.values = {}
		self.objgroup = pygame.sprite.LayeredUpdates()
		self.anims = {}
		self.forceplay = {}
		self.func = funcs.func(grandim)
		self.screen = screen
		self.realscreen = realscreeen
		self.grandim = univars.grandim
		self.tm = Textmanager.Textmanager(realscreeen)
		self.loadingmap = False
		#chunk id stored in a tuple "(x,y)"
		self.instances = {}
		"""
			a dictianry of sprite groups each sprite has collisions
		"""
		self.ghostinstances = {}
		"""
			a dictianry of sprite groups each sprite contains a reference to the instanciagte
		"""
		self.noncolghostinstances = {}
		"""
			a dictianry of sprite groups each sprite contains a reference to the instanciagte
		"""
		self.noncolinstances = {}
		self.instables = []
		self.toreinst = []
		self.loadedmap = "Null"
		self.baked = 0
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
		self.loadanims()
		

	def loadanims(self):
		for filename in os.listdir("Saved/animations"):
			if  not filename ==  "None":
				objfile = "Saved/animations" + "/" + filename
				for anim in os.listdir(objfile):
					anim = anim.replace(".json","")
					self.loadanim(filename,anim)


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

	# def default(self):
	# 	self.objects = {}
	# 	self.values = {}
	# 	self.layers = {}
	# 	self.loadingmap = False
	# 	#chunk id stored in a tuple "(x,y)"
	# 	self.instances = {}
	# 	self.instables = []
	# 	self.toreinst = []
	# 	self.loadedmap = "Null"
	# 	self.renderdist = univars.renderdist
	# 	self.dodist = 128
	# 	self.tracker = 0
	# 	self.tileup = 1
	# 	self.showmap = 0
	# 	self.loadedchunk = 0
	# 	self.showcolist = []
	
	# 	self.showall = False
	# 	self.speed = 0

	def loadtilemap(self,name):
		if not name == "null" and os.path.exists(f"Saved/tilemaps/{name}"):
			self.__init__(self.realscreen,self.screen,univars.grandim,self.aplhainst,self.renderinst)
			self.loadedmap = name
			self.decodeinst()
			self.decodeobj()
		else:
			self.__init__(self.realscreen,self.screen,univars.grandim,self.aplhainst,self.renderinst)

	def savetilemap(self,name,check = False):
		if not self.baked:
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
		else:
			pass
	def forcesavetilemap(self,name):
		self.savetilemap(name,check=True)
		

	def getcull(self,pos,grid_size,dim,ignore = []) -> list:
		return [i for i in list(self.objects.keys()) if pos[0] - grid_size * dim <= self.objects[i]["pos"][0] <= pos[0] + grid_size * dim  and pos[1] - grid_size * dim <= self.objects[i]["pos"][1] <= (pos[1]) + grid_size * dim and not i in ignore]                                                  

	def grouptosprite(self,chunk):
		
		if chunk in self.noncolinstances.keys() and len(self.noncolinstances[chunk]) > 1:
			size = (univars.renderdist[0] * univars.grandim,univars.renderdist[1] * univars.grandim)
			chunksprite = pygame.Surface(size)
			# chunksprite.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
			chunksprite.fill((0,0,0))
			chunksprite.set_colorkey((0,0,0))
			for instance in self.noncolinstances[chunk].sprites():
				pos =  [instance.realpos[0],instance.realpos[1]]
				relativepos = [   
								(16 * (univars.renderdist[0] - 2) ) + (pos[0] - (chunk[0] * univars.renderdist[0] * univars.grandim)  )   ,
								(16 * (univars.renderdist[1] - 2) ) + (pos[1] - (chunk[1] * univars.renderdist[1] * univars.grandim)  )  
							  ]
				chunksprite.blit(instance.bart,relativepos)
			self.noncolinstances[chunk] = pygame.sprite.LayeredUpdates()
			self.noncolghostinstances[chunk] = pygame.sprite.Group()
			newt = inst.inst("UNOS",univars.grandim,str(chunk) + "noncol" + "#BAKEDINST",(chunk[0] * univars.grandim * univars.renderdist[0]) + univars.grandim/2,(chunk[1] * univars.grandim * univars.renderdist[1]) + univars.grandim/2,0,[1,1],"unot",255,[chunksprite],size,0,0,0)
			self.noncolinstances[chunk].add(newt)

		
		if chunk in self.instances.keys() and len(self.instances[chunk]) > 1:
			size = (univars.renderdist[0] * univars.grandim,univars.renderdist[1] * univars.grandim)
			chunksprite = pygame.Surface(size)
			chunksprite.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
			chunksprite.fill((0,0,0))
			chunksprite.set_colorkey((0,0,0))
			for instance in self.instances[chunk].sprites():
				pos =  [instance.realpos[0],instance.realpos[1]]
				relativepos = [   
								(16 * (univars.renderdist[0] - 2) ) + (pos[0] - (chunk[0] * univars.renderdist[0] * univars.grandim)  )   ,
								(16 * (univars.renderdist[1] - 2) ) + (pos[1] - (chunk[1] * univars.renderdist[1] * univars.grandim)  )  
							  ]
				
				chunksprite.blit(instance.bart,relativepos)
			self.instances[chunk] = pygame.sprite.LayeredUpdates()
			newt = inst.inst("UNOS",univars.grandim,str(chunk) + "col" + "#BAKEDINST",(chunk[0] * univars.grandim * univars.renderdist[0]) + univars.grandim/2,(chunk[1] * univars.grandim * univars.renderdist[1]) + univars.grandim/2,0,[1,1],"unot",255,[chunksprite],size,-1,0,0)
			self.instances[chunk].add(newt)
			
	def BAKE(self):
		"""
			optimises rendering for all noncolliding instanciates by baking them all into one sprite for each chunk
		"""
		self.baked = 1
		for chunk in self.noncolghostinstances.keys():
			self.grouptosprite(chunk)
		for chunk in self.ghostinstances.keys():
			self.grouptosprite(chunk)

		



	def playanim(self,dt,id,name,forceplay = False,speed=1):
		"""
			plays an animation in a sprite\n
			forceplay: \n
				it interupts ONLY if another animation is playing\n
			
			speed:\n
				playbackspeed for the animation
		"""
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
			self.objects[id]["gothru"] += (dt * self.speed * speed)/10
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
				insts.append([{"pos":inst.realpos,"name":inst.name,"rot":inst.rot,"type":inst.type,"sizen":inst.sizen,"alpha":inst.alpha,"stagename":str(inst.stagename),"usecoll":inst.usecoll,"layer":inst.layer,"sn":inst.sn},chunk])
		for chunk in self.noncolinstances.keys():
			for inst in self.noncolinstances[chunk]:
				insts.append([{"pos":inst.realpos,"name":inst.name,"rot":inst.rot,"type":inst.type,"sizen":inst.sizen,"alpha":inst.alpha,"stagename":str(inst.stagename),"usecoll":inst.usecoll,"layer":inst.layer,"sn":inst.sn},chunk])
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
		self.objgroup.add(finalobj,layer = add["layer"])

	def datatoinst(self,chunk,data):
		sizen = data.get("sizen",[1,1])
		name = data["name"]
		if str([name,sizen]) in list(self.spritecache.keys()):
			spritelist = self.spritecache[str([name,sizen])]
		else:
			temp = univars.func.getsprites(name)[0]
			spritelist = univars.func.getspritesscale(name,[temp.get_width(),temp.get_height()])
			self.spritecache[str([name,sizen])] = spritelist
		newt = inst.inst(data["stagename"],self.grandim,data["name"],data["pos"][0],data["pos"][1],data["rot"],data["sizen"],univars.lumptype.get(data["stagename"],data["type"]),data["alpha"],spritelist,[spritelist[0].get_width() * sizen[0],spritelist[0].get_height() * sizen[1]],data["layer"],data["usecoll"],data["sn"])
		name = (int(round((data["pos"][0] - 16)/(univars.grandim * self.renderdist[0]))),int(round((data["pos"][1] - 16)/(univars.grandim * self.renderdist[1]))))
		newtg = Ghost(newt)
		if data["usecoll"]:
			if name in self.instances.keys():
				self.instances[name].add(newt,layer =data["layer"])
				self.ghostinstances[name].add(newtg)
			else:
				self.instances[name] = pygame.sprite.LayeredUpdates()
				self.ghostinstances[name] = pygame.sprite.Group()
				self.instances[name].add(newt,layer =data["layer"])
				self.ghostinstances[name].add(newtg)
		else:
			if name in self.noncolinstances.keys():
				self.noncolinstances[name].add(newt,layer =data["layer"])
				self.noncolghostinstances[name].add(newtg)
			else:
				self.noncolinstances[name] = pygame.sprite.LayeredUpdates()
				self.noncolinstances[name].add(newt,layer =data["layer"])
				self.noncolghostinstances[name] = pygame.sprite.Group()
				self.noncolghostinstances[name].add(newtg)
				



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
		for b in self.objgroup:
			if str(b.name) == str(id):
				return b

	def collide(self,id,show,camera,extra= 0) -> dict:
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" """
		if not self.objfromid(id) == None:
			#coll for non-inst
			dim = univars.grandim
			id = str(id)
			r1 = self.objfromid(id).fakerect
			r1.width = r1.width + extra
			r1.height = r1.height + extra

			# typel = self.getcull(self.objects[id]["pos"],extra + 1,dim)
			# typel.remove(id)



			colsprite =  Ghostcollinst(r1.x,r1.y,r1.width,r1.height)
			noninst = pygame.sprite.spritecollide(colsprite,self.objgroup,dokill=False)

			#coll for inst
			camchunk = [int(round(camera.x/(dim * self.renderdist[0]))),int(round(camera.y/(dim * self.renderdist[1])))]
			ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
			
			inst = []
			for offset in ranges:
				a = []
				campos = (offset[0] + camchunk[0],offset[1] + camchunk[1])
				if campos in self.instances.keys():
					# a = [ i for i in self.instances[campos] if r1.colliderect(i.fakerect)]
					a = pygame.sprite.spritecollide(colsprite,self.ghostinstances[campos],dokill=False)
					a = [i.inst for i in a]
				inst += a

			#render the collbox
			if show:
				if len(inst) > 0 and len(noninst) > 0:
					col = (0,225,255)
				elif len(inst) > 0:
					col = (0,225,0)
				elif len(noninst) > 0:
					col = (0,0,255)
				else:
					col = (225,0,0)
				# self.func.ssblitrect(r1,col,camera,5,univars.fakescreen)
				self.func.ssblitrect(colsprite.fakerect,col,camera,5,univars.fakescreen)


			return {"noninst":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}

	def colliderect(self,pos,dimensions,show,camera,ignore = []) -> dict:
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" """
		#coll for non-inst
		dim = univars.grandim
		id = str(id)
		r1 = pygame.Rect(pos[0],pos[1],dimensions[0],dimensions[1])
		
		colsprite =  Ghostcollinst(r1.x,r1.y,r1.width,r1.height)
		noninst = pygame.sprite.spritecollide(colsprite,self.objgroup,dokill=False)

		#coll for inst
		#coll for inst
		camchunk = [int(round(camera.x/(dim * self.renderdist[0]))),int(round(camera.y/(dim * self.renderdist[1])))]
		ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
		inst = []
		for offset in ranges:
			a = []
			campos = (offset[0] + camchunk[0],offset[1] + camchunk[1])
			if campos in self.instances.keys():
				# a = [ i for i in self.instances[campos] if r1.colliderect(i.fakerect)]
				a = pygame.sprite.spritecollide(colsprite,self.ghostinstances[campos],dokill=False)
				a = [i.inst for i in a]
			inst += a

		#render the collbox
		if show:
			if len(inst) > 0 and len(noninst) > 0:
				col = (0,225,255)
			elif len(inst) > 0:
				col = (0,225,0)
			elif len(noninst) > 0:
				col = (0,0,255)
			else:
				col = (225,0,0)
			self.func.ssblitrect(r1,col,camera,5,univars.fakescreen)


		return {"noninst":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}

	def collidep(self,pos,show,dim,pointsize=5,basecolor = (255,0,0),instcol = (0,225,0),noninstcol=(0,225,150),ignore_id = None,camera = Cameramod.cam,ignore = []) -> dict: 
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" """
		#coll for non-inst
		dim = univars.grandim
		r1 = pygame.Rect(pos[0],pos[1],1,1)
		colsprite =  collinst(r1.x,r1.y,math.ceil(r1.width +3),math.ceil(r1.height +3))
		noninst = pygame.sprite.spritecollide(colsprite,self.objgroup,dokill=False)
		# for obj in noninst:
		# 	if obj.name in ignore or obj.name == ignore_id:
		# 		noninst.remove(obj)

		#coll for inst
		camchunk = [int(round(pos[0]/(dim * self.renderdist[0]))),int(round(pos[1]/(dim * self.renderdist[1])))]
		ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
		inst = []
		for offset in ranges:
			a = []
			campos = (offset[0] + camchunk[0],offset[1] + camchunk[1])
			if campos in self.instances.keys():
				# a = [ i for i in self.instances[campos] if i.fakerect.collidepoint(pos)]
				a = pygame.sprite.spritecollide(Ghostcollinst(r1.x,r1.y,r1.width,r1.height),self.ghostinstances[campos],dokill=False)
				
				a = [ghost.inst for ghost in a]

			inst += a
		# print(inst)

		#render the collpoint
		if show:
			num = max(0.6,1/camera.size)
			if len(inst) > 0:
				col = instcol
			elif len(noninst) > 0:
				col = noninstcol
			else:
				col = basecolor
			self.func.ssblitrect(pygame.Rect(pos[0],pos[1],num * pointsize,num * pointsize),col,camera,0,univars.fakescreen)
			# self.func.ssblitrect(r1,col,camera,5,univars.fakescreen)


		
		return {"obj":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}

	def unopcollidep(self,pos,show,dim,pointsize=5,basecolor = (255,0,0),instcol = (0,225,0),noninstcol=(0,225,150),ignore_id = None,camera = Cameramod.cam,ignore = []) -> dict: 
		"""collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if" 
			\n Dim not needed"""
		#coll for non-inst
		dim = univars.grandim
		r1 = pygame.Rect(pos[0],pos[1],10,10)
		colsprite =  collinst(r1.x,r1.y,math.ceil(r1.width),math.ceil(r1.height))
		noninst = pygame.sprite.spritecollide(colsprite,self.objgroup,dokill=False)
		for obj in noninst:
			if obj.name in ignore or obj.name == ignore_id:
				noninst.remove(obj)

		#coll for inst
		camchunk = [int(round(pos[0]/(dim * self.renderdist[0]))),int(round(pos[1]/(dim * self.renderdist[1])))]
		ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
		inst = []
		for offset in ranges:
			a = []
			campos = (offset[0] + camchunk[0],offset[1] + camchunk[1])
			if campos in self.instances.keys():
				# a = [ i for i in self.instances[campos] if i.fakerect.collidepoint(pos)]
				a = pygame.sprite.spritecollide(Ghostcollinst(r1.x,r1.y,r1.width,r1.height),self.ghostinstances[campos],dokill=False)
				
				
				a = [ghost.inst for ghost in a]
			inst += a
			
			b = []
			if campos in self.noncolinstances.keys():
				# a = [ i for i in self.instances[campos] if i.fakerect.collidepoint(pos)]
				b = pygame.sprite.spritecollide(Ghostcollinst(r1.x,r1.y,r1.width,r1.height),self.noncolghostinstances[campos],dokill=False)
				
				
				b = [ghost.inst for ghost in b]

			inst += b



		#render the collpoint
		if show:
			num = max(0.6,1/camera.size)
			if len(inst) > 0:
				col = instcol
			elif len(noninst) > 0:
				col = noninstcol
			else:
				col = basecolor
			self.func.ssblitrect(pygame.Rect(pos[0],pos[1],num * pointsize,num * pointsize),col,camera,0,univars.fakescreen)
			# self.func.ssblitrect(r1,col,camera,5)


		
		return {"obj":noninst,"inst":inst,"all":noninst + inst,"if":len(noninst + inst) > 0}



	def collide9(self,id,show,camera,dim,pointsize = 5,offsets = { "topleft":[0,0],"topmid":[0,0],"topright":[0,0],"midleft":[0,0],"midmid":[0,0],"midright":[0,0],"botleft":[0,0],"botmid":[0,0],"botright":[0,0]},ignore = []) -> dict:
		""" points :\n
				[topleft , topmid , topright  , midleft  , midmid  ,  midright  ,  botleft  , botmid  , botleft] .\n

			selections:\n
				( collisions for non-instanciates -> "obj" .  collisions for instanciates -> "inst" . all collisions -> "all" . if collision -> "if")]\n
			
				     """
		if id in self.objects.keys():
			x = self.objects[id]["pos"][0]
			y = self.objects[id]["pos"][1]
			w = self.objects[id]["size"][0]/2
			h = self.objects[id]["size"][1]/2
			
			topleft  = self.collidep((x - w +  offsets["topleft"][0],  y - h +  offsets["topleft"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			topmid   = self.collidep((x     +   offsets["topmid"][0]  ,  y - h +   offsets["topmid"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			topright = self.collidep((x + w + offsets["topright"][0]  ,  y - h + offsets["topright"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			midleft  = self.collidep((x - w +  offsets["midleft"][0],    y   +  offsets["midleft"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			midmid   = self.collidep((x     +   offsets["midmid"][0]  ,    y   +   offsets["midmid"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			midright = self.collidep((x + w + offsets["midright"][0]  ,    y   + offsets["midright"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			botleft  = self.collidep((x - w +  offsets["botleft"][0],  y + h +  offsets["botleft"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			botmid   = self.collidep((x     +   offsets["botmid"][0]  ,  y + h +   offsets["botmid"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			botright = self.collidep((x + w + offsets["botright"][0]  ,  y + h + offsets["botright"][1]),show,dim,pointsize,ignore_id=id,camera=camera,ignore = ignore)
			ans = { "topleft":topleft,"topmid":topmid,"topright":topright,"midleft":midleft,"midmid":midmid,"midright":midright,"botleft":botleft,"botmid":botmid,"botright":botright}
			return ans

	def remove(self,pos,layer = 0):
		# postodel = self.func.get(dict(zip(self.objects.keys(),(self.objects[i]["pos"] for i in self.objects.keys()))),[pos[0],pos[1]])
		poscol = self.unopcollidep(pos,0,univars.grandim)
		postodel = [i.name for i in poscol["obj"]]
		instpostodel = poscol["inst"]

		#deleting non-instances
		if not postodel == []:
			for obj in self.objgroup:
				if obj.name == postodel[0]:
					if obj.layer == layer or layer == "all":
						self.objgroup.remove(obj)
						self.objects.pop(postodel[0])

		#deleting noncolinstances
		for a in self.noncolinstances.keys():
			for inst in self.noncolinstances[a]:
				if inst in instpostodel:
					if inst.layer == layer or layer == "all":
						self.noncolinstances[a].remove(inst)

		#deleting instances
		for a in self.instances.keys():
			for inst in self.instances[a]:
				if inst in instpostodel:
					if inst.layer == layer or layer == "all":
						self.instances[a].remove(inst)
						for ghost in self.ghostinstances[a]:
							if ghost.inst == inst:
								self.ghostinstances[a].remove(ghost)

	def removeid(self,id):
		"""removes an object and its obj"""
		postodel = id
		self.objects.pop(postodel)
		for b in self.objgroup:
			if b.name == postodel:
				self.objgroup.remove(b)

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

	def addinst(self,pos:tuple,name:str,dim:int,rot:int,type:str,sizen,stagename ,layer,usecoll,sn,keepprev = False):
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
			spritelist = univars.func.getspritesscale(name,[temp.get_width(),temp.get_height()])
			self.spritecache[str([name,sizen])] = spritelist

		newt = inst.inst(stagename,self.grandim,name,pos[0],pos[1],rot,sizen,univars.lumptype.get(stagename,type),alp,spritelist,[spritelist[0].get_width() * sizen[0],spritelist[0].get_height() * sizen[1]],layer,usecoll,sn)
		name = (int(round((pos[0] - 16)/(dim * self.renderdist[0]))),int(round((pos[1] - 16)/(dim * self.renderdist[1]))))
		newtg = Ghost(newt)
		if usecoll:
			if name in self.instances.keys():
				self.instances[name].add(newt,layer = layer)
				self.ghostinstances[name].add(newtg)
			else:
				self.instances[name] = pygame.sprite.LayeredUpdates()
				self.ghostinstances[name] = pygame.sprite.Group()
				self.instances[name].add(newt,layer = layer)
				self.ghostinstances[name].add(newtg)
		else:
			if name in self.noncolinstances.keys():
				self.noncolinstances[name].add(newt,layer = layer)
				self.noncolghostinstances[name].add(newtg)
			else:
				self.noncolinstances[name] = pygame.sprite.LayeredUpdates()
				self.noncolinstances[name].add(newt,layer = layer)
				self.noncolghostinstances[name] = pygame.sprite.Group()
				self.noncolghostinstances[name].add(newtg)

	def add(self,pos:tuple,sprites:str,rot:int,type,sizen,dim:int , keepprev = False,stagename = None,layer = 0,colforinst=True,sn = 0):
		"""adds an object to the manager  , gives an id of type str"""
		if stagename == None:
			stagename = sprites
		pos = list(pos)
		if sprites in univars.offsets.keys():
			pos[0] += univars.offsets[sprites][0]
			pos[1] -= univars.offsets[sprites][1]
		pos = tuple(pos)

		if layer == "all":
			layer = 0
		
		if not keepprev:
			self.remove(pos,layer=layer)

		if not sprites in univars.instables:


			


			self.tracker += 1
			if str([sprites,sizen]) in list(self.spritecache.keys()):
				spritelist = self.spritecache[str([sprites,sizen])]
				size = [self.spritecache[str([sprites,sizen])][0].get_width() * sizen[0],self.spritecache[str([sprites,sizen])][0].get_height() * sizen[1]]
			else:
				dummy  = univars.func.getsprites(sprites)[0]
				size = [dummy.get_width() * sizen[0],dummy.get_height() * sizen[1]]
				spritelist = univars.func.getspritesscale(sprites,size)
				self.spritecache[str([sprites,sizen])] = spritelist
			add = {"pos":list(pos),"name":sprites,"type":sprites,"rot":rot,"sn":sn,"gothru":0,"rendercond":1,"alpha":1000,"layer":layer,"animname":"none","size":size,"sizen":sizen}
			self.objects.update({str(self.tracker):add})
			finalobj = inst.obj(str(self.tracker),add,spritelist)
			self.objgroup.add(finalobj,layer = layer)
		else:
			self.addinst(pos,sprites,dim,rot,type,sizen,stagename,layer,colforinst,sn,keepprev=keepprev)


	def atpoint(self,pos):
		return self.collidep(pos,0,1)["if"]
		


	def adds(self,name,pos,sprites,type,rot,sizen,alpha,layer):
		"""add special for more unique items"""
		dummy  = univars.func.getsprites(sprites)[0]
		size = dummy.get_size()
		if str([sprites,size]) in list(self.spritecache.keys()):
			spritelist = self.spritecache[str([sprites,size])]
		else:
			spritelist = univars.func.getspritesscale(sprites,size)
			self.spritecache[str([sprites,size])] = spritelist
		add = {"pos":list(pos),"name":sprites,"type":type,"rot":rot,"sn":0,"gothru":0,"rendercond":1,"alpha":alpha,"layer":layer,"animname":"none","size":size,"sizen":sizen}
		if name in self.objects.keys():
			self.removeid(name)
		self.objects.update({str(name):add})
		finalobj = inst.obj(str(name),add,spritelist)
		self.objgroup.add(finalobj,layer=layer)

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
		camposdim = [int(round(camera.x/(dim * self.renderdist[0]))),int(round(camera.y/(dim * self.renderdist[1])))]
		#availabe chunks
		ranges = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
		#the instanciate chunks to be rendered
		lof = [  b   for b in self.instances.keys() for i in ranges   if b == ( i[0]  + camposdim[0],i[1] + camposdim[1]   )]
		noncollof = [  b   for b in self.noncolinstances.keys() for i in ranges   if b == ( i[0]  + camposdim[0],i[1] + camposdim[1]   )]
		# GameManager.println()
		
		# pygame.sprite.Group.draw(special_flags=)
		
		
		#rendering the instanciates
		if len(lof) > 0:
			for i in lof:
				# print(self.instances[i].sprites)
				# print()
				self.instances[i].update(showall)
				self.instances[i].draw(univars.screen,special_flags=0)

		# print("noncol:")
		#renders the non colliding instanciates
		if len(noncollof) > 0:
			for i in noncollof:
				# print(self.instances[i].sprites)
				# # print()
				self.noncolinstances[i].update(showall)
				self.noncolinstances[i].draw(univars.screen,special_flags=0)

		# print("/////////")

		#rendering the non-instanciates
		self.objgroup.update(camera,self,dim,showall,GameManager.fm.frame)
		self.objgroup.draw(univars.screen)



om = object_manager(univars.realscreeen,univars.screen,univars.grandim,univars.aplhatypes,univars.hideentypes)