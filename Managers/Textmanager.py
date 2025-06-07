#Textmanager
import pygame
class Textmanager:
    def __init__(self,screen):
        self.realscreen = screen

    def drawtext(self,text,font,size,bolder,italicer,aa,col,x,y):
        realfont = pygame.font.Font(f"Graphics/Fonts/{font}",size)
        img = realfont.render(text,aa,col)
        self.realscreen.blit(img,(x * self.realscreen.get_width()//2 - (img.get_width()/2) + self.realscreen.get_width()//2 ,-1 * y * self.realscreen.get_height()//2  - (img.get_height()/2)  + self.realscreen.get_height()//2 ))

    def drawtext2(self,text,font,size,bolder,italicer,aa,col,x,y):
        realfont = pygame.font.Font(f"Graphics/Fonts/{font}",size)
        img = realfont.render(text,aa,col)
        self.realscreen.blit(img,(x * self.realscreen.get_width()//2  + self.realscreen.get_width()//2,-1 * y * self.realscreen.get_height()//2  - (img.get_height()/2) + self.realscreen.get_height()//2 ))

    def textatmouse(self,text,font,size,aa,col,event_manager,x,y):
        realfont = pygame.font.Font(f"Graphics/Fonts/{font}",size)
        img = realfont.render(text,aa,col)
        self.realscreen.blit(img,(event_manager.mousepos[0] + x ,event_manager.mousepos[1] - y))

    def drawtext3(self,gm,text,font,size,bolder,italicer,aa,col,pos):
        realfont = pygame.font.Font(f"Graphics/Fonts/{font}",size)
        img = realfont.render(text,aa,col)
        gm.blitui2(img,pos)