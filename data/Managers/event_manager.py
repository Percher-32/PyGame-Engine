#event_manager
import pygame
import copy
import json
import data.Managers.inst as inst
import os
import data.Managers.univars as univars
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range (pygame.joystick.get_count())] 
for joystick in joysticks:
    joystick.init()
with open(os.path.join("data/Saved/controller-binds/ps.json"), "r+") as file:
    button_keys = json.load(file)
analog_keys =  {0:0,1:0,2:0,3:0,4:0,5:0}




init_dict = {
  "A": 0,
  "B": 0,
  "X": 0,
  "Y": 0,
  "START": 0,
  "BACK": 0,
  "OPT" : 0,
  "LSK": 0,
  "RSK": 0,
  "LB": 0,
  "RB": 0,
  "MAIN": 0,
  "SHARE":0,
  "SELECT":0,

  "up_arrow": 0,
  "down_arrow": 0,
  "left_arrow": 0,
  "right_arrow": 0,
  "touchpad": 0
  }


class event_manager:
	def __init__(self):
		self.code = 0
		self.key = pygame.key.get_pressed()
		self.mouse = pygame.mouse.get_pressed()
		self.mousepos = pygame.mouse.get_pos()
		self.Mouseb = False
		self.Mouser = False
		self.running = True
		self.scroll = 0
		self.releasekey = False
		self.open = True
		self.lastmouse = False
		self.keyb = False
		self.keyr = False
		self.analog_keys =  {0:0,1:0,2:0,3:0,4:0,5:0}
		self.controller = copy.deepcopy(init_dict)
		self.controllerrel = copy.deepcopy(init_dict)
		self.controllerjab = copy.deepcopy(init_dict)
		"""
			contains values for wether a button has just been pressed
		"""

	def next(self):
		
		self.lastmouse = self.mouse
		self.key = pygame.key.get_pressed()
		self.mouse = pygame.mouse.get_pressed()
		self.mousepos = [pygame.mouse.get_pos()[0]/univars.scaledown,pygame.mouse.get_pos()[1]/univars.scaledown]
		self.Mouseb = False
		self.Mouser = False
		self.scroll = 0
		self.releasekey = False
		self.keyb = False
		self.keyr = False
		self.keydown = False
#   
# 
		for i in self.controllerrel.keys():
			self.controllerrel[i] = False

		for i in self.controllerjab.keys():
			self.controllerjab[i] = False


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				self.running = False
				with open("data/Saved/Spritecache.json","w") as file:
					json.dump(inst.dataspritecache,file)


			if event.type == pygame.KEYDOWN:
				self.code = event.unicode
				self.keydown = 1
				self.releasekey = 0

			if event.type == pygame.JOYAXISMOTION:
				self.analog_keys[event.axis] = event.value 


			if event.type == pygame.KEYUP:
				self.releasekey = 1




			if event.type == pygame.JOYBUTTONDOWN:
				for i in button_keys.keys():
					if event.button == button_keys[i]:
						self.controller[i] = True
						self.controllerjab[i] = True
				
			if event.type == pygame.JOYBUTTONUP:
				for i in button_keys.keys():
					if event.button == button_keys[i]:
						self.controller[i] = False
						self.controllerrel[i] = True
				

			if event.type == pygame.MOUSEBUTTONDOWN:
				self.Mouseb = True
				self.mouse = pygame.mouse.get_pressed()

			if event.type == pygame.MOUSEBUTTONUP:
				self.Mouser = True

			if event.type == pygame.MOUSEWHEEL:
				self.scroll = event.y


			if event.type == pygame.KEYDOWN:
				self.keyb = True
				self.keydown = True


			if event.type == pygame.KEYUP:
				self.keyr = True
				self.keydown = False
		


	def close(self):
		pygame.quit()
		self.running = False
		with open("data/Saved/Spritecache.json","w") as file:
			json.dump(inst.dataspritecache,file)
		exit()

