import pygame
import Managers.univars as univars
import json
import Managers.Cameramod as Cameramod
import os



class Item(pygame.sprite.Sprite):
    def __init__(self,name,pos,alpha = 400,surf=None,color = univars.screencol,dimensions = (univars.screen_w,univars.screen_h),layer = 1):
        pygame.sprite.Sprite.__init__(self)
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
        
        self.image = surf
        self.pos = pos
        self.bcs = 1
        self.baseimg = surf
        self.rect = self.baseimg.get_rect(center = pos)
        self.layer = layer
        self.renderedpos = pos
        self.originalpos = self.pos
        self.pastbcs = Cameramod.cam.size
        self.lastframe = self.baseimg
        self.cache = {}
        camera = Cameramod.cam
        self.size = camera.size
        self.lastcampos = [camera.x,camera.y]
        self.lastcamsize = camera.size

    def update(self):
        
        camera = Cameramod.cam
        realestsize = round(self.size,4)
        if univars.camchange or univars.poschange:
            if univars.poschange:
                self.pos[0] -= (camera.x - self.lastcampos[0])*self.layer
                self.pos[1] -= (camera.y - self.lastcampos[1])*self.layer
                
            if univars.camchange:
                self.size += (camera.size - self.lastcamsize)*self.layer
                # pass




            if not str(realestsize) in self.cache.keys():
                self.image =  pygame.transform.scale_by(self.baseimg,  realestsize )
                self.cache[str(realestsize)] = self.image
            else:
                self.image = self.cache[str(realestsize)]
        else:
            self.image = self.lastframe





        # self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect(center = (             (round(self.pos[0]) * realestsize + univars.screen.get_width()//2   )     ,      round((self.pos[1]) * realestsize + univars.screen.get_height()//2   )                     ))
        
        self.lastframe = self.image
        self.lastrect = self.rect


        self.lastcampos = [camera.x,camera.y]
        self.lastcamsize = camera.size





class Backgroundmanager:
    def __init__(self):
        self.items = {}
        self.background = None
        self.backlayer = pygame.Surface((64 * univars.pixelscale,64 * univars.pixelscale))
        self.backlayer.fill(univars.screencol)


    def addbackground(self,name):
        self.items[name] = pygame.sprite.Group()

    def addbackgrounditem(self,name,backgroundname,pos,alpha = 400,surf=None,color = univars.screencol,dimensions = (univars.screen_w,univars.screen_h),layer = 1):
        item = Item(name,pos,alpha=alpha,surf=surf,color=color,dimensions=dimensions,layer=layer)
        self.items[backgroundname].add(item)


    def update(self,screencol):
        self.backlayer = pygame.transform.scale(self.backlayer,[64 * univars.pixelscale,64 * univars.pixelscale])
        self.backlayer.fill(screencol)
        if self.background in self.items.keys():
            self.items[self.background].update()
            self.items[self.background].draw(self.backlayer)


    def savebg(self):
        """
            saves all backgrounds and 
        """
        for item in self.items.keys():
            todump = [  [i.name,i.pos,i.alpha,i.surf,i.color,i.dimensions,i.layer]  for i in self.items[item]]
            with open (f"Saved/backgrounds/{item}.json","x") as file:
                json.dump(todump,file)
            

    def loadbg(self):
        self.items = {}
        for item in os.listdir("Saved/backgrounds"):
            ground = "Saved/backgrounds" + "/" + item
            self.addbackground(item.replace(".json",""))
            with open ("Saved/backgrounds" + "/" + item,"r") as thing:
                things = json.load(thing)
                for elem in things:
                    self.addbackgrounditem(elem[0],item.replace(".json",""),elem[1],alpha= elem[2],surf=elem[3],color = elem[4],dimensions=elem[5],layer = elem[6])

bg = Backgroundmanager()
      