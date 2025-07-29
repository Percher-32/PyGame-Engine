import pygame
import Managers.event_manager as event_manager
import Managers.Textmanager as Textmanager
import Managers.univars as univars
tm = Textmanager.Textmanager(univars.realscreeen)

# class Button(pygame.sprite.Sprite):
#     def __init__(self,surf,dim,col,alpha,states,rot,pos,endim,name):
#         pygame.sprite.Sprite.__init__(self)
#         self.dim = dim
#         self.name = name
#         self.endim = endim
#         self.click = False
#         self.hover = False
#         self.states = states
#         self.rot = rot
#         self.surf = surf
#         self.alpha = alpha
#         self.col = col
#         if surf == None:
#             self.image = pygame.Surface(dim)
#             self.image.fill(col)
#             self.image.set_alpha(alpha)
#             self.image = pygame.transform.rotate(self.image,self.rot)
#         else:
#             self.image = pygame.image.load(surf).convert_alpha()
#             self.image.set_alpha(alpha)
#             self.image = pygame.transform.scale(self.image,self.endim)
#             self.image = pygame.transform.rotate(self.image,self.rot)
#         self.realrect = self.image.get_rect(center = pos)
#         self.realpos = pos
#         pos =   (  self.image.get_width() + self.realpos[0] , self.image.get_height() + self.realpos[1]        )
#         self.rect = self.image.get_rect(center = pos)

#     def update(self,state,name):
#         if state in self.states:
#             pos =   (  univars.realscreeen.get_width()//2 -  self.image.get_width()//2 + self.realpos[0] , univars.realscreeen.get_height()//2 - self.image.get_height()//2 + self.realpos[1]        )
#             if not self.dim == None:
#                 self.image = pygame.Surface(self.dim)
#                 self.image.fill(self.col)
#                 self.image.set_alpha(self.alpha)
#                 self.image = pygame.transform.rotate(self.image,self.rot)
#             else:
#                 self.image = pygame.image.load(self.surf).convert_alpha()
#                 self.image.set_alpha(self.alpha)
#                 self.image = pygame.transform.scale(self.image,self.dim)
#                 self.image = pygame.transform.rotate(self.image,self.rot)
#             self.rect = self.image.get_rect(center = pos)
#             if self.rect.collidepoint(pygame.mouse.get_pos()) or name == self.name:
#                 self.hover = True
#                 self.image = pygame.transform.scale(self.image,self.endim)
#                 if em.x or em.mouse:
#                     self.click = True
#                 else:
#                     self.click = False
#         else:
#             self.image = pygame.Surface((0,0))
#             self.hover = False
#             self.click = False
        
# class Ui(pygame.sprite.Sprite):
#     def __init__(self,surf,dim,col,alpha,states,rot,pos,name):
#         pygame.sprite.Sprite.__init__(self)
#         self.dim = dim
#         self.name = name
#         self.states = states
#         self.rot = rot
#         self.surf = surf
#         self.alpha = alpha
#         self.col = col
#         if not col == None:
#             self.image = pygame.Surface(dim)
#             self.image.fill(col)
#             self.image.set_alpha = alpha
#         else:
#             self.image = pygame.image.load(surf).convert_alpha()
#             self.image.set_alpha = alpha
#             self.image = pygame.transform.scale_by(self.surf,dim)
#         self.rect = self.image.get_rect(center = pos)

#     def update(self,state,name):
#         if state in self.states:
#             if not self.dim == None:
#                     self.image = pygame.Surface(self.dim)
#                     self.image.fill(self.col)
#             else:
#                 self.image = pygame.image.load(self.surf).convert_alpha()
#                 self.image.set_alpha = self.alpha
#                 self.image = pygame.transform.scale(self.image,self.dim)
#                 self.image = pygame.transform.rotate(self.image,self.rot)
#         else:
#             self.image = pygame.Surface((0,0))
        

# class Text(pygame.sprite.Sprite):
#     def __init__(self,name,text,font,pos,col,size,states):
#         self.name = name
#         self.text = text
#         self.font = font
#         self.pos = pos
#         self.col = col
#         self.size = size
#         self.states = states

