import pygame
import Managers.Cameramod as Cameramod
import Managers.Cammanager as Cammanager
import Managers.Textmanager as Textmanager
import Managers.funcs as funcs
import Managers.univars as univars
import Managers.backgroundmanager as backgroundmanager
import Managers.Uimanager as Uimanager
import Managers.Cammanager as Cammanager
import Managers.objectmanager as objectmanager
import Managers.Particlesytem as particlesystem
import os
um = Uimanager.ingame
cam = Cameramod.cam
cam = Cammanager.camager.cameras["def"]
bg = backgroundmanager.bg
object_manager = objectmanager.om
pm = particlesystem.pm

spritesnlen = {}

for spritefolder in os.listdir("Graphics/sprites"):
	folder_dir = f"Graphics/sprites/{spritefolder}"
	spritesnlen[spritefolder] = len(os.listdir(folder_dir))


class TiledSoftwre:
	def __init__(self,realscreen,theme,grandim,screen,om):
		self.pause = True
		self.showconsolebool = univars.showdebugonstart
		self.realscreeen = realscreen
		self.consoletextscoll = 1
		self.theme = theme
		self.tm = Textmanager.Textmanager(realscreen)
		self.func = funcs.func(grandim)
		self.om = om
		self.secretword = "404 error"
		self.coll = True
		self.screen = screen
		self.savestring = ""
		self.mode = 0
		self.sprite = 0
		self.placable = 0
		self.rot = 0
		self.rotable = 0
		self.saveable = 0
		self.layer = 0
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
		self.parts = {"type":"circle","pos":[0,0],"divergence":[[-5,5],[0,0]],"color":(255,255,255),"initvel":[0,10],"force":[0,-1],"size":10,"sizedec":1,"dim":1,"alpha":1000,"alphadec":0,"colordec":(0,0,0),"quality":0.7,"divergenceforce":[[0,0],[0,0]],"divergencepos":[[0,0],[0,0]],"ntimes":1,"speed":1}
		self.comm = False
		self.loadedparticle = "None"
		self.actuallyload = True
		self.keydelay = 0
		self.sn = 0
		self.newparticle = None
		self.cht = univars.startstate
		self.loadingmap = False
		self.spritenames = univars.func.allsprites()
		self.typelist = univars.func.allsprites()
		self.allsize = univars.func.allones()
		self.spritelooks = univars.func.allsprites()
		self.newsprites()


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

	def newsprites(self):
		for i in univars.newsprites.keys():
			# print(self.spritelooks)
			self.spritenames.append(i)
			self.typelist.append(i)
			self.allsize.append([1,1])
			self.spritelooks.append(univars.newsprites[i])
			# print(self.spritelooks)


	def extra(self,extras):
		if not extras == ["none"]:
			for i in extras:
				self.spritelooks.append(i[0])
				self.spritenames.append(i[0])
				self.typelist.append(i[1])
				self.allsize.append(i[2])

	def commandline(self,GameManager,dostring,precursur):
		GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],200),(0,-1),univars.theme["dark"],200)
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

	def textline(self,GameManager,dostring,precursur,col = univars.theme["dark"]):
		GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],200),(0,-1),col,600)
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


	def uitext(self,name,GameManager):
		if not GameManager.event_manager.key[pygame.K_RETURN]:
			if GameManager.event_manager.key[pygame.K_BACKSPACE]:
				um.elements[name]["text"] = um.elements[name]["text"][:-1]
			else:
				if GameManager.event_manager.keyb:
					um.elements[name]["text"] += GameManager.event_manager.code



	def Run(self,work,speed,GameManager,camera,dim,debug,cm,smate):
		self.showdata = GameManager.publicvariables["showdata"]
		movecam = GameManager.publicvariables["cammove"]
		
	
		if work:
			if GameManager.states == "Editor":
				Cammanager.camager.setcam("def")
			if self.placable <= 0 and GameManager.event_manager.key[pygame.K_0] and GameManager.event_manager.key[pygame.K_LCTRL] or self.placable <= 0 and GameManager.event_manager.controller["touchpad"]:
				self.placable = 5
				if GameManager.smstate == "edit":
					GameManager.setbosh("debugame")
				else:
					GameManager.setbosh("edit")

			self.comm = False
			self.loadingmap = False
			self.dim = dim
			# um.addbutton([300,300],"all",[0,0],"srbiunp",color=(200,200,200))
			if GameManager.event_manager.key[pygame.K_p]:
				if GameManager.event_manager.key[pygame.K_LCTRL]:
					if self.placable <= 0:
						self.placable = 5
						self.showconsolebool = not self.showconsolebool

			if GameManager.event_manager.key[pygame.K_PAGEUP]:
				self.consoletextscoll -= 0.05 * GameManager.dt

			if GameManager.event_manager.key[pygame.K_PAGEDOWN]:
				self.consoletextscoll += 0.05 * GameManager.dt

			if GameManager.event_manager.key[pygame.K_LCTRL]:
				if GameManager.event_manager.key[pygame.K_PAGEUP]:
					self.consoletextscoll -= 0.05 * GameManager.dt

				if GameManager.event_manager.key[pygame.K_PAGEDOWN]:
					self.consoletextscoll += 0.05 * GameManager.dt
			# GameManager.print(self.consoletextscoll)

			self.showconsole(GameManager)
							


			#mode for level editing
			if self.mode == 0:
				if GameManager.states == "Editor":
					um.state = "def"
				if GameManager.event_manager.key[pygame.K_v]:
					if GameManager.event_manager.key[pygame.K_LCTRL]:
						if GameManager.publicvariables["showdata"] == 1:
							if self.showdatable < 1:
								GameManager.publicvariables["showdata"] = 0
								self.showdatable = 10
						if GameManager.publicvariables["showdata"] == 0:
							if self.showdatable < 1:
								GameManager.publicvariables["showdata"] = 1
								self.showdatable = 10

				if debug:
					#increaes len off typelist
					if len(self.typelist) < len(self.spritelooks):
						for i in range(len(self.spritelooks) - len(self.typelist)):
							self.typelist.append("none")


					
					# if GameManager.event_manager.releasekey:
					# 	self.placable = -1
					#to move spite on the rotar
					self.sprite += GameManager.event_manager.scroll
					if self.placable <= 0:
						if GameManager.event_manager.key[pygame.K_6]:
							self.placable = 6
							self.sprite -= 1
						if GameManager.event_manager.key[pygame.K_7]:						
							self.placable = 6
							self.sprite += 1



					

					#make sure it loops the sprite rotar
					if self.sprite > (len(self.spritelooks) - 1):
						self.sprite = 0
					elif self.sprite < 0:
						self.sprite = (len(self.spritenames) - 1)


					if self.placable <= 0 and GameManager.event_manager.key[pygame.K_4]:
						self.placable = 5
						self.sn -= 1

					if self.placable <= 0 and GameManager.event_manager.key[pygame.K_5]:
						self.placable = 5
						self.sn += 1


					if self.sn >= spritesnlen[self.spritelooks[self.sprite]] -1:
						self.sn = spritesnlen[self.spritelooks[self.sprite]] -1

					if self.sn < 0:
						self.sn = 0


					#some math
					renderwid = (univars.rw * 1980) + 200
					upscale = 1
					upscaley =  1


					# upscale = renderwid/ univars.screen.get_width()
					# print(upscale)


					# upscale *= 
					translationy = 0
					translationx = 0
					# translation = 0
					# print(upscale)
					# print(1/upscale)
					# print()
					a1 = (((   (GameManager.event_manager.mousepos[0] -  univars.realscreeen.get_width()//2 )/upscale   )  / camera.size ) + camera.x)
					a2 = (((   (GameManager.event_manager.mousepos[1] -  univars.realscreeen.get_height()//2 )/upscaley  )  / camera.size ) + camera.y)
				

					mousepos = (a1,a2)
					thingtogo = self.func.getsprites(self.spritelooks[self.sprite])[self.sn]
					thingtogo = pygame.transform.scale_by(thingtogo,self.allsize[self.sprite])
					thingtogo.set_alpha(100)
					GameManager.blitsurf(thingtogo,((round(a1/dim) * dim),(round(a2/dim) * dim)),self.rot,camera)
					gridpos = (round(mousepos[0]/self.dim) * self.dim , round(mousepos[1]/self.dim) * self.dim)


					#to confirm the starting position
					if self.gridable < 1:
						if self.grip == 0:
							if GameManager.event_manager.key[pygame.K_x]:	
								self.pos1 = gridpos
								self.grip = 1
								self.gridable = 10

					#to show the about to be gridded object
					if self.grip == 1:
						GameManager.blitsurf(thingtogo,self.pos1,self.rot,camera)
						# GameManager.blit(self.func.getsprites(self.spritenames[self.sprite])[0],self.func.getsprites(self.spritenames[self.sprite])[0].get_rect(center = (self.pos1)),self.rot,camera)

					#multi place/delete
					if self.gridable < 1:
						if self.grip == 1:
							if GameManager.event_manager.key[pygame.K_x]:
								cont = GameManager.event_manager.key[pygame.K_LCTRL]
								savedrot = self.rot
								savedsn = self.sn
								savedcol  = self.coll
								self.pos2 = list(gridpos)
								self.grip = 0
								self.gridable = 10
								#if endpos is greater than start  (x)
								xpos = (self.pos2[0] - self.pos1[0]) > 0
								#if endpos is greater than start  (y)
								ypos = (self.pos2[1] - self.pos1[1]) > 0
								yinc = univars.grandim
								xinc = univars.grandim
								if not ypos:
									yinc *= -1
									self.pos2[1] -= univars.grandim
								else:
									self.pos2[1] += univars.grandim
								if not xpos:
									xinc *= -1
									self.pos2[0] -= univars.grandim
								else:
									self.pos2[0] += univars.grandim
									
								for y in range(self.pos1[1],self.pos2[1],yinc):
									for x in range(self.pos1[0],self.pos2[0],xinc):
										already = False
										bevel = 0
										bevelsleek = 0
										if cont and self.spritenames[self.sprite] == "grass":
											xedge = x == self.pos2[0] - xinc 
											yedge = y == self.pos2[1] - yinc
											startxedge = x == self.pos1[0] 
											startyedge = y == self.pos1[1] 


											mincrustx = x == self.pos2[0] - xinc - xinc or x == self.pos1[0] + xinc
											mincrusty = y == self.pos2[1] - yinc - yinc or y == self.pos1[1] + yinc
											mincrust = mincrustx or mincrusty

											top = startyedge and ypos or yedge and not ypos
											bot =  yedge and ypos or startyedge and not ypos
											left = startxedge and xpos or xedge and not xpos
											right = xedge and xpos or startxedge and not xpos

											cor1 = top and right
											cor2 = top and left
											cor3 = bot and right
											cor4 = bot and left
											corner =  cor1 or cor2 or cor3  or cor4
											unop = object_manager.unopcollidep((x,y),0,0)

											if len(unop["inst"]) > 0:
												already = 1
												bevel = (unop["inst"][0].sn == 0 or unop["inst"][0].sn == 3  or unop["inst"][0].sn == 2) and (xedge or startxedge or yedge or startyedge)
												bevelsleek =  unop["inst"][0].usecoll == 1

											
											
											if ((not xedge and not yedge and not startxedge and not startyedge) or already) and not bevel:
												if (not mincrust) or already:
													self.coll = False
												else:
													self.coll = True
												self.sn = 1
											elif corner:
												self.sn = 2
												self.coll = True
											else:
												self.coll = True
												self.sn = 0


											if bevel:
												self.sn = 3
												self.coll = 1
												if left:
													self.rot = 0
												elif right:
													self.rot = -180
												elif top:
													self.rot = 90
												elif top:
													self.rot = 270
											elif corner:
												if cor1:
													self.rot = 0
												elif cor2:
													self.rot = 90
												elif cor3:
													self.rot = 270
												elif cor4:
													self.rot = 180
												
								
											elif self.sn == 0:
												if top:
													self.rot = 0
												elif bot:
													self.rot = 180
												elif left:
													self.rot = 90
												elif right:
													self.rot = 270
											else:
												self.rot = 0
												
											
										
											# # if ypos:
											# if yedge:
											# else:
											# else:
											# 	if startyedge:
											# 		self.sn = 0
											# 	else:
											# 		self.sn = 1

										if not already or bevel or bevelsleek:
											self.om.add(GameManager,(x,y),self.spritenames[self.sprite],self.rot,self.typelist[self.sprite],self.allsize[self.sprite],dim,keepprev=GameManager.event_manager.key[pygame.K_LCTRL],layer = self.layer,colforinst=self.coll,sn = self.sn)

								self.coll = savedcol
								self.sn = savedsn
								self.rot = savedrot
							if GameManager.event_manager.key[pygame.K_v]:
								self.pos2 = list(gridpos)
								self.grip = 0
								self.gridable = 10
								xpos = (self.pos2[0] - self.pos1[0]) > 0
								ypos = (self.pos2[1] - self.pos1[1]) > 0
								yinc = univars.grandim
								xinc = univars.grandim
								if not ypos:
									yinc *= -1
									self.pos2[1] -= univars.grandim
								else:
									self.pos2[1] += univars.grandim
								if not xpos:
									xinc *= -1
									self.pos2[0] -= univars.grandim
								else:
									self.pos2[0] += univars.grandim
									
								for y in range(self.pos1[1],self.pos2[1],yinc):
									for x in range(self.pos1[0],self.pos2[0],xinc):
										self.om.remove((x,y),layer=self.layer)		
							if GameManager.event_manager.key[pygame.K_f]:
								self.pos2 = list(gridpos)
								self.grip = 0
								self.gridable = 10
								xpos = (self.pos2[0] - self.pos1[0]) > 0
								ypos = (self.pos2[1] - self.pos1[1]) > 0
								yinc = univars.grandim
								xinc = univars.grandim
								if not ypos:
									yinc *= -1
									self.pos2[1] -= univars.grandim
								else:
									self.pos2[1] += univars.grandim
								xinc = univars.grandim
								if not xpos:
									xinc *= -1
									x = self.pos1[0] + univars.grandim
								else:

									x = self.pos1[0] - univars.grandim
								for y in range(self.pos1[1],self.pos2[1],yinc):
									x += xinc
									self.om.add(GameManager,(x,y),self.spritenames[self.sprite],self.rot,self.typelist[self.sprite],self.allsize[self.sprite],dim,keepprev=GameManager.event_manager.key[pygame.K_LCTRL],layer = self.layer,colforinst=self.coll,sn = self.sn)
							if GameManager.event_manager.key[pygame.K_g]:
								self.pos2 = list(gridpos)
								self.grip = 0
								self.gridable = 10
								xpos = (self.pos2[0] - self.pos1[0]) > 0
								ypos = (self.pos2[1] - self.pos1[1]) > 0
								yinc = univars.grandim
								xinc = univars.grandim
								if not ypos:
									yinc *= -1
									self.pos2[1] -= univars.grandim
								else:
									self.pos2[1] += univars.grandim
								xinc = univars.grandim
								if not xpos:
									xinc *= -1
									x = self.pos1[0] + univars.grandim
								else:

									x = self.pos1[0] - univars.grandim
								for y in range(self.pos1[1],self.pos2[1],yinc):
									x += xinc
									self.om.remove((x,y),layer=self.layer)		

					#to rotate
					if self.rotable < 1:
						if GameManager.event_manager.key[pygame.K_z]:
							self.rot += 45
							self.rotable = 10
						if GameManager.event_manager.key[pygame.K_c]:
							self.rot -= 45
							self.rotable = 10
						if self.rot == 180:
							self.rot = -180
						if self.rot < -180:
							self.rot = 360 + self.rot






					#to place
					if not GameManager.event_manager.mouse[0] and GameManager.event_manager.lastmouse[0]:
						object_manager.add(GameManager,gridpos,self.spritelooks[self.sprite],self.rot,self.typelist[self.sprite],self.allsize[self.sprite],dim,keepprev=GameManager.event_manager.key[pygame.K_LCTRL],stagename=self.spritenames[self.sprite],layer = self.layer,colforinst=self.coll,sn = self.sn)

					#to remove
					if GameManager.event_manager.mouse[2]:
						object_manager.remove(gridpos,layer=self.layer)
					
					if self.placable <= 0 and type(self.layer) == int:
						if GameManager.event_manager.key[pygame.K_1]:
							self.placable = 5
							self.layer -= 1
						if GameManager.event_manager.key[pygame.K_2]:
							self.placable = 5
							self.layer += 1

					if self.placable <= 0 and GameManager.event_manager.key[pygame.K_3]:
						self.placable = 5
						self.coll = not self.coll

					
					#to check an inst or non-inst's info
					if GameManager.event_manager.key[pygame.K_r]:
						mousecol = object_manager.unopcollidep(gridpos,0,camera,dim)
						if len(mousecol["obj"]) > 0:
							a = mousecol["obj"][0].info
							a1 = mousecol['obj'][0].name
							maxlen = 100
							off = 1
							if a1 in object_manager.values.keys():
								for i in object_manager.values[a1].keys():
									strb = len(f"{i} : {object_manager.values[a1][i]}") * 13
									if strb > maxlen:
										maxlen = strb
									off += 1
							b = pygame.Surface((maxlen,120 + (off * 10)))
							b.fill(univars.theme["dark"])
							b.set_alpha(150)
							GameManager.Gotomousepos2(b)
							self.tm.textatmouse(f"Normal Object\nId = { mousecol['obj'][0].name }\nName = {a['name']}\nType = {a['type']}\nPos = {a['pos']}\nSize = {a['size']}\nRot = {a['rot']}\nLayer = {a['layer']}\nRender = {bool(a['rendercond'])}","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,-20)
							if a1 in object_manager.values.keys():
								off = 0
								for i in object_manager.values[a1].keys():
									self.tm.textatmouse(f"{i} : {object_manager.values[a1][i]}","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,(-1 * off * 10) - 110)
									off += 1
							else:
								self.tm.textatmouse(f"No variables","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,0 - 110)

							if GameManager.event_manager.key[pygame.K_LCTRL]:
								self.dostring2 = ""
								self.dostring = mousecol["obj"][0]
								self.mode = "alterobj"

						if len(mousecol["inst"]) > 0:
							a = mousecol["inst"][0]
							b = pygame.Surface((100,110))
							b.fill(univars.theme["dark"])
							b.set_alpha(150)
							GameManager.Gotomousepos2(b)
							self.tm.textatmouse(f"Instanciated Object\nType = {a.type}\nName = { a.stagename }\nPos = {a.realpos}\nLayer = {a.layer}\nRot = {a.rot}\nCollision = {a.usecoll}\nSize = {a.size}\nAlpha = {a.alpha}","pixel2.ttf",30,0,univars.theme["bright"],GameManager.event_manager,10,-20)

							# if GameManager.event_manager.key[pygame.K_LCTRL]:
							# 	self.dostring2 = ""
							# 	self.dostring = mousecol["inst"][0]
							# 	self.mode = "alterinst"


					#to load levels
					if GameManager.event_manager.key[pygame.K_l]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							if self.saveable < 1:
								self.mode = 3
								self.savestring = ""
								self.saveable = 10


					#to save levels
					if GameManager.event_manager.key[pygame.K_s]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							if self.saveable < 1:
								if not object_manager.loadedmap == "Null":
									self.mode = 2
									self.savestring = object_manager.loadedmap
								else:
									self.mode = 1
									self.savestring = ""
								self.saveable = 10


					#to hide/show ui

					#to open command-line
					if GameManager.event_manager.key[pygame.K_b]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							self.commmandtring = ""
							self.mode = "command"



				else:
					object_manager.showall = False
					if GameManager.event_manager.key[pygame.K_b]:
						if GameManager.event_manager.key[pygame.K_LCTRL]:
							self.commmandtring = ""
							self.mode = "command"
							
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

			#mode to name save-file
			elif self.mode == 1:
				movecam = 0
				GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],pygame.display.get_desktop_sizes()[0][1]),(0,0),(0,0,0),100)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.savestring = self.savestring[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.savestring += GameManager.event_manager.code
					self.tm.drawtext2(f"What do you want to name your file: {self.savestring}","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,0)
				else:
					if not self.savestring == "":
						if object_manager.savetilemap(GameManager,self.savestring.rstrip()) == "No":
							self.mode = 2
						else:
							self.mode = 0
			
			#mode to force-save
			elif self.mode == 2:
				movecam = 0
				GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],pygame.display.get_desktop_sizes()[0][1]),(0,0),(0,0,0),100)
				self.tm.drawtext2(f"{self.savestring.rstrip()} already exists do you want to replace it Y/N","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,0)
				if GameManager.event_manager.keyb:
					if GameManager.event_manager.code == "y":
						object_manager.forcesavetilemap(GameManager,self.savestring.rstrip())
						self.mode = 0
					else:
						self.mode = 1

			#save mode for loading
			elif self.mode == 3:
				movecam = 0
				GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],pygame.display.get_desktop_sizes()[0][1]),(0,0),(0,0,0),100)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.savestring = self.savestring[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.savestring += GameManager.event_manager.code
					self.tm.drawtext2(f"What file do you want to load: {self.savestring}","pixel2.ttf",60,0,0,0,(0,0,0),-0.8,0)
				else:
					object_manager.loadtilemap(GameManager,self.savestring.rstrip())
					self.loadingmap = True
					self.mode = 0


			elif self.mode == "command":
				movecam = 0
				GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],200),(0,-1),univars.theme["dark"],200)
				if not GameManager.event_manager.key[pygame.K_RETURN]:
					if GameManager.event_manager.key[pygame.K_BACKSPACE]:
						self.commmandtring = self.commmandtring[:-1]
					else:
						if GameManager.event_manager.keyb:
							self.commmandtring += GameManager.event_manager.code
					self.tm.drawtext2(f"Input a command: {self.commmandtring}","pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.95,-0.9)
				else:
					self.dostring = ""
					self.mode = "Com" + self.commmandtring.rstrip()

			elif self.mode == "Comcamera" or self.mode == "Comcam":
				a = self.commandline(GameManager,self.dostring,"What Camera X:")
				if not a == self.secretword:
					self.dostring = a
				else:
					self.dostring2 = ""
					Cammanager.camager.setcond("def","posx",float(self.dostring.rstrip()))
					self.mode = "camy"

			elif self.mode == "camy":
				a = self.commandline(GameManager,self.dostring2,"What Camera Y:")
				if not a == self.secretword:
					self.dostring2 = a
				else:
					Cammanager.camager.setcond(Cammanager.camager.currentcam,"posy",-1 * float(self.dostring2.rstrip()))
					self.mode = 0

			elif self.mode == "Comspeed":
				a = self.commandline(GameManager,self.dostring,"What Speed ?:")
				if not a == self.secretword:
					self.dostring = a
				else:
					object_manager.speed = float(self.dostring.rstrip())
					self.mode = 0

			elif "show" in self.mode and "all" in self.mode and "col" in self.mode and "Com" in self.mode:
				object_manager.showcolist = "all"
				self.mode = 0

			elif "all" in self.mode and "hide" in self.mode and "col" in self.mode and "Com" in self.mode:
				object_manager.showcolist = []
				self.mode = 0

			elif "all" in self.mode and "hide" in self.mode and "rend" in self.mode and "Com" in self.mode:
				object_manager.showall = False
				self.mode = 0

			elif "all" in self.mode and "show" in self.mode and "rend" in self.mode and "Com" in self.mode:
				object_manager.showall = True
				self.mode = 0

			elif "tile" in self.mode and "Com" in self.mode:
				object_manager.tile()
				self.mode = 0

								
			elif self.mode == "alterobj":
				movecam = 0
				GameManager.uibox((400,pygame.display.get_desktop_sizes()[0][1] ),(-0.75,0.15),self.theme["dark"] ,400)
				b = self.dostring
				Cammanager.camager.setcond("def","pos",   univars.func.lerp(Cammanager.camager.getcam("def","pos")   ,b.info["pos"],4,roundto=8)    )
				Cammanager.camager.setcond("def","size",   univars.func.lerp(Cammanager.camager.getcam("def","size"),1/b.info["sizen"][0],4,roundto=8)    )
				strbuf = ""
				for i in b.info.keys():
					strbuf += f"{i} = {b.info[i]}\n"
				self.tm.drawtext2(strbuf,"pixel2.ttf",40,0,0,0,self.theme["bright"],-0.9,0.2 + 0.25)
				if b.name in object_manager.values.keys():
					off = 0
					for i in object_manager.values[b.name].keys():
						self.tm.drawtext2(f"{i} : {object_manager.values[b.name][i]}"                                                                                                                             ,"pixel2.ttf",40,0,0,0,self.theme["bright"],-0.9,(-1 * 0.08 * off) - 0.3 + 0.25)
						off += 1
				else:
					self.tm.drawtext2(f"no variables"                                                                                                                                                              ,"pixel2.ttf",40,0,0,0,self.theme["bright"],-0.9,                   -0.3 + 0.25)
					
				

				if not self.textline(GameManager,self.dostring2,f"what command for object {b.name}:")== self.secretword:
					self.dostring2 = self.textline(GameManager,self.dostring2,f"what command for object {b.name}:")
				else:
					self.mode = "Obj" + self.dostring2.rstrip()

			elif "Objvar:" in self.mode:
				st = self.mode.rstrip()
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
				varlue = eval(str(varlue))
				object_manager.set_value(self.dostring.name,varname,varlue)
				self.mode = "alterobj"
				self.dostring2 = ""

			elif "Objdelvar:" in self.mode:
				st = self.mode.rstrip()
				st = st.strip()
				st = st.replace("Objdelvar:", "")
				varname = st
				if self.dostring.name in object_manager.values.keys():
					if varname in object_manager.values[self.dostring.name].keys():
						object_manager.values[self.dostring.name].pop(varname)
				self.mode = "alterobj"
				self.dostring2 = ""
		
			elif "Obj" in self.mode and "=" in self.mode:
				st = self.mode.rstrip()
				st = st.replace("Obj","")
				st = st.strip()
				st = st.split("=")
				try:
					if st[0] in object_manager.objects[self.dostring.name].keys():
						object_manager.objects[self.dostring.name][st[0]] = eval(st[1])
						self.mode = "alterobj"
						self.dostring2 = ""
				except:
					try:
						if st[0] in object_manager.objects[self.dostring.name].keys():
							object_manager.objects[self.dostring.name][st[0]] = str(st[1])
							self.mode = "alterobj"
							self.dostring2 = ""
					except:
						self.mode = "alterobj"
						self.dostring2 = ""





			elif self.mode == "Objanim":
				self.buttonsforanim = []
				self.textsforanim = []
				self.mode = "animate"
				self.showdata = False
				um.state = "anim"
				self.animstr = self.dostring.name
				self.animobj = object_manager.objects[self.animstr]
				um.addrect([2000,2000],["anim","animplaying","newanim"],[0,0],"animbg",color = univars.theme["dark"])
				um.addrect([64 * 2.4,64 * 2.4],["anim","animplaying","newanim"],[2,0.7],"animspriteuibox",color=univars.theme["semibright"])
				um.addrect([64 * 2,64 * 2],["anim","animplaying","newanim"],[2,0.7],"animspriteui",surf = self.animobj["name"],sn = self.animobj["sn"],usesprite=True)
				self.curanim = None
				a = -1.1
				if self.animobj["name"] in object_manager.animations.keys():
					for i in object_manager.animations[self.animobj["name"]].keys():
						a += 0.3
						um.addbutton(univars.sizes["smallbutton"],["anim","animplaying"],[a,0],i + "button",color=univars.theme["mid"])
						um.addtext(i + "text",i,univars.defont,[a,0],univars.theme["bright"],30,["anim","animplaying"])
						um.bindtobutton(i + "text",i + "button")
						um.addglide(i + "button",univars.sizes["mediumbutton"],univars.sizes["semilargebutton"])
						self.buttonsforanim.append(i + "button")
				a += 0.3


				um.addbutton(univars.sizes["smallbutton"],["anim","animplaying"],[a,0],"plusbutton",color=univars.theme["mid"])
				um.addtext("plustext","+",univars.defont,[a,0],univars.theme["bright"],60,["anim","animplaying"])
				um.bindtobutton("plustext","plusbutton")
				um.addglide("plusbutton",univars.sizes["mediumbutton"],univars.sizes["semilargebutton"])

				um.addbutton([32,32],["anim"],[0.95,0.9],"exitbutton",color=univars.theme["accent"])
				um.addtext("exittext","x",univars.defont,[a,0],univars.theme["bright"],60,["anim"])
				um.bindtobutton("exittext","exitbutton")
				um.addglide("exitbutton",[64,64],[64*1.2,64*1.2])


				um.addrect([2000,60],["animplaying","newanim"],[0,-0.5],"frame bar",univars.theme["accent"],alpha = 150)
				um.addtext("spritenames","None",univars.defont,[2,0.7],univars.theme["bright"],60,["anim","animplaying","newanim"])
				self.snts = ""


				um.addrect((pygame.display.get_desktop_sizes()[0][0] + 1000,200),["newanim","animplaying"],(0,-1),"commandtextbox",color=univars.theme["accent"])
				um.addtext("commandtext","","pixel2.ttf",(-0.95,-0.9),univars.theme["bright"],40,["newanim","animplaying"],center = False)

				self.textsfornewanim = []


			elif self.mode == "animate":


				def showanim(anim,states):
					for b in self.textsforanim:
						um.deleleelem(b)
					self.textsforanim = []
					a = -1.1
					for g in sorted([int(brent) for brent in anim.keys()]):
						g = str(g)
						a += 0.2
						um.addtext(g + "framepoint",g + "\n" + str(anim[g]),univars.defont,[a,-0.5],univars.theme["bright"],30,states)
						self.textsforanim.append(g + "framepoint")



				self.animobj = object_manager.objects[self.animstr]
				um.lerpval("animspriteuibox","pos",[-0.8,0.7],4)
				um.lerpval("animspriteui","pos",[-0.8,0.7],6)
				um.lerpval("spritenames","pos",[-0.4,0.7],6)
				um.elements["animspriteui"]["surf"] = univars.func.getsprites(self.animobj["name"])[self.animobj["sn"]]
				um.elements["animspriteui"]["cache"] = {}
				um.elements["spritenames"]["text"] = f"sprite-num:{self.animobj['sn']} \ncurrent anim:{self.curanim}"
				um.elements["frame bar"]["dimensions"][0] = pygame.display.get_desktop_sizes()[0][0]



	


				if not um.state == "newanim":
					for i in self.buttonsforanim:

						if um.state == "anim":
							if GameManager.key["alt-x"] != 0:
								um.elements[i]["pos"][0] = um.elements[i]["pos"][0] - GameManager.key["alt-x"]/10
								
						if um.clicked(GameManager.em,i):
							object_manager.speed = 1
							self.curanim = i.replace("button","")
							self.newanim = object_manager.animations[self.animobj["name"]][self.curanim]
							showanim(object_manager.animations[self.animobj["name"]][self.curanim],["animplaying"])


						if self.curanim == i.replace("button",""):
							um.elements[i]["color"] = univars.theme["accent"]
						else:
							um.elements[i]["color"] = univars.theme["mid"]


					for i in self.textsforanim:
						if GameManager.key["alt-x"] != 0:
							um.elements[i]["pos"][0] = um.elements[i]["pos"][0] - GameManager.key["alt-x"]/40
						if str(int(round(object_manager.objects[self.animstr]["gothru"]))) == i.replace("framepoint",""):
							um.elements[i]["color"] = univars.theme["bright"]
						else:
							um.elements[i]["color"] = univars.theme["mid"]

				

				if not self.curanim == None and not um.state == "newanim":
					object_manager.playanim(GameManager.frame_manager.dt,self.animstr,self.curanim)
					um.state = "animplaying"




				if um.clicked(GameManager.em,"plusbutton"):
					self.newanim = {}
					um.state = "newanim"
					self.curanim = None

				if um.clicked(GameManager.em,"exitbutton"):
					um.deleleelem(self.buttonsforanim)
					self.curanim = None
					um.state = "def"
					self.mode = 0
					self.showdata = 1
				



				if um.state == "newanim":
					self.uitext("commandtext",GameManager)				
					self.snts = um.elements["commandtext"]["text"]
					if GameManager.event_manager.key[pygame.K_RETURN]:
						if "fr:" in self.snts:
							self.snts = self.snts.replace("fr:","")
							self.snts = self.snts.strip()
							self.snts = self.snts.replace("="," ")
							a = self.snts.split()
							self.newanim[str(a[0])] = int(a[1])
							showanim(self.newanim,["newanim"])
							
						if "v:" in self.snts:
							self.snts = self.snts.replace("v:","")
							self.snts = self.snts.strip()
							object_manager.objects[self.animstr]["sn"] = int(self.snts)


						if "n:" in self.snts:
							self.snts = self.snts.replace("n:","")
							self.snts = self.snts.rstrip()
							self.namefornewanim = self.snts
							self.curanim = self.snts

						if self.snts.rstrip() == "/s":
							object_manager.saveanim(self.animobj["name"],self.namefornewanim,self.newanim)
							GameManager.loadanims()

						if self.snts.rstrip() == "/x":
							GameManager.loadanims()
							self.mode = "Objanim"

						if "del:" in self.snts.rstrip():
							self.snts = self.snts.rstrip()
							self.snts = self.snts.replace("del:","")
							self.snts = self.snts.strip()
							self.newanim.pop(self.snts)
							showanim(self.newanim,["newanim"])

						if self.snts == "delanim":
							object_manager.deleteanim(self.animobj["name"],self.curanim)
							object_manager.animations[self.animobj["name"]].pop(self.curanim)
							GameManager.loadanims()
							self.mode = "Objanim"

					
						um.elements["commandtext"]["text"] = ""

				if um.state == "animplaying":	
					self.uitext("commandtext",GameManager)				
					self.snts = um.elements["commandtext"]["text"]
					if GameManager.event_manager.key[pygame.K_RETURN]:
						if "fr:" in self.snts:
							self.snts = self.snts.replace("fr:","")
							self.snts = self.snts.strip()
							self.snts = self.snts.replace("="," ")
							a = self.snts.split()
							self.newanim[str(a[0])] = int(a[1])
							showanim(self.newanim,["animplaying"])

						if "v:" in self.snts:
							self.snts = self.snts.replace("v:","")
							self.snts = self.snts.strip()
							object_manager.objects[self.animstr]["sn"] = int(self.snts)


						if "n:" in self.snts:
							self.snts = self.snts.replace("n:","")
							self.snts = self.snts.rstrip()
							self.namefornewanim = self.snts
							self.curanim = self.snts

						if self.snts.rstrip() == "/s":
							object_manager.saveanim(self.animobj["name"],self.curanim,self.newanim)
							GameManager.loadanims()


						if self.snts.rstrip() == "/x":
							GameManager.loadanims()
							self.mode = "Objanim"

						if "del:" in self.snts.rstrip():
							self.snts = self.snts.rstrip()
							self.snts = self.snts.replace("del:","")
							self.snts = self.snts.strip()
							self.newanim.pop(self.snts)
							showanim(self.newanim,["animplaying"])

						if self.snts.rstrip() == "delanim":
							object_manager.deleteanim(self.animobj["name"],self.curanim)
							object_manager.animations[self.animobj["name"]].pop(self.curanim)
							GameManager.loadanims()
							self.mode = "Objanim"

						
						um.elements["commandtext"]["text"] = ""

					for i in self.textsforanim:
						if GameManager.key["alt-x"] != 0:
							um.elements[i]["pos"][0] = um.elements[i]["pos"][0] - GameManager.key["alt-x"]/40
							if str(int(round(object_manager.objects[self.animstr]["gothru"]))) == i.replace("framepoint",""):
								um.elements[i]["color"] = univars.theme["bright"]
							else:
								um.elements[i]["color"] = univars.theme["mid"]

					if GameManager.key["alt-x"] != 0 and not um.state in ["animplaying","newanim"]:
						um.elements["plusbutton"]["pos"][0] = um.elements["plusbutton"]["pos"][0] - GameManager.key["alt-x"]/10










			elif self.mode == "Particle-edit":
				movecam = 0
				um.state = "particle-edit"
				self.showdata = False
				use = self.parts
				pm.particlespawn(use["type"],cam[0],use["divergence"],
								use["color"],use["initvel"],use["force"],
								use["size"],use["sizedec"],dim = use["dim"],
								alpha = use["alpha"],alphadec=use["alphadec"],
								colordec=use["colordec"],quality=use["quality"],
								divergenceforce=use["divergenceforce"],
								divergencepos=use["divergencepos"],
								ntimes=use["ntimes"],
								speed=use["speed"])
				um.elements["loadedbluprint"]["text"] = "Loaded:" + self.loadedparticle
				um.elements["particledata"]["text"] = f"type:{use['type']} \ndivergence:{use['divergence']} \ninitvel:{use['initvel']} \ncolor:{use['color']} \nforce:{use['force']} \nsize:{use['size']} \nsizedec:{use['sizedec']} \ndim:{use['dim']} \nalpha:{use['alpha']} \nalphadec:{use['alphadec']} \nntimes:{use['ntimes']} \nspeed:{use['speed']} \ncolordec:{use['colordec']} \ndivforce:{use['divergenceforce']} \ndivpos:{use['divergencepos']}"                      
				self.uitext("particlecommandtext",GameManager)
				if GameManager.em.key[pygame.K_RETURN]:
						text = um.elements["particlecommandtext"]["text"].rstrip()
						if text == "/x":
							self.mode = 0
						if "load:" in text:
							self.loadedparticle = text.replace("load:","").strip()
							self.parts = pm.bluprints[self.loadedparticle]
						if text == "new" :
							self.loadedparticle = None
							self.actuallyload = False
						if "=" in text:
							text = text.split("=")
							val = text[0].replace(" ","")
							newvalue = text[1].replace(" ","")
							if not val == "name":
								if val in use.keys():
									try:
										use[val] = eval(newvalue)
									except:
										use[val] = str(newvalue)
							else:
								self.loadedparticle = newvalue
						if not self.loadedparticle == None:
							if text == "save":
								pm.savebluprint(self.loadedparticle,use["type"],use["divergence"],
												use["color"],use["initvel"],use["force"],
												use["size"],use["sizedec"],dim = use["dim"],
												alpha = use["alpha"],alphadec=use["alphadec"],
												colordec=use["colordec"],quality=use["quality"],
												divergenceforce=use["divergenceforce"],
												divergencepos=use["divergencepos"],
												ntimes=use["ntimes"],
												speed=use["speed"])
								pm.loadallbluprints()
								self.parts = pm.bluprints[self.loadedparticle]
						
						um.elements["particlecommandtext"]["text"] = ""

					# um.elements["particlecommandtext"]["text"] = "error"



			elif self.mode == "ui-edit":
				movecam = 0
				um.state = "ui-edit"
				um.elements["loadedbluprint"]["text"] = "Loaded:" + self.loadedparticle
				um.elements["particledata"]["text"] = f"type:{use['type']} \ndivergence:{use['divergence']} \ncolor:{use['color']} \nforce:{use['force']} \nsize:{use['size']} \nsizedec:{use['sizedec']} \ndim:{use['dim']} \nalpha:{use['alpha']} \nalphadec:{use['alphadec']} \nntimes:{use['ntimes']} \nspeed:{use['speed']} \ncolordec:{use['colordec']} \ndivforce:{use['divergenceforce']} \ndivpos:{use['divergencepos']}"                      
				self.uitext("particlecommandtext",GameManager)
				if GameManager.em.key[pygame.K_RETURN]:
					text = um.elements["particlecommandtext"]["text"].rstrip()
					if text == "/x":
						self.mode = 0
						um.state = "def"
					if "load:" in text:
						self.loadedparticle = text.replace("load:","").strip()
						self.parts = pm.bluprints[self.loadedparticle]
					if text == "new" :
						self.loadedparticle = None
						self.actuallyload = False
					if "=" in text:
						text = text.split("=")
						val = text[0].replace(" ","")
						newvalue = text[1].replace(" ","")
						if not val == "name":
							if val in use.keys():
								use[val] = eval(newvalue)
						else:
							self.loadedparticle = newvalue
					if not self.loadedparticle == None:
						if text == "save":
							pm.savebluprint(self.loadedparticle,use["type"],use["divergence"],
											use["color"],use["initvel"],use["force"],
											use["size"],use["sizedec"],dim = use["dim"],
											alpha = use["alpha"],alphadec=use["alphadec"],
											colordec=use["colordec"],quality=use["quality"],
											divergenceforce=use["divergenceforce"],
											divergencepos=use["divergencepos"],
											ntimes=use["ntimes"],
											speed=use["speed"])
							pm.loadallbluprints()
							self.parts = pm.bluprints[self.loadedparticle]
					
					um.elements["particlecommandtext"]["text"] = ""



			elif "clear" in self.commmandtring.rstrip():
				univars.output = []
				self.commmandtring = ""
			elif "setbg:" in self.commmandtring.rstrip():
				bg.background = self.commmandtring.rstrip().replace("setbg:", "")
			elif "savebg" in self.commmandtring.rstrip():
				bg.savebg()
				self.comm = True
				self.mode = 0
			elif "state:" in self.commmandtring.rstrip():
				self.cht = self.commmandtring.rstrip().replace("state:", "")
				self.comm = True
				self.mode = 0
			elif "find:" in self.commmandtring.rstrip():
				self.cht = self.commmandtring.rstrip().replace("find:", "")
				self.dostring = object_manager.objfromid(self.cht)
				if not self.dostring == None:
					self.dostring2 = ""
					self.mode = "alterobj"
				self.commmandtring = ""
			elif "delete:" in self.commmandtring.rstrip():
				self.cht = self.commmandtring.rstrip().replace("delete:", "")
				self.dostring = object_manager.objfromid(self.cht)
				if not self.dostring == None:
					object_manager.removeid(self.cht)
				self.commmandtring = ""
			elif "layer:" in self.commmandtring.rstrip():
				self.cht = self.commmandtring.rstrip().replace("layer:", "")
				if not self.cht == "all":
					self.layer = int(self.cht)
				else:
					self.layer = self.cht
				self.commmandtring = ""
			elif ("debug:" in self.commmandtring.rstrip() or "db:" in self.commmandtring.rstrip()) and "=" in self.commmandtring.rstrip() : 
				self.cht = self.commmandtring.rstrip().split(":")[1]
				self.cht.replace(" ","")
				vartochange = self.cht.split("=")[0]
				valtoreplace = self.cht.split("=")[1]
				try:
					GameManager.publicvariables[vartochange] = eval(valtoreplace)
				except:
					GameManager.publicvariables[vartochange] = valtoreplace
				
				GameManager.print(f"{vartochange} = {valtoreplace}")
				# GameManager.print(self.cht)
				self.commmandtring = ""
			elif ("debug:" in self.commmandtring.rstrip() or "db:" in self.commmandtring.rstrip()) and not "=" in self.commmandtring.rstrip() : 
				self.cht = self.commmandtring.rstrip().split(":")[1]
				self.cht.replace(" ","")
				if self.cht in GameManager.publicvariables.keys():
					GameManager.print(f"{self.cht} = {GameManager.publicvariables[self.cht]}")
				else:
					GameManager.print(f"ERROR:\n    {self.cht} is not a publicvariable")
				self.showconsolebool = 1
				self.commmandtring = ""
			elif self.commmandtring.rstrip() in self.spritenames : 
				self.sprite = self.spritenames.index(self.commmandtring.rstrip())
				self.commmandtring = ""
			elif self.commmandtring.rstrip() in ["rel","reload"]:
				GameManager.initial()
				self.commmandtring = ""
			elif self.commmandtring.rstrip() == "bake":
				object_manager.BAKE()
				self.commmandtring = ""
			elif self.commmandtring.rstrip() == "baked":
				GameManager.print(object_manager.baked)
				self.showconsolebool = 1
				self.commmandtring = ""
			elif   "print:" in self.commmandtring.rstrip():
				self.cht = self.commmandtring.rstrip().split(":")[1]
				GameManager.print(self.cht)
				self.commmandtring = ""
			elif "println:" in self.commmandtring.rstrip():
				self.cht = self.commmandtring.rstrip().split(":")[1]
				line = self.commmandtring.rstrip().split(",")[1]
				GameManager.println(self.cht,line)
				self.commmandtring = ""

			elif self.commmandtring.rstrip() in ["particle","part","particle-edit","particle-editor"]:
				self.mode = "Particle-edit"
				um.addrect((pygame.display.get_desktop_sizes()[0][0]+ 500,200),["particle-edit"],[0,-1],"particle_edit_hud",color = univars.theme["dark"])
				um.addrect((500,2000),["particle-edit"],[-0.9,0],"particle_edit_side_bar",color = univars.theme["dark"])
				um.addtext("loadedbluprint","Loaded:None",univars.defont,[-0.97,0.8],univars.theme["semibright"],30,["particle-edit"],center=False)
				um.addtext("particledata","",univars.defont,[-0.97,0.75],univars.theme["semibright"],30,["particle-edit"],center=False)
				um.addtext("particlecommandtext","",univars.defont,[-0.98,-0.9],univars.theme["bright"],40,["particle-edit"],center = False)
			elif self.commmandtring.rstrip() in ["ui","ui-edit","ui-editor"]:
				self.mode = "Ui-edit"
				um.addrect((pygame.display.get_desktop_sizes()[0][0] + 500,200),"all",[0,-1],"ui_edit_hud",color = univars.theme["dark"])
				um.addrect((500,2000),["ui-edit"],[-0.9,0],"ui_edit_side_bar",color = univars.theme["dark"])
				um.addtext("uistatetext",f"state:{um.state}",univars.defont,[-0.97,0.8],univars.theme["semibright"],30,"all",center=False)
			






			elif self.mode == "Objinst":
				self.om.instables.append(self.om.objects[self.dostring.name]["name"])
				self.dostring = 0
				self.mode = 0



			else:
				if not self.commmandtring.rstrip() in ["Com","Obj"]:
					self.mode = 0


			self.placable -= 1 * GameManager.frame_manager.dt
			self.rotable -= 1 * GameManager.frame_manager.dt
			self.gridable -= 1 * GameManager.frame_manager.dt
			self.saveable -= 1 * GameManager.frame_manager.dt
			self.rectable -= 1 * GameManager.frame_manager.dt
			self.showdatable -= 1 * GameManager.frame_manager.dt
			if movecam:
				if GameManager.event_manager.key[pygame.K_q] or GameManager.event_manager.controller["L1"]:
					cam[1] += (camera.size)/speed * GameManager.frame_manager.dt 
				if GameManager.event_manager.key[pygame.K_e] or GameManager.event_manager.controller["R1"]:
					cam[1] -= (camera.size)/speed * GameManager.frame_manager.dt 
				cam[0][0] += speed * (1/camera.size) * GameManager.frame_manager.dt  * self.screen.get_width()/pygame.display.get_desktop_sizes()[0][0] * GameManager.key["x"]
				cam[0][1] -= speed * (1/camera.size) * GameManager.frame_manager.dt  * self.screen.get_width()/pygame.display.get_desktop_sizes()[0][0]* GameManager.key["y"]
			






			if self.showdata and self.mode == 0:
				# print(self.spritelooks)
				fulllist = self.spritelooks + self.spritelooks
				GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],200),(0,-1),univars.theme["dark"],200)
				self.tm.drawtext(f"Camera-name : {cm.currentcam}"                        ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],0.6,-0.9)
				self.tm.drawtext2(f"Camera size: { round(1 / camera.size,2)}"            ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],0,-0.9)
				self.tm.drawtext2(f"Camera pos: {[round(camera.x),-1 * round(camera.y)]}","pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.6,-0.9)
				GameManager.uibox((400,160),(-0.78,0.75),univars.theme["dark"],200)
				self.tm.drawtext2(f"State : {smate}",                                     "pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.97,0.85 - 0.05)
				self.tm.drawtext2(f"Map : {object_manager.loadedmap}",                    "pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.97,0.75 - 0.05)
					


				#the ui for object placement
				if debug:
					GameManager.uibox((360,420),(0.8,0.65 -0.087),        univars.theme["dark"],200)
					GameManager.uibox((64 + 10,64 + 10),(0.8,0.8 ),univars.theme["semibright"],400)
					GameManager.uibox((64 + 10,64 + 10),(0.92,0.8),univars.theme["semibright"],50)
					GameManager.uibox((64 + 10,64 + 10),(0.68,0.8),univars.theme["semibright"],50)
					GameManager.blituis(self.func.getsprites(self.spritelooks[self.sprite])[self.sn],(0.8,0.8),(64,64),self.rot,1000)
					GameManager.blituis(self.func.getsprites(fulllist[self.sprite + 1])[0],(0.92,0.8),(64,64),self.rot,100)
					GameManager.blituis(self.func.getsprites(self.spritelooks[self.sprite - 1])[0],(0.68,0.8),(64,64),self.rot,100)
					self.tm.drawtext(f"Object-name : {self.spritenames[self.sprite]}",       "pixel2.ttf",35,0,0,0,univars.theme["semibright"],0.8,0.6)
					self.tm.drawtext(f"Object-type : {self.typelist[self.sprite]}",          "pixel2.ttf",35,0,0,0,univars.theme["semibright"],0.8,0.52)
					self.tm.drawtext(f"layer:{self.layer}",          "pixel2.ttf",35,0,0,0,univars.theme["semibright"],0.8,0.44)
					self.tm.drawtext(f"Collision:{self.coll}",          "pixel2.ttf",35,0,0,0,univars.theme["semibright"],0.8,0.37)
					self.tm.drawtext(f"sn:{self.sn}",          "pixel2.ttf",35,0,0,0,univars.theme["semibright"],0.8,0.30)


				



				GameManager.frame_manager.showfps = 1
			else:
				object_manager.showmap = False
				GameManager.frame_manager.showfps = 0

			#show input
			if self.mode == 0 and not self.showdata:
				if GameManager.publicvariables["showinput"]:
					self.showinput(GameManager)









					
		elif GameManager.publicvariables["showinput"]:
			self.showinput(GameManager)


	def showconsole(self,GM):
		if self.showconsolebool:
			um.addrect([1000,pygame.display.get_desktop_sizes()[0][1]],"all",[-1,0],"#debugrect",color = univars.theme["dark"],alpha=200)
			um.addtext("#debugtext",GM.console(),univars.defont,[-1,self.consoletextscoll],univars.theme["semibright"],35,"all",center=False)
			um.elements["#debugtext"]["text"] = GM.console()
			um.elements["#debugtext"]["pos"][1] = self.consoletextscoll
		else:
			um.deleleelem("#debugrect")
			um.deleleelem("#debugtext")
			

	def showinput(self,GameManager):
		GameManager.uibox((190,190),(-0.8,-0.5),univars.theme["dark"],200)
		GameManager.uibox((50,50),[-0.8 + GameManager.key["x"]/18,-0.5 + GameManager.key["y"]/12],univars.theme["accent"],200)
		GameManager.uibox((pygame.display.get_desktop_sizes()[0][0],200),(0,-1),univars.theme["dark"],200)

		# GameManager.uibox((190,190),(-0.5,-0.5),univars.theme["dark"],200)


		if GameManager.key["jump"]:
			self.tm.drawtext(f"jump"                        ,"pixel2.ttf",40,0,0,0,univars.theme["accent"],-0.9,-0.9)
		else:
			self.tm.drawtext(f"jump"                        ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.9,-0.9)
		if GameManager.key["secondary"]:
			self.tm.drawtext(f"secondary"                        ,"pixel2.ttf",40,0,0,0,univars.theme["accent"],-0.7,-0.9)
		else:
			self.tm.drawtext(f"secondary"                        ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.7,-0.9)
		if GameManager.key["attack"]:
			self.tm.drawtext(f"attack"                        ,"pixel2.ttf",40,0,0,0,univars.theme["accent"],-0.5,-0.9)
		else:
			self.tm.drawtext(f"attack"                        ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.5,-0.9)
		if GameManager.key["throw"]:
			self.tm.drawtext(f"throw"                        ,"pixel2.ttf",40,0,0,0,univars.theme["accent"],-0.3,-0.9)
		else:
			self.tm.drawtext(f"throw"                        ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.3,-0.9)
		if GameManager.key["option"]:
			self.tm.drawtext(f"option"                        ,"pixel2.ttf",40,0,0,0,univars.theme["accent"],-0.1,-0.9)
		else:
			self.tm.drawtext(f"option"                        ,"pixel2.ttf",40,0,0,0,univars.theme["semibright"],-0.1,-0.9)
