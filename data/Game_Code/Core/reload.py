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
    
    self.a = 0

    # bg.addbackground("night")
    # bg.addbackgrounditem("stars","night",[0,-70],layer=0.01,infiniscroll=True,dimensions=[300,300],zdep=-2,surf="stars")
    # bg.addbackgrounditem("moon","night",[200,-60]                ,surf = "moon",dimensions=[200,200],layer = 0.015,infiniscroll=False,zdep=-1)
    # bg.addbackgrounditem("mount1","night",[0, -140]                ,surf = "mount",dimensions=[2500, 1250],layer = 0.05,infiniscroll=True,zdep=0)
    # bg.addbackgrounditem("mount2","night",[0, -20]                ,surf = "mount",dimensions=[2000, 700],layer = 0.1,infiniscroll=True,zdep=1)


    # bg.addbackground("day")
    # bg.addbackgrounditem("sun","day",[200,10]                ,surf = "sun",dimensions=[200,200],layer = 0.015,infiniscroll=False,zdep=-1)
    # bg.addbackgrounditem("mount1","day",[0, -140]                ,surf = "mount",dimensions=[2500, 1250],layer = 0.05,infiniscroll=True,zdep=0)
    # bg.addbackgrounditem("mount2","day",[0, -20]                ,surf = "mount",dimensions=[2000, 700],layer = 0.1,infiniscroll=True,zdep=1)
    # bg.savebg()

    if "game" == self.states:
        # initialise player and all its variables
        Player.init(self,[0,60])


    if "veiw" == self.states:
        um.changestate("test1","but1")
        # um.addbutton(univars.sizes["mediumbutton"],["test1"],[-0.5,0],"but1",color=univars.theme["dark"],surf = "testbutton")
        # um.addglide("but1",univars.sizes["mediumbutton"],univars.sizes["largebutton"])
        # um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0],"but2",color=univars.theme["dark"])
        # um.addbutton(univars.sizes["mediumbutton"],["test1"],[0.5,0],"but3",color=univars.theme["dark"])
        # um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0.5],"but4",color=univars.theme["dark"])
        # um.savealluielements()


    if self.states == "test":
        om.add(self,(0,0),"player",0,"green",[1,1],self.dim)

    if sm.state == "game":
        om.BAKE()
