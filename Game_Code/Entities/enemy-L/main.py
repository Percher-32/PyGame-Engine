import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import pygame
import random
from functools import partial
import Game_Code.Utils.Entities as Entities





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




def get(var_name,index = None):
    if index == None:
        return om.get_value(id,var_name)
    else:
        return om.get_value(id,var_name)[index]
    
def set(var_name,to,index = None):
    if index == None:
        return om.set_value(id,var_name,to)
    else:
        newlist = get(var_name)
        listtype = type(newlist)
        newlist = list(newlist)
        newlist[index] = to
        
        newlist = listtype(newlist)
        return om.set_value(id,var_name,newlist)
    




def skated(id):
    om.set_value(id,"knock",4)
    om.set_value(id,"yeetvel",[self.key["x"] * 20,self.key["y"] * 10])
    
def hit(id):
    om.set_value(id,"knock",3)
    om.set_value(id,"yeetvel",[self.key["x"] * 20,self.key["y"] * 20])
    






def logic_movement():
    """
        moves the entity
    """
    if not self.isthere("#Throwing" + str(id)):      
        om.translate(self,id,[get("act_vel",0)*st * om.speed,get("act_vel",1)*st * om.speed],usedt=0)

        rotvec = pygame.Vector2()
        set("orbitrot",om.get_value(id,"orbitrot") + om.get_value(id,"rotspeed")/20)
        rotvec.from_polar((om.get_value(id,"spacing"),om.get_value(id,"orbitrot")))


        playerpos = om.objects["player"]["pos"]
        togoto=  [ playerpos[0] + (self.gp("act_vel")[0]*get("superspeed")) + rotvec.x  - (get("side") * (self.gp("act_vel")[0] + 20) * 3), playerpos[1]  - (self.gp("act_vel")[1]*get("superspeed")) + rotvec.y   ]
        ltogoto = get("lasttogoto")
        newvel = [ (togoto[0] - info["pos"][0])/5 , (togoto[1] - info["pos"][1])/-5    ]

        set("des_vel",newvel)
        set("lasttogoto",togoto)

def logic_throwing():
    """
        Throwing logic
    """
    if self.isthere("#Throwing" + str(id)):
        if not id + "[obj-light]"+ "FIREBALL" in om.lights :
            om.lighttoenemy(id,"FIREBALL",color=(255,0,100),colorinc=(0,0,0),nits=20,sizeinc=5,size=30,alphadec=3,alpha=50)
            
        om.rotate(self,id,20)
        cm.setcond("playercam","shake",10)
        pm.particlespawnbluprint(self.listadd((om.objects[id]["pos"],(-32,-32))),"exp")

        set("fireball",1)
        set("canhome",0)
        if not get("throwvel") == 0:
            # print(self.gp("throwaxis"))
            set("act_vel",get("throwvel"))
            set("des_vel",get("throwvel"))
            om.translate(self,id,[get("act_vel",0)*st * om.speed,get("act_vel",1)*st * om.speed],usedt=0)
            set("HP",get("HP") - (10*st)/10)



            set("throwvel",[get("throwvel")[0]/1.0000005,get("throwvel")[1]/1.0000005 - 1])
        


        col = om.collide(id,0,cam,extrax=500,extray=500)["obj"]
        if not None in col:
            for obj in col:
                om.set_value(obj.name,"flashtimer",2)
                om.set_value(obj.name,"HP",om.get_value(obj.name,"HP") - (1))
    else:
        if id + "[obj-light]"+ "FIREBALL" in om.lights :
            om.lights.pop(id + "[obj-light]"+ "FIREBALL")
        set("fireball",0)
        set("canhome",1)
        om.objects[id]["rot"] = 0
        
def logic_laser():
    """
         laser logic
    """
    playervec = pygame.Vector2(om.objects["player"]["pos"])
    selfpos =  pygame.Vector2(info["pos"])


    vectoplayer = playervec-selfpos

    set("timer",get("timer") - (st * self.gp("wantime"))/10)
    if  abs(vectoplayer.length()) > 300:
        if get("timer") < 0 :
            rot = vectoplayer.angle * -1 + random.randint(-1 * abs(int(self.gp("des_vel")[0]/100)),1 * abs(int(self.gp("des_vel")[0]/100)))
            self.spawnlaser(info["pos"],40,rot,id,3,extraspeed=self.listdiv(self.gp("act_vel"),2))
            set("timer",get("maxtimer"))

def logic_flash():
    """
        flash timer logic
    """
    if get("flashtimer") > 0:
        set("flashtimer",get("flashtimer") - (1*st)/40)
        if round(get("flashtimer") * 5)%2 == 0:
            om.objects[id]["sn"] = 1
        else:
            om.objects[id]["sn"] = 0
    else:
        om.objects[id]["sn"] = 0

def logic_knock():
    """
        logic for entoty to be knocked back
    """
    if get("knock") > 0:
        set("knock",get("knock") - (1*st)/40)
        set("act_vel",  self.listadd((   self.listdiv(get("yeetvel"),1/st)   ,get("act_vel")))    )
        set("des_vel",  self.listadd((   self.listdiv(get("yeetvel"),1/st)     ,get("des_vel")))       )

def logic_vel_update():
    """
        move act_vel closer to des_vel by using var:speed
    """
    set("act_vel",self.customunilerp(get("act_vel"),get("des_vel"),get("speed"),om.speed,st))
    
def logic_hp():
    """
        kills entity if hp is below 0
    """
    if get("HP") <= 0:
        om.removeid(id)
    
def logic_water():
    if info["pos"][1] > 64 * 10:
            info["pos"][1] = 64 * 10
                     
def logic_damage():
    """
        allows the entity to be damaged by player
    """
    Entities.damageable(id,20,functhrow=partial(skated,id = id)  ,func=partial(hit,id = id)   , self=self)

def logic_out_of_bounds():
    if id in om.objects.keys():
        if not univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < 1600:
            if not self.isthere("#Throwing" + str(id)):
                om.objects[id]["pos"] = get("master_pos")
            else:
                om.removeid(id)







    
def main(self,id,info,st):
    """
        var table:

            act_vel     : velocity
            des_vel     : desired - velocity
            speed       : smoothing from act_vel to des_vel
            orbitrot    : angle its orbiting at
            rotspeed    : speed at which orbitrot changes
            superspeed  : how much the player velocity changes desired desired position
            lasttogoto  : last frames desired position
            knock       : timer when its ticking the enemy gets knocked back by yeetvel
            yeetvel     : how much the enemy get s knocked back by
            
            
    """
    
    if "player" in om.values.keys():
        if id in om.values.keys() and "act_vel" in om.values["player"].keys():
            in_range = univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < 1600 
            if in_range:
                logic_water()
                
                logic_laser()
                
                logic_movement()
                
                logic_damage()

                logic_flash()

                logic_knock()
                
                logic_throwing()
                
                logic_vel_update()

                logic_hp()
            else:
                logic_out_of_bounds()


                
                
                
                
                

self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)