#     def update(self,state):
#         if state in self.states:
#             tm.drawtext2(self.text,self.font,self.size,0,0,0,self.col,self.pos[0],self.pos[1])

class Ui(pygame.sprite.Sprite):
    def __init__(self,surf,states,pos,name,cando = True):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.pos = pos
        self.name = name
        self.baseimg = surf
        self.rect = self.baseimg.get_rect(center = pos)
        self.states = states
        self.cando = cando

    def update(self,state,elements,em):
        if self.name in elements.keys():
            if state in self.states or "all" in self.states:
                if self.cando:
                    self.baseimg.fill(elements[self.name]["color"])
                else:
                    self.baseimg = elements[self.name]["surf"]
                self.states = elements[self.name]["states"]
                self.baseimg.set_alpha(elements[self.name]["alpha"])
                baseimg1 = pygame.transform.scale(self.baseimg,elements[self.name]["dimensions"])
                self.baseimg = baseimg1
                self.pos = elements[self.name]["pos"]
                self.image = self.baseimg
                pos = self.pos
                self.rect = self.baseimg.get_rect(center = (pos[0] * univars.realscreeen.get_width()//2  + univars.realscreeen.get_width()//2 ,-1 * pos[1] * univars.realscreeen.get_height()//2  + univars.realscreeen.get_height()//2 ))
                self.extra(em,elements,state)
            else:
                self.image = pygame.Surface((0,0))
                self.hover = 0
                self.click = 0
        else:
            self.kill()


    def extra(self,em,element,state):
        pass


class Uirect(Ui):
    def __init__(self,dimensions,states,pos,name,surf = None):
        if not surf == None:
            img = surf
            cd = 0
        else:
            img = pygame.Surface(dimensions)
            cd  = 1
        
        super().__init__(img,states, pos, name,cando=cd)
        self.surf = surf
        self.dimensions = dimensions

        
class Uibutton(Uirect):
    def __init__(self, dimensions, states, pos,name,surf = None):
        super().__init__(dimensions, states, pos,name,surf=surf)
        self.click = 0
        self.hover = 0

    def extra(self,em,elements,state):
        if em.controller["x"] or em.mouse:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.hover = True
                if em.mouse[0]:
                    self.click = True
                else:
                    self.click = False
            else:
                self.hover = False
                self.click = False


class Uitext(pygame.sprite.Sprite):
    def __init__(self, name, text, font, pos, col, size,states):
        self.name = name
        self.text = text
        self.font = font
        self.pos = pos
        self.col = col
        self.states = states
        self.realfont = pygame.font.Font(f"Graphics/Fonts/{font}",100)
        self.bart = self.realfont.render(text,1,col)
        self.image = self.realfont.render(text,1,col)
        self.rect = self.image.get_rect(center = (self.pos[0] * univars.realscreeen.get_width()//2 + univars.realscreeen.get_width()//2, -1 * self.pos[1] * univars.realscreeen.get_height()//2 + univars.realscreeen.get_height()//2))
        pygame.sprite.Sprite.__init__(self)

    def update(self,state,element,em):
        if self.name in element:
            if state in self.states or "all" in self.states:
                self.col = element[self.name]["color"]
                self.pos = element[self.name]["pos"]
                self.states = element[self.name]["states"]
                pos = self.pos
                self.text = element[self.name]["text"]
                self.bart = self.realfont.render(self.text, 1, self.col)
                self.image = pygame.transform.scale_by(self.bart,[element[self.name]["size"]/100,element[self.name]["size"]/100])
                self.rect = self.image.get_rect(center = (pos[0] * univars.realscreeen.get_width()//2 + univars.realscreeen.get_width()//2 ,-1 * pos[1] * univars.realscreeen.get_height()//2   + univars.realscreeen.get_height()//2 ))
            else:
                self.image = pygame.Surface((0, 0))
                self.rect = pygame.Rect(0, 0, 0, 0)
        else:
            self.kill()

    



