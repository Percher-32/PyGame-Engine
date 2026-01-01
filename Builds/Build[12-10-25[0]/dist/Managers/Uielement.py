import pygame
import Managers.event_manager as event_manager
import Managers.Textmanager as Textmanager
import Managers.univars as univars
tm = Textmanager.Textmanager(univars.realscreeen)



class Ui(pygame.sprite.Sprite):
    def __init__(self,surf,states,pos,name,cando = True,fromstart = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.pos = pos
        self.name = name
        self.baseimg = surf
        self.fromstart = fromstart
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


                realscale = [int(round(elements[self.name]["dimensions"][0] * ((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983)),int(round(elements[self.name]["dimensions"][1] * ((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983))]
                if not str([realscale,elements[self.name]["alpha"]]) in elements[self.name]["cache"]:
                    self.baseimg.set_alpha(elements[self.name]["alpha"])
                    baseimg1 = pygame.transform.scale(self.baseimg,   realscale   )
                    elements[self.name]["cache"][str([realscale,elements[self.name]["alpha"]])] = baseimg1
                else:
                    baseimg1 = elements[self.name]["cache"][str([realscale,elements[self.name]["alpha"]])]





                self.baseimg = baseimg1
                self.pos = elements[self.name]["pos"]
                self.image = self.baseimg
                pos = self.pos
                if not self.fromstart:
                    self.rect = self.baseimg.get_rect(center = (pos[0] * univars.realscreeen.get_width()//2  + univars.realscreeen.get_width()//2 ,-1 * pos[1] * univars.realscreeen.get_height()//2  + univars.realscreeen.get_height()//2 ))
                else:
                    self.rect = self.baseimg.get_rect(center = (pos[0] * univars.realscreeen.get_width()//2  + univars.realscreeen.get_width()//2 + self.image.get_width()/2,-1 * pos[1] * univars.realscreeen.get_height()//2  + univars.realscreeen.get_height()//2 ))
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
    def __init__(self,dimensions,states,pos,name,surf = None,fromstart = 0):
        if not surf == None:
            img = surf
            cd = 0
        else:
            img = pygame.Surface(dimensions)
            cd  = 1
        
        super().__init__(img,states, pos, name,cando=cd,fromstart = fromstart)
        self.surf = surf
        self.dimensions = dimensions

        
class Uibutton(Uirect):
    def __init__(self, dimensions, states, pos,name,surf = None,fromstart = 0):
        super().__init__(dimensions, states, pos,name,surf=surf,fromstart = fromstart)
        self.click = 0
        self.hover = 0

    def extra(self,em,elements,state):
        if em.controller["x"] or em.mouse:
            if self.rect.collidepoint([pygame.mouse.get_pos()[0]/univars.scaledown,pygame.mouse.get_pos()[1]/univars.scaledown]):
                self.hover = True
                if em.mouse[0] or em.controller["x"]:
                    self.click = True
                else:
                    self.click = False
            else:
                self.hover = False
                self.click = False


class Uitext(pygame.sprite.Sprite):
    def __init__(self, name, text, font, pos, col, size,states,center = True):
        self.name = name
        self.text = text
        self.font = font
        self.pos = pos
        self.col = col
        self.center = center
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
                sc =   element[self.name]["size"]/100 * ((univars.realscreeen.width**2 +  univars.realscreeen.height**2)**0.5)/2202.9071700822983 
                # print(sc)
                self.image = pygame.transform.scale_by(self.bart,[sc,sc])
                if self.center:
                    self.rect = self.image.get_rect(center = (pos[0] * univars.realscreeen.get_width()//2 + univars.realscreeen.get_width()//2 ,-1 * pos[1] * univars.realscreeen.get_height()//2   + univars.realscreeen.get_height()//2 ))
                else:
                    self.rect = self.image.get_rect(center = (pos[0] * univars.realscreeen.get_width()//2 + univars.realscreeen.get_width()//2 + self.image.get_size()[0]//2,-1 * pos[1] * univars.realscreeen.get_height()//2   + univars.realscreeen.get_height()//2 + self.image.get_size()[1]//2))
            else:
                self.image = pygame.Surface((0, 0))
                self.rect = pygame.Rect(0, 0, 0, 0)
        else:
            self.kill()

    



