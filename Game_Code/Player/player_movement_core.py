import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math


import Game_Code.Player.state_rail as state_rail



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



def main(self,collisionbox,slanted,rail,collision,collisionlisttype,axis,vec,instlist,collisionboxtype,smallcollisionbox,ground):
    raildir = None
    railrot = None
    ground = ground
    if "spring" in [i.info["type"] for i in collisionbox["obj"]]:
        ground = 0
        self.sp("dashmeter",self.gp("dashmeter") + 30)
        self.sp("jumpable",1)
        self.sp("homing",0)
        self.wait("bouncerem",3)
        info = collisionbox["obj"][[i.info["type"] for i in collisionbox["obj"]].index("spring")].info
        sid = collisionbox["obj"][[i.info["type"] for i in collisionbox["obj"]].index("spring")].name
        # cm.setcond("playercam","shake",6)
        actmult = [1,1]
        actvel = [  math.sin(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * actmult[0] * -1.5 , math.cos(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * actmult[1] ]
        desmult = [1,1]
        desvel = [  math.sin(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * desmult[0] * -1.5 , math.cos(info["rot"]/180 * math.pi) * om.get_value(sid,"power") * desmult[1] ]


        self.sp("dashav",self.listdiv(actvel,5))
        self.sp("dashdv",self.listdiv(desvel,5))

        self.sp("act_vel",0,1)
        self.sp("des_vel",0,1)
        self.sp("act_vel",0,0)
        self.sp("des_vel",0,0)
        self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
        self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))


    if not slanted:
        if slanted == self.lastframeslanted or self.key["jump"]:
            #MAIN
            
            if not rail:
                if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ):
                    #IN HERE IS EITHER [NO MIDMID] OR [Yes MIDMID AND GROUND]
                    if self.key["trick"] and not len(collisionbox["inst"] ) >0:
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
                        

                    self.sp("dashmeter",max([self.gp("dashmeter"),0])) 

                    
                    
                    self.sp("dashmeter",max([self.gp("dashmeter"),0])) 


                    # if self.key["attack"] and not self.lastkey["attack"]:
                    # 	for i in range(int(self.gp("dashmeter"))):
                    # 		pm.particlespawnbluprint(om.objects["player"]["pos"],"star")
                    


                    if self.lastrail:
                        # self.spin(21,0.4,0.1)
                        pass




                    #TRICKS
                    


                    if abs(self.gp("des_vel",0)) > 250:
                        self.sp("des_vel",250 * self.valsign(self.gp("des_vel",0)),0)
                    if abs(self.gp("act_vel",0)) > 250:
                        self.sp("act_vel",250 * self.valsign(self.gp("act_vel",0)),0)


                    #x dir movement
                    if abs(self.key["x"]) > 0:
                        if self.isthere("leftjump"):
                            self.key["x"] = 1
                        if self.isthere("rightjump"):
                            self.key["x"] = -1 * 1

                        if self.gp("xinit") or not self.valsign(self.gp("act_vel",0)) == self.valsign(self.key["x"]):
                            self.sp("xinit",False)
                            self.sp("des_vel",[self.key["x"] * 120,self.gp("des_vel")[1]])
                            self.sp("act_vel",[self.key["x"] * 20,self.gp("act_vel")[1]])
                        
                        
                        if ground:
                            if self.key["throw"] and self.dropdashinit == 0:
                                # self.sp("act_vel",self.gp("des_vel"))
                                self.sp("des_vel",[        self.key["x"] * self.gp("machspeed")/10            ,    self.gp("des_vel")[1]   ])
                            else:
                                if abs(self.gp("des_vel",0)) < self.gp("machspeed") or not self.valsign(self.gp("act_vel",0)) == self.valsign(self.key["x"]):
                                    self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * self.gp("machspeed"),30 )              ,    self.gp("des_vel")[1]   ])
                                else:
                                    pass
                        else:
                            if abs(self.gp("des_vel",0)) < self.gp("machspeed") or not self.valsign(self.gp("act_vel",0)) == self.valsign(self.key["x"]):
                                self.sp("des_vel",[          self.unilerp(self.gp("des_vel")[0],self.key["x"] * self.gp("machspeed"),30 )              ,    self.gp("des_vel")[1]   ])
                            else:
                                pass
                    else:
                        self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
                        self.sp("xinit",True)



                    self.sp("machspeed",150)


                    

                    #Wall clinging
                    if not collision["midmid"]["inst"]:
                        if len(collision["midleft"]["inst"]) > 0 :
                            if collision["midleft"]["inst"][0].type == "ground":
                                self.sp("leftwall",True)
                                self.sp("lastwall","l")
                                self.sp("jumpable",True)	
                                om.objects["player"]["pos"][0] = collision["midleft"]["inst"][0].realpos[0] + 32

                                if not collision["botmid"]["inst"]:
                                    self.sp("des_vel",[0,self.gp("des_vel")[1]])
                                    self.sp("act_vel",[0,self.gp("act_vel")[1]])
                                else:
                                    if self.gp("des_vel")[0] < 0:
                                        self.sp("des_vel",[0,0])
                                    if self.gp("act_vel")[0] < 0:
                                        self.sp("act_vel",[0,0])

                            else:
                                self.sp("leftwall",False)
                        else:
                            self.sp("leftwall",False)


                        if len(collision["midright"]["inst"]) > 0 :
                            if  collision["midright"]["inst"][0].type == "ground":
                                self.sp("rightwall",True)
                                self.sp("lastwall","r")
                                self.sp("jumpable",True)	
                                om.objects["player"]["pos"][0] = collision["midright"]["inst"][0].realpos[0] -32
                                if not collision["botmid"]["inst"]:
                                    self.sp("des_vel",[0,self.gp("des_vel")[1]])
                                    self.sp("act_vel",[0,self.gp("act_vel")[1]])
                                else:
                                    if self.gp("des_vel")[0] > 0:
                                        self.sp("des_vel",[0,0])
                                    if self.gp("act_vel")[0] > 0:
                                        self.sp("act_vel",[0,0])

                            else:
                                self.sp("rightwall",False)
                        else:
                            self.sp("rightwall",False)


                    #wall ledge spin
                    if self.gp("des_vel",1) > 0:
                        if self.gp("lastframewall") and not self.gp("leftwall") and not self.gp("rightwall") and not (collision["botmid"]["inst"] and collision["botleft"]["inst"] and collision["botright"]["inst"]):
                            self.sp("xinit",False)
                            self.sp("mode","in-air")
                            ground = False
                            if not abs(self.key["x"]):
                                if not self.key["jump"]:
                                    if self.gp("lastwall") == "r":
                                        self.spin(11 ,1,spindec = 0.2)
                                        self.sp("des_vel",[0,200])
                                    else:
                                        self.spin(-11 ,1,spindec = 0.2)
                                        self.sp("des_vel",[0,200])
                            else:
                                
                                if not self.key["jump"]:
                                    self.spin(self.valsign(self.key["x"]) * -11 ,1,spindec = 0.2)
                                    self.sp("des_vel",[self.key["x"] * 150,200])


                        

                    #Skid detection 
                    if abs(self.gp("act_vel")[0]  - self.gp("des_vel")[0]) > 50:
                        self.sp("skidding",True)
                    else:
                        self.sp("skidding",False)


                    #rerout detection
                    if not self.isthere("leftjump") or not self.isthere("rightjump"):
                        if not self.sign(self.key["x"]) == self.sign(self.gp("lastx")):
                            self.sp("xinit",True)
                            if ground and abs(self.gp("act_vel")[0]) > 100:
                                self.wait("skid",0.3)
                                # self.print("shid")
                        self.sp("lastx",self.key["x"])


                    if self.isthere("skid"):
                        if ground:
                            pm.particlespawnbluprint(om.objects["player"]["pos"],"grind",initvel=[0,0])
                    
                    # if self.gp("dashmeter") > -100:
                        # pm.particlespawnbluprint([om.objects["player"]["pos"][0] + (self.gp("act_vel")[0]/100) - 32/2,om.objects["player"]["pos"][1] + 10],"ultra",initvel=[self.gp("act_vel")[0]/10,self.gp("act_vel")[1]/10])

                    #ground detection + falling
                    if ground:
                        if self.bailable:
                            self.wait("BAIL",0.6)
                            self.sp("dashmeter",0)
                            self.bailable = 0
                            # for i in range(10):
                            # 	pm.particlespawnbluprint(om.objects["player"]["pos"],"dust",initvel=[0,5])
                        self.sp("desrot",0)
                        self.sp("mode","grounded")
                        self.sp("jumpable",True)
                        self.sp("onboard",True)
                    else:
                        if self.key["jump"]:
                            self.sp("onboard",True)
                        if not self.gp("leftwall") or not self.gp("rightwall"):
                            self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    self.unilerp(self.gp("des_vel")[1],-130,self.gp("fss"),roundto = 0)   ]     )
                            self.sp("mode","in-air")
                        # else:
                        # 	self.sp("des_vel",    [  self.gp("des_vel")[0]    ,    self.unilerp(self.gp("des_vel")[1],-130,8,roundto = 0)   ]     )
                        # 	self.sp("mode","in-air")

                        if not self.key["jump"] and not self.isthere("rotate"):
                            if  self.gp("leftwall") or  self.gp("rightwall"):
                                self.sp("onboard",True)
                            else:
                                if not self.bailable:
                                    self.sp("desrot",self.key["x"] * 20)


                    #prevent rotation on walls
                    if self.gp("leftwall") or self.gp("rightwall"):
                        self.killtimer("rotate")
                        self.sp("rotoffset",0)

                    #AIR DASH
                    if self.key["jump"] and not ground and not self.lastkey["jump"]:
                        if not self.isthere("doublejumpcd") and self.gp("candj"):
                            self.bailable = 0
                            self.sp("candj",0)
                            self.wait("inv",0.3,0)
                            self.sp("dashmeter",self.gp("dashmeter") + 30)
                            self.wait("dashrem",2)
                            # cm.setcond("playercam","shake",6)
                            actmult = [160,160]
                            actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
                            desmult = [160,160]
                            desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]
                            # self.spin(21,0.4,0.1)

                            self.sp("dashav",self.listdiv(actvel,80))
                            self.sp("dashdv",self.listdiv(desvel,80))

                            self.sp("act_vel",0,1)
                            self.sp("des_vel",0,1)
                            self.sp("act_vel",0,0)
                            self.sp("des_vel",0,0)
                            self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
                            self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))

                    # self.println(collisionlisttype,4)
                    if not self.gp("homing") == 0:
                        if "ground" in collisionlisttype:							
                            self.sp("homing",0)
                            self.key["secondary"] = 0




                    if not self.gp("homing") == 1:
                        if self.key["secondary"] and not self.key["trick"]:
                            if not vec == None:
                                if not self.isthere("homecooldown"):
                                    if not self.lastkey["secondary"]:
                                        self.wait("homecooldown",0.2)
                                        self.sp("homing",1)
                                        self.sp("target",vec)
                                        if ground:
                                            self.key["jump"] = 1
                                            self.sp("act_vel",40,index=1)


                    #GOTO TARGET
                    if self.gp("homing") == 1:
                        # self.wait("teltimer",1)
                        self.wait("inv",0.1)
                        enposvec = pygame.math.Vector2(self.gp("target").info["pos"])
                        playerposvec = pygame.math.Vector2(om.objects["player"]["pos"])

                        envec = enposvec - playerposvec
                        if envec.length() > 0:
                            nenvec = envec.normalize()
                            nenvec = [nenvec.x,nenvec.y * -1]
                            ground = 0
                            if self.gp("target").info["type"] in ["enemy-L","omnispring","goal","turret","rocket","easybot","HURT:biglaser","spring"]:
                                if envec.length() > 40:
                                    a = (380 + (abs(envec.length()/3)))/2
                                    d = (380 + (abs(envec.length()/3)))/2
                                    
                                    if self.gp("target").info["type"] == "rocket":
                                        a += om.get_value(self.gp("target").name,"vel") * 4
                                        d += om.get_value(self.gp("target").name,"vel") * 4
                                    av = [a * nenvec[0] , a * nenvec[1]]
                                    dv = [d * nenvec[0] , d * nenvec[1]]
                                    self.sp("act_vel",av)
                                    self.sp("act_vel",dv)
                                    if self.gp("target").info["type"] == "enemy-L":
                                        om.set_value(self.gp("target").name,"des_vel",[0,0])
                                        om.set_value(self.gp("target").name,"act_vel",[0,0])
                                else:
                                    self.sp("homing",2)
                                    # om.objects["player"]["pos"] = self.gp("target").info["pos"]
                                    self.sp("HOLD",self.gp("target").info["pos"])
                                    self.sp("act_vel",200,1)

                    #DISMOUNT
                    if self.gp("homing") == 2:
                        if self.gp("target").info["type"] == "enemy-L":
                            if self.key["secondary"]:
                                # self.sp("des_vel",[0,0])
                                self.sp("wantime",0.1)
                                om.set_value(self.gp("target").name,"act_vel",[0,0])
                                om.set_value(self.gp("target").name,"des_vel",[0,0])
                                self.gp("target").info["pos"] = self.listadd((om.objects["player"]["pos"],[  self.valsign(self.gp("des_vel")[0]) * 40  ,  -30   ]))
                            else:
                                self.sp("homing",0)
                                if self.lastkey["secondary"]:
                                    self.sp("dashmeter",self.gp("dashmeter") + 30)
                                    od = self.timers.copy()
                                    for timer in self.timers.keys():
                                        if "#Throwing" in timer:
                                            od.pop(timer)
                                    self.timers = od

                                    
                                    if round(axis[0]) == 0:
                                        if round(axis[1]) == 0:
                                            actmult = [0,100]
                                    actmult = [axis[0] * 100,axis[1] * 100]
                                    if actmult == [0,0]:
                                        actmult = [100,0]


                                    om.set_value(self.gp("target").name,"throwvel",actmult)
                                    self.wait("#Throwing" + self.gp("target").name,3,0)
                                    self.sp("dashmeter",self.gp("dashmeter") + 30)

                                    self.wait("dashrem",2)
                                    # cm.setcond("playercam","shake",6)
                                    actmult = [160,160]
                                    actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
                                    desmult = [160,160]
                                    desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]
                                    # self.spin(21,0.4,0.1)

                                    self.sp("dashav",self.listdiv(actvel,80))
                                    self.sp("dashdv",self.listdiv(desvel,80))

                                    self.sp("act_vel",0,1)
                                    self.sp("des_vel",0,1)
                                    self.sp("act_vel",0,0)
                                    self.sp("des_vel",0,0)
                                    self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))

                                    self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))
                                else:
                                    
                                    self.sp("dashmeter",self.gp("dashmeter") + 30)
                                    self.wait("dashrem",2)
                                    # cm.setcond("playercam","shake",6)
                                    actmult = [160,160]
                                    actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
                                    desmult = [160,160]
                                    desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]

                                    if actmult == [0,0]:
                                        actmult = [160,50]
                                        desmult = [160,50]
                                    # self.spin(21,0.4,0.1)

                                    self.sp("dashav",self.listdiv(actvel,80))
                                    self.sp("dashdv",self.listdiv(desvel,80))

                                    self.sp("act_vel",0,1)
                                    self.sp("des_vel",0,1)
                                    self.sp("act_vel",0,0)
                                    self.sp("des_vel",0,0)
                                    self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
                                    self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))
                        if self.gp("target").info["type"] == "goal":
                            if not self.isthere("show-score"):
                                # self.print(    "attempt" + str(self.timesdone) + ":" + um.elements["Speed-timer"]["text"]     )
                                self.storedscore = "attempt" + " "+str(self.timesdone) +  " =" + " "+ um.elements["Speed-timer"]["text"] 
                                self.scores[self.timesdone] = float(um.elements["Speed-timer"]["text"])
                                self.timesdone += 1

                                self.highest = 10000000000000000
                                self.highestatt = 0
                                for i in self.scores.keys():
                                    if self.scores[i] < self.highest:
                                        self.highest = self.scores[i]
                                        self.highestatt = i
                                # print(self.highestatt)

                                self.wait("show-score",7)
                            self.sp("homing",0)
                        if self.gp("target").info["type"] in ["omnispring","turret"]:
                            if self.key["secondary"]:
                                self.sp("des_vel",[0,0])
                                self.sp("act_vel",[0,0])
                                self.sp("wantime",0.5)
                                om.objects["player"]["pos"] = self.gp("HOLD")
                            else:
                                self.sp("dashmeter",self.gp("dashmeter") + 30)
                                self.sp("jumpable",1)
                                self.sp("homing",0)
                                self.wait("bouncerem",3)
                                # cm.setcond("playercam","shake",6)
                                actmult = [150,150]
                                actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
                                desmult = [150,150]
                                desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]

                                if actmult == [0,0]:
                                    actmult = [160,50]
                                    desmult = [160,50]
                                # self.spin(23,0.4,0.1)

                                self.sp("dashav",self.listdiv(actvel,16))
                                self.sp("dashdv",self.listdiv(desvel,16))

                                self.sp("act_vel",0,1)
                                self.sp("des_vel",0,1)
                                self.sp("act_vel",0,0)
                                self.sp("des_vel",0,0)
                                self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
                                self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))

                        

                        if self.gp("target").info["type"] in ["easybot"]:
                            if self.key["secondary"]:
                                self.sp("des_vel",[0,0])
                                self.sp("act_vel",[0,0])
                                self.sp("wantime",0.5)
                                
                                om.objects["player"]["pos"] = self.gp("target").info["pos"]
                            else:

                                self.sp("dashmeter",self.gp("dashmeter") + 30)

                                om.set_value(self.gp("target").name,"HP",om.get_value(self.gp("target").name,"HP") - 200)
                                om.set_value(self.gp("target").name,"flashtimer",1)
                                self.spin(14,1,spindec=0.3)
                                self.sp("jumpable",1)
                                self.sp("homing",0)
                                self.wait("bouncerem",3)
                                # cm.setcond("playercam","shake",6)
                                actmult = [150,150]
                                actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
                                desmult = [150,150]
                                desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]

                                if actmult == [0,0]:
                                    actmult = [160,50]
                                    desmult = [160,50]
                                # self.spin(23,0.4,0.1)

                                self.sp("dashav",self.listdiv(actvel,16))
                                self.sp("dashdv",self.listdiv(desvel,16))

                                self.sp("act_vel",0,1)
                                self.sp("des_vel",0,1)
                                self.sp("act_vel",0,0)
                                self.sp("des_vel",0,0)
                                self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
                                self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))

                        if self.gp("target").info["type"] in ["HURT:biglaser"]:
                            if self.gp("target").name in om.objects.keys():
                                om.set_value(self.gp("target").name,"HP",om.get_value(self.gp("target").name,"HP") - 30)
                                om.set_value(self.gp("target").name,"flashtimer",1)
                                self.spin(14,1,spindec=0.3)
                                self.sp("jumpable",1)
                                self.sp("homing",0)
                                self.wait("bouncerem",3)
                                # cm.setcond("playercam","shake",6)
                                actmult = [150,150]
                                actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
                                desmult = [150,150]
                                desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]

                                if actmult == [0,0]:
                                    actmult = [160,50]
                                    desmult = [160,50]
                                # self.spin(23,0.4,0.1)

                                self.sp("dashav",self.listdiv(actvel,16))
                                self.sp("dashdv",self.listdiv(desvel,16))

                                self.sp("act_vel",0,1)
                                self.sp("des_vel",0,1)
                                self.sp("act_vel",0,0)
                                self.sp("des_vel",0,0)
                                self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
                                self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))


                        if self.gp("target").info["type"] in ["rocket"]:
                            if self.key["secondary"] and not self.gp("exithm"):
                                self.sp("des_vel",[0,0])
                                self.sp("act_vel",[0,0])
                                self.sp("wantime",0.5)
                                om.objects["player"]["pos"] = self.gp("target").info["pos"]
                            else:
                                
                                self.sp("exithm",0)
                                self.sp("dashmeter",self.gp("dashmeter") + 70)
                                self.sp("jumpable",1)
                                self.sp("homing",0)
                                self.wait("bouncerem",3)
                                # cm.setcond("playercam","shake",6)
                                actmult = [150,150]
                                # actvel = [  axis[0] * actmult[0], axis[1] * actmult[1]]
                                actvel = [0,0]
                                desmult = [150,150]
                                desvel = [  axis[0] * desmult[0], axis[1] * desmult[1]]
                                # om.set_value(self.gp("target").name,"exp",1)
                                actvel[0] = math.cos(self.gp("target").info["rot"]/180 * math.pi) * 12 * om.get_value(self.gp("target").name,"vel") + (axis[0]*50)
                                actvel[1] = math.sin(self.gp("target").info["rot"]/180 * math.pi) * 12 * om.get_value(self.gp("target").name,"vel") + (axis[1]*50)

                                if self.gp("exithm"):
                                    actvel[0] /= 3
                                    actvel[1] /= 3

                                if actmult == [0,0]:
                                    actmult = [160,50]
                                    desmult = [160,50]
                                # self.spin(23,0.4,0.1)

                                self.sp("dashav",self.listdiv(actvel,16))
                                self.sp("dashdv",self.listdiv(desvel,16))

                                self.sp("act_vel",0,1)
                                self.sp("des_vel",0,1)
                                self.sp("act_vel",0,0)
                                self.sp("des_vel",0,0)
                                self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
                                self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))



                    if self.isthere("show-score"):
                        um.state = "vic"
                        um.addrect([6000,6000],["vic"],[(-0.5 + 0.02) - 0.5,0.8],"atnum",color=(0,0,0),fromstart=0,alpha = 200)
                        um.addtext("Victory-lap","",univars.defont,[0,0],univars.theme["accent"],100,"vic")
                        um.elements["Victory-lap"]["text"] = self.storedscore + "    " + str(int(self.timers["show-score"]/60) + 1) + "\n\n"  + f"Lowest - time:{self.highest}  on-attempt:{self.highestatt}"

                    


                    


                    #jumping
                    if self.key["jump"]:
                        self.sp("fss",16)
                        # self.sp("desmooth",5)
                        if self.gp("jumpable"):
                            self.sp("jumpable",0)
                            self.deltimer("doublejumpcd")
                            self.wait("doublejumpcd",0.2)
                            self.sp("candj",1)
                            #normal
                            self.lastframejumped = 1
                            self.sp("jumpable",False)
                            self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
                            self.sp("mode","in-air")



                            #Wall jumping
                            # if self.key["y"] > 0.4:
                            a = 200
                            # else:
                            # 	a = 120
                            if self.gp("leftwall") and not  len(collision["botmid"]["inst"]) > 0:
                                self.sp("dashmeter",self.gp("dashmeter") + (30 * self.dt))
                                self.deltimer("rightjump")
                                self.wait("leftjump",0.1)
                                
                                self.spin(-7 ,1,spindec = 0)
                                self.sp("jumpable",False)
                                self.sp("des_vel",[ self.key["x"] * self.gp("machspeed")  , a     ])
                                self.sp("act_vel",[  120 , self.gp("act_vel")[1]     ])
                                self.sp("dashmeter",self.gp("dashmeter") + 15)
                                self.sp("mode","in-air")
                            if self.gp("rightwall") and not  len(collision["botmid"]["inst"]) > 0:
                                self.sp("dashmeter",self.gp("dashmeter") + (30 * self.dt))
                                self.deltimer("leftjump")
                                
                                self.spin(7 ,1,spindec = 0)
                                self.wait("rightjump",0.1)
                                self.sp("jumpable",False)
                                self.sp("des_vel",[  self.key["x"] * self.gp("machspeed") , a     ])
                                self.sp("act_vel",[  -120 , self.gp("act_vel")[1]     ])
                                self.sp("dashmeter",self.gp("dashmeter") + 15)
                                self.sp("mode","in-air")

                    else:
                        self.lastframejumped = 0
                        self.sp("fss",8)

                        if self.gp("leftwall") or self.gp("rightwall"):
                            self.sp("des_vel",[self.gp("des_vel")[0],self.key["y"] * 200])
                            # if self.gp("dashmeter") < 200:
                            # 	if abs(self.key["y"]) > 0:
                            # 		self.sp("dashmeter",self.gp("dashmeter")+ (self.dt * 3 * abs(self.key["y"])))

                        if not ground:
                            if self.gp("leftwall"):
                                self.sp("desrot",-90)
                                self.sp("desmooth",3)

                            elif self.gp("rightwall"):
                                self.sp("desrot",90)
                                self.sp("desmooth",3)

                        # else:
                        # 	if not ground:


                    #tilt when moving
                    if not ground:
                        if not self.gp("leftwall") and not self.gp("rightwall"):
                            if abs(self.key["x"]) > 0:
                                if not self.isthere("rotate"):
                                    # if not abs()
                                    
                                    if not self.bailable:
                                        self.sp("rotoffset",self.rotlerp(self.gp("rotoffset"),0,5))
                                        self.sp("desrot",self.rotlerp(self.gp("desrot"),self.gp("act_vel")[0]/4,5) )


                    

                    # #slingshot
                    # if self.key["secondary"] and self.gp("dashmeter") > 0 and not ground:
                    # 	self.sp("slinging",1)
                    # 	self.sp("wantime",0.1)
                    # 	self.sp("dashmeter",self.gp("dashmeter") - self.dt/10)
                    # 	om.speed = self.unilerp(om.speed,0.1,5,roundto=2,useigt=0) 
                    # 	self.sp("slomorot",vecaxis.angle)
                    # else:
                    # 	self.sp("slinging",0)


                        if self.gp("lastframeswing"):
                            self.sp("dashmeter",self.gp("dashmeter") - 10)
                            self.wait("dashrem",2)
                            # cm.setcond("playercam","shake",6)
                            actmult = [190,190]
                            actvel = [  axis[0] * actmult[0] , axis[1] * actmult[1] ]
                            desmult = [190,190]
                            desvel = [  axis[0] * desmult[0] , axis[1] * desmult[1] ]
                            # self.spin(20,0.7,0.1)

                            self.sp("dashav",self.listdiv(actvel,40))
                            self.sp("dashdv",self.listdiv(desvel,40))

                            self.sp("act_vel",0,1)
                            self.sp("des_vel",0,1)
                            self.sp("act_vel",0,0)
                            self.sp("des_vel",0,0)
                            self.sp("act_vel",self.listadd((self.gp("act_vel"),actvel)))
                            self.sp("des_vel",self.listadd((self.gp("des_vel"),desvel)))	

                    
                    self.sp("lastframeswing",self.gp("slinging"))	

                    

                    
                                
                    
                    if self.isthere("dashrem"):
                        # print(self.gp("dashav"))
                        if not type(self.gp("dashav")) == list:
                            self.sp("dashav",[0,0])

                        self.unilerp(self.gp("dashav"),[0,0],3)
                        self.unilerp(self.gp("dashdv"),[0,0],3)
                        self.sp("act_vel",self.listadd((self.gp("act_vel"),self.gp("dashav"))))
                        self.sp("des_vel",self.listadd((self.gp("des_vel"),self.gp("dashdv"))))
                        
                        # cm.setcond("playercam","shake",0)

                    if self.isthere("bouncerem"):
                        # if not type(self.gp("dashav")) == list:
                        # 	self.sp("dashav",[0,0])
                        # print(self.gp("dashav"))
                        self.sp("dashav",self.unilerp(self.gp("dashav"),[0,0],7))
                        self.sp("dashdv",self.unilerp(self.gp("dashdv"),[0,0],7))
                        self.sp("act_vel",self.listadd((self.gp("act_vel"),self.gp("dashav"))))
                        self.sp("des_vel",self.listadd((self.gp("des_vel"),self.gp("dashdv"))))
                        
                        # cm.setcond("playercam","shake",0)



                    if ground:
                            # self.print("AAAHHH")
                        self.killtimer("rotate")
                        self.sp("rotoffset",0)
                        if not self.lastframejumped and not self.gp("lastframewall"):
                            
                            if not self.bailable:
                                self.sp("desrot",0)
                            self.sp("mode","grounded")
                            self.sp("jumpable",True)
                            self.sp("onboard",True)
                            self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
                            self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
                            om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32
                        else:
                            self.lastframejumped = 0


                
                    
                    if collision["topmid"]["inst"] and not collision["midmid"]["inst"]:
                        self.sp("act_vel",[   self.gp("act_vel")[0] * 1  , -10 ])
                        om.objects["player"]["pos"][1] =  collision["topmid"]["inst"][0].realpos[1] + 40
                        # self.sp("des_vel",[  self.gp("des_vel")[0] * 1   ,  abs(self.gp("des_vel")[1]) * -1 ])
                        self.sp("jumpable",False)

                    
                    #water skid
                    if  800 > om.objects["player"]["pos"][1] > 700 and not (self.key["jump"] and self.gp("act_vel")[1] >= 0) :
                        if abs(self.gp("act_vel")[0]) >= 120:
                            if self.gp("act_vel")[0] > 100:
                                parts = [om.objects["player"]["pos"][0] -5,om.objects["player"]["pos"][1] + 9]
                            else:
                                parts = [om.objects["player"]["pos"][0] -5,om.objects["player"]["pos"][1] + 9]
                            vel = [self.gp("act_vel")[0]/self.dim * 4,4]
                            pm.particlespawnbluprint(parts,"water",initvel= vel)
                            self.sp("act_vel",[   self.gp("act_vel")[0] , 0  ]  ) 
                            self.sp("des_vel",[   self.gp("des_vel")[0] , 0  ]  ) 
                            om.objects["player"]["pos"][1] = 768

                            self.sp("jumpable",1)
                            self.sp("candj",0)


            else:
                #RAIL
                ret_dict_rail = state_rail.main(self,collisionbox,rail,collisionboxtype)
                
                railrot = ret_dict_rail["railrot"]
                raildir = ret_dict_rail["raildir"]
                
                




            for ty in ["HURT:laser"]:
                if ty in [ i.info["type"] for i in smallcollisionbox["obj"]]:
                    if self.gp("homing") == 0:
                        if not self.isthere("inv"):
                            self.wait("BAIL",0.5)
                        
                        # self.sp("act_vel",[0,0])
                        # self.sp("des_vel",[0,0])

                    

            #UPDATE POSITIONS AND ROTATIONS
            if not (collision["topmid"]["inst"] and collision["botmid"]["inst"] and collision["midright"]["inst"] and collision["midleft"]["inst"] ) or rail:
                self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
                om.translate(self,"player",self.gp("act_vel"),usedt=1)
                if self.isthere("BAIL"):
                    self.sp("desrot",90)
                
                if self.isthere("trick3"):
                    if self.key["x"] > 0:
                        self.sp("desrot",-180)
                    else:
                        self.sp("desrot",180)

                # if round(self.gp("desrot")) == 270:
                # 	self.sp("desrot",-90)
                    # print(self.gp("desrot"))
                # if self.gp("desrot") < 0:
                # 	self.sp("desrot",0 - self.gp("desrot"))
                if self.isthere("rotate"):
                    self.sp("rotoffset",self.gp("rotoffset") + (self.gp("rot")*self.dt) )

                    self.sp("rot",self.gp("rot") - (self.valsign(self.gp("rot")) * abs(self.gp("rotdes") * self.dt)       ) )
                    
                # om.objects["playersprite"]["rot"] = a
                if abs(self.gp("unboundrot")) > 180 and abs(self.gp("rotoffset")) > 180 :
                    min_value = -180
                    max_value = 180
                    range_size = max_value - min_value

                    self.sp("rotoffset",((self.gp("rotoffset") - min_value) % range_size) + min_value)
                    self.sp("unboundrot",((self.gp("unboundrot") - min_value) % range_size) + min_value)


                if self.gp("slinging"):
                    if abs(self.gp("unboundrot")) > 180 :
                        min_value = -180
                        max_value = 180
                        range_size = max_value - min_value

                        self.sp("unboundrot",((self.gp("unboundrot") - min_value) % range_size) + min_value)
                    

                # min_value = -180
                # max_value = 180
                # range_size = max_value - min_value
                # self.sp("rotoffset", ((self.gp("rotoffset") - min_value) % range_size) + min_value)
                # 	self.sp("rotoffset",self.gp("rotoffset") - 360)
                # if self.gp("rotoffset") < -180:
                # 	self.sp("rotoffset",self.gp("rotoffset") + 360)


                rot = self.gp("unboundrot")
                if not self.gp("slinging"):
                    dest = self.gp("desrot")+ self.gp("rotoffset")
                else:
                    dest = self.gp("slomorot")

                d1 = abs(rot - (dest - 360))
                d2 = abs(rot - (dest + 360))
                d3 = abs(rot - (dest + 0))
                
                destinations = {d1:dest-360,d2:dest+360,d3:dest}


                dest = destinations[min([d1,d2,d3])]


                # if path == d1: 
                # dest = fm.frame* 30
                # print(dest)
                # om.objects["playersprite"]["rot"]   +=  30
                sm = 5
                
                if self.isthere("trick3"):
                    sm = 3
                # om.objects["playersprite"]["rot"]   =  
                if not self.gp("slinging"):
                    self.sp("unboundrot",self.unilerp(rot,dest,sm,roundto=2))
                    a = self.gp("unboundrot")
                    min_value = -180
                    max_value = 180
                    range_size = max_value - min_value
                    a = ((a - min_value) % range_size) + min_value
                    if -5 < a < 5:
                        om.objects["playersprite"]["rot"]  =  0
                    else:
                        om.objects["playersprite"]["rot"] = a
                else:
                    self.sp("unboundrot",self.unilerp(rot,dest,sm,roundto=2,useigt=0))
                    a = self.gp("unboundrot")
                    min_value = -180
                    max_value = 180
                    range_size = max_value - min_value
                    a = ((a - min_value) % range_size) + min_value
                    om.objects["playersprite"]["rot"] = a
                

                    
            
            

                if not rail:
                    #prevent no-clip
                    if self.gp("mode") == "grounded":
                        if "ground" in collisionlisttype:
                            self.sp("des_vel",[  self.gp("des_vel")[0]    ,    0   ])
                            self.sp("act_vel",[  self.gp("act_vel")[0]    ,    0   ])
                            om.objects["player"]["pos"][1] = instlist[0].realpos[1] - 32

                    if not self.gp("onboard"):
                        if om.get_value("skateboard","fallvalue")< 20:
                            om.set_value("skateboard","fallvalue",om.get_value("skateboard","fallvalue") - 2* self.dt)
                        om.objects["skateboard"]["pos"] = [om.objects["player"]["pos"][0],om.objects["player"]["pos"][1] - 0]
                        om.translate(self,"skateboard",[0,om.get_value("skateboard","fallvalue")])
                    else:
                        om.set_value("skateboard","fallvalue",5)

        else:

            if self.gp("slantdir") == "r":
                if self.lastdirslant == "l":
                    om.translate(self,"player",[100,40])
                    if abs(self.gp("act_vel",0)) > 30:
                        self.sp("act_vel",[self.gp("act_vel",0) + (200) ,self.gp("act_vel",0) + (110) ])
                if self.lastdirslant == "r":
                    om.translate(self,"player",[-100,0])
            if self.gp("slantdir") == "l":
                if self.lastdirslant == "r":
                    if abs(self.gp("act_vel",0)) > 30:
                        self.sp("act_vel",[self.gp("act_vel",0) - (200) ,self.gp("act_vel",0) + (110) ])
                    om.translate(self,"player",[-100,40])
                if self.lastdirslant == "l":
                    om.translate(self,"player",[300,0])
    else:                                                                                                                               
        
        
        self.sp("candj",1)
        self.sp("jumpable",1)
        if "slantr" in collisionboxtype:
            self.sp("slantdir","r")
            if not slanted == self.lastframeslanted:
                # if not ground:
                index = collisionboxtype.index("slantr")
                om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] - 20,collisionbox["inst"][index].realpos[1] - 20]
                self.sp("act_vel",[  self.gp("act_vel")[0]    ,    self.gp("act_vel")[0]   ])
                self.sp("des_vel",[  self.gp("des_vel")[0]    ,    self.gp("des_vel")[0]   ])
                    # else:
                    # 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
            else:
                if abs(self.key["x"]) > 0:
                    self.sp("des_vel",[         self.key["x"] * 70             ,    self.gp("des_vel")[1]   ])
                else:
                    self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
                self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
                if not self.key["jump"]:
                    self.sp("act_vel",[self.gp("act_vel")[0],self.gp("act_vel")[0]])
                else:
                    self.sp("act_vel",[self.gp("act_vel")[0],abs(self.gp("act_vel")[1])])
                om.translate(self,"player", self.gp("act_vel"),usedt=1)
                self.sp("desrot",45) 
        else:
            
            self.sp("slantdir","l")
            if not slanted == self.lastframeslanted:
                index = collisionboxtype.index("slantl")
                # if not ground2:
                om.objects["player"]["pos"] = [collisionbox["inst"][index].realpos[0] +16,collisionbox["inst"][index].realpos[1] -20]
                self.sp("act_vel",[  self.gp("act_vel")[0] * 1.1    ,    -1 * self.gp("act_vel")[0] * 1.1   ])
                self.sp("des_vel",[  self.gp("des_vel")[0] * 1.1    ,    -1 * self.gp("des_vel")[0] * 1.1   ])
                    # else:
                    # 	om.objects["player"]["pos"] = [collisionbox["inst"][0].realpos[0] +16,collisionbox["inst"][0].realpos[1] +16]
            else:
                if abs(self.key["x"]) > 0:
                    self.sp("des_vel",[         self.key["x"] * 70             ,    self.gp("des_vel")[1]   ])
                else:
                    self.sp("des_vel",[  0    ,    self.gp("des_vel")[1]   ])
                self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
                if not self.key["jump"]:
                    self.sp("act_vel",[self.gp("act_vel")[0],-1 * self.gp("act_vel")[0]])
                else:
                    self.sp("act_vel",[self.gp("act_vel")[0], self.gp("act_vel")[1]])
                om.translate(self,"player", self.gp("act_vel"),usedt=1)
                self.sp("desrot",-45)








        if -5 < self.gp("desrot") < 5:
            om.objects["playersprite"]["rot"]  =  0
        else:
            om.objects["playersprite"]["rot"]  =  self.unilerp(om.objects["playersprite"]["rot"],self.gp("desrot"),5,roundto=2) 

        if self.key["jump"]:
            self.sp("fss",16)
            self.sp("desmooth",5)

            #normal
            self.sp("jumpable",False)
            self.sp("des_vel",[  self.gp("des_vel")[0] , 150     ])
            self.sp("mode","in-air")
            self.unilerp(self.gp("act_vel"),self.gp("des_vel"),8,roundto = 2)
            om.translate(self,"player",[0,self.gp("act_vel")[1]],usedt=1)
            
            
            
    return {"railrot":railrot,"raildir":raildir}
