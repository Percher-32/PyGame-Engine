import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math





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

def main(self,collisionlisttype,selected_obj,axis,ground):
    """
    SELF.GP("HOMING"):
        0 - NONE
        1 - GOING TO TARGET
        2 - ON TARGET
    """
    
    
    
    
    #make sure homing = 0 if 
    if not self.gp("homing") == 0:
        if "ground" in collisionlisttype:							
            self.sp("homing",0)
            self.key["secondary"] = 0




    #INITIATE HOMING ATTACK
    if not self.gp("homing") == 1:
        if self.key["secondary"] and not self.key["trick"]:
            if not selected_obj == None:
                if not self.isthere("homecooldown"):
                    if not self.lastkey["secondary"]:
                        self.wait("homecooldown",0.2)
                        self.sp("homing",1)
                        self.sp("target",selected_obj)
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