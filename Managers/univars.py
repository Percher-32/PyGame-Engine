import pygame
import funcs
import statemanager as sm



screen_w = 1500


screen_h = 1000


pixelscale = 10


grandim = 32


name = "Project ender"




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

hideentypes = ["camz"]

aplhatypes = {}

map = "null"

startuistate = "def"

screencol = (110,189,234)

startstate = "edit"

camspeeed = 45
