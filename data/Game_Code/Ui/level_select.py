import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Player.player_init as player_init




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
    inc = 0
    um.addrect([univars.ui_screen_size[0],univars.ui_screen_size[1]],["level_select"],pos = [0,0],name="background2",color=(20,0,20),layer=0)
    um.addtext("level_select_header","LEVEL SELECT",univars.defont,[0,0.8],col=univars.theme["semibright"],size=80,states=["level_select"])
    
    um.addbutton(univars.sizes["smallbutton"],["level_select"],[-0.8,-0.8],"back_button",color=univars.theme["dark"],layer=1)
    um.addtext("back_button_text","BACK",univars.defont,[0,-0.5],col=univars.theme["bright"],states=["level_select"],layer = 2,size=40)
    um.bindtobutton("back_button_text","back_button")
    um.addglide("back_button",univars.sizes["smallbutton"],univars.sizes["mediumbutton"])
    
    self.level_buttons = []
    self.level_buttons_initpos = {}
    self.level_buttons_incs = {}
    self.level_buttons_slider = 0
    for level in self.playablelevels:
        pos = [-0.3,-0.1-(inc*0.5)]
        um.addbutton([400,200],["level_select"],pos,level + "button",color=univars.theme["accent"],layer=1)
        self.level_buttons.append(level + "button")
        self.level_buttons_initpos[level + "button"] = pos.copy()
        self.level_buttons_incs[level + "button"] = inc
        
        
        
        um.addrect([1000,150],states=["level_select"],pos=[0,0],name=level + "text_backer",color=univars.theme["mid"],alpha=100,fromstart=1,layer=0)
        # um.addrect([800,150],states=["level_select"],pos=[0,0],name=level + "text_backer2",color=univars.theme["mid"],alpha=100,fromstart=1,layer=0)
        um.bindtorect(level + "text_backer",level + "button" ,offset=[0,0],glidesize=[1000,200],size=[0,0])
        # um.bindtorect(level + "text_backer2",level + "button",offset=[0,0],glidesize=[800,200],size=[800,250/2])
        
        um.addtext(level + "text",level,univars.defont,[0,0.1],col=univars.theme["bright"],states=["level_select"],layer = 2,size=50,center=0)
        um.bindtobutton(level + "text",level + "button",offset=[0.3,0.05])
        
        
        
        
        um.addglide(level + "button",[250,250/2],[350,200])
        inc += 1

def main(self):
    # print("WNETBIWD")
    if um.selectedbutton == None:
        um.changestate("level_select",self.playablelevels[0] + "button")
        
    if um.clicked(em,"back_button") or self.key["back"]:
        um.changestate("start_menu","start_button")
        
        
    # if 
        
        
        
    for button in self.level_buttons:
        um.setroute(button,"up",self.level_buttons[self.level_buttons.index(button) - 1])
        
        um.setroute(button,"down",self.level_buttons[(self.level_buttons.index(button) + 1)%len(self.level_buttons)])
        um.setroute(button,"left","back_button")
        
        
        if um.clicked(em,button):
            self.setbosh("debugame")
            um.changestate("maingame",None)
            om.loadtilemap(self,button.replace("button",""))
            player_init.main(self,[0,60])
            
        if um.conthover(button):
            # if abs(self.level_buttons_slider - self.level_buttons_incs[button]) > 1:
            self.level_buttons_slider = self.level_buttons_incs[button] 
            
        if not um.mode == "arrow":
            self.level_buttons_slider -= em.scroll/30
            
            
        self.level_buttons_slider = self.level_buttons_slider%len(self.level_buttons)
            
            
        despos = [
            self.level_buttons_initpos[button][0],
            self.level_buttons_initpos[button][1] + round(self.level_buttons_slider)*0.5
            ]
        desalph = 100
        
        
        
        if abs(round(self.level_buttons_slider )- self.level_buttons_incs[button]) > 1.2:
            despos[0] = 1.3
            despos[1] += (round(self.level_buttons_slider) - self.level_buttons_incs[button]) * -0.05
            desalph = 0
            
        if round(self.level_buttons_slider) - self.level_buttons_incs[button] == -1:
            despos[0] += 0.3
            
        if round(self.level_buttons_slider) - self.level_buttons_incs[button] == 1:
            despos[0] += 0.3
            
        
        um.lerpval(button,"pos",despos,4)  
        um.lerpval(button.replace("button","") + "text_backer","alpha",desalph,4)  
        # um.lerpval(button.replace("button","") + "text_backer2","alpha",desalph,4)  
        
        
    
