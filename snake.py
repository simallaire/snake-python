
size = 500
class Snake:
	def __init__(self, size = 500):
		self.position = [size/5,size/10]
		self.body = [[size/5,size/10],[size/5-10,size/10],[size/5-20,size/10]] 
		self.direction = "R"
		self.changeDirectionTo = self.direction


	def changeDirTo(self,dir):
		if dir=="R" and not self.direction=="L":
			self.direction = "R"
		if dir=="L" and not self.direction=="R":
			self.direction = "L"
		if dir=="U" and not self.direction=="D":
			self.direction = "U"
		if dir=="D" and not self.direction=="U":
			self.direction = "D"

	def move(self,foodPos):
		if self.direction == "R":
			self.position[0] += 10
		if self.direction == "L":
			self.position[0] -= 10
		if self.direction == "U":
			self.position[1] -= 10
		if self.direction == "D":
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