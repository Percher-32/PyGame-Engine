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
    om.translate(self,id,get("act_vel"),usedt=1)
    
    
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
    linsts = om.is_inst_at_pos([info["pos"][0] - univars.grandim,info["pos"][1]])
    linst = None
    if len(linsts):
        linst = linsts[0]
    rinsts = om.is_inst_at_pos([info["pos"][0] + univars.grandim,info["pos"][1]])
    rinst = None
    if len(rinsts):
        rinst = rinsts[0]
    
        
    if len(insts) > 0:
        set("ground",1)
    else:
        set("ground",0)
        
        
    if get("ground"):
        
        if inst.type == "ground":
            set("des_vel",0,1)
            set("des_vel",20,0)
            set("downvel",0)
            om.objects[id]["pos"][1] = inst.realpos[1] - (univars.grandim*1)
            
        if inst.type == "slantr":
            # print("R")
            # mag = util_math.magnitude(get("des_vel"))
            
            # newx = mag * math.cos(math.pi)
            # newy = mag * math.sin(math.pi)
            
            
            # set("des_vel",[newx,newy])
            # set("act_vel",[newx,newy])
            
            rot = 45
            item = inst
            om.objects[id][1] = -1 * (     ( (rot/45)*info["pos"][0] )  + (   (-1* item.realpos[1]) -    (item.realpos[0]*(rot/45))       )                      )
                
        if inst.type == "slantl":
            # print("L")
            # mag = util_math.magnitude(get("des_vel"))
            
            # newx = mag * math.cos(math.pi) * -1
            # newy = mag * math.sin(math.pi)
            
            
            
            # set("des_vel",[newx,newy])
            # set("act_vel",[newx,newy])
            
            rot = -45
            item = inst
            om.objects[id][1] = -1 * (     ( (rot/45)*info["pos"][0] )  + (   (-1* item.realpos[1]) -    (item.realpos[0]*(rot/45))       )                      )
            
            
    if not linst == None:
        # mag = util_math.magnitude(get("des_vel"))
        
        # newx = mag * math.cos(math.pi)
        # newy = mag * math.sin(math.pi)
        
        
        # set("des_vel",[newx,newy])
        # set("act_vel",[newx,newy])
        
        rot = 45
        item = linst
        om.objects[id][1] = -1 * (     ( (rot/45)*info["pos"][0] )  + (   (-1* item.realpos[1]) -    (item.realpos[0]*(rot/45))       )                      )
            
    if not rinst == None:
        if rinst.type == "slantl":
            # mag = util_math.magnitude(get("des_vel"))
            
            # newx = mag * math.cos(math.pi) * -1
            # newy = mag * math.sin(math.pi)
            
            
            # set("des_vel",[newx,newy])
            # set("act_vel",[newx,newy])
            
            rot = 45
            item = rinst
            om.objects[id][1] = -1 * (     ( (rot/45)*info["pos"][0] )  + (   (-1* item.realpos[1]) -    (item.realpos[0]*(rot/45))       )                      )
            
    
    
    
    
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
    set("canhome",1)
    gravity()
    ground_col()
    Entities.damageable(id,20,self,func = hit,range=(  400 + util_math.magnitude(self.gp("act_vel"))/10  )      )
    update()



self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)