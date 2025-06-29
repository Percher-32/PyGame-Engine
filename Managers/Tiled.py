import pygame
import Cameramod
import Cammanager
import Textmanager
import funcs
import univars
import Uimanager
import Cammanager
import objectmanager
um = Uimanager.ingame
cam = Cameramod.cam
cam = Cammanager.camager.cameras["def"]

object_manager = objectmanager.om

class TiledSoftwre:
	def __init__(self,realscreen,theme,grandim,screen,om):
		self.pause = True
		self.realscreeen = realscreen
		self.theme = theme
		self.tm = Textmanager.Textmanager(realscreen)
		self.func = funcs.func(screen,grandim)
		self.om = om
		self.secretword = "404 error"
		self.screen = screen
		self.savestring = ""
		self.savemode = 0
		self.sprite = 0
		self.placable = 0
		self.rot = 0
		self.rotable = 0
		self.saveable = 0
		self.grip = 0
		self.gridable = 0
		self.pos1 = [0,0]
		self.pos2 = [0,0]
		self.recter = 0
		self.rectable = 0
		self.pos3 = [0,0]
		self.pos4 = [0,0]
		self.showdata = True
		self.showdatable = 0
		self.commmandtring = ""
		self.comm = False
		self.cht = univars.startstate
		self.loadingmap = False
		self.spritenames = univars.func.allsprites()
		self.typelist = univars.func.allsprites()
		self.allsize = univars.func.allones()

	def altmode(self,GameManager,object_manager):
		um.remall()
		um.addsurfu("stuff",self.theme["dark"],(0,0),(2000,2000),"def")
		# um.add_button("chap","testbutton",(4,4),(4.5,4.5),(0,0),"def")
		# GameManager.uibox((self.realscreeen.get_width(),self.realscreeen.get_height()),(0,0),self.theme["dark"]	,400)
		# GameManager.uibox((400,self.realscreeen.get_height() - 40),(-0.75,0),self.theme[1] ,400)
		# GameManager.blituis(object_manager.sprites[self.dostring][0],(-0.8,0.7),(3 * 64,3 * 64),self.rot,1000)
		# self.tm.drawtext2(f"pos = {object_manager.objects[self.dostring][0]}\nId = {self.dostring}\nName = {object_manager.objects[self.dostring][1]}\nSize = {(object_manager.sprites[self.dostring][0].get_width(),object_manager.sprites[self.dostring][0].get_height())}   \nRot = {object_manager.objects[self.dostring][3]}\nType = {object_manager.objects[self.dostring][9]}\nRender = {bool(object_manager.objects[self.dostring][6])}","pixel2.ttf",40,0,0,0,self.theme["semibright"],-0.9,0.2)
		# try:
		# 	off = 0
		# 	if len(list(object_manager.values[self.dostring].keys())) > 0:
		# 		for i in object_manager.values[self.dostring].keys():
		# 			self.tm.drawtext(f"{i} : {object_manager.values[self.dostring][i]}","pixel2.ttf",40,0,0,0,self.theme["semibright"],-0.8,off/10 - 0.2)
		# 			off += 1
		# except:
		# 	self.tm.drawtext(f"no variables","pixel2.ttf",40,0,0,0,self.theme["semibright"],-0.8,-0.2)

	def extra(self,extras):
		if not extras == ["none"]:
			for i in extras:
				self.spritenames.append(i[0])
				self.typelist.append(i[1])
				self.allsize.append(i[2])

	def commandline(self,GameManager,dostring,precursur):
		GameManager.uibox((self.realscreeen.get_width(),200),(0,-1),univars.theme["dark"],200)
		if not GameManager.event_manager.key[pygame.K_RETURN]:
			if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						dostring = dostring[:-1]
			else:
				if GameManager.event_manager.keyb:
					dostring += GameManager.event_manager.code
			self.tm.drawtext2(f"{precursur} {dostring}","pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.95,-0.9)
			return dostring
		else:
			if not dostring == "":
				return self.secretword
			else:
				return dostring

	def textline(self,GameManager,dostring,precursur):
		GameManager.uibox((self.realscreeen.get_width(),200),(0,-1),univars.theme["dark"],600)
		if not GameManager.event_manager.key[pygame.K_RETURN]:
			if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						dostring = dostring[:-1]
			else:
				if GameManager.event_manager.keyb:
					dostring += GameManager.event_manager.code
			self.tm.drawtext2(f"{precursur} {dostring}","pixel2.ttf",40,0,0,0,univars.theme["bright"],-0.95,-0.9)
			return dostring
		else:
			if not dostring == "":
				return self.secretword
			else:
				return dostring



	def Run(self,work,speed,GameManager,camera,dim,debug,cm,smate):
		if work:
			self.comm = False
			self.loadingmap = False
			self.dim = dim
			#savemode for level editing
			if self.savemode == 0:
				if debug:
					#random
					if len(self.typelist) < len(self.spritenames):
						for i in range(len(self.spritenames) - len(self.typelist)):
							self.typelist.append("none")


					#movement
					if GameManager.event_manager.key[pygame.K_q]:
						cam[1] += (camera.size)/speed * GameManager.frame_manager.dt 
					if GameManager.event_manager.key[pygame.K_e]:
						cam[1] -= (camera.size)/speed * GameManager.frame_manager.dt 
					if GameManager.event_manager.key[pygame.K_d]:
						cam[0][0] += speed * (1/camera.size) * GameManager.frame_manager.dt  * self.screen.get_width()/self.realscreeen.get_width()
					if GameManager.event_manager.key[pygame.K_a]:
						cam[0][0] -= speed * (1/camera.size) * GameManager.frame_manager.dt  * self.screen.get_width()/self.realscreeen.get_width()
					if GameManager.event_manager.key[pygame.K_w]:
						cam[0][1] -= speed * (1/camera.size) * GameManager.frame_manager.dt  * self.screen.get_width()/self.realscreeen.get_width()
					if GameManager.event_manager.key[pygame.K_s]:
						cam[0][1] += speed * (1/camera.size) * GameManager.frame_manager.dt  * self.screen.get_width()/self.realscreeen.get_width()


					#to move spite on the 
					self.sprite += GameManager.event_manager.scroll

					#make sure it loops the sprite rotar
					if self.sprite > (len(self.spritenames) - 1):
						self.sprite = 0
					elif self.sprite < 0:
						self.sprite = (len(self.spritenames) - 1)


					#some math
					upscale = self.realscreeen.get_width() / self.screen.get_width()
					translation = self.realscreeen.get_width()//4
					a1 = (((   (GameManager.event_manager.mousepos[0])/upscale  - self.screen.get_width()//2) / camera.size) + camera.x)
					a2 = (((   (GameManager.event_manager.mousepos[1] + translation)/upscale  - self.screen.get_height()//2) / camera.size) + camera.y)
					mousepos = (a1,a2)
					thingtogo = self.func.getsprites(self.spritenames[self.sprite])[0]
					thingtogo = pygame.transform.scale_by(thingtogo,self.allsize[self.sprite])
					thingtogo.set_alpha(100)
					GameManager.blitsurf(thingtogo,((round(a1/dim) * dim),(round(a2/dim) * dim)),self.rot,camera)
					gridpos = (round(mousepos[0]/self.dim) * self.dim , round(mousepos[1]/self.dim) * self.dim)


					#to show about to be placed object
					if self.gridable < 1:
						if self.grip == 0:
							if GameManager.event_manager.key[pygame.K_x]:	
								self.pos1 = gridpos
								self.grip = 1
								self.gridable = 10

					#to show the about to be gridded object
					if self.grip == 1:
						GameManager.blit(self.func.getsprites(self.spritenames[self.sprite])[0],self.func.getsprites(self.spritenames[self.sprite])[0].get_rect(center = (self.pos1)),self.rot,camera)

					#multi place/delete
					if self.gridable < 1:
						if self.grip == 1:
							if GameManager.event_manager.key[pygame.K_x]:
								self.pos2 = gridpos
								self.grip = 0
								self.gridable = 10
								rectpos = (self.pos1)
								rectwidth = ( (self.pos2[0] - self.pos1[0])/self.dim , (self.pos2[1] - self.pos1[1])/self.dim )
								rangex = rectpos[0] - self.dim
								rangey = rectpos[1] - self.dim
								widthx = int(rectwidth[0])+ 1
								widthy = int(rectwidth[1])+ 1
								if widthy > 0:
									y = rangey
								else:
									if widthx == 1:
										y = rangey + self.dim + self.dim
										widthy += -2
									else:
										y = rangey
								for i in range(abs(widthy)):
									if widthy > 0:
										y += self.dim
									else:
										y -= self.dim

									if widthx > 0:
										x = rangex
									else:
										if widthy == 1:
											x = rangex + self.dim + self.dim
											widthx += -2
										else:
											x = rangex
									for i in range(abs(widthx)):
										if widthx > 0:
											x += self.dim
										else:
											x -= self.dim
										self.om.add((x,y),self.spritenames[self.sprite],self.rot,self.typelist[self.sprite],self.allsize[self.sprite],dim)
							if GameManager.event_manager.key[pygame.K_v]:
								self.pos2 = gridpos
								self.grip = 0
								self.gridable = 10
								rectpos = (self.pos1)
								rectwidth = ( (self.pos2[0] - self.pos1[0])/self.dim , (self.pos2[1] - self.pos1[1])/self.dim )
								rangex = rectpos[0] - self.dim
								rangey = rectpos[1] - self.dim
								widthx = int(rectwidth[0])+ 1
								widthy = int(rectwidth[1])+ 1
								if widthy > 0:
									y = rangey
								else:
									if widthx == 1:
										y = rangey + self.dim + self.dim
										widthy += -2
									else:
										y = rangey
								for i in range(abs(widthy)):
									if widthy > 0:
										y += self.dim
									else:
										y -= self.dim

									if widthx > 0:
										x = rangex
									else:
										if widthy == 1:
											x = rangex + self.dim + self.dim
											widthx += -2
										else:
											x = rangex
									for i in range(abs(widthx)):
										if widthx > 0:
											x += self.dim
										else:
											x -= self.dim
										self.om.remove((x,y))		


					#to rotate
					if self.rotable < 1:
						if GameManager.event_manager.key[pygame.K_z]:
							self.rot += 45
							self.rotable = 10
						if GameManager.event_manager.key[pygame.K_c]:
							self.rot -= 45
							self.rotable = 10






					#to place
					if GameManager.event_manager.mouse[0]:
						if self.placable < 1:
							object_manager.add(gridpos,self.spritenames[self.sprite],self.rot,self.typelist[self.sprite],self.allsize[self.sprite],dim)
							self.placable = 1

					#to remove
					if GameManager.event_manager.mouse[2]:
						object_manager.remove(gridpos)
					

					#to check an inst or non-inst's info
					if GameManager.event_manager.key[pygame.K_r]:
						mousecol = object_manager.collidep(gridpos,0,camera,dim)
						if len(mousecol["obj"]) > 0:
							a = mousecol["obj"][0].info
							a1 = mousecol['obj'][0].name
							maxlen = 270
							off = 1
							if a1 in object_manager.values.keys():
								for i in object_manager.values[a1].keys():
									strb = len(f"{i} : {object_manager.values[a1][i]}") * 13
									if strb > maxlen:
										maxlen = strb
									off += 1
							b = pygame.Surface((maxlen,250 + (off * 30)))
							b.fill(univars.theme["dark"])
							b.set_alpha(150)
							GameManager.Gotomousepos2(b)
							self.tm.textatmouse(f"Normal Object\nId = { mousecol['obj'][0].name }\nName = {a['name']}\nSize = {a['size']}\nRot = {a['rot']}\nType = {a['type']}\nRender = {bool(a['rendercond'])}\nPos = {a['pos']}","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,-20)
							if a1 in object_manager.values.keys():
								off = 0
								for i in object_manager.values[a1].keys():
									self.tm.textatmouse(f"{i} : {object_manager.values[a1][i]}","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,(-1 * off * 30) - 240)
									off += 1
							else:
								self.tm.textatmouse(f"No variables","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,0 - 240)

							if GameManager.event_manager.key[pygame.K_LCTRL]:
								self.dostring2 = ""
								self.dostring = mousecol["obj"][0]
								self.savemode = "alterobj"

						if len(mousecol["inst"]) > 0:
							a = mousecol["inst"][0]
							b = pygame.Surface((270,250))
							b.fill(univars.theme["dark"])
							b.set_alpha(150)
							GameManager.Gotomousepos2(b)
							self.tm.textatmouse(f"Instanciated Object\nType = {a.type}\nName = { a.name }\nPos = {a.realpos}\nRot = {a.rot}\nSize = {a.size}\nAlpha = {a.alpha}","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,-20)

							if GameManager.event_manager.key[pygame.K_LCTRL]:
								self.dostring2 = ""
								self.dostring = mousecol["inst"][0]
								self.savemode = "alterinst"



					#to load levels
					if GameManager.event_manager.key[pygame.K_l]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							if self.saveable < 1:
								self.savemode = 3
								self.savestring = ""
								self.saveable = 10


					#to save levels
					if GameManager.event_manager.key[pygame.K_s]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							if self.saveable < 1:
								if not object_manager.loadedmap == "Null":
									self.savemode = 2
									self.savestring = object_manager.loadedmap
								else:
									self.savemode = 1
									self.savestring = ""
								self.saveable = 10


					#to hide/show ui
					if GameManager.event_manager.key[pygame.K_v]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							if self.showdata == 1:
								if self.showdatable < 1:
									self.showdata = 0
									self.showdatable = 10
							if self.showdata == 0:
								if self.showdatable < 1:
									self.showdata = 1
									self.showdatable = 10


					#to open command-line
					if GameManager.event_manager.key[pygame.K_b]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							self.commmandtring = ""
							self.savemode = "command"



				else:
					object_manager.showall = False
					if GameManager.event_manager.key[pygame.K_b]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							self.commmandtring = ""
							self.savemode = "command"
							
					if GameManager.event_manager.key[pygame.K_v]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							if self.showdata == 1:
								if self.showdatable < 1:
									self.showdata = 0
									self.showdatable = 10
							if self.showdata == 0:
								if self.showdatable < 1:
									self.showdata = 1
									self.showdatable = 10

			#savemode to name save-file
			elif self.savemode == 1:
				GameManager.uibox((self.realscreeen.get_width(),self.realscreeen.get_height()),(0,0),(0,0,0),100)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.savestring = self.savestring[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.savestring += GameManager.event_manager.code
					self.tm.drawtext2(f"What do you want to name your file: {self.savestring}","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,0)
				else:
					if not self.savestring == "":
						if object_manager.savetilemap(self.savestring.rstrip()) == "No":
							self.savemode = 2
						else:
							self.savemode = 0
			
			#savemode to force-save
			elif self.savemode == 2:
				GameManager.uibox((self.realscreeen.get_width(),self.realscreeen.get_height()),(0,0),(0,0,0),100)
				self.tm.drawtext2(f"{self.savestring.rstrip()} already exists do you want to replace it Y/N","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,0)
				if GameManager.event_manager.keyb:
					if GameManager.event_manager.code == "y":
						object_manager.forcesavetilemap(self.savestring.rstrip())
						self.savemode = 0
					else:
						self.savemode = 0

			elif self.savemode == 3:
				GameManager.uibox((self.realscreeen.get_width(),self.realscreeen.get_height()),(0,0),(0,0,0),100)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.savestring = self.savestring[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.savestring += GameManager.event_manager.code
					self.tm.drawtext2(f"What file do you want to load: {self.savestring}","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,0)
				else:
					object_manager.loadtilemap(self.savestring.rstrip())
					self.loadingmap = True
					camera.x = 0
					camera.y = 0
					self.savemode = 0

			elif self.savemode == 4:
					GameManager.uibox((self.realscreeen.get_width(),self.realscreeen.get_height()),(0,0),(0,0,0),100)
					if not GameManager.event_manager.key[pygame.K_RETURN]:
						if GameManager.event_manager.key[pygame.K_BACKSPACE]:
							self.chunksave = self.chunksave[:-1]
						else:
							if GameManager.event_manager.keyb:
								self.chunksave += GameManager.event_manager.code
						self.tm.drawtext2(f"What chunksize?: {self.chunksave}","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,0)
					else:
						if not self.chunksave == "":
							if object_manager.savetilemap(self.savestring.rstrip(),self.chunksave.rstrip()) == "No":
								self.savemode = 2
							else:
								self.savemode = 0

			elif self.savemode == "command":
				GameManager.uibox((self.realscreeen.get_width(),200),(0,-1),univars.theme["dark"],200)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.commmandtring = self.commmandtring[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.commmandtring += GameManager.event_manager.code
					self.tm.drawtext2(f"Input a command: {self.commmandtring}","pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.95,-0.9)
				else:
					self.dostring = ""
					self.savemode = "Com" + self.commmandtring.rstrip()

			elif self.savemode == "Comcamera" or self.savemode == "Comcam":
				a = self.commandline(GameManager,self.dostring,"What Camera X:")
				if not a == self.secretword:
					self.dostring = a
				else:
					self.dostring2 = ""
					Cammanager.camager.setcond("def","posx",float(self.dostring.rstrip()))
					self.savemode = "camy"

			elif self.savemode == "camy":
				a = self.commandline(GameManager,self.dostring2,"What Camera Y:")
				if not a == self.secretword:
					self.dostring2 = a
				else:
					Cammanager.camager.setcond("def","posy",-1 * float(self.dostring2.rstrip()))
					self.savemode = 0

			elif self.savemode == "Comspeed":
				a = self.commandline(GameManager,self.dostring,"What Speed ?:")
				if not a == self.secretword:
					self.dostring = a
				else:
					object_manager.speed = float(self.dostring.rstrip())
					self.savemode = 0

			elif "show" in self.savemode and "all" in self.savemode and "col" in self.savemode and "Com" in self.savemode:
				object_manager.showcolist = "all"
				self.savemode = 0

			elif "all" in self.savemode and "hide" in self.savemode and "col" in self.savemode and "Com" in self.savemode:
				object_manager.showcolist = []
				self.savemode = 0

			elif "all" in self.savemode and "hide" in self.savemode and "rend" in self.savemode and "Com" in self.savemode:
				object_manager.showall = False
				self.savemode = 0

			elif "all" in self.savemode and "show" in self.savemode and "rend" in self.savemode and "Com" in self.savemode:
				object_manager.showall = True
				self.savemode = 0

			elif "tile" in self.savemode and "Com" in self.savemode:
				object_manager.tile()
				self.savemode = 0

			#savemode for object veiw
			elif self.savemode == "alterobj":
				GameManager.uibox((400,self.realscreeen.get_height() - 200),(-0.75,0.15),self.theme["dark"] ,400)
				b = self.dostring
				Cammanager.camager.setcond("def","pos",   univars.func.lerp(Cammanager.camager.getcam("def","pos")   ,b.info["pos"],4)    )
				Cammanager.camager.setcond("def","size",   univars.func.lerp(Cammanager.camager.getcam("def","size"),((max(b.info["size"])/dim)),4)    )
				GameManager.blituis(b.image,(-0.8,0.7),(3 * 64,3 * 64),self.rot,1000)
				self.tm.drawtext2(f"pos = {b.info['pos']}\nId = {b.name}\nName = {b.info['name']}\nSize = {b.info['size']}\nRot = {b.info['rot']}\nType = {b.info['type']}\nRender = {bool(b.info['rendercond'])}","pixel2.ttf",40,0,0,0,self.theme["bright"],-0.9,0.2)
				if b.name in object_manager.values.keys():
					off = 0
					for i in object_manager.values[b.name].keys():
						self.tm.drawtext2(f"{i} : {object_manager.values[b.name][i]}"                                                                                                                             ,"pixel2.ttf",40,0,0,0,self.theme["bright"],-0.9,(-1 * 0.08 * off) - 0.3)
						off += 1
				else:
					self.tm.drawtext(f"no variables"                                                                                                                                                              ,"pixel2.ttf",40,0,0,0,self.theme["bright"],-0.8,-0.2)
					

				if not self.textline(GameManager,self.dostring2,f"what command for object {b.name}:")== self.secretword:
					self.dostring2 = self.textline(GameManager,self.dostring2,f"what command for object {b.name}:")
				else:
					self.savemode = "Obj" + self.dostring2.rstrip()

			elif "Objvar:" in self.savemode:
				st = self.savemode.rstrip()
				st = st.strip()
				st = st.replace("Objvar:", "")
				varname = ""
				varlue = ""
				gate = 0
				for i in st:
					if gate:
						varlue = varlue + str(i)
					if not i == "=" and not gate:
						varname = varname + str(i)
					else:
						gate = 1
					
				varname = str(varname)
				varlue = str(varlue)
				object_manager.set_value(self.dostring.name,varname,varlue)
				self.savemode = "alterobj"
				self.dostring2 = ""

			elif "Objdelvar:" in self.savemode:
				st = self.savemode.rstrip()
				st = st.strip()
				st = st.replace("Objdelvar:", "")
				varname = st
				if self.dostring.name in object_manager.values.keys():
					if varname in object_manager.values[self.dostring.name].keys():
						object_manager.values[self.dostring.name].pop(varname)
				self.savemode = "alterobj"
				self.dostring2 = ""
		
			elif "Objmove:" in self.savemode:
				st = self.savemode.rstrip()
				st = st.strip()
				st = st.replace("Objmove:[", "")
				st = st.replace("]", "")
				st = st.strip()
				varname = st
				x = []
				y = []
				gate = 0
				for i in st:
					if gate:
						x.append(int(i))
					if not i == "," and not gate:
						y.append(int(i))
					else:
						gate = 1
				xnum = int(''.join(str(i) for i in x))
				ynum = int(''.join(str(i) for i in y))
				object_manager.objects[self.dostring.name]["pos"] = [xnum,ynum]
				self.savemode = "alterobj"
				self.dostring2 = ""


			elif "Objrot:" in self.savemode:
				st = self.savemode.rstrip()
				st = st.strip()
				st = st.replace("Objrot:", "")
				st = st.strip()
				varname = int(st)
				object_manager.objects[self.dostring.name]["rot"] = varname
				self.savemode = "alterobj"
				self.dostring2 = ""



			elif self.savemode == "Objanim":
				self.savemode = "animate"
				self.showdata = False
				um.state = "anim"
				self.animstr = self.dostring.name
				self.animobj = object_manager.objects[self.animstr]
				um.addrect([2000,2000],["anim"],[0,0],"animbg",color = univars.theme["dark"])
				um.addrect([64 * 2.4,64 * 2.4],["anim"],[2,0.7],"animspriteuibox",color=univars.theme["semibright"])
				um.addrect([64 * 2,64 * 2],["anim"],[2,0.7],"animspriteui",surf = self.animobj["name"],sn = self.animobj["sn"])
				um.addtext("spritenames","None",univars.defont,[2,0.7],univars.theme["bright"],60,["anim"])
				self.snts = ""





			elif self.savemode == "animate":
				um.lerpval("animspriteuibox","pos",[-0.8,0.7],4)
				um.lerpval("animspriteui","pos",[-0.8,0.7],6)
				um.lerpval("spritenames","pos",[-0.5,0.7],6)
				um.elements["spritenames"]["text"] = f"sprite-num:{self.animobj['sn']}"
				if not self.textline(GameManager,self.snts,f"/s , /o , /p, /f:")== self.secretword:
					self.snts = self.textline(GameManager,self.snts,f"/s , /o , /p, /f:")
				else:
					try:
						if int(self.snts) in range(len(univars.func.getsprites(self.animobj["name"]))):
							object_manager.objects[self.animstr]["sn"] = int(self.snts)
							um.elements["animspriteui"]["surf"] = univars.func.getsprites(self.animobj["name"])[self.animobj["sn"]]
					except:
						pass
					self.snts = ""






					





			elif self.savemode == "Objinst":
				self.om.instables.append(self.om.objects[self.dostring.name]["name"])
				self.dostring = 0
				self.savemode = 0

			elif self.savemode in ["Objretype","Objtype","Objre-type","Objre type"]:
				self.altmode(GameManager,object_manager)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.dostring3 = self.dostring3[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.dostring3 += GameManager.event_manager.code
					self.tm.drawtext2(f"What type do you want to set it's type to?","pixel2.ttf",60,0,0,0,self.theme["semibright"],-0.4,0.9)
					GameManager.uibox((1170,80),(0.2,-0.6),self.theme[2],400)
					self.tm.drawtext2(f"{self.dostring3}","pixel2.ttf",60,0,0,0,self.theme["semibright"],-0.4,-0.6)
					GameManager.blituis(object_manager.sprites[self.dostring][0],(0.2,0.1),(7 * 64,7 * 64),self.rot,1000)
				else:
					if not self.dostring3 == "":
						object_manager.objects[self.dostring][9] = self.dostring3.rstrip()
						self.savemode = 0

			elif self.savemode in ["Objrescale","Objscale","Objre-scale","Objre scale"]:
				GameManager.uibox((self.realscreeen.get_width(),self.realscreeen.get_height()),(0,0),(0,0,0),100)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.dostring3 = self.dostring3[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.dostring3 += GameManager.event_manager.code
					GameManager.blituis(object_manager.sprites[self.dostring][0],(0,0.5),(4 * self.dim,4 * self.dim),self.rot,1000)
					self.tm.drawtext(f"name = {self.dostring}","pixel2.ttf",70,0,0,0,(0,0,0),0,-0.1)
					self.tm.drawtext2(f"width: {self.dostring3}","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,-0.5)
				else:
					if not self.dostring3 == "":
						self.dostring4 = ""
						self.savemode = "Rescaley"

			elif self.savemode == "Rescaley":
				GameManager.uibox((self.realscreeen.get_width(),self.realscreeen.get_height()),(0,0),(0,0,0),100)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.dostring4 = self.dostring4[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.dostring4 += GameManager.event_manager.code
					GameManager.blituis(object_manager.sprites[self.dostring][0],(0,0.5),(4 * self.dim,4 * self.dim),self.rot,1000)
					self.tm.drawtext(f"name = {self.dostring}","pixel2.ttf",70,0,0,0,(0,0,0),0,-0.1)
					self.tm.drawtext2(f"Height: {self.dostring4}","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,-0.5)
				else:
					if not self.dostring4 == "":
						object_manager.scaleto(self.dostring,[int(self.dostring3.rstrip()) * self.dim, int(self.dostring4.rstrip()) * self.dim])
						self.savemode = 0

			elif "rend" in self.savemode and "true" in self.savemode and "Obj" in self.savemode:
				object_manager.objects[self.dostring][6] = 1
				self.dotring = ""
				self.savemode = "alterobj"

			elif "rend" in self.savemode and "false" in self.savemode and "Obj" in self.savemode:
				object_manager.objects[self.dostring][6] = 0
				self.dotring = ""
				self.savemode = "alterobj"

			else:
				if not self.commmandtring.rstrip() in ["Com","Obj"]:
					if "state:" in self.commmandtring.rstrip():
						self.cht = self.commmandtring.rstrip().replace("state:", "")
						self.comm = True
						self.savemode = 0
					elif "find:" in self.commmandtring.rstrip():
						self.cht = self.commmandtring.rstrip().replace("find:", "")
						self.dostring = object_manager.objfromid(self.cht)
						if not self.dostring == None:
							self.dostring2 = ""
							self.savemode = "alterobj"
						self.commmandtring = ""
					elif "delete:" in self.commmandtring.rstrip():
						self.cht = self.commmandtring.rstrip().replace("delete:", "")
						self.dostring = object_manager.objfromid(self.cht)
						if not self.dostring == None:
							object_manager.removeid(self.cht)
						self.commmandtring = ""
					else:
						self.savemode = 0


			self.placable -= 1 * GameManager.frame_manager.dt
			self.rotable -= 1 * GameManager.frame_manager.dt
			self.gridable -= 1 * GameManager.frame_manager.dt
			self.saveable -= 1 * GameManager.frame_manager.dt
			self.rectable -= 1 * GameManager.frame_manager.dt
			self.showdatable -= 1 * GameManager.frame_manager.dt
			

			if self.showdata and self.savemode == 0 :
				fulllist = self.spritenames + self.spritenames
				GameManager.uibox((self.realscreeen.get_width(),200),(0,-1),univars.theme["dark"],200)
				self.tm.drawtext(f"Camera-name : {cm.currentcam}"                        ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],0.6,-0.9)
				self.tm.drawtext2(f"Camera size: { round(1 / camera.size,2)}"            ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],0,-0.9)
				self.tm.drawtext2(f"Camera pos: {[round(camera.x),-1 * round(camera.y)]}","pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.6,-0.9)
				GameManager.uibox((400,160),(-0.78,0.75),univars.theme["dark"],200)
				self.tm.drawtext2(f"State : {smate}",                                     "pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.97,0.85 - 0.05)
				self.tm.drawtext2(f"Map : {object_manager.loadedmap}",                    "pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.97,0.75 - 0.05)
					


				#the ui for object placement
				if debug:
					GameManager.uibox((360,252),(0.8,0.65),        univars.theme["dark"],200)
					GameManager.uibox((64 + 10,64 + 10),(0.8,0.8 ),univars.theme["semibright"],400)
					GameManager.uibox((64 + 10,64 + 10),(0.92,0.8),univars.theme["semibright"],50)
					GameManager.uibox((64 + 10,64 + 10),(0.68,0.8),univars.theme["semibright"],50)
					GameManager.blituis(self.func.getsprites(self.spritenames[self.sprite])[0],(0.8,0.8),(64,64),self.rot,1000)
					GameManager.blituis(self.func.getsprites(fulllist[self.sprite + 1])[0],(0.92,0.8),(64,64),self.rot,100)
					GameManager.blituis(self.func.getsprites(self.spritenames[self.sprite - 1])[0],(0.68,0.8),(64,64),self.rot,100)
					self.tm.drawtext(f"Object-name : {self.spritenames[self.sprite]}",       "pixel2.ttf",40,0,0,0,univars.theme["semibright"],0.8,0.6)
					self.tm.drawtext(f"Object-type : {self.typelist[self.sprite]}",          "pixel2.ttf",40,0,0,0,univars.theme["semibright"],0.8,0.5)





				GameManager.frame_manager.showfps = 1
			else:
				object_manager.showmap = False
				GameManager.frame_manager.showfps = 0
