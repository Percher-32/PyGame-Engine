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
    str = "BRIEF: \n Arron Dash has just \n done some crazy stuff which\n im sure ill actually plan out \n but for now this \n is just some \n flavour text."
    um.addtext("level_text",str,univars.defont,[0.15,0.5],col=univars.theme["bright"],size=50,states=["level_select_big","level_select"],center=0)
    um.addtext("level_text2","Time of day : NIGHT",univars.defont,[0.15,-0.2],col=univars.theme["bright"],size=50,states=["level_select_big","level_select"],center=0)
    
    um.addbutton(univars.sizes["smallbutton"],["level_select_big","level_select"],[0.47,-0.5],"start_level",univars.theme["mid"],layer=1)
    um.addtext("start_level_text","START",univars.defont,[0,0],univars.theme["bright"],40,["level_select_big"],layer=2)
    um.bindtobutton("start_level_text","start_level")
    um.addglide("start_level",univars.sizes["smallbutton"],univars.sizes["mediumbutton"])


def rel(self):
    um.elements["level_text"]["pos"] = [0.15 + 1,0.5]
    um.elements["level_text2"]["pos"] = [0.15 + 1,-0.2]
    um.elements["start_level"]["pos"] = [0.47 + 1,-0.5]

def main(self):
    
    um.lerpval("level_text","pos" ,[0.15 ,0.5 ],4)
    um.lerpval("level_text2","pos",[0.15 ,-0.2],4)
    um.lerpval("start_level","pos",[0.47 ,-0.5],4)
    
    
    
    
    
    
    buttonid = self.leveldo + "button"
    if not "level_select_big" in um.elements[buttonid]["states"]:
        um.elements[buttonid]["states"].append("level_select_big")
    # um.d
    um.lerpval(buttonid,"pos",[-0.5,-0.1],4)
    um.lerpval(buttonid,"dimensions",[750,750/2],4)
    # um.addglide(buttonid,[750,750/2],[750,750/2])
    
    if self.key["back"] and not self.lastkey["back"]:
        um.changestate("level_select",buttonid)
        
        
    um.lerpval("back_button","pos",[-0.8,-1.5],4)
    um.lerpval("level_select_header","pos",[0,1.2],4)
    
    
    um.lerpval(buttonid.replace("button","") + "text"       ,"offset",[0.4,1],4)
    um.elements[buttonid.replace("button","") + "text"]["size"] = 80
    
    backersize = [500,500]
    backeroffset = [0.6,0]
    
    
    
    um.lerpval(buttonid.replace("button","") + "text_backer","glidesize",backersize   ,4)  
    um.lerpval(buttonid.replace("button","") + "text_backer","offset"   ,backeroffset        ,4)  
    um.lerpval(buttonid.replace("button","") + "text_backer","normsize" ,backersize        ,4)  
    
    
    
    if um.clicked(em,"start_level"):
        self.setbosh("debugame")
        um.changestate("maingame",None)
        om.loadtilemap(self,self.leveldo)
        player_init.main(self,[0,60])
    
    
    for button in self.level_buttons:
        if not button == buttonid:
            despos = [
                self.level_buttons_initpos[button][0] + 1.7,
                self.level_buttons_initpos[button][1] + round(self.level_buttons_slider)*0.5
                ]
            um.lerpval(button,"pos",despos,4)
    
        
    
