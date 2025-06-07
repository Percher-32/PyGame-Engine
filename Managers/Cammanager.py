#Cammanager
import random
import Cameramod
class Cammanager:
	def __init__(self,cam):
		self.cameras = {"def":[[0,0],1,0]}
		self.currentcam = "def"
		self.cam = cam

	def addcam(self,name,pos,size):
		self.cameras[name] = [pos,size,0]

	def setcam(self,name):
		self.cam.x = self.cameras[name][0][0]
		self.cam.y = self.cameras[name][0][1]
		self.cam.size = self.cameras[name][1]
		self.cam.screenshakevalue = self.cameras[name][2]
		self.currentcam = name
	
	def setcond(self,cam,item,val):
		index = {"pos":0,"size":1,"shake":2}
		toch = index[item]
		self.cameras[cam][toch] = val

	def delcam(self,name):
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
