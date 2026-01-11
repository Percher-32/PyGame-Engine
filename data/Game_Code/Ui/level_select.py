import data.Managers.Gamemanager as Gamemananager
import data.Managers.univars as univars
import data.Game_Code.Player.player_init as player_init
import data.Game_Code.Ui.level_select_big as level_select_big
import random



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
am = Gamemananager.am

def init(self):
    inc = 0
    um.addrect([univars.ui_screen_size[0],univars.ui_screen_size[1]],["level_select","level_select_big","settings"],pos = [0,0],name="background2",color=(20,0,20),layer=-2)
    um.addtext("level_select_header","LEVEL SELECT",univars.defont,[0,0.8],col=univars.theme["semibright"],size=80,states=["level_select","level_select_big"])
    
    um.addbutton(univars.sizes["smallbutton"],["level_select","level_select_big"],[-0.8,-0.8],"back_button",color=univars.theme["dark"],layer=1)
    um.addtext("back_button_text","BACK",univars.defont,[0,-0.5],col=univars.theme["bright"],states=["level_select","level_select_big"],layer = 2,size=50)
    um.bindtobutton("back_button_text","back_button")
    um.addglide("back_button",univars.sizes["smallbutton"],univars.sizes["mediumbutton"])
    um.addoutline("back_button",0,hoverthickness=20)
    
    self.level_buttons = []
    self.level_buttons_initpos = {}
    self.level_buttons_incs = {}
    self.level_buttons_slider = 0
    for level in self.playablelevels:
        pos = [-0.3,-0.1-(inc*0.5)]
        
        paths = [f"test_level_pic{i}" for i in range(0,7)]
        
        um.addbutton([400,200],["level_select","level_select_big"],pos,level + "button",color=univars.theme["accent"],layer=1,surf=paths[random.randint(0,6)])
        self.level_buttons.append(level + "button")
        self.level_buttons_initpos[level + "button"] = pos.copy()
        self.level_buttons_incs[level + "button"] = inc
        
        
        
        um.addrect([1000,150],states=["level_select"],pos=[0,0],name=level + "text_backer",color=univars.theme["mid"],alpha=100,fromstart=1,layer=0)
        # um.addrect([800,150],states=["level_select"],pos=[0,0],name=level + "text_backer2",color=univars.theme["mid"],alpha=100,fromstart=1,layer=0)
        um.bindtorect(level + "text_backer",level + "button" ,offset=[0,0],glidesize=[1000,200],size=[0,0])
        # um.bindtorect(level + "text_backer2",level + "button",offset=[0,0],glidesize=[800,200],size=[800,250/2])
        
        um.addtext(level + "text",level,univars.defont,[0,0.1],col=univars.theme["bright"],states=["level_select"],layer = 2,size=50,center=0)
        # um.addoutline(level + "button",0,hoverthickness=20)
        um.bindtobutton(level + "text",level + "button",offset=[0.3,0.05])
        
        
        
        
        um.addglide(level + "button",[250,250/2],[350,200])
        inc += 1

def rel(self):
    um.elements["back_button"]["pos"]      = [-0.8 + 1.6,-0.8]   
    um.elements["level_select_header"]["pos"]      = [0 + 1.6,0.8]  
    for button in self.level_buttons:
        despos = [
        self.level_buttons_initpos[button][0]  + 1.6,
        self.level_buttons_initpos[button][1] + round(self.level_buttons_slider)*0.5
        ]
        um.elements[button]["pos"]      = despos       

def main(self):
    
    um.lerpval("back_button","pos",[-0.8,-0.8],4)
    
    
    
    um.lerpval("level_text","pos" ,[0.15 + 1.3,0.5 ],2)
    um.lerpval("level_text2","pos",[0.15 + 1.3,-0.2],2)
    um.lerpval("start_level","pos",[0.47 + 1.3,-0.5],2)
    
    
    
    
    if um.selectedbutton == None:
        um.changestate("level_select",self.playablelevels[0] + "button",sound=None)
        
    if um.clicked(em,"back_button") or (self.key["back"] and not self.lastkey["back"]):
        um.changestate("start_menu","start_button")
        
        
        
    # if 
        
        
        
    for button in self.level_buttons:
        # um.addglide(button,[250,250/2],[350,200])
        # if "level_select_big" in um.elements[button]["states"]:
        #     um.elements[button]["states"].remove("level_select_big")
        um.setroute(button,"up",self.level_buttons[self.level_buttons.index(button) - 1])
        
        um.setroute(button,"down",self.level_buttons[(self.level_buttons.index(button) + 1)%len(self.level_buttons)])
        um.setroute(button,"left","back_button")
        
        
        if um.clicked(em,button,sound="IN"):
            self.leveldo = button.replace("button","")
            level_select_big.rel(self)
            um.changestate("level_select_big","start_level",sound=None)
            
            
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
            
        
        um.lerpval(button                                     ,"pos"      ,despos       ,4)  
        um.lerpval(button.replace("button","") + "text_backer","glidesize",[1000,200]   ,4)  
        um.lerpval(button.replace("button","") + "text_backer","color",univars.theme["mid"]   ,4) 
        um.lerpval(button.replace("button","") + "text_backer","offset"   ,[0,0]        ,4)  
        um.lerpval(button.replace("button","") + "text_backer","normsize" ,[0,0]        ,4)  
        um.lerpval(button.replace("button","") + "text_backer","alpha"    ,desalph      ,4) 
        um.lerpval(button.replace("button","") + "text"       ,"offset"   ,[0.3,0.05]   ,4)
        
        
    
    um.lerpval("level_select_header","pos",[0,0.8],4)
        
    
