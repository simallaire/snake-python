import pygame
import sys
import random
import time
from snake import Snake
from foodspawner import FoodSpawner
from fileio import FileIO
import numpy


baseFramerate = 20
size = 500
fIO =  FileIO()



def gameOver(quit=False, score = 0,framerate=0):
	pygame.quit()
	fIO.printScore(score,framerate)
	if quit == True:
		sys.exit()
	init(baseFramerate)


def init(framerate):
	framerate = framerate	
	window = pygame.display.set_mode((size,size))
	pygame.display.set_caption("SNAKE")
	fps = pygame.time.Clock()

	score = 0

	snake = Snake(size)
	food = FoodSpawner()

	highscore = "\t Highscore: "+str(fIO.getHighScore())


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver(True)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					snake.changeDirTo("RIGHT")
				
				if event.key == pygame.K_LEFT:
					snake.changeDirTo("LEFT")
				
				if event.key == pygame.K_DOWN:
					snake.changeDirTo("DOWN")
				
				if event.key == pygame.K_UP:
					snake.changeDirTo("UP")


		for i in range(random.randrange(1,3)):
			foodPos = food.spawnFood()

		if(snake.move(foodPos)==1):
			score+=1
			if(score%5==0 and score>0):
				framerate+=3.5
			food.setFoodOnScreen(False)

		window.fill(pygame.Color(0,0,int(abs(numpy.sin(score)*50))))
		for pos in snake.getBody():
			pygame.draw.rect(window,pygame.Color(0,255,0),pygame.Rect(pos[0],pos[1],10,10))
		pygame.draw.rect(window,pygame.Color(255,0,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
		if snake.checkCollision()==1:
			gameOver(False,score,framerate)
		pygame.display.set_caption("Snake | Score:"+str(score)+highscore+"\t speed:"+str(framerate))
		pygame.display.flip()
		fps.tick(framerate)

	

			
init(baseFramerate)
