import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import Game_Code.Utils.Entities as Entities
import math
import Game_Code.Utils.math as util_math


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
    
def inc(var_name,inc,index = None):
    if index == None:
        set(var_name,get(var_name) + inc)
    else:
        set(var_name,get(var_name,index) + inc,index)
    
    

def hit():
    self.print("HIT")
    set("yeet_timer",4)
    set("knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("des_knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("downvel",0)
    
    
def update():
    
    if get("yeet_timer") > 0:
        inc("yeet_timer",-1 * st)
        set("act_vel",get("knock_back"))
    
    set("act_vel",util_math.customunilerp(get("act_vel"),get("des_vel"),10,om.speed,st))
    
    if not get("inst_type") == 0:
        if get("inst_type") == "slantr":
            set("act_vel",get("act_vel",0),1)
        if get("inst_type") == "slantl":
            set("act_vel",get("act_vel",0) * -1,1)
    
        # if not get("last_frame_slope"):
        #     if get("inst_type") == "slantl":
        #         self.print("INIT")
        #         om.objects["player"]["pos"] = [get("inst").realpos[0] +16,get("inst").realpos[1] -20]
        #     elif get("inst_type") == "slantr":
        #         self.print("INIT")
        #         om.objects["player"]["pos"] = [get("inst").realpos[0] -20,get("inst").realpos[1] -20]
            
    om.translate(self,id,get("act_vel"),usedt=1)
    
    
    set("last_frame_slope",get("slope"))
    
    
def gravity():
    if not get("ground"):
        if not get("yeet_timer" ) > 0:
            set("des_vel",get("downvel"),1)
        
            if get("downvel") > -70:
                inc("downvel",-1*st)
        
        
def ground_col():
    
    insts = om.is_inst_at_pos([info["pos"][0],info["pos"][1] + univars.grandim])
    inst = None
    if len(insts):
        inst = insts[0]
        
    curinsts = om.is_inst_at_pos([info["pos"][0],info["pos"][1] ])
    curinst = None
    if len(curinsts):
        curinst = curinsts[0]
    
        
    if len(insts) > 0:
        set("ground",1)
        set("slope",inst.type == "slantr" or inst.type == "slantl")
        if not get("slope"):
            if len(curinsts):
                set("slope",curinst.type == "slantr" or curinst.type == "slantl")
        set("inst",inst)
        set("inst_type",inst.type)
    else:
        set("ground",0)
        set("slope",0)
        set("inst_type",0)
        set("inst",0)
        
        
    if get("ground"):
        
        if inst.type == "ground":
            set("des_vel",0,1)
            set("yeet_timer",-1)
            set("knock_back",0,1)
            set("downvel",0)
            om.objects[id]["pos"][1] = inst.realpos[1] - (univars.grandim*1)
            # if not curinst == None:
            #     while not 
            
            
    
            
        
    
    
    
    set("last_frame_ground",get("ground"))
        
    


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
    set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0])/2,250]),0)
    set("canhome",1)
    gravity()
    Entities.damageable(id,20,self,func = hit,range=(  400 + util_math.magnitude(self.gp("act_vel"))/10  )      )
    ground_col()
    update()



self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)