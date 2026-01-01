import Managers.Gamemanager as Gamemananager
import Managers.univars as univars





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



def sign(value):
    """
            returns + or -
    """
    if abs(value) == value:
        return "+"
    else:
        return "-"

def valsign(value):
    """
            returns 1 or -1
    """
    if abs(value) == value:
        return 1
    else:
        return -1

def listadd(lists:tuple) -> list:
    """
        lists = tuple of lists to add together
    """
    # print(lists[0])
    mainlist = [0 for i in lists[0]]
    for lst in lists:
        for index in range(len(lst)):
            mainlist[index] += lst[index]
    return mainlist

def listdiv(list,num):
    """
        divides a list by single number
    """
    return [i/num for i in list]




def rotlerp(rot,dest,sm,self,roundto = 2):
    """
        a ROTATION lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int\n
        FINDS SHORTEST DISTANCE
    """
    d1 = abs(rot - (dest - 360))
    d2 = abs(rot - (dest + 360))
    d3 = abs(rot - (dest + 0))

    destinations = {d1:dest-360,d2:dest+360,d3:dest}

    dest = destinations[min([d1,d2,d3])]

    rot = self.unilerp(rot,dest,sm,roundto=roundto)
    return rot

def unilerp(val,max,sm,self,roundto = 2,useigt = True):
    """
        a lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int
    """
    if om.speed == 0:
        om.speed = 0.1
    if self.dt == 0:
        self.dt = 1

    if useigt:
        return univars.func.lerp(val,max,              (  (sm/om.speed) / self.dt)*1.5              ,roundto = roundto)
    else:
        return univars.func.lerp(val,max,              (  (sm) / self.dt)*1.5              ,roundto = roundto)

def customunilerp(val,max,sm,gamespeed,deltatime,roundto = 2):
    """
        a lerp function that incorperates IN-GAME time and DELTA-TIME into its incorperation.  sm -> float or int
    """
    return univars.func.lerp(val,max,              (  (sm/gamespeed) / deltatime)*1.5              ,roundto = roundto)

def dist(pos1,pos2):
    """
        distance between 2 points
    
    :param pos1: list/tuple
    :param pos2: list/tuple
    """
    return univars.func.dist(pos1,pos2)

def magnitude(vec):
    """
        magnitude of a list/pos/vector
    
    :param vec: list/tuple
    """
    return univars.func.dist([0,0],vec)
    
    
    
    
    