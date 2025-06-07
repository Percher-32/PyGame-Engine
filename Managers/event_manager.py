#event_manager
import pygame
import json
import os
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range (pygame.joystick.get_count())] 
for joystick in joysticks:
    joystick.init()
with open(os.path.join("ps4_keys.json"), "r+") as file:
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
		self.x = False
		self.sq = False
		self.tri = False
		self.cir = False
		self.xb = False
		self.sqb = False
		self.trib = False
		self.cirb = False
		self.xr = False
		self.sqr = False
		self.trir = False
		self.cirr = False
		self.scroll = 0
		self.open = True
		self.keyb = False
		self.keyr = False

	def next(self):
		self.key = pygame.key.get_pressed()
		self.mouse = pygame.mouse.get_pressed()
		self.mousepos = pygame.mouse.get_pos()
		self.Mouseb = False
		self.Mouser = False
		self.xb = False
		self.sqb = False
		self.trib = False
		self.cirb = False
		self.xr = False
		self.sqr = False
		self.trir = False
		self.cirr = False
		self.scroll = 0
		self.keyb = False
		self.keyr = False
		self.keydown = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()


			if event.type == pygame.KEYDOWN:
				self.code = event.unicode

			if event.type == pygame.JOYAXISMOTION:
				analog_keys[event.axis] = event.value 
			if event.type == pygame.JOYBUTTONDOWN:
				if event.button == button_keys["x"]:
					self.x = True
					self.xb = True
				if event.button == button_keys["circle"]:
					self.cir = True
					self.cirb = True
				if event.button == button_keys["triangle"]:
					self.tri = True
					self.trib = True
				if event.button == button_keys["square"]:
					self.sq = True
					self.sqb = True
				
				
			if event.type == pygame.JOYBUTTONUP:
				if event.button == button_keys["x"]:
					self.x = False
					self.xr = True
				if event.button == button_keys["circle"]:
					self.cir = False
					self.cirr = True 
				if event.button == button_keys["triangle"]:
					self.tri = False
					self.trir = True 
				if event.button == button_keys["square"]:
					self.sq = False
					self.sqr = True





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
