import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Ui.level_select as level_select




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
    um.addrect([univars.ui_screen_size[0],univars.ui_screen_size[1]],["start_menu"],pos = [0,0],name="background",color=(0,0,0),layer=-2)
    
    #BANNER
    um.addrect([univars.ui_screen_size[0]/4,univars.ui_screen_size[1]],["start_menu"],[-0.5,0],"banner",color=(40,0,40),rot=45)
    
    
    #START BUTTON
    um.addbutton(univars.sizes["mediumbutton"],["start_menu"],[0.6,-0.2],"start_button",color=univars.theme["dark"])
    um.addtext("start_button_text","START",univars.defont,[0,0],col=univars.theme["bright"],size=40,states=["start_menu"],layer=1)
    um.bindtobutton("start_button_text","start_button")
    um.addglide("start_button",univars.sizes["smallbutton"],univars.sizes["mediumbutton"])
    um.addoutline("start_button",0,hoverthickness=20,layer = -1)
    
    
    um.addbutton(univars.sizes["mediumbutton"],["start_menu"],[0.6,-0.5],"settings_button",color=univars.theme["dark"])
    um.addtext("settings_button_text","SETTINGS",univars.defont,[0,0],col=univars.theme["bright"],size=40,states=["start_menu"],layer=1)
    um.bindtobutton("settings_button_text","settings_button")
    um.addglide("settings_button",univars.sizes["smallbutton"],univars.sizes["mediumbutton"])
    um.addoutline("settings_button",0,hoverthickness=20,layer=-1)
    
    um.addbutton(univars.sizes["mediumbutton"],["start_menu"],[0.6,-0.8],"quit_button",color=univars.theme["dark"])
    um.addtext("quit_button_text","QUIT",univars.defont,[0,0],col=univars.theme["bright"],size=40,states=["start_menu"],layer=1)
    um.bindtobutton("quit_button_text","quit_button")
    um.addglide("quit_button",univars.sizes["smallbutton"],univars.sizes["mediumbutton"])
    um.addoutline("quit_button",0,hoverthickness=20,layer = -1)
    
    
def main(self):
    
    
    
    if um.clicked(em,"start_button"):
        self.wait("transition:LEVEL_SELECT",0.2)
        
        
    if self.isthere("transition:LEVEL_SELECT"):
        um.lerpval("start_button","pos",[0 - 1.4,-0.2],4)
        um.lerpval("settings_button","pos",[0 - 1.4,-0.5],4)
        um.lerpval("quit_button","pos",[0 - 1.4,-0.8],4)
        um.lerpval("banner","pos",[0 - 2,0.5],4)
        
    else:
        # print(um.elements["settings_button"]["pos"])
        um.lerpval("start_button","pos"   ,[0.6,-0.2 + 0.2],4)
        um.lerpval("settings_button","pos",[0.6,-0.5 + 0.2],4)
        um.lerpval("quit_button"    ,"pos",[0.6,-0.8 + 0.2],4)
        um.lerpval("banner","pos"         ,[0,0],4)
        
    if um.clicked(em,"quit_button"):
        self.wait("transition:LEVEL_SELECT",0)
        em.close()
        
    if self.ondone("transition:LEVEL_SELECT"):
        level_select.rel(self)
        um.changestate("level_select",None)
    
    
