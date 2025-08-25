#Cammanager
import random
import Managers.univars as univars
import Managers.Cameramod as Cameramod
class Cammanager:
	def __init__(self,cam):
		self.cameras = {"def":[[0,0],1,0]}
		self.currentcam = "def"
		self.cam = cam

	def addcam(self,name,pos,size):
		"""add a new camera or set the conditions of a camera"""
		self.cameras[name] = [pos,size,0]

	def setcam(self,name):
		"""set the in-use camera to a different one"""
	
		if self.cam.size != self.cameras[name][1]:
			univars.camchange = True
		else:
			univars.camchange = False
		if self.cam.x == self.cameras[name][0][0] and self.cam.y == self.cameras[name][0][1]:
			univars.poschange = False
		else:
			univars.poschange = True
		self.cam.x = self.cameras[name][0][0]
		self.cam.y = self.cameras[name][0][1]
		self.cam.size = self.cameras[name][1]
		self.cam.screenshakevalue = self.cameras[name][2]
		self.currentcam = name


	def getcam(self,cam,item):
		"""to get the conditions for a camera , cam : camera-name  ,  item : [ pos ,size or shake ] """
		index = {"pos":0,"size":1,"shake":2}
		if item == "posx":
			return self.cameras[cam][0][0]
		elif item == "posy":
			return self.cameras[cam][0][1]
		else:
			toch = index[item]
			return self.cameras[cam][toch]

	def setcond(self,cam,item,val):
		"""to set the conditions for a camera , cam : camera-name  ,  item : [ pos ,size or shake ]  ,  val :  what to set it to \n
			["pos","size","shake"] """
		index = {"pos":0,"size":1,"shake":2}
		if item == "posx":
			self.cameras[cam][0][0] = val
		elif item == "posy":
			self.cameras[cam][0][1] = val
		else:
			toch = index[item]
			self.cameras[cam][toch] = val

	def delcam(self,name):
		"""remove a camera"""
		self.cameras.pop(name)

	def cam_focus(self,name,end_pos,smoothing):
		self.cameras[name][0][0] += (end_pos[0] - self.cameras[name][0][0])/smoothing + random.randint(-1 * self.cameras[name][2],self.cameras[name][2])
		self.cameras[name][0][1] += (end_pos[1] - self.cameras[name][0][1])/smoothing + random.randint(-1 * self.cameras[name][2],self.cameras[name][2])
		# self.cameras[name][1] = abs(self.cameras[name][1])

	def cam_focus_size(self,name,end_pos,smoothing,new_size):
		self.cameras[name][0][0] += (end_pos[0] - self.cameras[name][0][0])/smoothing + random.randint(-1 * self.cameras[name][2],self.cameras[name][2])
		self.cameras[name][0][1] += (end_pos[1] - self.cameras[name][0][1])/smoothing + random.randint(-1 * self.cameras[name][2],self.cameras[name][2])
		self.cameras[name][1] += (new_size - self.cameras[name][1])/smoothing
		self.cameras[name][1] = abs(self.cameras[name][1])

	def update(self):
		self.setcam(self.currentcam)

camager = Cammanager(Cameramod.cam)
