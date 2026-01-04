import pygame
import data.Managers.event_manager as event_manager
import data.Managers.Textmanager as Textmanager
import data.Managers.Uielement as Uielement
import data.Managers.univars as univars
import json
tm = Textmanager.Textmanager(univars.realscreeen)
em = event_manager.event_manager()


class Uimanager:
	def __init__(self):
		self.metadata = {"element":[],"rect":[],"button":[],"text":[]}
		"""
			stores the data inputed into addfunctions
		"""
		self.elements = {}
		self.binds = []
		self.enterpress = 0
		self.enterpressnull = 0
		self.enterheld = 0
		self.lastaxis = [0,0]
		self.glidens = []
		self.addedcounter = 0
		self.sprites = pygame.sprite.LayeredUpdates()
		self.state = "default"
		self.manroutes = {}
		self.selectedbutton = None
		self.selectedbuttonclass = None
		self.canshowvar = True
		self.realscreeen = pygame.Surface((univars.screen_w,univars.screen_h))
		self.reset = pygame.Surface((univars.screen_w,univars.screen_h))
		self.realscreeen = self.reset
		self.mode = "arrow"
		self.toroute = None
		self.timetillnextswap = 1

	def addelement(self,surf,states,pos,name,type=None,layer = 0):
		self.metadata["element"].append([surf,states,pos,name,type])
		ui = self.Uielement.Ui(surf,states,pos,name)
		self.elements[name] = {"name":name,"pos":pos,"type":type,"cache":{}}
		self.sprites.add(ui,layer = layer)
		
	def addrect(self,dimensions,states,pos,name,color=(0,0,0),alpha=255,surf = None,sn = 0,usesprite = False,fromstart = False,layer = 0):
		key = [dimensions,states,pos,name,color,alpha,surf,sn,usesprite]
		if key in self.metadata["rect"]:
			self.metadata["rect"].remove(key)
		self.metadata["rect"].append(key)
		if not name in self.elements.keys():
			if not surf == None:
				if not usesprite:
					surf = pygame.image.load(f"data/Graphics/ui/{surf}.png").convert_alpha()
				else:
					surf = univars.func.getsprites(surf)[sn]
			ui = Uielement.Uirect(dimensions,states,pos,name,surf = surf,fromstart = fromstart)
			self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"pos":pos,"states":states,"surf":surf,"type":"rect","cache":{},"command":[]}
			self.sprites.add(ui,layer = layer)

	def addbutton(self,dimensions,states,pos,name,color=(0,0,0),alpha=255,surf = None,sn = 0,usesprite = False,layer = 0):
		key = [dimensions,states,pos,name,color,alpha,surf,sn,usesprite]
		if key in self.metadata["button"]:
			self.metadata["button"].remove(key)
		self.metadata["button"].append(key)
		if not name in self.elements.keys():
			if not surf == None:
				if not usesprite:
					surf = pygame.image.load(f"data/Graphics/ui/{surf}.png").convert_alpha()
				else:
					surf = univars.func.getsprites(surf)[sn]
			ui = Uielement.Uibutton(dimensions,states,pos,name,surf = surf)
			self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"click":0,"hover":0,"command":[],"pos":pos,"states":states,"surf":surf,"type":"button","dir":{"up":None,"down":None,"left":None,"right":None},"cache":{}}
			self.sprites.add(ui,layer = layer)

	def addtext(self,name, text, font, pos, col, size,states,center = True,layer = 0):
		key = [name,text,font,pos,col,size,states,center]
		if key in self.metadata["text"]:
			self.metadata["text"].remove(key)
		self.metadata["text"].append(key)
		if not name in self.elements.keys():
			ui = Uielement.Uitext(name,text,font,pos,col,size,states,center=center)
			self.elements[name] = {"name":name,"text":text,"color":col,"size":size,"command":[],"pos":pos,"states":states,"type":"text"}
			self.sprites.add(ui,layer = layer)

	
	def deleleelem(self,name):
		"""name -> str or list"""
		if type(name) == str:
			if name in self.elements.keys():
				if "text" in self.elements[name] and not self.elements[name]["type"] == "text":
					self.elements.pop(self.elements[name]["text"])
				if "button" in self.elements[name]:
					self.elements.pop(self.elements[name]["button"])
					self.elements.pop()
				self.elements.pop(name)

		else:
			for i in name:
				if i in self.elements.keys():
					if "text" in self.elements[i] and not self.elements[i]["type"] == "text":
						self.elements.pop(self.elements[i]["text"])
					if "button" in self.elements[i]:
						self.elements.pop(self.elements[i]["button"])
						self.elements.pop()
					self.elements.pop(i)


	def showvar(self,name,var,posl,textsize = 25,dimensions = univars.sizes["mediumbutton"]): 
		if self.canshowvar:
			if str(name) + "but" in self.elements.keys():
				self.elements[str(name) + "tex"]["text"] = str(name) + ":" + str(var)
			else:
				self.addbutton(dimensions,["all"],posl,str(name) + "but",univars.theme["dark"],alpha = 200)
				self.addtext(str(name) + "tex",str(name) + ":" + str(var),univars.defont,posl,univars.theme["accent"],textsize,["all"])
				self.bindtobutton(str(name) + "tex",str(name) + "but")
		else:
			self.unshowvar(name)

	def unshowvar(self,name):
		self.deleleelem(str(name) + "but")
		self.deleleelem(str(name) + "tex")


	def bindtobutton(self,text,button,offset = [0,0]):
		self.elements[text]["button"] = button
		self.elements[button]["text"] = text
		self.elements[text]["offset"] = offset
		self.binds.append([text,button])

	def bindtorect(self,rect,button,offset = [0,0],size = None,glidesize=None):
		self.binds.append([rect,button])
		self.elements[rect]["button"] = button
		self.elements[button]["rect"] = rect
		self.elements[rect]["offset"] = offset

  
		if size == None:
			size = self.elements[rect]["dimensions"]
		if glidesize == None:
			glidesize = size
  
		self.elements[rect]["normsize"] = size
		self.elements[rect]["glidesize"] = glidesize

	def lerpval(self,elem,val,max,sm):
		self.elements[elem][val] =   univars.func.lerp(self.elements[elem][val],max,sm,roundto=4)
 
	def route(self,button):
		"""
			button = name of button.
			creates its dirctions to new buttons
		"""
		left = None
		left = left
		right = None
		right = right
		up = None
		up = up
		down = None
		down = down

		leftval = None
		rightval = None
		upval = None
		downval = None


		buttonsinstate = [ i for i in self.elements.keys() if  self.state in self.elements[i]["states"] and self.elements[i]["type"] == "button"]

		for i in buttonsinstate:
			val = self.elements[i]
			if val["pos"][0] < self.elements[button]["pos"][0]:
				if leftval == None:
					left = i
					leftval = val["pos"][0]
				elif val["pos"][0] > leftval:
					left = i
					leftval = val["pos"][0]

			# print(val["pos"][0])
			# print(self.elements[button]["pos"][0])
			if val["pos"][0] > self.elements[button]["pos"][0]:
				if rightval == None:
					right = i
					rightval = val["pos"][0]
				elif val["pos"][0] < rightval :
					right = i
					rightval = val["pos"][0]

					
			if val["pos"][1] < self.elements[button]["pos"][1]:
				if upval == None:
					up = i
					upval = val["pos"][1]
				elif val["pos"][1] > upval:
					up = i
					upval = val["pos"][1]

					
			if val["pos"][1] > self.elements[button]["pos"][1]:
				if downval == None:
					down = i
					downval = val["pos"][1]
				elif val["pos"][1] < downval:
					down = i
					downval = val["pos"][1]



		
		self.elements[button]["dir"] = {"up":up,"down":down,"left":left,"right":right}
		if button in self.manroutes.keys():
			for direction in self.manroutes[button].keys():
				self.elements[button][direction] = self.manroutes[button][direction]
		self.elements[button]["routed"] = True

	def setroute(self,button,dir,buttonname):
		"""
			ovveriders an direction for the buttons route
		
		:param button: button-id
		:param dir: ["up","down","left","right"]
		:param buttonname: destination button id
		"""
		if dir == "down":
			dir = "up"
		elif dir == "up":
			dir = "down"
		# elif dir == "left":
		# 	dir = "right"
		# elif dir == "right":
		# 	dir = "left"
		self.elements[button]["dir"][dir] = buttonname
  
		
   
		if not button in self.manroutes.keys():
			self.manroutes[button] = {}
   
		self.manroutes[button][dir] = buttonname

	def addglide(self,button,glidenorm,glidehov):
		"""
			Makes a buttton chane size when hovered over
		
		:param button: buttton-id
		:param glidenorm: normal size
		:param glidehov: hover size
		"""
		if [button,glidenorm,glidehov] in self.glidens:
			self.glidens.remove([button,glidenorm,glidehov])
		self.glidens.append([button,glidenorm,glidehov])
		if button in self.elements.keys():
			self.elements[button]["command"].append("glide")
			self.elements[button]["glidenorm"] = glidenorm
			self.elements[button]["glidehov"] = glidehov
			if "text" in self.elements[button].keys():
				text = self.elements[self.elements[button]["text"]]
				ratio = glidehov[0] / glidenorm[0]
				base = text["size"]
				rbase = text["size"] * ratio
				text["command"].append("glide")
				text["glidenorm"] = base
				text["glidehov"] = rbase
    
			if "rect" in self.elements[button].keys():
				self.elements[self.elements[button]["rect"]]["command"].append("glide")



	def clicked(self,em,button):
		"""
			returns wether a button has been clicked
		"""
		if self.mode == "arrow":
			return (self.selectedbutton == button) and ( em.controllerjab["A"] or em.controllerjab["SELECT"] or self.enterpress  ) and self.state in self.elements[button]["states"]
		else:
			return (self.elements[button]["click"] and self.state in self.elements[button]["states"])
			
	def hover(self,button):
		"""
			returns wether a button has been hovered over
		"""
		if self.mode == "arrow":
			return  self.selectedbutton == button
		else:
			return self.elements[button]["hover"]

	def conthover(self,button):
		return (self.selectedbutton == button) and (self.mode == "arrow")

	def changestate(self,state,startbutton):
		self.state = state
		self.mode = "arrow"
		self.selectedbutton = startbutton
		if startbutton in self.elements:
			self.route(startbutton)
		else:
			self.toroute = startbutton

	def update(self,em,pubvar,axis,dt):
		self.canshowvar = pubvar["debug-mode"]
		self.sprites.update(self.state, self.elements,em)
  
		# if em.key[pygame.K_RETURN] and not self.enterpress == 1:
		self.enterpressnull = em.key[pygame.K_RETURN]
  
		if self.enterpressnull:
			if self.enterheld  == 0:
				self.enterpress = 1
				self.enterheld = 1
			else:
				self.enterpress = 0
		else:
			self.enterheld = 0
			self.enterpress = 0

  




		if not self.toroute == None:
			self.route(self.toroute)
			self.toroute = None

		# if self.timetillnextswap <= 0:
			# self.timetillnextswap = 0
		if not self.lastaxis == axis:
			if self.selectedbutton in self.elements.keys():
				self.timetillnextswap = 5
				old = self.selectedbutton
				if axis[0] < 0:
					self.mode = "arrow"
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["left"]
				elif axis[0] > 0:
					self.mode = "arrow"
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["right"]
				elif axis[1] < 0:
					self.mode = "arrow"
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["up"]
				elif axis[1] > 0:
					self.mode = "arrow"
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["down"]
				if not self.selectedbutton in self.elements.keys():
					self.selectedbutton = old


				self.route(self.selectedbutton)


		self.lastaxis = [axis[0],axis[1]]
		self.timetillnextswap -= dt



		for a in self.sprites:
			if a.name in self.elements.keys():
				if a.__class__.__name__ == "Uibutton":
					self.elements[a.name]["click"] = a.click
					self.elements[a.name]["hover"] = a.hover

					if a.click or a.hover:
						self.mode = "mouse"



					if self.mode == "mouse":
						if self.elements[a.name]["hover"]:
							self.selectedbutton = a.name
							if "glide" in self.elements[a.name]["command"]:
								self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["glidehov"],4)
						else:
							if "glide" in self.elements[a.name]["command"]:
								self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["glidenorm"],4)

					if self.mode == "arrow":
						if self.selectedbutton == a.name:
							if "glide" in self.elements[a.name]["command"]:
								self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["glidehov"],4)
						else:
							if "glide" in self.elements[a.name]["command"]:
								self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["glidenorm"],4)

				if a.__class__.__name__ == "Uitext":
					if "button" in self.elements[a.name].keys():
						if "glide" in self.elements[a.name]["command"]:
							if self.mode == "arrow":
								if self.selectedbutton == self.elements[a.name]["button"]:
									self.elements[a.name]["size"] = univars.func.lerp(self.elements[a.name]["size"],self.elements[a.name]["glidehov"],4)
								else:
									self.elements[a.name]["size"] = univars.func.lerp(self.elements[a.name]["size"],self.elements[a.name]["glidenorm"],4)
							else:
								if self.elements[self.elements[a.name]["button"]]["hover"]:
									self.elements[a.name]["size"] = univars.func.lerp(self.elements[a.name]["size"],self.elements[a.name]["glidehov"],4)
								else:
									self.elements[a.name]["size"] = univars.func.lerp(self.elements[a.name]["size"],self.elements[a.name]["glidenorm"],4)
						self.elements[a.name]["pos"][0] = self.elements[self.elements[a.name]["button"]]["pos"][0] + self.elements[a.name]["offset"][0] 
						self.elements[a.name]["pos"][1] = self.elements[self.elements[a.name]["button"]]["pos"][1] + self.elements[a.name]["offset"][1] 
						self.elements[a.name]["states"] = self.elements[self.elements[a.name]["button"]]["states"]
						self.elements[a.name]["alpha"] = self.elements[self.elements[a.name]["button"]]["alpha"]	

				if a.__class__.__name__ == "Uirect":
					if "button" in self.elements[a.name].keys():
						if "glide" in self.elements[a.name]["command"]:
							if self.mode == "arrow":
								if self.selectedbutton == self.elements[a.name]["button"]:
									self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["glidesize"],4)
								else:
									self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["normsize"],4)
							else:
								if self.elements[self.elements[a.name]["button"]]["hover"]:
									self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["glidesize"],4)
								else:
									self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["normsize"],4)
						self.elements[a.name]["pos"][0] = self.elements[self.elements[a.name]["button"]]["pos"][0] + self.elements[a.name]["offset"][0] 
						self.elements[a.name]["pos"][1] = self.elements[self.elements[a.name]["button"]]["pos"][1] + self.elements[a.name]["offset"][1] 
						self.elements[a.name]["states"] = self.elements[self.elements[a.name]["button"]]["states"]

			

ingame = Uimanager()
	