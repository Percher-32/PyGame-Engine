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
		self.elements[name] = {"name":name}
		self.sprites.add(ui)
		
	def addrect(self,dimensions,states,pos,name,color=(0,0,0),alpha=255):
		ui = Uielement.Uirect(dimensions,states,pos,name)
		self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha}
		self.sprites.add(ui)

	def addbutton(self,dimensions,states,pos,name,color=(0,0,0),alpha=255):
		ui = Uielement.Uibutton(dimensions,states,pos,name)
		self.elements[name] = {"name":name,"dimensions":dimensions,"color":color,"alpha":alpha,"click":0,"hover":0,"command":[]}
		self.sprites.add(ui)

	def addglide(self,button,glidenorm,glidehov):
		if button in self.elements.keys():
			self.elements[button]["command"].append("glide")
			self.elements["glidenorm"] = glidenorm
			self.elements["glidehov"] = glidehov

	def update(self,em):
		self.sprites.update(self.state, self.elements,em)
		self.sprites.draw(univars.realscreeen)
		for a in self.sprites:
			if a.__class__.__name__ == "Uibutton":
				self.elements[a.name]["click"] = a.click
				self.elements[a.name]["hover"] = a.hover
				if "glide" in self.elements[a.name]["command"]:
					if self.elements["testbutton" ]["hover"]:
						self.elements["testbutton"]["dimensions"] = univars.func.lerp(self.elements["testbutton"]["dimensions"],self.elements["glidehov"],4)
					else:
						self.elements["testbutton"]["dimensions"] = univars.func.lerp(self.elements["testbutton"]["dimensions"],self.elements["glidenorm"],4)

			

ingame = Uimanager()
	