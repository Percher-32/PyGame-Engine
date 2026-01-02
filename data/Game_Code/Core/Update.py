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



def main(self,Player):
    # self.print(self.reactions,20)
    bg.background = "test2"

    # print/
    # print(self.dt * 60)
    # om.speed = 0.8
    # pm.particlespawn("circle",[0,0],[[-5,5],[-5,5]],(0,100,255),[0,0],[0,-1],5,0.001,alpha=300,alphadec=4,divergencepos=[[-1000,1000],[0,0]],ntimes=1)

    # cm.setcond("def","pos",[random.randint(-10000,10000),random.randint(-10000,10000)])


    if "game" == self.states:
        Player.main(self)
        self.publicvariables["showater"] = True
        


        if self.isthere("show-score"):
            um.state = "vic"
            um.addrect([6000,6000],["vic"],[(-0.5 + 0.02) - 0.5,0.8],"atnum",color=(0,0,0),fromstart=0,alpha = 200)
            um.addtext("Victory-lap","",univars.defont,[0,0],univars.theme["accent"],100,"vic")
            um.elements["Victory-lap"]["text"] = self.storedscore + "    " + str(int(self.timers["show-score"]/60) + 1) + "\n\n"  + f"Lowest - time:{self.highest}  on-attempt:{self.highestatt}"

        



    mood = self.publicvariables["mood"]

    # self.publicvariables["waterh"] -= 0.002
    sd.program['time'] = fm.frame
    sd.program['state'] = self.publicvariables["shaderstate"]
    # univars.pixelscale = abs(math.sin(fm.frame/100) * 3) + 1




    if mood == "afternoon":
        bg.background = "day"
        self.publicvariables["screencol"] = (90-30 ,234 ,234 )
        sd.program["illuminace"] = 1
        sd.program["hurt"] = -0.4
        sd.program["sunpos"] = [0,0]
        sd.program["pacify"] = -0.7
        sd.program["night"] = 0

    if mood == "sunset":
        bg.background = "day"
        self.publicvariables["screencol"] = (174, 99, 142)
        sd.program["illuminace"] = 0.34

        sd.program["hurt"] = 3.4
        sd.program["sunpos"] = [0,-1 * self.actualwaterheight/20 + 0.5 ]
        sd.program["pacify"] = -0.2

        sd.program["night"] = 0


    if mood == "daybreak":

        bg.background = "day"
        self.publicvariables["screencol"] = (110 ,189 ,234 )
        sd.program["hurt"] = 0
        sd.program["illuminace"] = 0.5
        sd.program["sunpos"] = [0,0]
        sd.program["pacify"] = 0

        sd.program["night"] = 0

    if mood == "night":
        bg.background = "night"
        self.publicvariables["screencol"] = (20,0,30)
        sd.program["illuminace"] = 0.22
        sd.program["hurt"] = 1
        sd.program["sunpos"] = [0,0]
        sd.program["pacify"] = 0.2
        sd.program["night"] = 1









    self.actualwaterheight =(self.publicvariables["waterh"] - cam.y)/(univars.realscreeen.height / cam.size) * -1 - cam.size

    if self.publicvariables["showater"]:
        sd.program["waterlevel"] = self.actualwaterheight
    else:
        sd.program["waterlevel"] = -1



    sd.program["camx"] = cam.x/(univars.startdims[0] * univars.scaledown)
