import pygame
import os
import numpy as np
class func:
    def __init__(self,screen,granddim):
        self.screen = screen
        self.grandim = granddim
    def getsprites(self,name:str):
        sprites = []
        folder_dir = f"Graphics/sprites/{name}"
        for images in os.listdir(folder_dir):
            try:
                frame = pygame.transform.scale_by(pygame.image.load(f"Graphics/sprites/{name}/" + images).convert_alpha(),[(self.grandim/32) +0.1,(self.grandim/32) +0.1])
                sprites.append(frame)
            except:
                pass
        return sprites
    def getspritesscale(self,name:str,scale):
        sprites = []
        folder_dir = f"Graphics/sprites/{name}"
        for images in os.listdir(folder_dir):
            try:
                frame = pygame.transform.scale_by(pygame.transform.scale(pygame.image.load(f"Graphics/sprites/{name}/" + images).convert_alpha(), [scale[0],scale[1]]),[1,1])
                sprites.append(frame)
            except:
                print("duygfre")
        return sprites
    def allsprites(self,):
        return os.listdir("Graphics/sprites")
    def dist(self,pos1:float,pos2:float):
        return ((((pos1[0] - pos2[0]) ** 2) + ((pos1[1] - pos2[1]) ** 2)) ** 0.5)
    def rectblit(self,pos,width,col,camera,dim):
        rect = pygame.Rect((pos[0] - camera.x) * camera.size + self.screen.get_width()//2,(pos[1] - camera.y) * camera.size + self.screen.get_height()//2 ,width[0] * abs(camera.size),width[1] * abs(camera.size))
        pygame.draw.rect(self.screen,col,rect,5)
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
    def lerp(self,val,max,sm):
        val = val + (max - val)/sm
        return val