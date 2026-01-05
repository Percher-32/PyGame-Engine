import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Ui.level_select as level_select
import data.Game_Code.Ui.settings as settings




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
    um.addrect([univars.ui_screen_size[0],univars.ui_screen_size[1]],["start_menu"],pos = [0,0],name="background",color=(20,0,20),layer=-2)
    
    #BANNER
    um.addrect([univars.ui_screen_size[0]/2,univars.ui_screen_size[1]*2],["start_menu"],[-0.5,0],"banner",color=(40,0,40),rot=15,alpha=150)
    
    
    um.addtext("header_text","AARON DASH \n VS \n BOB",univars.defont       ,[-0.4       ,0.5       ],univars.theme["bright"],120,["start_menu"],1,layer=3)
    um.addtext("header_text_shadow","AARON DASH \n VS \n BOB",univars.defont,[-0.4 - 0.01,0.5 - 0.03],univars.theme["dark"],120,["start_menu"],1,layer=2)
    
    
    um.addrect([univars.ui_screen_size[0]/2,univars.ui_screen_size[1]*2],["start_menu"],[-0.5,0],"banner2",color=(40,0,40),rot=15,alpha=150)
    
    
    # um.addrect([univars.ui_screen_size[0]/2,univars.ui_screen_size[1]*2],["start_menu"],[-0.5,0],"banner3",color=(40,0,40),rot=-90+5,alpha=150)
    
    
    #START BUTTON
    um.addbutton(univars.sizes["mediumbutton"],["start_menu"],[0.6,-0.2],"start_button",color=univars.theme["dark"])
    um.addtext("start_button_text","START",univars.defont,[0,0],col=univars.theme["bright"],size=50,states=["start_menu"],layer=1)
    um.bindtobutton("start_button_text","start_button")
    um.addglide("start_button",[200 + 60,100-10],[250 + 60,125-10])
    um.addoutline("start_button",0,hoverthickness=20,layer = -1,color=  univars.theme["semibright"])
    
    
    um.addbutton(univars.sizes["mediumbutton"],["start_menu"],[0.6,-0.5],"settings_button",color=univars.theme["dark"])
    um.addtext("settings_button_text","SETTINGS",univars.defont,[0,0],col=univars.theme["bright"],size=50,states=["start_menu"],layer=1)
    um.bindtobutton("settings_button_text","settings_button")
    um.addglide("settings_button",[200 + 60,100-10],[250 + 60,125-10])
    um.addoutline("settings_button",0,hoverthickness=20,layer=-1,color= univars.theme["semibright"])
    
    um.addbutton(univars.sizes["mediumbutton"],["start_menu"],[0.6,-0.8],"quit_button",color=univars.theme["dark"])
    um.addtext("quit_button_text","QUIT",univars.defont,[0,0],col=univars.theme["bright"],size=50,states=["start_menu"],layer=1)
    um.bindtobutton("quit_button_text","quit_button")
    um.addglide("quit_button",[200 + 60,100-10],[250 + 60,125-10])
    um.addoutline("quit_button",0,hoverthickness=20,layer = -1,color=   univars.theme["semibright"])
    
    
def main(self):
    
    # startcolor = univars.theme["dark"]
    # if um.hover("start_button"):
    #     startcolor = univars.theme["accent"]
    # um.lerpval("start_button","color",startcolor,10)
    
    
    # if univars.func.dist(um.elements["start_button"]["color"],univars.theme["accent"])  < 10:
    #     um.elements["start_button"]["color"] = univars.theme["accent"]
    
    
    # settingcolor = univars.theme["dark"]
    # if um.hover("settings_button"):
    #     settingcolor = univars.theme["mid"]
    # um.lerpval("settings_button","color",settingcolor,4)
    
    
    
    
    if um.clicked(em,"start_button"):
        self.wait("transition:LEVEL_SELECT",0.2)

    if um.clicked(em,"settings_button"):
        self.wait("transition:SETTINGS",0.2)

    if um.clicked(em,"quit_button"):
        self.wait("transition:LEVEL_SELECT",0)
        em.close()
        
    if self.ondone("transition:LEVEL_SELECT"):
        level_select.rel(self)
        um.changestate("level_select",None)
    
    if self.ondone("transition:SETTINGS"):
        settings.rel(self)
        um.changestate("settings",None)
        
    if self.isthere("transition:LEVEL_SELECT"):
        um.lerpval("start_button","pos",[0 - 1.4,-0.2],4)
        um.lerpval("settings_button","pos",[0 - 1.4,-0.5],4)
        um.lerpval("quit_button","pos",[0 - 1.4,-0.8],4)
        um.lerpval("banner","pos",[0 - 2,0.5],4)
        
        um.lerpval("banner2","pos",[0 - 2,0.5],4)
        um.lerpval("header_text","pos"       ,[-0.4        - 2,0.5       ],4)
        um.lerpval("header_text_shadow","pos",[-0.4 - 0.01 - 2,0.5 - 0.03],4)
        
        
        # um.lerpval("banner3","pos",[0 - 2,0.5],4)
        
    elif self.isthere("transition:SETTINGS"):
        um.lerpval("start_button","pos",[0 + 2,-0.2],4)
        um.lerpval("settings_button","pos",[0 + 2,-0.5],4)
        um.lerpval("quit_button","pos",[0 + 2,-0.8],4)
        um.lerpval("banner","pos",[0 + 2,0.5],4)
        
        um.lerpval("banner2","pos",[0 + 2,0.5],4)
        um.lerpval("header_text","pos"       ,[-0.4        + 2,0.5       ],4)
        um.lerpval("header_text_shadow","pos",[-0.4 - 0.01 + 2,0.5 - 0.03],4)
        
    else:
        # print(um.elements["settings_button"]["pos"])
        um.lerpval("start_button","pos"   ,[0.4   + 0.2  ,-0.2 + 0.4 + 0.2],4)
        um.lerpval("settings_button","pos",[0.45  + 0.2   ,-0.5 + 0.2 + 0.2],4)
        um.lerpval("quit_button"    ,"pos",[0.5   + 0.2  ,-0.8 + 0 + 0.2],4)
        um.lerpval("banner","pos"         ,[-0.8  + 0.2  ,0],4)
        
        um.lerpval("banner2","pos"         ,[-0.8  + 0.3  ,0],4)
        um.lerpval("header_text","pos",[-0.4       ,0.5       ],4)
        um.lerpval("header_text_shadow","pos",[-0.4 - 0.01,0.5 - 0.03],4)
        # um.lerpval("banner3","pos"         ,[-0.8  ,0.5],4)
        
