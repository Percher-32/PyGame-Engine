import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import Game_Code.Utils.Entities as Entities
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
    pass
    
    
    
    
    
self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"



main(self,id,info)



FLAG = "<PASS>"