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
		self.sprites = pygame.sprite.Group()
		self.state = "default"

	def addelement(self,surf,states,pos,name):
		ui = self.Uielement.Ui(surf,states,pos,name)
		self.elements[name] = {"name":name,"pos":pos}
		self.sprites.add(ui)
		
	def addrect(self,dimensions,states,pos,name,color=(0,0,0),alpha=255):
		ui = Uielement.Uirect(dimensions,states,pos,name)
		self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"pos":pos}
		self.sprites.add(ui)

	def addbutton(self,dimensions,states,pos,name,color=(0,0,0),alpha=255):
		ui = Uielement.Uibutton(dimensions,states,pos,name)
		self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"click":0,"hover":0,"command":[],"pos":pos}
		self.sprites.add(ui)

	def addtext(self,name, text, font, pos, col, size,states):
		ui = Uielement.Uitext(name,text,font,pos,col,size,states)
		self.elements[name] = {"name":name,"text":text,"color":col,"size":size,"command":[],"pos":pos}
		self.sprites.add(ui)


	def bindtobutton(self,text,button):
		self.elements[text]["button"] = button
		self.elements[button]["text"] = text

	def addglide(self,button,glidenorm,glidehov):
		if button in self.elements.keys():
			self.elements[button]["command"].append("glide")
			self.elements[button]["glidenorm"] = glidenorm
			self.elements[button]["glidehov"] = glidehov
			if "text" in self.elements[button].keys():
				print("yapy")
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


			

ingame = Uimanager()
	