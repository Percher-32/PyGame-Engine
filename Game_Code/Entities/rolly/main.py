import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import Game_Code.Utils.Entities as Entities
import math
import Game_Code.Utils.math as util_math
import random


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
    set("flash_timer",30)
    set("yeet_timer",10)
    set("flash_timer",30)
    set("stunned",30)
    set("knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("des_knock_back",[self.key["x"] * 400 , self.key["y"] * 200])
    set("downvel",0)
    

    
def slope():
    slantr = get("inst_type") == "slantr" or (get("inst_name") == "rail-diag" and (get("inst").rot%180 == 0 ))
    slantl = get("inst_type") == "slantl" or (get("inst_name") == "rail-diag" and ((get("inst").rot+90)%180 == 0 ))
    
    
    if  get("slope"):
        if slantr:
            set("act_vel",get("act_vel",0),1)
        if slantl:
            set("act_vel",get("act_vel",0) * -1,1)
            
    
    if get("last_frame_slope") and not get("slope"):
        if slantl:
            if get("des_vel",0) > 0:
                om.translate(self,id,[
                    abs((abs(get("des_vel",0)) * st * 1) + univars.grandim),
                    abs((abs(get("des_vel",1)) * st * 1) + univars.grandim)
                ])
                set("des_vel",0,1)
                set("act_vel",0,1)
    
        if slantr:
            if get("des_vel",0) < 0:
                om.translate(self,id,[
                    abs((abs(get("des_vel",0)) * st * 1) + univars.grandim) * -1,
                    abs((abs(get("des_vel",1)) * st * 1) + univars.grandim)
                ])
                set("des_vel",0,1)
                set("act_vel",0,1)
            
    if get("slope") and not get("last_frame_slope"):
        if slantr:
            om.objects[id]["pos"] = [get("inst").realpos[0] - 0,get("inst").realpos[1] - 0]
            
        if slantl:
            om.objects[id]["pos"] = [get("inst").realpos[0] - 0,get("inst").realpos[1] - 0]
            
            
    
    set("last_frame_slope",get("slope"))
    set("last_frame_inst_type",get("inst_type"))
    
def update():
    if get("yeet_timer") > 0:
        pm.particlespawnbluprint(self.listadd((om.objects[id]["pos"],(-32,-32))),"exp")
        inc("yeet_timer",-1 * st)
        set("act_vel",get("knock_back"))
        set("des_vel",get("act_vel"))
        
    
    
    
    
    if get("cdb"):
        if get("bomb_timer") > 0:
            if round(fm.frame)%(math.ceil(get("flash_frq"))) == 0:
                if om.objects[id]["sn"] == 0:
                    om.objects[id]["sn"] = 1
                elif om.objects[id]["sn"] == 1:
                    om.objects[id]["sn"] = 2
                elif om.objects[id]["sn"] == 2:
                    om.objects[id]["sn"] = 1
                
                
    elif get("flash_timer") > 0:
        inc("flash_timer",-1 * st)
        if round(fm.frame)%(math.ceil(get("flash_frq"))) == 0:
            if om.objects[id]["sn"] == 1:
                om.objects[id]["sn"] = 0
            elif om.objects[id]["sn"] == 0:
                om.objects[id]["sn"] = 1
                
                
    else:
        om.objects[id]["sn"] = 0
    

    if get("stunned") > -10:
        inc("stunned",-1 * st)
    
    
    inc("bomb_timer",-1 * st)
    
    
    
    set("act_vel",    util_math.customunilerp(get("act_vel"),get("des_vel"),10,om.speed,st)        )
    
    
    slope()
    

    om.translate(self,id,get("act_vel"),usedt=1)
    
    if get("jump_timer") > 0:
        inc("jump_timer",-1 * st)
        
    
def bomb_diffuse():
    set("cdb",0)
    set("bomb_timer",50)
    om.objects[id]["sn"] = 0
    
def bomb_logic():
    set("cdb",1)
    if get("bomb_timer") > 0:
        intensity = max([(50 - get("bomb_timer") )/50 * 20,0])
        set("flash_frq", get("bomb_timer")/10)
        om.objects[id]["pos"][1] += random.randint(-1 * int(intensity),int(intensity))
        om.objects[id]["pos"][0] += random.randint(-1 * int(intensity),int(intensity))
        # self.print("WERTYUI")
        
    else:
        boom()
        
def boom():
    if not get("boom"):
        set("boom",1)
        for _ in range(3):
            pm.particlespawnbluprint([om.objects[id]["pos"][0],om.objects[id]["pos"][1] ],"exp2",initvel=[(get("des_vel")[0]/20) * 0 ,(get("des_vel")[1]/20) * 0 ])
        die()
    
    
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
        if inst.type == "ground" or (inst.type == "rail" and inst.rot == 0):
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

    
def jump(power,lungepow,jumprem):
    if not get("jump_timer") > 0:
        set("jump_timer",60)
        set("jump_h",power)
        set("des_vel",get("jump_h"),1)
        set("act_vel",get("jump_h"),1)
        # set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0]),500]),0)
        # set("act_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * 400,0)
        set("knock_back",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * lungepow,0)
        set("knock_back",jumprem,1)
        set("yeet_timer",1)
        set("downvel",0)
    
def player_track():
    if not get("stunned") > 0:
        if get("ground") or get("slope"):
            set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0])/1.2,300]),0)
        else:
            set("des_vel",util_math.valsign(om.objects["player"]["pos"][0] - info["pos"][0]) * min([abs(om.objects["player"]["pos"][0] - info["pos"][0])/2,260]),0)
            
        if om.objects["player"]["pos"][1] - info["pos"][1] < -200:
            lungepow = 400
            jumprem = 0
            if abs(om.objects["player"]["pos"][1] - info["pos"][1]) > 400:
                lungepow = 600
                
            if om.objects["player"]["pos"][1] - info["pos"][1] < -500:
                jumprem = 500
                
            jump( min(abs(om.objects["player"]["pos"][1] - info["pos"][1]) * 1 ,500),lungepow ,jumprem)
        
        if util_math.dist(om.objects["player"]["pos"],info["pos"]) < 400:
            bomb_logic()
        else:
            bomb_diffuse()
            
            

def damageable():
    Entities.damageable(id,20,self,func = hit     )
        
def die():
    om.objects[id]["rendercond"] = 0
    set("canhome",0)

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
    
    
    
    player_track()
    
    
    
    
    gravity()
    
    ground_col()
    
    damageable()
    
    
    
    update()
    
    
    if not get("HP") > 0 or util_math.dist(om.objects["player"]["pos"],info["pos"]) > 6000:
        die()
        
 


self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)