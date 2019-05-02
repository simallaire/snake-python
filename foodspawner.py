import random
class FoodSpawner():
	size = 500
    	
	def __init__(self, sizen=500):
		global size
		size=sizen
		self.position = [random.randrange(1,size/10)*10,random.randrange(1,size/10)*10]
		self.isFoodOnScreen = True
	def getX(self):
		return self.position[0]
	def getY(self):
		return self.position[1]
	def spawnFood(self):
		if self.isFoodOnScreen == False:
			self.position = [random.randrange(1,size/10)*10,random.randrange(1,size/10)*10]
			self.isFoodOnScreen = True
		return self.position
	def setFoodOnScreen(self,b):
		self.isFoodOnScreen = b

