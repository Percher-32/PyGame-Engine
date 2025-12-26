import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math



import Game_Code.Player.player_movement_core as player_movement_core
import Game_Code.Player.logic_spindash as logic_spindash
import Game_Code.Player.logic_homingattack as logic_homingattack
import Game_Code.Player.logic_trick as logic_trick
import Game_Code.Player.logic_dashbar as logic_dashbar




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

def main(self):
    um.elements["Speed-timer"]["text"]  = str(round(float(um.elements["Speed-timer"]["text"]) + (self.dt/60 *self.publicvariables["gamespeed"] ),2))
    um.elements["attemps"]["text"]  = str(self.timesdone)
    
    self.sp("wantime",self.publicvariables["gamespeed"])
    self.sp("dashmeter",min([300,self.gp("dashmeter")]))
    self.sp("dashmeter",max([0,self.gp("dashmeter")]))




    um.elements["dashbar"]["dimensions"][0] = self.unilerp( um.elements["dashbar"]["dimensions"][0] ,   max([((self.gp("dashmeter") * 10) - 50)/2,0])/3 ,4  )

    if self.gp("homing"):
        if self.gp("target").info["type"] == "rocket":
            um.elements["missiletime"]["dimensions"][0] = 950 * self.gp("MISSIILETIME")
            um.elements["missiletimeback"]["dimensions"][0] = 950
        else:
            um.elements["missiletime"]["dimensions"][0] = 0
            um.elements["missiletimeback"]["dimensions"][0] = 0
    else:
        um.elements["missiletime"]["dimensions"][0] = 0
        um.elements["missiletimeback"]["dimensions"][0] = 0

    if self.gp("dashmeter") <= 0:
        um.elements["dashbar"]["dimensions"][0] = 0
    um.elements["dashbar"]["color"] = (0,100,255)
    collision = om.collide9("player",0,cam,self.dim,ignore= ["playersprite","skateboard"])
    lonepoint1 = om.collidep([om.objects["player"]["pos"][0] + 60,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
    lonepoint2 = om.collidep([om.objects["player"]["pos"][0] - 50,om.objects["player"]["pos"][1] + 17 ],0,32,camera=cam,basecolor=(0,1,0))
    collisionbox = om.collide("player",0,cam,extra=20)
    smallcollisionbox = om.collide("player",1,cam,extra=-60)
    bigcollisionbox = om.collide("player",0,cam,extra=600)
    attackbox = om.colliderect([cm.getcam("playercam","pos")[0] +(self.lookahead*0),cm.getcam("playercam","pos")[1] + (self.lookaheady*0)],[1300,700],0,cam)

    ground1 = len(collision["botmid"]["inst"]) > 0
    ground2 = len(collision["botleft"]["inst"]) > 0    and not (len(collision["topleft"]["inst"])  > 0  ) and not (len(collision["midleft"]["inst"])  > 0  )
    ground3 = len(collision["botright"]["inst"]) > 0   and not (len(collision["topright"]["inst"]) > 0  ) and not (len(collision["midright"]["inst"]) > 0  )
    ground = ground1 or ground2 or ground3
    instlist = collision["botmid"]["inst"] + collision["botleft"]["inst"] + collision["botright"]["inst"]
    collisionlisttype = [i.type for i in instlist]
    collisionboxtype = [i.type for i in collisionbox["inst"]] 

    
    #TRAIL
    if self.flowstate:
        self.wait("dotrail",0.2)
        if self.ondone("dotrail"):
            colid = random.randint(6,11)
            if colid == 6:
                col = (255, 79, 0)
            elif colid == 7:
                col = (255, 225, 0)
            elif colid == 8:
                col = (26, 255, 0)
            elif colid == 9:
                col = (0, 255, 255)
            elif colid == 10:
                col = (0, 8, 255)
            elif colid == 11:
                col = (255, 0, 203)

            
            ltid = om.add(self,om.objects["player"]["pos"],"player",om.objects["playersprite"]["rot"],"RAINBOWTRAIL",[1.1,1.1],self.dim,layer=0,sn = colid ,keepprev=1,info={"col":col})

            

            


            om.lighttoenemy(ltid,"l1",color=col,colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=30)

    

    rail = False
    if len(collisionboxtype) > 0:
        rail = collisionboxtype[0] == "rail"
        
    
    self.rail = rail
    self.railrot = 0
    self.raildir = "r"
    
    if not rail:
        self.sp("dashmeter",self.gp("dashmeter") + (abs(self.gp("des_vel",0))/150 * self.dt))
    else:
        self.sp("dashmeter",self.gp("dashmeter") + (abs(self.gp("des_vel",0))/150 * self.dt))

    if abs(self.key["x"]) > 0:
        if self.key["x"] > 0:
            self.lastdirslant = "l"
        else:
            self.lastdirslant = "r"

    if self.dt == 0 or self.dt > 10:
        self.dt = 1

    if len(collisionboxtype) > 0:
        if "slantl"  in collisionboxtype or "slantr" in collisionboxtype:
            slanted = True
            if "slantr" in collisionboxtype:
                if self.lastdirslant == "r":
                    if len(lonepoint2["inst"]) > 0:
                        slanted = False
                        om.objects["player"]["pos"] = [lonepoint2["inst"][0].realpos[0] + univars.grandim,lonepoint2["inst"][0].realpos[1] - 32]
            else:
                if self.lastdirslant == "l":
                    if len(lonepoint1["inst"]) > 0 :
                        slanted = False
                        om.objects["player"]["pos"] = [lonepoint1["inst"][0].realpos[0] + univars.grandim,lonepoint1["inst"][0].realpos[1] - 32]

            
        else:
            slanted = False	
    else: 
        slanted = False

    if self.key["attack"] and self.attackheld > 13:
        self.sp("wantime",max([3/self.attackheld,0.4]))

    if not self.key["attack"] and self.lastkey["attack"] and not self.isthere("cooldownattack"):
        if self.attackheld < 10:
            self.wait("attack",0.4)
            self.wait("cooldownattack",0.5)
            
            self.spin(30,0.3)
        else:
            self.wait("skatego",0.5,barrier=1)
            self.spin(30,1)
            
            # self.bailable = 1
            self.skatevel = [
                                (self.key["x"] * 1000 * 2 )  + om.objects["player"]["pos"][0],
                                (self.key["y"] * -500 * 2 )  + om.objects["player"]["pos"][1]
                            ]	
            
                
    if self.key["x"] > 0:
        self.lastdir = "r"
    if self.key["x"] < 0:
        self.lastdir = "l"

    axis = [self.key["x"],self.key["y"] * 1]
    vecaxis = pygame.math.Vector2(axis[0],axis[1])
    if vecaxis.length()> 0:
        vecaxis.normalize()
        vecaxis.scale_to_length(1.2)
    axis = [vecaxis.x,vecaxis.y]
    axis[1] = round(axis[1],2)

    
    vec = None
    #HOMING ATTACK SELECT
    if len(attackbox["obj"]):
        om.objects["enemyzoom"]["rendercond"] = 1
        if pygame.math.Vector2(self.key["x"],self.key["y"] ).length() > 0:
            self.joyaxis = pygame.math.Vector2(-1 *self.key["x"],1 *self.key["y"] )
            self.joyaxis.normalize()
        enaxis = self.joyaxis
        vec = None
        closeness = None
        playervec = pygame.math.Vector2(om.objects["player"]["pos"])
        for obj in attackbox["obj"]:	
            if not obj == None:
                emvec = pygame.math.Vector2(obj.info["pos"])
                distvec = playervec - emvec
                if distvec.length() > 0:
                    distvec.normalize()
                    if obj.info["type"] in self.typesofhoming and om.get_value(obj.name,"canhome"):
                        if vec == None:
                            vec = obj
                            closeness = 1 - distvec.dot(enaxis) 
                        else:
                            if 1-distvec.dot(enaxis) < closeness:
                                vec = obj
                                closeness = 1 - distvec.dot(enaxis) 
        if vec == None:
            om.objects["enemyzoom"]["rendercond"] = 0
        else:
            om.objects["enemyzoom"]["pos"] = vec.info["pos"]
            om.objects["enemyzoom"]["sizen"] = self.listadd((vec.info["sizen"],[0.5,0.5]))





        

    

        if self.gp("homing") == 2:
            vec = self.gp("target")

    else:
        om.objects["enemyzoom"]["rendercond"] = 0








    #MAIN
    ret_dict_player_movement_core =   player_movement_core.main(self,collisionbox,slanted,rail,collision,collisionlisttype,axis,vec,instlist,collisionboxtype,smallcollisionbox,ground)


    
    
    
    
    
    
    
    
    #LOGIC
    
    
    
    
    logic_dashbar.main(self,ground,rail)
    logic_spindash.main(self,collisionbox["inst"],ground)
    logic_homingattack.main(self,collisionlisttype,vec,axis,ground)
    logic_trick.main(self,collisionbox,ground)









    #get out of wall
    if len(collision["midmid"]["inst"] )> 0 and not slanted and not rail :
        top = collision["topmid"]["inst"] or collision["topleft"]["inst"] or collision["topright"]["inst"]
        bot = collision["botmid"]["inst"] or collision["botleft"]["inst"] or collision["botright"]["inst"]
        left = collision["topleft"]["inst"] or collision["midleft"]["inst"] or collision["botleft"]["inst"]
        right = collision["topright"]["inst"] or collision["midright"]["inst"] or collision["botright"]["inst"]
        mip = collision["midmid"]["inst"][0].realpos
        if collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] :
            # self.publicvariables["shaderstate"] = not self.publicvariables["shaderstate"]
            om.translate(self,"player",[self.gp("act_vel")[0] * -1,self.gp("act_vel")[1] * -1],usedt=1)
            self.sp("des_vel",[0,0])
        elif top and not collision["botmid"]["inst"]:
            om.objects["player"]["pos"][1] =  mip[1] + 32
        elif bot and not collision["topmid"]["inst"]:
            om.objects["player"]["pos"][1] =  mip[1] - 32
        elif right and not collision["midleft"]["inst"]:
            om.objects["player"]["pos"][0] = mip[0] - 32
        elif left  and not collision["midright"]["inst"]:
            om.objects["player"]["pos"][0] = mip[0] + 32
    else:
        self.lastframeslanted = slanted
        self.sp("prev_act_vel",self.gp("act_vel"))
        self.sp("prev_des_vel",self.gp("des_vel"))
        self.sp("prevprevpos",om.objects["player"]["pos"])

    


                                

            
    


    #LOOK AHEAD


    




    if self.key["attack"] and not self.key["trick"]:
        self.attackheld += self.dt
    else:
        self.attackheld = 0

        
    
    self.lastrail = rail
    self.lastground = ground
    self.sp("lastframewall",self.gp("leftwall") or self.gp("rightwall"))
    om.speed = univars.func.lerp(om.speed,self.gp("wantime"),5,roundto=2)
    
    
    if self.ondone("show-score"):
        um.state = "maingame"
        # self.wait()
        self.initialiseplayer([0,60])

