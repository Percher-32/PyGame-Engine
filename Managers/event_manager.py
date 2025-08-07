#event_manager
import pygame
import json
import Managers.inst as inst
import os
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range (pygame.joystick.get_count())] 
for joystick in joysticks:
    joystick.init()
with open(os.path.join("Saved/ps4_keys.json"), "r+") as file:
    button_keys = json.load(file)
analog_keys =  {0:0,1:0,2:0,3:0,4:0,5:0}
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
		self.open = True
		self.keyb = False
		self.keyr = False
		self.analog_keys =  {0:0,1:0,2:0,3:0,4:0,5:0}
		self.controller = {
							"x": False,
							"circle": False,
							"square": False,
							"triangle": False,
							"share": False,
							"PS": False,
							"options": False,
							"left_stick_click": False,
							"right_stick_click": False,
							"L1": False,
							"R1": False,
							"up_arrow": False,
							"down_arrow": False,
							"left_arrow": False,
							"right_arrow": False,
							"touchpad": False

							}
		self.controllerrel = {
							"x": False,
							"circle": False,
							"square": False,
							"triangle": False,
							"share": False,
							"PS": False,
							"options": False,
							"left_stick_click": False,
							"right_stick_click": False,
							"L1": False,
							"R1": False,
							"up_arrow": False,
							"down_arrow": False,
							"left_arrow": False,
							"right_arrow": False,
							"touchpad": False

							}
							

		self.controllerjab = {
							"x": False,
							"circle": False,
							"square": False,
							"triangle": False,
							"share": False,
							"PS": False,
							"options": False,
							"left_stick_click": False,
							"right_stick_click": False,
							"L1": False,
							"R1": False,
							"up_arrow": False,
							"down_arrow": False,
							"left_arrow": False,
							"right_arrow": False,
							"touchpad": False

							}

	def next(self):
		self.key = pygame.key.get_pressed()
		self.mouse = pygame.mouse.get_pressed()
		self.mousepos = pygame.mouse.get_pos()
		self.Mouseb = False
		self.Mouser = False
		self.scroll = 0
		self.keyb = False
		self.keyr = False
		self.keydown = False

		for i in self.controllerrel.keys():
			self.controllerrel[i] = False

		for i in self.controllerjab.keys():
			self.controllerjab[i] = False


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				self.running = False
				with open("Saved/Spritecache.json","w") as file:
					json.dump(inst.dataspritecache,file)
				exit()


			if event.type == pygame.KEYDOWN:
				self.code = event.unicode

			if event.type == pygame.JOYAXISMOTION:
				self.analog_keys[event.axis] = event.value 




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
		self.open = False

