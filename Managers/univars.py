import pygame
import json
import Managers.funcs as funcs
import Managers.statemanager as sm



screen_w = 1500


screen_h = 1000

camchange = True

pixelscale = 15


grandim = 32


name = "Project ender"

maxfps = 500


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
uiscreen = pygame.Surface((screen_w,screen_h))
realscreeen = pygame.display.set_mode((screen_w,screen_h),pygame.RESIZABLE)
pygame.display.set_caption(name)

screen_rect = screen.get_rect(center = (0,0))

func = funcs.func(screen,grandim)





sizeoffsets = {"grass":[0.1,0.1],"dirt":[0.1,0.1]}

instables = ["dirt","grass","def"]

extras = [["def","camz",[20,20]]]

offsets = {"tree":[0,-13]}

hideentypes = ["camz"]

aplhatypes = {}


with open(f"Saved/sizeoffsets.json","w") as file:
    json.dump(sizeoffsets,file)







map = "null"

startstate = "edit"



#opt to optimise
mode = 1

startuistate = "def"

screencol = (110 - 100,189 - 100,234 - 100)


camspeeed = 45


poschange = 0

defont = "pixel2.ttf"

renderdist = 45


maxfpsbuffersize = 5

def update():
    global screen_w
    global screen_h 
    global uiscreen
    screen_w = realscreeen.get_width()
    screen_h = realscreeen.get_height()
    uiscreen = pygame.transform.scale(uiscreen,[screen_w,screen_h])


