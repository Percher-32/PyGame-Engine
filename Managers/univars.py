import pygame
import funcs
import statemanager as sm



screen_w = 1500


screen_h = 1000

camchange = False

pixelscale = 7


grandim = 32


name = "Project ender"

maxfps = 10000


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


screen = pygame.Surface((64 * pixelscale,64 * pixelscale))
realscreeen = pygame.display.set_mode((screen_w,screen_h),pygame.RESIZABLE)
pygame.display.set_caption(name)

screen_rect = screen.get_rect(center = (0,0))

func = funcs.func(screen,grandim)


instables = ["dirt","grass","def"]

extras = [["def","camz",[20,20]]]

offsets = {"tree":[0,-13]}

hideentypes = ["camz"]

aplhatypes = {}

map = "green"

mode = 1

startuistate = "def"

screencol = (110,189,234)

startstate = "editgame"

camspeeed = 45

sizes = {
    "smallbutton": (150,75),
    "mediumbutton": (200,100),
    "semilargebutton":(250,250/2),
    "largebutton": (300,150),
}

poschange = 0

defont = "pixel2.ttf"

renderdist = 45

def update():
    global screen_w
    global screen_h 
    screen_w = realscreeen.get_width()
    screen_h = realscreeen.get_height()
