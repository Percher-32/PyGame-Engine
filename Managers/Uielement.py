import pygame
import event_manager
import Textmanager
import univars
tm = Textmanager.Textmanager(univars.realscreeen)
em = event_manager.event_manager()

class Button(pygame.sprite.Sprite):
    def __init__(self,surf,dim,col,alpha,states,rot,pos,endim,name):
        pygame.sprite.Sprite.__init__(self)
        self.dim = dim
        self.name = name
        self.endim = endim
        self.click = False
        self.hover = False
        self.states = states
        self.rot = rot
        self.surf = surf
        self.alpha = alpha
        self.col = col
        if surf == None:
            self.image = pygame.Surface(dim)
            self.image.fill(col)
            self.image.set_alpha(alpha)
            self.image = pygame.transform.rotate(self.image,self.rot)
        else:
            self.image = pygame.image.load(surf).convert_alpha()
            self.image.set_alpha(alpha)
            self.image = pygame.transform.scale(self.image,self.endim)
            self.image = pygame.transform.rotate(self.image,self.rot)
        self.realrect = self.image.get_rect(center = pos)
        self.realpos = pos
        pos =   (  self.image.get_width() + self.realpos[0] , self.image.get_height() + self.realpos[1]        )
        self.rect = self.image.get_rect(center = pos)

    def update(self,state,name):
        if state in self.states:
            pos =   (  univars.realscreeen.get_width()//2 -  self.image.get_width()//2 + self.realpos[0] , univars.realscreeen.get_height()//2 - self.image.get_height()//2 + self.realpos[1]        )
            if not self.dim == None:
                self.image = pygame.Surface(self.dim)
                self.image.fill(self.col)
                self.image.set_alpha(self.alpha)
                self.image = pygame.transform.rotate(self.image,self.rot)
            else:
                self.image = pygame.image.load(self.surf).convert_alpha()
                self.image.set_alpha(self.alpha)
                self.image = pygame.transform.scale(self.image,self.dim)
                self.image = pygame.transform.rotate(self.image,self.rot)
            self.rect = self.image.get_rect(center = pos)
            if self.rect.collidepoint(pygame.mouse.get_pos()) or name == self.name:
                self.hover = True
                self.image = pygame.transform.scale(self.image,self.endim)
                if em.x or em.mouse:
                    self.click = True
                else:
                    self.click = False
        else:
            self.image = pygame.Surface((0,0))
            self.hover = False
            self.click = False
        
class Ui(pygame.sprite.Sprite):
    def __init__(self,surf,dim,col,alpha,states,rot,pos,name):
        pygame.sprite.Sprite.__init__(self)
        self.dim = dim
        self.name = name
        self.states = states
        self.rot = rot
        self.surf = surf
        self.alpha = alpha
        self.col = col
        if not col == None:
            self.image = pygame.Surface(dim)
            self.image.fill(col)
            self.image.set_alpha = alpha
        else:
            self.image = pygame.image.load(surf).convert_alpha()
            self.image.set_alpha = alpha
            self.image = pygame.transform.scale_by(self.surf,dim)
        self.rect = self.image.get_rect(center = pos)

    def update(self,state,name):
        if state in self.states:
            if not self.dim == None:
                    self.image = pygame.Surface(self.dim)
                    self.image.fill(self.col)
            else:
                self.image = pygame.image.load(self.surf).convert_alpha()
                self.image.set_alpha = self.alpha
                self.image = pygame.transform.scale(self.image,self.dim)
                self.image = pygame.transform.rotate(self.image,self.rot)
        else:
            self.image = pygame.Surface((0,0))
        

class Text(pygame.sprite.Sprite):
    def __init__(self,name,text,font,pos,col,size,states):
        self.name = name
        self.text = text
        self.font = font
        self.pos = pos
        self.col = col
        self.size = size
        self.states = states

    def update(self,state):
        if state in self.states:
            tm.drawtext2(self.text,self.font,self.size,0,0,0,self.col,self.pos[0],self.pos[1])


        