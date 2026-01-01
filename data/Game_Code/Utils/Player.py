import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars





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

def sp(val:str,to,index=None):
    """
    changes the value a players variable
    """
    if index == None:
        om.set_value("player",val,to)
    else:
        change = to
        to = gp(val)
        to[index] = change
        om.set_value("player",val,to)
        
def gp(val:str,index=None):
    """
    gets the value a players variable
    """
    if index == None:
        return om.get_value("player",val)
    else:
        return om.get_value("player",val)[index]
    
    
    





def spin(angle,time,spindec = 0,self = None):
    """
        rotates the player by (angle) for (time) seconds
    """
    self.wait(f"rotate",time,barrier=False)
    self.sp("rotdes",spindec)
    self.sp("rot",angle)




