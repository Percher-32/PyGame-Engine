import pygame
import univars
import Cameramod


class Item(pygame.sprite.Sprite):
    def __init__(self,pos,alpha = 400,surf=None,color = univars.screencol,dimensions = (univars.screen_w,univars.screen_h),layer = 1):
        pygame.sprite.Sprite.__init__(self)
        if surf == None:
            surf = pygame.Surface(dimensions)
            surf.fill(color)
            surf.set_alpha(alpha)
        self.color = color
        self.alpha = alpha
        self.dimensions = dimensions
        self.image = surf
        self.pos = pos
        self.baseimg = surf
        self.rect = self.baseimg.get_rect(center = pos)
        self.layer = layer
        self.renderedpos = pos

    def update(self):
        camera = Cameramod.cam
        self.renderedpos =  (            ( (self.pos[0] - camera.x) * camera.size / self.layer) + univars.screen.get_width()//2 ,      (self.pos[1] - camera.y) * camera.size / self.layer + univars.screen.get_height()//2               )
        # self.image = pygame.transform.scale(self.baseimg,[self.dimensions[0] * camera.size/self.layer,self.dimensions[1] * camera.size/self.layer])
        self.image = pygame.transform.scale_by(self.baseimg,camera.size/self.layer)
        # self.image = self.baseimg
        self.rect = self.image.get_rect(center = self.renderedpos )






class Backgroundmanager:
    def __init__(self):
        self.items = {}
        self.background = None


    def addbackground(self,name):
        self.items[name] = pygame.sprite.Group()

    def addbackgrounditem(self,backgroundname,pos,alpha = 400,surf=None,color = univars.screencol,dimensions = (univars.screen_w,univars.screen_h),layer = 1):
        item = Item(pos,alpha=alpha,surf=surf,color=color,dimensions=dimensions,layer=layer)
        self.items[backgroundname].add(item)


    def update(self):
        if not self.background == None:
            self.items[self.background].update()
            self.items[self.background].draw(univars.screen)

bg = Backgroundmanager()
      