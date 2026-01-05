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


def main(self):

    mood = self.publicvariables["mood"]

    sd.program['time'] = fm.frame
    sd.program['state'] = self.publicvariables["shaderstate"]




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

