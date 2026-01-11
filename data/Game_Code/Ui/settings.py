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
am = Gamemananager.am


def main(self):
    
    if um.clicked(em,"back_button") or (self.key["back"] and not self.lastkey["back"]):
        um.changestate("start_menu","start_button")
        
    
    
        

    um.lerpval("video_settings_button"   ,"pos" ,  [-0.7     -0.1/3 ,0.7],4)
    um.lerpval("audio_settings_button"   ,"pos" ,  [-0.7 + 0.1/2,0.7 - 0.5],4)
    um.lerpval("controls_settings_button","pos" ,  [-0.7 + (0.1/2)*2 + 0.1/3,0.7 - (0.5)*2],4)
    um.lerpval("settings_banner","pos" ,  [-1,0],4)
    
    # um.addbutton([600,200],["settings"],[-1,0.7],"audio_settings_button",univars.theme["dark"])

def rel(self):
    um.changestate("settings","video_settings_button",sound=None)
    
    um.elements["video_settings_button"]["pos"]    = [-0.7 -0.1/3 -1,0.7]
    um.elements["audio_settings_button"]["pos"]    =  [-0.7 + 0.1/2 -1,0.7 - 0.5]
    um.elements["controls_settings_button"]["pos"] = [-0.7 + (0.1/2)*2 + 0.1/3 -1,0.7 - (0.5)*2]
    um.elements["settings_banner"]["pos"] = [-2,0]

def init(self):
    # self.ch
    um.addbutton([300,100],["settings"],[-0.7 -0.1/3,0.7],"video_settings_button",univars.theme["dark"],layer=0)
    um.addtext("video_settings_text","VIDEO",univars.defont,pos=[0,0],col=univars.theme["bright"],size=60,states=["settings"],layer=1)
    um.bindtobutton("video_settings_text","video_settings_button",col=univars.theme["bright"],hcol=(255,255,255))
    um.addglide("video_settings_button",[300,100],[300+25,100+25],univars.theme["dark"],univars.theme["accent"])
    
    um.addbutton([300,100],["settings"],[-0.7 + 0.1/2,0.7 - 0.5],"audio_settings_button",univars.theme["dark"],layer=0)
    um.addtext("audio_settings_text","AUDIO",univars.defont,pos=[0,0],col=univars.theme["bright"],size=60,states=["settings"],layer=1)
    um.bindtobutton("audio_settings_text","audio_settings_button",col=univars.theme["bright"],hcol=(255,255,255))
    um.addglide("audio_settings_button",[300,100],[300+25,100+25],univars.theme["dark"],univars.theme["accent"])
    
    um.addbutton([300,100],["settings"],[-0.7 + (0.1/2)*2 + 0.1/3,0.7 - (0.5)*2],"controls_settings_button",univars.theme["dark"],layer=0)
    um.addtext("controls_settings_text","CONTROLS",univars.defont,pos=[0,0],col=univars.theme["bright"],size=60,states=["settings"],layer=1)
    um.bindtobutton("controls_settings_text","controls_settings_button",col=univars.theme["bright"],hcol=(255,255,255))
    um.addglide("controls_settings_button",[300,100],[300+25,100+25],univars.theme["dark"],univars.theme["accent"])
    
    um.addrect([univars.ui_screen_size[0]/2.5,univars.ui_screen_size[1]*2],["settings"],[-1,0],"settings_banner",color=(40,0,40),rot=20,alpha=255,layer=-1)