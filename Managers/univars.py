import pygame
import funcs
import statemanager as sm



screen_w = 1500


screen_h = 1000


pixelscale = 8


grandim = 32


name = "Project ender"


theme = [(100, 13, 95),(217, 22, 86),(235, 91, 0),(255, 178, 0)]


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


