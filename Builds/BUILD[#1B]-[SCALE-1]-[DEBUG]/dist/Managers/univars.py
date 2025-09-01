import pygame
import json
import Managers.funcs as funcs
import Managers.statemanager as sm


pygame.display.init()

scaledown = 3




screen_w = pygame.display.get_desktop_sizes()[0][0]/scaledown
screen_h = pygame.display.get_desktop_sizes()[0][1]/scaledown
# print((pygame.display.get_desktop_sizes()[0][0] **2 + pygame.display.get_desktop_sizes()[0][1] **2  ) ** 0.5)
startdims = (screen_w,screen_h)

camchange = True

pixelscale = 15


grandim = 32


name = "Project ender"

maxfps = 60


(40, 41, 83)
(75, 63, 114)
(220, 214, 247)
(163, 173, 225)
(169, 117, 145)


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
}

screen = pygame.Surface((64 * pixelscale,64 * pixelscale))
fakescreen = pygame.Surface((64 * pixelscale,64 * pixelscale))
fakescreen.set_colorkey((0,0,0))


uiscreen = pygame.Surface((screen_w,screen_h))
finalscreen = pygame.display.set_mode((screen_w,screen_h),pygame.OPENGL|pygame.DOUBLEBUF|pygame.SCALED|pygame.FULLSCREEN,vsync=1)
realscreeen = pygame.Surface((screen_w,screen_h))
pygame.display.set_caption(name)

screen_rect = screen.get_rect(center = (0,0))

func = funcs.func(grandim)
"""
    Use this one
"""



lumptype = {"grass":"ground","dirt":"ground","slantl":"slantl","slantr":"slantr","slantdecor":"ground","rail":"rail","rail-diag":"rail"}

sizeoffsets = {}

instables = ["dirt","grass","def","slantl","slantr","slantlbot","slantrbot","rail","rail-diag"]

extras = [["def","camz",[20,20]]]
"""
    [Original sprite  ,  new sprite type  ,  size scale]
"""

newsprites = {"slantdecor":"slantr"}
"""
    oldspritename :newspritename
"""


offsets = {"tree":[0,-13]}

hideentypes = ["camz"]

aplhatypes = {}


with open(f"Saved/sizeoffsets.json","w") as file:
    json.dump(sizeoffsets,file)












map = "maindemo"
startstate = "debugame"
startshaderstate = 0
bakeonreload = 0
showdebugonstart = 0
profile = 0
safemode = 1
startuistate = "def"
showinput = 0







screencol = (110 ,189 ,234 )


camspeeed = 45


poschange = 0

defont = "pixel2.ttf"

renderdist = [12,12]



maxfpsbuffersize = 5




def update():
    pass
    # global screen_w
    # global screen_h 
    # screen_w = pygame.display.get_window_size()[0]
    # screen_h = pygame.display.get_window_size()[1]
    # realscreeen = pygame.transform.scale(realscreeen,[screen_w,screen_h])
    # print(realscreeen.get_size())

























