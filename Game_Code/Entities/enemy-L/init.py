import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import random
import Game_Code.Utils.Entities as Entities



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

def main(self,id,info):
    # om.objects["sizen"] = 0.5
    # om.rescale(id,sizen=[0.5,0.5])
    om.objects[id]["sizen"] = [0.8,0.8]

    om.set_value(id,"master_pos",info["pos"])
    om.set_value(id,"canhome",1)
    om.set_value(id,"state","idle")
    om.set_value(id,"HP",100)
    om.set_value(id,"des_vel",[0,0])
    om.set_value(id,"act_vel",[0,0])
    om.set_value(id,"rotspeed",random.randint(30,60))
    pl0 = random.randint(15,40)
    om.set_value(id,"pl0",pl0)
    om.set_value(id,"side",random.randint(0,1))
    om.set_value(id,"pl1",pl0 + random.randint(40,80) )
    om.set_value(id,"level",0 )
    om.set_value(id,"speed",random.randint(2,10))
    om.set_value(id,"superspeed",random.randint(5,5))
    om.set_value(id,"yfac",random.randint(-100,0))
    om.set_value(id,"inner_spacing",random.randint(200,200))
    om.set_value(id,"outer_spacing",om.get_value(id,"spacing") + random.randint(20,70))
    om.set_value(id,"orbitrot",0)
    om.set_value(id,"lasttogoto",info["pos"])
    om.set_value(id,"act_vel",[0,0])
    om.set_value(id,"vel",[0,0])
    om.set_value(id,"tarvel",[0,0])
    om.set_value(id,"clipspeed",5)
    om.set_value(id,"timer",5)
    om.set_value(id,"maxtimer",random.randint(10 * 2,15 * 2))
    om.set_value(id,"flashtimer",0)

    if self.publicvariables["mood"] == "night":
        om.lighttoenemy(id,"l1",color=(255,0,255),colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=20)
    elif self.publicvariables["mood"] == "sunset":
        om.lighttoenemy(id,"l1",color=(255,0,255),colorinc=(0,0,0),nits=10,sizeinc=5,size=20,alphadec=3,alpha=10)


    Entities.createhpbar(id,1,[0,30],self=self)
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)
