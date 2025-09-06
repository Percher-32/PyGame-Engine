import pygame
import Managers.univars as univars
import json
import Managers.Cameramod as Cameramod
import os

tol = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]



class Item(pygame.sprite.Sprite):
    def __init__(self,name,pos,alpha = 400,surf=None,color = univars.screencol,dimensions = (univars.screen_w,univars.screen_h),layer = 1,infiniscroll = 0):
        pygame.sprite.Sprite.__init__(self)
        self.infiniscroll = infiniscroll
        self.surf = surf
        self.name = name
        self.color = color
        self.alpha = alpha
        self.dimensions = dimensions
        if surf == None:
            surf = pygame.Surface(dimensions)
            surf.fill(color)
            surf.set_alpha(alpha)
        else:
            surf = pygame.image.load(f"Graphics/background/{surf}.png").convert_alpha()
            surf = pygame.transform.scale(surf,dimensions)
        
        self.pos = pos
        self.startpos = pos
        if infiniscroll:
            temporary = pygame.Surface((self.dimensions[0] * 5,self.dimensions[1]))
            temporary.set_colorkey((0,0,0))
            temporary.blit(surf , (  self.dimensions[0] ,0     )    )
            temporary.blit(surf , (  self.dimensions[0] * 2,0     )    )
            temporary.blit(surf , (  0,0     )    )
            temporary.blit(surf , (  self.dimensions[0] * 4,0     )    )
            temporary.blit(surf , (  self.dimensions[0] * 3,0     )    )
            temporary.blit(surf , (  self.dimensions[0] * 5,0     )    )
            self.baseimg = temporary
        else:
            self.baseimg = surf

        self.image = self.baseimg

        self.rect = self.image.get_rect(center = pos)
        self.layer = layer
        self.lastframe = self.image
        self.cache = {}
        camera = Cameramod.cam
        self.size = 1
        self.lastcampos = [0,0]
        self.bd = {}
        self.lastcamsize = 1
        
        self.load()
        

    def load(self):
        for i in tol:
            inst =  pygame.transform.scale_by(self.baseimg,  i )
            self.cache[str(i)] = inst


    def update(self):
        
        camera = Cameramod.cam
        realestsize = abs(round(self.size * 0.01,2)/0.01)
        self.pos[0] -= (camera.x - self.lastcampos[0])*(self.layer)*camera.size
        self.pos[1] -= (camera.y - self.lastcampos[1])*(self.layer)*camera.size
        
        self.size += (camera.size - self.lastcamsize)*self.layer *(univars.scaledown)


        # if self.layer == 0.1:
        #     self.bd[(int(camera.x/16) * 16,int(camera.y/16) * 16,round(camera.size,2))] = (             (round(self.pos[0]) * realestsize + univars.screen.get_width()//2   )     ,      round((self.pos[1]) * realestsize + univars.screen.get_height()//2   )  )
        #     for a in [ str(i) + ":" +  str(self.bd[i]) for i in self.bd.keys()]:
        #         print(a)
        #     print("///////////////")



        if not str(realestsize) in self.cache.keys():
            self.image =  pygame.transform.scale_by(self.baseimg,  realestsize )
            self.cache[str(realestsize)] = self.image
        else:
            self.image = self.cache[str(realestsize)]
        self.lastcampos = [camera.x,camera.y]
        self.lastcamsize = camera.size

        if abs((self.pos[0])) > self.dimensions[0] and self.infiniscroll:
            self.pos[0] = 0
                


        # self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect(center = (             (round(self.pos[0]) * realestsize + univars.screen.get_width()//2   )     ,      round((self.pos[1]) * realestsize + univars.screen.get_height()//2   )                     ))
        
        self.lastframe = self.image
        self.lastrect = self.rect


       





class Backgroundmanager:
    def __init__(self):
        self.items = {}
        self.background = None
        self.backlayer = pygame.Surface((64 * univars.pixelscale,64 * univars.pixelscale))
        self.backlayer.fill(univars.screencol)
        self.infiniscrollers = []


    def addbackground(self,name):
        self.items[name] = pygame.sprite.Group()

    def addbackgrounditem(self,name,backgroundname,pos,alpha = 400,layer = 1,surf=None,infiniscroll = False,color = univars.screencol,dimensions = (univars.screen_w,univars.screen_h)):
        item = Item(name,pos,alpha=alpha,surf=surf,color=color,dimensions=dimensions,layer=layer,infiniscroll=infiniscroll)
        self.items[backgroundname].add(item)


    def update(self,screencol):
        # self.backlayer = pygame.transform.scale(self.backlayer,[64 * univars.pixelscale,64 * univars.pixelscale])
        self.backlayer.fill(screencol)
        if self.background in self.items.keys():
            self.items[self.background].update()
            self.items[self.background].draw(self.backlayer)


    def savebg(self):
        """
            saves all backgrounds and items within
        """
        for item in self.items.keys():
            todump = [  [i.name,i.pos,i.alpha,i.surf,i.color,i.dimensions,i.layer,i.infiniscroll]  for i in self.items[item]]
            with open (f"Saved/backgrounds/{item}.json","w") as file:
                json.dump(todump,file)
            

    def loadbg(self):
        self.items = {}
        for item in os.listdir("Saved/backgrounds"):
            ground = "Saved/backgrounds" + "/" + item
            self.addbackground(item.replace(".json",""))
            with open ("Saved/backgrounds" + "/" + item,"r") as thing:
                things = json.load(thing)
                for elem in things:
                    self.addbackgrounditem(elem[0],item.replace(".json",""),elem[1],alpha= elem[2],surf=elem[3],color = elem[4],dimensions=elem[5],layer = elem[6],infiniscroll=elem[7])

bg = Backgroundmanager()
      