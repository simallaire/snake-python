class FileIO:
	def __init__(self, score = 0 ):
		self.score = score


	def printScore(self, score = 0,framerate = 0):
		self.score = score
		self.framerate = framerate
		f = open('highscoreCOMP','a+')
		if self.score > 0:
			f.write(str(self.score)+"\t"+str(self.framerate)+"\n")

	def getHighScore(self):
		f = open('highscoreCOMP','r+')
		highscore = 0 
		for l in f:
			strs = l.split("\t")
			if(int(strs[0])>highscore):
				highscore = int(strs[0])
		return highscore
