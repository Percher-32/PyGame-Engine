import pygame
import Managers.event_manager as event_manager
import Managers.Textmanager as Textmanager
import Managers.Uielement as Uielement
import Managers.univars as univars
tm = Textmanager.Textmanager(univars.realscreeen)
em = event_manager.event_manager()


class Uimanager:
	def __init__(self):
		self.elements = {}
		self.addedcounter = 0
		self.sprites = pygame.sprite.Group()
		self.state = "default"
		self.selectedbutton = None
		self.selectedbuttonclass = None
		self.canshowvar = True
		self.realscreeen = pygame.Surface((univars.screen_w,univars.screen_h))
		self.reset = pygame.Surface((univars.screen_w,univars.screen_h))
		self.realscreeen = self.reset
		self.mode = "arrow"
		self.toroute = None

	def addelement(self,surf,states,pos,name,type=None):
		ui = self.Uielement.Ui(surf,states,pos,name)
		self.elements[name] = {"name":name,"pos":pos,"type":type}
		self.sprites.add(ui)
		
	def addrect(self,dimensions,states,pos,name,color=(0,0,0),alpha=255,surf = None,sn = None):
		if not surf == None:
			if not sn == None:
				surf = univars.func.getsprites(surf)[sn]
			else:
				surf = pygame.image.load(f"Graphics/ui/{surf}").convert_alpha()
		ui = Uielement.Uirect(dimensions,states,pos,name,surf = surf)
		self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"pos":pos,"states":states,"surf":surf,"type":"rect"}
		self.sprites.add(ui)

	def addbutton(self,dimensions,states,pos,name,color=(0,0,0),alpha=255,surf = None,sn = None):
		if not surf == None:
			if not sn == None:
				surf = univars.func.getsprites(surf)[sn]
			else:
				surf = pygame.image.load(f"Graphics/ui/{surf}").convert_alpha()
		ui = Uielement.Uibutton(dimensions,states,pos,name,surf = surf)
		self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"click":0,"hover":0,"command":[],"pos":pos,"states":states,"surf":surf,"type":"button","dir":{"up":None,"down":None,"left":None,"right":None}}
		self.sprites.add(ui)

	def addtext(self,name, text, font, pos, col, size,states):
		ui = Uielement.Uitext(name,text,font,pos,col,size,states)
		self.elements[name] = {"name":name,"text":text,"color":col,"size":size,"command":[],"pos":pos,"states":states,"type":"text"}
		self.sprites.add(ui)

	
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


	def bindtobutton(self,text,button):
		self.elements[text]["button"] = button
		self.elements[button]["text"] = text


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
				if val["pos"[0]] > leftval or leftval == None:
					left = i
					leftval = val["pos"][0]

			# print(val["pos"][0])
			# print(self.elements[button]["pos"][0])
			if val["pos"][0] > self.elements[button]["pos"][0]:
				if val["pos"[0]] < rightval or rightval == None:
					right = i
					rightval = val["pos"][0]

					
			if val["pos"][1] < self.elements[button]["pos"][0]:
				if val["pos"[0]] > upval or upval == None:
					up = i
					upval = val["pos"][0]

					
			if val["pos"][1] > self.elements[button]["pos"][0]:
				if val["pos"[0]] > downval or downval == None:
					down = i
					downval = val["pos"][0]



		print({"up":up,"down":down,"left":left,"right":right})
		
		self.elements[button]["dir"] = {"up":up,"down":down,"left":left,"right":right}
		self.elements[button]["routed"] = True


	def addglide(self,button,glidenorm,glidehov):
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

	# def autoroute(self):
	# 	"""
	# 		routes all buttons
	# 	"""

	# 	buttonsinstate = [ i for i in self.elements.keys() if self.elements[i]["state"] == self.state and self.elements[i]["type"] == "button"]

	# 	for i in buttonsinstate:
	# 		self.route(i)

	def clicked(self,button):
		"""
			returns wether a button has been clicked
		"""
		return self.selectedbutton == button and self.elements[button]["click"]
			
	def hover(self,button):
		"""
			returns wether a button has been hovered over
		"""
		return  self.selectedbutton == button

	def changestate(self,state,startbutton):
		self.state = state
		self.selectedbutton = startbutton
		if startbutton in self.elements:
			self.route(startbutton)
		else:
			self.toroute = startbutton

	def update(self,em,pubvar,axis):
		self.canshowvar = pubvar["debug-mode"]
		self.sprites.update(self.state, self.elements,em)

		if not self.toroute == None:
			self.route(self.toroute)
			self.toroute = None

		if self.mode == "arrow":
			if self.selectedbutton in self.elements.keys():
				old = self.selectedbutton
				if axis[0] < 0:
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["left"]
				elif axis[0] > 0:
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["right"]
				elif axis[1] < 0:
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["up"]
				elif axis[1] > 0:
					self.elements[self.selectedbutton]["hover"] = False
					self.selectedbutton = self.elements[self.selectedbutton]["dir"]["down"]
				if not self.selectedbutton in self.elements.keys():
					self.selectedbutton = old
				self.route(self.selectedbutton)



		for a in self.sprites:
			if a.name in self.elements.keys():
				if a.__class__.__name__ == "Uibutton":
					self.elements[a.name]["click"] = a.click
					self.elements[a.name]["hover"] = a.hover

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
							if self.elements[self.elements[a.name]["button"]]["hover"]:
								self.elements[a.name]["size"] = univars.func.lerp(self.elements[a.name]["size"],self.elements[a.name]["glidehov"],4)
							else:
								self.elements[a.name]["size"] = univars.func.lerp(self.elements[a.name]["size"],self.elements[a.name]["glidenorm"],4)
						self.elements[a.name]["pos"] = self.elements[self.elements[a.name]["button"]]["pos"]
						self.elements[a.name]["states"] = self.elements[self.elements[a.name]["button"]]["states"]

		
			

ingame = Uimanager()
	