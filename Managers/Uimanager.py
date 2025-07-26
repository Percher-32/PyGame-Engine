import pygame
import event_manager
import Textmanager
import Uielement
import univars
tm = Textmanager.Textmanager(univars.realscreeen)
em = event_manager.event_manager()


class Uimanager:
	def __init__(self):
		self.elements = {}
		self.addedcounter = 0
		self.sprites = pygame.sprite.Group()
		self.state = "default"

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
		self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"click":0,"hover":0,"command":[],"pos":pos,"states":states,"surf":surf,"type":"button"}
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


	def showvar(self,name,var,posl):
		if str(name) + "but" in self.elements.keys():
			self.elements[str(name) + "tex"]["text"] = str(name) + ":" + str(var)
		else:
			self.addbutton(univars.sizes["mediumbutton"],["all"],posl,str(name) + "but",univars.theme["dark"],alpha = 200)
			self.addtext(str(name) + "tex",str(name) + ":" + str(var),univars.defont,posl,univars.theme["accent"],25,["all"])
			self.bindtobutton(str(name) + "tex",str(name) + "but")



	def bindtobutton(self,text,button):
		self.elements[text]["button"] = button
		self.elements[button]["text"] = text


	def lerpval(self,elem,val,max,sm):
		self.elements[elem][val] =   univars.func.lerp(self.elements[elem][val],max,sm)
 
	

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



	def update(self,em):
		self.sprites.update(self.state, self.elements,em)
		self.sprites.draw(univars.realscreeen)
		for a in self.sprites:
			if a.name in self.elements.keys():
				if a.__class__.__name__ == "Uibutton":
					self.elements[a.name]["click"] = a.click
					self.elements[a.name]["hover"] = a.hover
					if "glide" in self.elements[a.name]["command"]:
						if self.elements[a.name]["hover"]:
							self.elements[a.name]["dimensions"] = univars.func.lerp(self.elements[a.name]["dimensions"],self.elements[a.name]["glidehov"],4)
						else:
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
	