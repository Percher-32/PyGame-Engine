import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import cProfile
import pygame
import random
import math


import Game_Code.Player.util_gp as util_gp





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

def main(val:str,to,index=None):
    """
    changes the value a players variable
    """
    if index == None:
        om.set_value("player",val,to)
    else:
        change = to
        to = util_gp.main(val)
        to[index] = change
        om.set_value("player",val,to)