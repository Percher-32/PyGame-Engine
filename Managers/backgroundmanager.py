import pygame
import univars
import json
import Cameramod
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
        self.prevcampos = [Cameramod.cam.x,Cameramod.cam.y]
        self.pastbcs = Cameramod.cam.size

    def update(self):
        camera = Cameramod.cam
        self.renderedpos =  (            ( (self.pos[0]) * camera.size) + univars.screen.get_width()//2    ,      (self.pos[1]) * camera.size + univars.screen.get_height()//2               )
        # self.image = pygame.transform.scale(self.baseimg,[self.dimensions[0] * camera.size/self.layer,self.dimensions[1] * camera.size/self.layer])
        # self.image = pygame.transform.scale_by(self.baseimg,camera.size/self.layer)
        # self.image = self.baseimg
        if univars.camchange:
            self.bcs += (Cameramod.cam.size - self.pastbcs)/self.layer
            self.pastbcs = Cameramod.cam.size
        if univars.poschange:
            self.pos[0] -= (camera.x - self.prevcampos[0])/self.layer
            self.pos[1] -= (camera.y - self.prevcampos[1])/self.layer
            self.prevcampos = [Cameramod.cam.x,Cameramod.cam.y]

        self.image = pygame.transform.scale_by(self.baseimg,self.bcs)
        self.rect = self.image.get_rect(center = self.renderedpos )






class Backgroundmanager:
    def __init__(self):
        self.items = {}
        self.background = None


    def addbackground(self,name):
        self.items[name] = pygame.sprite.Group()

    def addbackgrounditem(self,name,backgroundname,pos,alpha = 400,surf=None,color = univars.screencol,dimensions = (univars.screen_w,univars.screen_h),layer = 1):
        item = Item(name,pos,alpha=alpha,surf=surf,color=color,dimensions=dimensions,layer=layer)
        self.items[backgroundname].add(item)


    def update(self):
        if self.background in self.items.keys():
            self.items[self.background].update()
            self.items[self.background].draw(univars.screen)


    def savebg(self):
        for item in self.items.keys():
            if not os.path.exists(f"Saved/backgrounds/{item}.json"):
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
        print(ground)

bg = Backgroundmanager()
      