import pygame
import Managers.univars as univars

class Textmanager:
    def __init__(self,screen):
        # univars.realscreeen = univars.realscreeen 
        self.fonts = {}

    def drawtext(self,text,font,size,bolder,italicer,aa,col,x,y):
        img = self.img(text,font,size,aa,col)
        univars.realscreeen.blit(img,(x * univars.realscreeen.get_width()//2 - (img.get_width()/2) + univars.realscreeen.get_width()//2 ,-1 * y * univars.realscreeen.get_height()//2  - (img.get_height()/2)  + univars.realscreeen.get_height()//2 ))

    def drawtext2(self,text,font,size,bolder,italicer,aa,col,x,y):
        img = self.img(text,font,size,aa,col)
        univars.realscreeen.blit(img,(x * univars.realscreeen.get_width()//2  + univars.realscreeen.get_width()//2,-1 * y * univars.realscreeen.get_height()//2  - (img.get_height()/2) + univars.realscreeen.get_height()//2 ))

    def textatmouse(self,text,font,size,aa,col,event_manager,x,y):
        img = self.img(text,font,size,aa,col)
        univars.realscreeen.blit(img,(event_manager.mousepos[0] + x ,event_manager.mousepos[1] - y))

    def drawtext3(self,gm,text,font,size,bolder,italicer,aa,col,pos):
        img = self.img(text,font,size,aa,col)
        gm.blitui2(img,pos)

    def img(self,text,font,size,aa,col):
        if not (f"Graphics/Fonts/{font}",size,aa,col,text) in self.fonts.keys():
            realfont = pygame.font.Font(f"Graphics/Fonts/{font}",size)
            img = realfont.render(text,aa,col)
            self.fonts[(f"Graphics/Fonts/{font}",size,aa,col,text)] = img
        else:
            img = self.fonts[(f"Graphics/Fonts/{font}",size,aa,col,text)]
        return img