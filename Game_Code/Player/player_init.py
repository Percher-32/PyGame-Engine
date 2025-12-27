import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math





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


def main(self,pos):
    """
    Initialises the players variables
    """
    #create the cameras
    startpos = pos
    cm.addcam("playercam",startpos,univars.pixelscale/7 * 0.4)
    cm.setcam("playercam")

    om.speed = 1


    #create player
    self.prevtricks = []
    
    self.lastaxis = [0,0]

    self.slanted = 0

    om.adds(self,"player",startpos,"player","player",0,[1,1],400,5)
    self.sp("#DEBUG","HELLO WOLRD")
    om.objects["player"]["rendercond"] = False

    self.sp("dashmeter",0)
    self.lastframejumped = 0

    self.sp("dashcooldown",0)
    self.sp("deshrem",0)
    sc = 1.4
    #creates the player sprite you actually see
    om.adds(self,"playersprite",[-1400,400],"player","player",0,[sc,sc],400,5)
    om.objects["playersprite"]["rendercond"] = True
    om.includeflipping("playersprite")

    #creates the skateboard
    om.adds(self,"skateboard",[-1400,400],"skateboard","skateboard",0,[sc,sc],400,5)
    om.objects["skateboard"]["rendercond"] = True

    #desired velocity


    self.sp("lastframewall",0)

    self.flowstate = 0

    self.sp("slinging",0)

    self.lastrail = 0

    self.sp("des_vel",[0,0])

    self.sp("candj",0)

    self.sp("dashav",[0,0])
    self.sp("dashdv",[0,0])

    self.dropdashinit = 0
    self.lastground = 0




    self.println(self.slanted,6)
    self.attackheld = 0

    self.sp("exithm",0)

    #actual velocity
    self.sp("act_vel",[0,0])

    #smoothing
    self.sp("smoothing",2)

    self.sp("prevprevpos",om.objects["player"]["pos"])

    #modes
    self.sp("mode","grounded")

    #able to jump?
    self.sp("jumpamble",False)

    #fall speed smoothing
    self.sp("fss",8)

    self.lastframeslanted = False
    self.gate = "r"

    self.lastdirrail = 0
    self.sp("lastframeswing",0)


    self.lastdir = "r"

    self.lastdirslant = "r"

    #previous frames actual velocity
    self.sp("prev_act_vel",[0,0])

    #shidding?
    self.sp("skidding",False)

    self.reclock = 1

    self.sp("rot",0)


    #on skateboard?
    self.sp("onboard",True)

    self.sp("unboundrot",0)

    self.sp("rotoffset",0)
    self.sp("rotdes",0)

    self.sp("desrot",0)
    self.sp("desmooth",5)

    self.sp("machspeed",150)

    self.sp("lastwall","l")


    self.sp("slantdir","r")

    om.set_value("skateboard","fallvalue",5)

    self.sp("thickness",1)




    self.sp("homing",0)
    self.sp("target",None)

    self.joyaxis = pygame.math.Vector2(self.key["x"],self.key["y"])
    if self.joyaxis.length()> 0:
        self.joyaxis.normalize()
    else:
        self.joyaxis = pygame.math.Vector2(-1,0)




    #In_game_UI
    om.adds(self,"enemyzoom",[0,0],"enemyzoom","In_Game_UI",0,[1.6,1.6],255,5)
    om.objects["enemyzoom"]["rendercond"] = 0





    #UI
    um.changestate("maingame",None)
    um.addrect([6000,100 + 30 - 30],["maingame"],[(-0.5 + 0.02) - 0.5,0.8],"dashbarback",color=(0,0,0),fromstart=0,alpha = 200)
    um.addrect([(1000 -19)/2 + 20,100 + 30 - 30],["maingame"],[(-0.5 + 0.02) - 0.5,0.8],"dashbarback",color=(0,0,0),fromstart=1,alpha = 200)
    um.addrect([1000 - 30 - 20,90 - 30],["maingame"],[(-0.5 + 0.04/2 + 0.02) - 0.5,0.8],"dashbar",color=(225,100,100),fromstart=1,alpha = 200)



    um.addrect([1000 - 30 - 20 + 30,90 - 30 + 30],["maingame"],[(-0.5 + 0.04/2 + 0.02) - 0.5 -0.02,-0.8],"missiletimeback",color=(0,0,0),fromstart=1,alpha = 200)
    um.addrect([1000 - 30 - 20,90 - 30],["maingame"],[(-0.5 + 0.04/2 + 0.02) - 0.5,-0.8],"missiletime",color=(225,0,0),fromstart=1,alpha = 200)

    um.addtext("Speed-timer","0",univars.defont,[0,0.8],univars.theme["accent"],60,["maingame"])
    um.elements["Speed-timer"]["text"]  = str(0)

    um.addtext("attemps","0",univars.defont,[0.5,0.8],univars.theme["accent"],60,["maingame"])
    um.elements["attemps"]["text"]  = str(0)

