import random
class camera:
	def __init__(self,pos,size):
		self.x = pos[0]
		self.y = pos[1]
		self.a = pos[0]
		self.b = pos[1]
		self.size = size
		self.screenshakevalue = 1000
		self.end = [(0,0),1]
		self.smooth = 3

	def update(self):		
		self.a = self.x
		self.b = self.y
		self.x = self.a
		self.y = self.b
		self.x += random.randint(-1 * self.screenshakevalue,self.screenshakevalue)
		self.y += random.randint(-1 * self.screenshakevalue,self.screenshakevalue)

	def endupdate(self):
		self.cam_focus_size(self.end[0],self.smooth,self.end[1])

	def cam_focus(self,end_pos,smoothing):
		self.x += (end_pos[0] - self.x)/smoothing + random.randint(-1 * self.screenshakevalue,self.screenshakevalue)
		self.y += (end_pos[1] - self.y)/smoothing + random.randint(-1 * self.screenshakevalue,self.screenshakevalue)
		self.size = abs(self.size) + random.randint(-1 * self.screenshakevalue,self.screenshakevalue)

	def cam_focus_size(self,end_pos,smoothing,new_size):
		self.x += (end_pos[0] - self.x)/smoothing + random.randint(-1 * self.screenshakevalue,self.screenshakevalue)
		self.y += (end_pos[1] - self.y)/smoothing + random.randint(-1 * self.screenshakevalue,self.screenshakevalue)
		self.size += (new_size - self.size)/smoothing
		self.size = abs(self.size) + random.randint(-1 * self.screenshakevalue,self.screenshakevalue)

	def cinemachine(self,startpos,endpos,startsize,endsize,smoothing):
		self.x = startpos[0]
		self.y = startpos[1]
		self.size = startsize
		self.cam_focus_size(endpos,smoothing,endsize)
cam = camera((0,0),1)
