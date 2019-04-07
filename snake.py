
size = 500
class Snake:
	def __init__(self, size = 500):
		self.position = [size/5,size/10]
		self.body = [[size/5,size/10],[size/5-10,size/10],[size/5-20,size/10]] 
		self.direction = "RIGHT"
		self.changeDirectionTo = self.direction


	def changeDirTo(self,dir):
		if dir=="RIGHT" and not self.direction=="LEFT":
			self.direction = "RIGHT"
		if dir=="LEFT" and not self.direction=="RIGHT":
			self.direction = "LEFT"
		if dir=="UP" and not self.direction=="DOWN":
			self.direction = "UP"
		if dir=="DOWN" and not self.direction=="UP":
			self.direction = "DOWN"

	def move(self,foodPos):
		if self.direction == "RIGHT":
			self.position[0] += 10
		if self.direction == "LEFT":
			self.position[0] -= 10
		if self.direction == "UP":
			self.position[1] -= 10
		if self.direction == "DOWN":
			self.position[1] += 10
		self.body.insert(0,list(self.position))
		if self.position == foodPos:
			return 1
		else:
			self.body.pop()
			return 0

	def checkCollision(self):
		if self.position[0] > size-10 or self.position[0] < 0:
			return 1
		elif self.position[1] > size-10 or self.position[1]<0:
			return 1
		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1

		return 0 

	def getHeadPos(self):
		return self.position
	def getBody(self):
		return self.body