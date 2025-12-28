import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import pygame
import random





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


def main(self,id,info,st):
    if "player" in om.values.keys():
        if id in om.values.keys() and "act_vel" in om.values["player"].keys():
            def skated():
                om.set_value(id,"knock",4)
                om.set_value(id,"yeetvel",[self.key["x"] * 20,self.key["y"] * 10])
            def hit():
                om.set_value(id,"knock",3)
                om.set_value(id,"yeetvel",[self.key["x"] * 20,self.key["y"] * 20])
            self.damageable(id,20,functhrow=skated,func=hit)

            # print(om.get_value(id,"master_pos"),om.objects[id]["pos"])
            if univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < 1600:
                if om.objects[id]["pos"][1] > 64 * 10:
                    om.objects[id]["pos"][1] = 64 * 10


                om.translate(self,id,[om.get_value(id,"act_vel")[0]*st * om.speed,om.get_value(id,"act_vel")[1]*st * om.speed],usedt=0)

                rotvec = pygame.Vector2()
                om.set_value(id,"orbitrot",om.get_value(id,"orbitrot") + om.get_value(id,"rotspeed")/20)
                rotvec.from_polar((om.get_value(id,"spacing"),om.get_value(id,"orbitrot")))
                # rotvec.y -= om.get_value(id,"spacing")/2
                # rotvec.y *= 0.3
                # rotvec.x *= 1.4
                # rotvec.y = abs(rotvec.y)* -1 * om.get_value(id,"yfac")/100
                # rotvec.y -=  om.get_value(id,"yfac")
                # rotvec = pygame.Vector2((0,0))


                playerpos = om.objects["player"]["pos"]
                togoto=  [ playerpos[0] + (self.gp("act_vel")[0]*om.get_value(id,"superspeed")) + rotvec.x  - (om.get_value(id,"side") * (self.gp("act_vel")[0] + 20) * 3), playerpos[1]  - (self.gp("act_vel")[1]*om.get_value(id,"superspeed")) + rotvec.y   ]
                ltogoto = om.get_value(id,"lasttogoto")
                # togoto[0] /= 2
                # togoto[1] /= 2
                # togoto[0]
                newvel = [ (togoto[0] - info["pos"][0])/5 , (togoto[1] - info["pos"][1])/-5    ]
                # togoto=[0,0]



                om.set_value(id,"des_vel",newvel)


                om.set_value(id,"lasttogoto",togoto)




                if self.isthere("#Throwing" + str(id)):
                    if not id + "[obj-light]"+ "FIREBALL" in om.lights :
                        om.lighttoenemy(id,"FIREBALL",color=(255,0,100),colorinc=(0,0,0),nits=20,sizeinc=5,size=30,alphadec=3,alpha=50)

                    om.set_value(id,"fireball",1)
                    om.set_value(id,"canhome",0)
                    if not om.get_value(id,"throwvel") == 0:
                        # print(self.gp("throwaxis"))
                        om.set_value(id,"act_vel",om.get_value(id,"throwvel"))
                        om.set_value(id,"HP",om.get_value(id,"HP") - (1*st)/10)
                        om.set_value(id,"des_vel",om.get_value(id,"throwvel"))



                        om.set_value(id,"throwvel",[om.get_value(id,"throwvel")[0]/1.0000005,om.get_value(id,"throwvel")[1]/1.0000005 - 1])


                    col = om.collide(id,0,cam,extrax=500,extray=500)["obj"]
                    if not None in col:
                        for obj in col:
                            om.set_value(obj.name,"flashtimer",2)
                            om.set_value(obj.name,"HP",om.get_value(obj.name,"HP") - (1))



                else:
                    if id + "[obj-light]"+ "FIREBALL" in om.lights :
                        om.lights.pop(id + "[obj-light]"+ "FIREBALL")
                    om.set_value(id,"fireball",0)
                    om.set_value(id,"canhome",1)
                    om.objects[id]["rot"] = 0

                    # if len(collide) > 0:
                    # 	om.set_value(id,"rotspeed",om.get_value(id,"rotspeed") * -1)


                # om.set_value(id,"HP",abs(math.sin(fm.frame/100) * 100))
                # if len(collide) > 0:
                # 	lt = om.get_value(id,"des_vel")

                # 	lt[0] *= -1
                # 	lt[1] *= -1
                # 	om.set_value(id,"act_vel",lt)
                # 	om.set_value(id,"des_vel",[0,0])
                # 	om.set_value(id,"throwvel",0)


                # om.translate(self,id,[0,20*st],usedt=0)

                if om.get_value(id,"gotoplay") > 0:
                    om.set_value(id,"gotoplay",om.get_value(id,"gotoplay") - (1*st)/40)
                    # om.set_value(id,"des_vel",[random.randint(-20,20),random.randint(-20,20)])
                    om.set_value(id,"act_vel",[3*(om.objects["player"]["pos"][0] + self.gp("act_vel")[0] - info["pos"][0]),
                                            -3*(om.objects["player"]["pos"][1]  + self.gp("act_vel")[1] -  info["pos"][1])])

                    om.set_value(id,"act_vel",[0,
                                            -0])

                    om.set_value(id,"des_vel",[0,
                                            -0])

                if om.get_value(id,"knock") > 0:
                    om.set_value(id,"knock",om.get_value(id,"knock") - (1*st)/40)
                    om.set_value(id,"act_vel",  self.listadd((   self.listdiv(om.get_value(id,"yeetvel"),1/st)   ,om.get_value(id,"act_vel")))    )
                    om.set_value(id,"des_vel",  self.listadd((   self.listdiv(om.get_value(id,"yeetvel"),1/st)     ,om.get_value(id,"des_vel")))       )
                    # if om.get_value(id,"act_vel")[0] + om.get_value(id,"act_vel")[1] < 2:
                    # 	om.set_value(id,"act_vel",om.get_value(id,"embedvel"))
                    # 	om.set_value(id,"des_vel",om.get_value(id,"embedvel"))
                    # 	om.set_value(id,"gotoplay",0)





                om.set_value(id,"act_vel",self.customunilerp(om.get_value(id,"act_vel"),om.get_value(id,"des_vel"),om.get_value(id,"speed"),om.speed,st))

                # a = pygame.math.Vector2( om.get_value(id,"act_vel"))
                # if a.length() > 0 and not self.isthere("#Throwing" + str(id)):
                # 	if om.get_value(id,"pl0") > pygame.math.Vector2( om.get_value(id,"act_vel")).length() < om.get_value(id,"pl1"):
                # 		a = pygame.math.Vector2( om.get_value(id,"act_vel"))
                # 		a.scale_to_length(self.valsign(a.length()) * om.get_value(id,"pl0"))
                # 		om.set_value(id,"act_vel",list(a))
                # 	elif om.get_value(id,"pl1") < pygame.math.Vector2( om.get_value(id,"act_vel")).length():
                # 		a = pygame.math.Vector2( om.get_value(id,"act_vel"))
                # 		a.scale_to_length(self.valsign(a.length()) * om.get_value(id,"pl1"))
                # 		om.set_value(id,"act_vel",list(a))

                if self.isthere("#Throwing" + str(id)):

                        om.rotate(self,id,20)
                        cm.setcond("playercam","shake",10)
                        pm.particlespawnbluprint(self.listadd((om.objects[id]["pos"],(-32,-32))),"exp")

                # if not None in col["obj"]:
                # 	if  True in [ om.get_value(obj.name,"fireball") for obj in col["obj"] ]:
                # 		om.set_value(id,"HP",om.get_value(id,"HP") - (1*st))
                # 		# pm.particlespawnbluprint(self.listadd((om.objects[id]["pos"],(-32,-32))),"exp")
                # 		om.set_value(id,"flashtimer",2)
                # 		om.objects[id]["sn"] = 1


                if om.get_value(id,"flashtimer") > 0:
                    om.set_value(id,"flashtimer",om.get_value(id,"flashtimer") - (1*st)/40)
                    if round(om.get_value(id,"flashtimer") * 5)%2 == 0:
                        om.objects[id]["sn"] = 1
                    else:
                        om.objects[id]["sn"] = 0
                else:
                    om.objects[id]["sn"] = 0








                om.set_value(id,"timer",om.get_value(id,"timer") - (st * self.gp("wantime"))/10)


                playervec = pygame.Vector2(om.objects["player"]["pos"])
                selfpos =  pygame.Vector2(info["pos"])


                vectoplayer = playervec-selfpos

                if  abs(vectoplayer.length()) > 300:
                    if om.get_value(id,"timer") < 0 :
                        rot = vectoplayer.angle * -1 + random.randint(-1 * abs(int(self.gp("des_vel")[0]/100)),1 * abs(int(self.gp("des_vel")[0]/100)))
                        self.spawnlaser(om.objects[id]["pos"],40,rot,id,3,extraspeed=self.listdiv(om.get_value("player","act_vel"),2))
                        om.set_value(id,"timer",om.get_value(id,"maxtimer"))









                if om.get_value(id,"HP") <= 0:
                    om.removeid(id)
                    # if self.gp("target") == id:


            else:
                om.objects[id]["pos"] = om.get_value(id,"master_pos")
                
                
                
                
                

self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)