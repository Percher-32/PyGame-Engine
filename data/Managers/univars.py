import pygame
import json
import data.Managers.funcs as funcs
import data.Managers.statemanager as sm


pygame.display.init()

scaledown = 2


pixelscale = 1


screen_w = pygame.display.get_desktop_sizes()[0][0]/scaledown
screen_h = pygame.display.get_desktop_sizes()[0][1]/scaledown
# print()
oldnum = (pygame.display.get_desktop_sizes()[0][0]**2 +  pygame.display.get_desktop_sizes()[0][1]**2)**0.5
rw = ((screen_w**2 +  screen_h**2)**0.5)/oldnum
startdims = (screen_w*scaledown,screen_h*scaledown)



ui_screen_size =  startdims
camchange = True



grandim = 32


name = "Project ender"

maxfps = 60




theme = {
"dark" :       (40, 41, 83)                              ,
"mid" :        (75, 63, 114)                             ,
"bright" :     (220, 214, 247)                           ,
"accent" :     (242, 140, 84)                            ,
"semibright":  (163, 173, 225)
}


sizes = {
    "smallbutton": (150,75),
    "mediumbutton": (200,100),
    "semilargebutton":(250,250/2),
    "largebutton": (300,150),
    "display": (400,200),
    "display_select": (400+25,200+25 )
}


minsize = (screen_w/pixelscale,screen_h/pixelscale)


screen = pygame.Surface(minsize,pygame.SCALED)
fakescreen = pygame.Surface((screen_w*1,screen_h*1))
fakescreen.set_colorkey((0,0,0))


uiscreen = pygame.Surface((screen_w,screen_h))
try:
    finalscreen = pygame.display.set_mode((screen_w,screen_h),pygame.OPENGL|pygame.DOUBLEBUF|pygame.SCALED|pygame.FULLSCREEN,vsync=1)
except:
    finalscreen = pygame.display.set_mode((screen_w,screen_h),pygame.OPENGL|pygame.DOUBLEBUF|pygame.SCALED|pygame.FULLSCREEN,vsync=0)
realscreeen = pygame.Surface((screen_w,screen_h))
pygame.display.set_caption(name)

screen_rect = screen.get_rect(center = (0,0))

func = funcs.func(grandim)
"""
    Use this one
"""



lumptype = {"grass":"ground","dirt":"ground","slantl":"slantl","slantr":"slantr","slantlbot":"slantl","slantrbot":"slantr","slantdecor":"ground","rail":"rail","rail-diag":"rail"}

swaptypes = {"target":"omnispring","enemy":"enemy-L"}
"""
    all objects with the name (key)
    will have thier type set to type (Vale)
"""

sizeoffsets = {}

instables = ["dirt","grass","def","slantl","slantr","slantlbot","slantrbot","rail","rail-diag"]

domainexpansions = {}


extras = []
"""
    [Original sprite  ,  new sprite type  ,  size scale]
"""

newsprites = {}
"""
    oldspritename :newspritename
"""


offsets = {"tree":[0,-13]}

hideentypes = []

sizeaddons = {"camz":[30,30]}
layeraddons = {}

aplhatypes = {}


with open(f"data/Saved/sizeoffsets.json","w") as file:
    json.dump(sizeoffsets,file)













map = "finale"
startstate = "uitest"
startshaderstate = 0
bakeonreload = 1
showdebugonstart = 0
profile = 0
safemode = 0
startuistate = "def"
showinput = 0
dontsavevar = ["player","easybot","HURT_laser","HURT_biglaser","rolly"]
dontsaveobjtype = ["HPBAR"]







screencol = (110 ,189 ,234 )


camspeeed = 45


poschange = 0

defont = "pixel2.ttf"

renderdist = [20,20]

output = []

buffersize = 50

maxfpsbuffersize = 5


def print(string):
    global output
    """
        prints a string in game in the debug menu
    """
    output.append(str(string))
    if len(output) > buffersize:
        output.pop(0)

def println(string,line):
    global output
    """
        prints onto a specific line if it exists\n
        if not it just adds it on the next line
    """
    while len(output) <= line:
        output.append("")
    output[line] = str(string)
    
	

def update():
    pass
    # global screen_w
    # global screen_h 
    # global realscreeen
    # screen_w = pygame.display.get_window_size()[0]
    # screen_h = pygame.display.get_window_size()[1]
    # realscreeen = pygame.transform.scale(realscreeen,[screen_w,screen_h])
    # print(realscreeen.get_size())














#pyinstaller Engine.py --noconsole --onefile