import pygame
import univars



class Text(pygame.sprite.Sprite):
	# __slots__ = ["text","font","size","aa","col"]


	def __init__(self,text,font,size,aa,col,id):
		pygame.sprite.Sprite.__init__(self)
		self.text = text
		self.font = f"Graphics/Fonts/{font}"
		self.size = size
		self.aa = aa
		self.col = col
		self.realfont = pygame.font.Font(f"Graphics/Fonts/{font}",size)
		self.saved = self.realfont.render(text,aa,col)
		self.image = self.realfont.render(text,aa,col)
		pos = (0,0)
		self.rect = self.image.get_rect(center = (pos[0]  * univars.realscreeen.get_width()//2 - (self.image.get_width()/2)  + univars.realscreeen.get_width()//2  ,-1 * pos[1]  * univars.realscreeen.get_width()//2 - (self.image.get_height()/2)  + univars.realscreeen.get_height()//2 ) )
		self.id = id
		
	
	def update(self,show):
		if show[self.id][0]:
			pos = show[self.id][1]
			self.image = self.saved
			realpos = pos
			self.rect = self.image.get_rect(topleft = realpos )
		else:
			self.image = pygame.Surface((0,0))
		


class Textmanager:
	def __init__(self,screen):
		self.realscreen = screen
		self.fonts = {}
		self.srg = pygame.sprite.Group()

	def drawtext(self,text,font,size,bolder,italicer,aa,col,x,y):
		img = self.img(text,font,size,aa,col)
		self.fonts[img[0]][1] = (x * self.realscreen.get_width()//2 - (img[1].image.get_width()/2) + self.realscreen.get_width()//2 ,-1 * y * self.realscreen.get_height()//2  - (img[1].image.get_height()/2)  + self.realscreen.get_height()//2 )
		self.fonts[img[0]][0] = 1

	def drawtext2(self,text,font,size,bolder,italicer,aa,col,x,y):
		img = self.img(text,font,size,aa,col)
		self.fonts[img[0]][1] = (x * self.realscreen.get_width()//2  + self.realscreen.get_width()//2,-1 * y * self.realscreen.get_height()//2  - (img[1].image.get_height()/2) + self.realscreen.get_height()//2 )
		self.fonts[img[0]][0] = 1

	def textatmouse(self,text,font,size,aa,col,event_manager,x,y):
		img = self.img(text,font,size,aa,col)
		self.fonts[img[0]][1] = (event_manager.mousepos[0] + x ,event_manager.mousepos[1] - y)
		self.fonts[img[0]][0] = 1

	def drawtext3(self,gm,text,font,size,bolder,italicer,aa,col,pos):
		img = self.img(text,font,size,aa,col)
		self.fonts[img[0]][1] = gm.blitui2pos(self,img[0],pos)
		self.fonts[img[0]][0] = 1

	def update(self):
		self.srg.draw(univars.realscreeen)
		self.srg.update(self.fonts)
		for i in self.fonts.keys():
			self.fonts[i][0] = 0
			

	def img(self,text,font,size,aa,col):
		if not (f"Graphics/Fonts/{font}",size,aa,col,text) in self.fonts.keys():
			self.fonts[(f"Graphics/Fonts/{font}",size,aa,col,text)] = [0,(0,0)]
			stext = Text(text,font,size,aa,col,(f"Graphics/Fonts/{font}",size,aa,col,text))
			self.srg.add(stext)
		else:
			stext = [i for i in self.srg if i.id == (f"Graphics/Fonts/{font}",size,aa,col,text)][0]
		return [ (f"Graphics/Fonts/{font}",size,aa,col,text) ,stext]
	


tm = Textmanager(univars.realscreeen)