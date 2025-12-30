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
    set("yeet_timer",30)
    set("knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("des_knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("downvel",0)
    
    
    
def slope():
    
    if not get("inst_type") == 0:
        if get("inst_type") == "slantr":
            set("act_vel",get("act_vel",0),1)
        if get("inst_type") == "slantl":
            set("act_vel",get("act_vel",0) * -1,1)
            
    
    if get("last_frame_slope") and not get("slope"):
        if get("last_frame_inst_type") == "slantl":
            if get("des_vel",0) > 0:
                om.translate(self,id,[
                    +100 +  abs(get("des_vel",0) * 1),
                    50 + abs(get("des_vel",0) * 2)
                    
                ])
            
            
    if get("slope") and not get("last_frame_slope"):
        if get("inst_type") == "slantr":
            om.objects[id]["pos"] = [get("inst").realpos[0] - 0,get("inst").realpos[1] - 0]
        if get("inst_type") == "slantl":
            om.objects[id]["pos"] = [get("inst").realpos[0] - 0,get("inst").realpos[1] - 0]
            
            
    
    set("last_frame_slope",get("slope"))
    set("last_frame_inst_type",get("inst_type"))
    
    
def update():
    if get("yeet_timer") > 0:
        inc("yeet_timer",-1 * st)
        set("act_vel",get("knock_back"))
        set("des_vel",0,0)
        
    
    set("act_vel",util_math.customunilerp(get("act_vel"),get("des_vel"),10,om.speed,st))
    
    
    slope()
    

    om.translate(self,id,get("act_vel"),usedt=1)
    
    if get("jump_timer") > 0:
        inc("jump_timer",-1 * st)
        set("des_vel",get("jump_h"),1)
    
    
def gravity():
    if not get("ground"):
        if not get("yeet_timer" ) > 0:
            set("des_vel",get("downvel"),1)
        
            if get("downvel") > -200:
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
        
        
    linsts = om.is_inst_at_pos([info["pos"][0] - univars.grandim,info["pos"][1] ])
    linst = None
    if len(linsts):
        linst = linsts[0]
        
        
    rinsts = om.is_inst_at_pos([info["pos"][0] + univars.grandim,info["pos"][1] ])
    rinst = None
    if len(rinsts):
        rinst = rinsts[0]
    
        
    
        
    #GROUND
    if len(insts):
        set("ground",1)
    else:
        set("ground",0)
        
        
    if len(insts):
        # univars.print("INST")
        set("inst",inst)
        set("inst_type",inst.type)
    elif len(curinsts):
        univars.print("CURINST")
        set("inst",curinst)
        set("inst_type",curinst.type)
    elif len(linsts):
        univars.print("LINST")
        set("inst",linst)
        set("inst_type",linst.type)
    elif len(rinsts):
        univars.print("RINST")
        set("inst",rinst)
        set("inst_type",rinst.type)
    else:
        set("inst",0)
        set("inst_type",0)
        
        
    
    set("slope",get("inst_type") == "slantr" or get("inst_type") == "slantl")
        
        
        
        
    if get("ground"):
        
        if inst.type == "ground":
            set("des_vel",abs(get("des_vel",1))/3,1)
            set("yeet_timer",-1)
            set("knock_back",abs(get("knock_back",1))/3,1)
            set("downvel",0)
            om.objects[id]["pos"][1] = inst.realpos[1] - (univars.grandim*1)
            # if not curinst == None:
            #     while not 
            
            
    wall_col(linsts,rinsts)
            
        
    
    
    
    set("last_frame_ground",get("ground"))
        
def wall_col(linsts,rinsts):
    if not get("slope"):
        if len(linsts):
            linst = linsts[0]
            if linst.type == "ground":
                set("des_vel",1 * abs(get("des_vel",0)),0)
                set("act_vel",1 * abs(get("act_vel",0)),0)
                
        if len(rinsts):
            rinst = rinsts[0]
            if rinst.type == "ground":
                set("des_vel",-1 * abs(get("des_vel",0)),0)
                set("act_vel",-1 * abs(get("act_vel",0)),0)
    
    
    
    
    
def jump():
    if get("ground") and not get("jump_timer") > 0:
        set("jump_timer",1)
        # univars.print("JUMP")
        set("jump_h",500)
    
    
    


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
    set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0])/2,300]),0)
    set("canhome",1)
    gravity()
    Entities.damageable(id,20,self,func = hit     )
    
    if om.objects["player"]["pos"][1] - info["pos"][1]  > 10:
        jump()
    
    ground_col()
    
    
    # if self.key["jump"]:
    jump()
    
    
    update()
 


self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)