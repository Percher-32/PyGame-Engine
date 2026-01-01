import pygame
import os
import json


gscache = {}

with open(f"Saved/sizeoffsets.json","r") as file:
    sizeoffsets = json.load(file)
class func:
    def __init__(self,granddim):
        self.grandim = granddim
        self.getspritescache = {}
        self.getspritesscalecache = {}

    def getsprites(self,name:str):
        if not name in self.getspritescache.keys():
            sprites = []
            offset = [0,0]
            if name in sizeoffsets:
                offset = sizeoffsets[name]
            folder_dir = f"Graphics/sprites/{name}"
            for images in os.listdir(folder_dir):
                frame = pygame.transform.scale_by(pygame.image.load(f"Graphics/sprites/{name}/" + images).convert_alpha(),[(self.grandim/32) + offset[0] ,(self.grandim/32) + offset[1]  ])
                sprites.append(frame)
            self.getspritescache[name] = sprites
            return sprites
        else:
            return self.getspritescache[name]

    def getspritesscale(self,name:str,scale):
        if not str((name,scale)) in self.getspritesscalecache.keys():
            sprites = []
            folder_dir = f"Graphics/sprites/{name}"
            offset = [0,0]
            if name in sizeoffsets:
                offset = sizeoffsets[name]
            for images in os.listdir(folder_dir):
                frame = pygame.transform.scale_by(pygame.transform.scale(pygame.image.load(f"Graphics/sprites/{name}/" + images).convert_alpha(), [scale[0] + offset[0],scale[1] + offset[1]]),[1,1])
                sprites.append(frame)
            self.getspritesscalecache[str((name,scale))] = sprites
            return sprites 
        else:
            return self.getspritesscalecache[str((name,scale))]
    def allsprites(self):
        return os.listdir("Graphics/sprites")
    def dist(self,pos1:list,pos2:list):
        return ((((pos1[0] - pos2[0]) ** 2) + ((pos1[1] - pos2[1]) ** 2)) ** 0.5)
    def rectblit(self,pos,width,col,camera,dim,screen):
        screen
        rect = pygame.Rect((pos[0] - camera.x) * camera.size + screen.get_width()//2,(pos[1] - camera.y) * camera.size + screen.get_height()//2 ,width[0] * abs(camera.size),width[1] * abs(camera.size))
        pygame.draw.rect(screen,col,rect,5)
    def get(self,d:dict,val):
        return list(filter(lambda key: d[key] == val, d))
    def getif(self,d:dict,val):
        if val in list(d.values()):
            return True
        else:
            return False
    def intersect(self,a:dict,b:dict):
        return list(set(a) & set(b))
    def allsprites(self):
        return os.listdir("Graphics/sprites")
    def allnone(self):
        n = ["none" for i in os.listdir("Graphics/sprites")]
        return n
    def allones(self):
        n = [[1,1] for i in os.listdir("Graphics/sprites")]
        return n
    def blitui(self,surf,pos,size,realscreeen):
        a = surf
        a = pygame.transform.scale(a,(abs(size[0]),abs(size[1])))
        realscreeen.blit(a,(pos[0]  * realscreeen.get_width()//2 - (a.get_width()/2)  + realscreeen.get_width()//2  ,-1 * pos[1]  * realscreeen.get_width()//2 - (a.get_height()/2)  + realscreeen.get_height()//2 ))
    def lerp(self,val,max,sm,roundto = None):
        if type(val) == int or type(val) == float:
            if round == None:
                val = val + (max - val)/sm
            else:
                val = round(val + (max - val)/sm,roundto)
            return val
        else:
            if type(val) == tuple:
                val = list(val)
                max = list(max)
            for i in range(len(val)):
                if round == None:
                    val[i] += (max[i] - val[i])/sm
                else:
                    val[i] += round((max[i] - val[i])/sm,roundto)
            if type(val) == tuple:
                return tuple(val)
            else:
                return val
    
    def ssblitrect(self,rect,col,camera,thickness,screen,sd):
        """"blits a rect onto screen space  , (for thinckness -1 means filled)"""
        rect = pygame.Rect( ((  rect.x - camera.x) * (camera.size*1)) + screen.get_width()//2   ,((rect.y - camera.y) * (camera.size*1)) + screen.get_height()//2  ,rect.width * abs(camera.size),rect.height * abs(camera.size))
        # rect  = pygame.Rect(0,0,1000,1000)
        pygame.draw.rect(screen,col,rect,thickness)
