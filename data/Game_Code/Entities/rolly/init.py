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
    if not "hit_dam" in om.values[id]:
        set("hit_dam",40)
    if not "MAXHP" in om.values[id]:
        set("MAXHP",100)
        
    set("HP",get("MAXHP"))
    
    om.objects[id]["rendercond"] = 1
    om.objects[id]["sizen"] = [3,3]
    Entities.createhpbar(id,1.8,[0,100],self)
    
    
def set_all():
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
    set("start_boom",800)
    set("bomb_timer",get("start_boom"))
    set("can_exp",0)
    set("flash_frq",10)
    set("boom",0)
    set("activated",0)
    set("hasboomed",0)
    set("thrown",0)
    set("expdam",1)
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)