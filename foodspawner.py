import random
size = 500
class FoodSpawner():
	def __init__(self):
		self.position = [random.randrange(1,size/10)*10,random.randrange(1,size/10)*10]
		self.isFoodOnScreen = True

	def spawnFood(self):
		if self.isFoodOnScreen == False:
			self.position = [random.randrange(1,size/10)*10,random.randrange(1,size/10)*10]
			self.isFoodOnScreen = True
		return self.position
	def setFoodOnScreen(self,b):
		self.isFoodOnScreen = b

