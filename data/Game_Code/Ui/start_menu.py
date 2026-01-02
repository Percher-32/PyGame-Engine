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


def init(self):
    #BACKGROUND
    um.addrect([univars.ui_screen_size[0],univars.ui_screen_size[1]],["start_menu"],pos = [0,0],name="background",color=(0,0,0))
    
    #BANNER
    um.addrect([univars.ui_screen_size[0],univars.ui_screen_size[1]/4],["start_menu"],[0,0.5],"banner",color=(40,0,40))
    
    
    #START BUTTON
    um.addbutton(univars.sizes["mediumbutton"],["start_menu"],[0,-0.5],"start_button",color=univars.theme["dark"],surf = "testbutton")
    um.addglide("start_button",univars.sizes["smallbutton"],univars.sizes["mediumbutton"])
    
    
def main(self):
    pass
    
    
    # um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0],"but2",color=univars.theme["dark"])
    # um.addbutton(univars.sizes["mediumbutton"],["test1"],[0.5,0],"but3",color=univars.theme["dark"])
    # um.addbutton(univars.sizes["mediumbutton"],["test1"],[0,0.5],"but4",color=univars.theme["dark"])
