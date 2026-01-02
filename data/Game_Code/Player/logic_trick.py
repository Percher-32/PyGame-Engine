import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars




em = Gamemananager.em
tm = Gamemananager.tm
fm = Gamemananager.fm
om = Gamemananager.om
Tiled = Gamemananager.Tiled
cam =Gamemananager.cam
cm = Gamemananager.cm
sd = Gamemananager.sd
sm = Gamemananager.sm
um = Gamemananager.um
bg = Gamemananager.bg
pm = Gamemananager.pm

def main(self,collisionbox,ground):
    
    #styles
    if self.key["bumper"] and not len(collisionbox["inst"] ) >0:
        times = 0.7
        self.wait("inv",times)
        if not self.isthere("tcd"):
            if self.key["throw"] and not self.lastkey["throw"]:
                self.prevtricks.append(1)
                self.wait("tcd",0.2)
                self.wait("VULNERABLE",times,barrier=False)
                self.wait("trick1",times,barrier=False)
                self.spin(12,times,0.1)
                if self.prevtricks[-1] == 1:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
                else:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))
            elif self.key["secondary"] and not self.lastkey["secondary"]:
                self.prevtricks.append(2)
                self.wait("tcd",0.2)
                self.wait("VULNERABLE",times,barrier=False)
                self.wait("trick2",times,barrier=False)
                self.sp("dashmeter",self.gp("dashmeter") + 20)
                if self.prevtricks[-1] == 2:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
                else:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))
            elif self.key["attack"] and not self.lastkey["attack"]:
                self.prevtricks.append(3)
                self.wait("tcd",0.2)
                self.wait("VULNERABLE",times,barrier=False)
                self.wait("trick3",times,barrier=False)
                self.sp("dashmeter",self.gp("dashmeter") + 20)
                if self.prevtricks[-1] == 3:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 4),60]))
                else:
                    self.sp("dashmeter",self.gp("dashmeter") + min([((len(self.prevtricks) + 1) * 13),100]))


    #Bail timer
    if self.isthere("BAIL"):

        self.key["x"] = 0
        self.key["y"] = 0
        self.key["jump"] = 0
        if self.gp("leftwall") or self.gp("rightwall"):
            self.key["jump"] = 1
    if self.ondone("BAIL"):
        self.key["jump"] = 1
        self.sp("act_vel",100,1)
        self.sp("des_vel",100,1)
     
            
    
    #BAIL LOGIC
    if len(collisionbox["inst"] ) >0:
        if self.isthere("VULNERABLE"):
            self.bailable = 1
            self.prevtricks = []
            self.deltimer("VULNERABLE")
   
    if ground:
        if self.bailable:
            self.wait("BAIL",0.6)
            self.sp("dashmeter",0)
            self.bailable = 0
            
    
    
    #TRICK LOOKS
    if self.isthere("trick1")and self.isthere("VULNERABLE"):
        om.objects["playersprite"]["sn"] = 12
        # self.boardoffset[0] = self.unilerp(self.boardoffset[0],math.sin((rot/180) * math.pi) * 0,4)
        self.boardoffset[1] += 10 * self.dt
        self.playeroffset[1] -= 10 * self.dt
        om.objects["skateboard"]["rot"] = 0
    if self.isthere("trick2")and self.isthere("VULNERABLE"):
        om.objects["playersprite"]["sn"] = 0
        
        self.playeroffset[1] = self.unilerp(self.playeroffset[1],-40,8)
        om.objects["playersprite"]["sn"] = 13
        
        if self.key["x"] > 0:
            om.objects["skateboard"]["rot"] = 45
            self.boardoffset[0] = self.unilerp(self.boardoffset[0],10,3)
        elif self.key["x"] < 0:
            om.objects["skateboard"]["rot"] = -45
            self.boardoffset[0] = self.unilerp(self.boardoffset[0],-10,3)
        else:
            self.boardoffset[1] = self.unilerp(self.boardoffset[1],10,5)
            self.playeroffset[1] = self.unilerp(self.playeroffset[1],-10,5)

        om.playanim(self.dt,"skateboard","kickflip",1,speed=3)
        # om.objects["playersprite"]["rot"] = 180
    elif self.isthere("trick3")and self.isthere("VULNERABLE"):
        
        om.playanim(self.dt,"skateboard","kickflip",1,speed=3)
        om.objects["playersprite"]["sn"] = 13
        
        self.playeroffset[1] = self.unilerp(self.playeroffset[1],-50,8)
        self.boardoffset[1] = self.unilerp(self.boardoffset[1],50,8)
        
        if self.key["x"] > 0:
            om.objects["skateboard"]["rot"] = 0
            # self.playeroffset[0] = self.unilerp(self.playeroffset[0],30,3)
            
            # self.boardoffset[0] = self.unilerp(self.boardoffset[0],30,3)
        else :
            om.objects["skateboard"]["rot"] =0
            # self.playeroffset[0] = self.unilerp(self.playeroffset[0],-30,3)
            
            # self.boardoffset[0] = self.unilerp(self.playeroffset[0],-30,3)

        # om.playanim(self.dt,"skateboard","kickflip",1,speed=3)
        # om.objects["playersprite"]["rot"] = 180
    else:
        
        self.boardoffset[0] = self.unilerp(self.boardoffset[0],0,4)
        self.boardoffset[1] = self.unilerp(self.boardoffset[1],0,4)
        self.playeroffset[0] = self.unilerp(self.playeroffset[0],0,4)
        self.playeroffset[1] = self.unilerp(self.playeroffset[1],0,4)

        
    

