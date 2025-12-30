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
    set("yeet_timer",10)
    set("knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("des_knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("downvel",0)
    
    
    
def slope():
    
    if  get("slope"):
        if get("inst_type") == "slantr" or (get("inst_type") == "rail-diag" and (get("inst").rot%180 == 0 )):
            set("act_vel",get("act_vel",0),1)
        if get("inst_type") == "slantl" or (get("inst_type") == "rail-diag" and ((get("inst").rot+90)%180 == 0 )):
            set("act_vel",get("act_vel",0) * -1,1)
            
    
    if get("last_frame_slope") and not get("slope"):
        if get("last_frame_inst_type") == "slantl" or (get("inst_type") == "rail-diag" and ((get("inst").rot+90)%180 == 0 )):
            if get("des_vel",0) > 0:
                om.translate(self,id,[
                    abs((abs(get("des_vel",0)) * st * 1) + univars.grandim),
                    abs((abs(get("des_vel",1)) * st * 1) + univars.grandim)
                ])
                set("des_vel",0,1)
                set("act_vel",0,1)
    
        if get("last_frame_inst_type") == "slantr" or (get("inst_type") == "rail-diag" and (get("inst").rot%180 == 0 )):
            if get("des_vel",0) < 0:
                om.translate(self,id,[
                    abs((abs(get("des_vel",0)) * st * 1) + univars.grandim) * -1,
                    abs((abs(get("des_vel",1)) * st * 1) + univars.grandim)
                ])
                set("des_vel",0,1)
                set("act_vel",0,1)
            
    if get("slope") and not get("last_frame_slope"):
        if get("inst_type") == "slantr" or (get("inst_type") == "rail-diag" and (get("inst").rot%180 == 0 )):
            om.objects[id]["pos"] = [get("inst").realpos[0] - 0,get("inst").realpos[1] - 0]
            
        if get("inst_type") == "slantl" or (get("inst_type") == "rail-diag" and ((get("inst").rot+90)%180 == 0 )):
            om.objects[id]["pos"] = [get("inst").realpos[0] - 0,get("inst").realpos[1] - 0]
            
            
    
    set("last_frame_slope",get("slope"))
    set("last_frame_inst_type",get("inst_type"))
    
    
def update():
    if get("yeet_timer") > 0:
        inc("yeet_timer",-1 * st)
        set("act_vel",get("knock_back"))
        set("des_vel",get("act_vel"))
        
    
    set("act_vel",    util_math.customunilerp(get("act_vel"),get("des_vel"),10,om.speed,st)        )
    
    
    slope()
    

    om.translate(self,id,get("act_vel"),usedt=1)
    
    if get("jump_timer") > 0:
        inc("jump_timer",-1 * st)
        
    
    
def gravity():
    if not get("ground"):
        if not get("yeet_timer" ) > 0:
            set("des_vel",get("downvel"),1)
        
            if get("downvel") > -200:
                inc("downvel",-1*st)
            
def ground_col():
    
    univars.println(f"SLOPE:{get("slope")}",14)
    if get("slope"):
        univars.print("SLOPELPSW")
    
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
        set("inst_name",inst.name)
    elif len(curinsts):
        set("inst",curinst)
        set("inst_type",curinst.type)
        set("inst_name",curinst.name)
    elif len(linsts):
        set("inst",linst)
        set("inst_type",linst.type)
        set("inst_name",linst.name)
    elif len(rinsts):
        set("inst",rinst)
        set("inst_type",rinst.type)
        set("inst_name",rinst.name)
    else:
        set("inst",0)
        set("inst_type",0)
        set("inst_name",0)
        
        
    
    set("slope",get("inst_type") == "slantr" or get("inst_type") == "slantl" or (get("inst_name") == "rail-diag") )
        
        
        
        
    if get("ground"):
        if inst.type == "ground" or (inst.name == "rail" and inst.rot == 0):
            set("des_vel",abs(get("des_vel",1))/3,1)
            set("yeet_timer",-1)
            set("knock_back",abs(get("knock_back",1))/3,1)
            set("downvel",-120)
            om.objects[id]["pos"][1] = inst.realpos[1] - (univars.grandim*1)
            if not curinst == None:
                while len(curinsts):
                    if curinst.type == "ground" or (inst.name == "rail" and inst.rot == 0):
                        om.objects[id]["pos"][1] = curinst.realpos[1] - (univars.grandim*1)
                        curinsts = om.is_inst_at_pos([info["pos"][0],info["pos"][1] ])
                        curinst = None
                        if len(curinsts):
                            curinst = curinsts[0]
                    else:
                        break
                    
                    
            
            
    wall_col(linsts,rinsts)
            
        
    
    
    
    set("last_frame_ground",get("ground"))
        
def wall_col(linsts,rinsts):
    if not get("slope") and not get("last_frame_slope"):
        if len(linsts):
            linst = linsts[0]
            if linst.type == "ground":
                set("des_vel",1 * abs(get("des_vel",0)),0)
                set("act_vel",1 * abs(get("act_vel",0)),0)
                # set("des_vel",100,1)
                
        if len(rinsts):
            rinst = rinsts[0]
            if rinst.type == "ground":
                set("des_vel",-1 * abs(get("des_vel",0)),0)
                set("act_vel",-1 * abs(get("act_vel",0)),0)
                # set("des_vel",100,1)

    
def jump(power):
    if get("ground") and not get("jump_timer") > 0:
        set("jump_timer",60)
        set("jump_h",power)
        set("des_vel",get("jump_h"),1)
        set("act_vel",get("jump_h"),1)
        # set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0]),500]),0)
        # set("act_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * 400,0)
        set("knock_back",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * 400,0)
        set("yeet_timer",1)
        set("downvel",0)
    
def player_track():
    if get("ground") or get("slope"):
        set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0])/2,300]),0)
    else:
        set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0])/3,200]),0)
        
    univars.println(om.objects["player"]["pos"][1] - info["pos"][1],12)
    if om.objects["player"]["pos"][1] - info["pos"][1] < -200:
        jump( min(abs(om.objects["player"]["pos"][1] - info["pos"][1]) * 1 ,500) )
        
    

def damageable():
    Entities.damageable(id,20,self,func = hit     )
    

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
    univars.println(f'JUMPTIMER:{get("jump_timer")}',13)
    player_track()
    
    
    gravity()
    
    ground_col()
    
    damageable()
    
    
    
    
    update()
 


self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)