import pygame
import event_manager
import Textmanager
import Uielement
import univars
tm = Textmanager.Textmanager(univars.realscreeen)
em = event_manager.event_manager()


class Uimanager:
    def __init__(self):
        self.uis = pygame.sprite.Group()
        self.texts = []
        self.state = univars.startuistate

    def addbutton(self,surf,dim,col,alpha,states,rot,pos,endim,name):
        butt = Uielement.Button(surf,dim,col,alpha,states,rot,pos,endim,name)
        self.uis.add(butt)

    def addui(self,surf,dim,col,alpha,states,rot,pos,name):
        ui = Uielement.Ui(surf,dim,col,alpha,states,rot,pos,name)
        self.uis.add(ui)

    def addtext(self,name,text,font,pos,col,size,states):
        temptext = Uielement.Text(name,text,font,pos,col,size,states)
        self.texts.append(temptext)

    def showvar(self,gm,name,var,pos):
        strvar = f"{name}:{var}"
        surf = pygame.Surface((len(strvar) * 20,40))
        surf.fill((0,0,30))
        surf.set_alpha(200)
        gm.blitui(surf,pos,surf.get_size())
        tm.drawtext3(gm,strvar,"pixel2.ttf",30,0,0,0,(225,225,225),pos)
        

    def update(self):
        self.uis.update(self.state,None)
        self.uis.draw(univars.realscreeen)
        for i in self.texts:
            i.update(self.state)

ingame = Uimanager()
Engine = Uimanager()
    