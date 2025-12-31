import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
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
    set_all()
    if not "master_pos" in om.values[id]:
        set("master_pos",info["pos"])
    
    om.objects[id]["rendercond"] = 1
    Entities.createhpbar(id,1,[0,30],self)
    
    
def set_all():
    set("HP",100)
    set("act_vel",[0,0])
    set("des_vel",[0,0])
    set("canhome",True)
    set("down_vel",0)
    set("ground",0)
    set("yeet_timer",0)
    set("last_frame_ground",0)
    set("slope",0)
    set("knock_back",[0,0])
    set("stunned",0)
    set("bomb_timer",800)
    set("can_exp",0)
    set("flash_frq",10)
    set("boom",0)
    set("activated",0)
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)