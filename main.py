import random
import sys
import pygame
import numpy
from snake import Snake
from foodspawner import FoodSpawner
from fileio import FileIO

baseFramerate = 1000
size = 600
fIO = FileIO()



def gameover(quitGame=False, score = 0, framerate = 0):
	pygame.quit()
	fIO.printScore(score,framerate)
	if quitGame == True:
		sys.exit(0)
	init(baseFramerate)

def userInput(snake):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover(True)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				snake.changeDirTo("R")
			
			if event.key == pygame.K_LEFT:
				snake.changeDirTo("L")
			
			if event.key == pygame.K_DOWN:
				snake.changeDirTo("D")
			
			if event.key == pygame.K_UP:
				snake.changeDirTo("U")

def compInput(snake, foodpos):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover(True)
	moved = False
	if snake.getDir() != "U" and snake.getDir() != "D":
		if snake.getX()+10 >= size and moved==False:
			if snake.getY() <= size/2:
				snake.changeDirTo("D")
				moved = True
			else:
				snake.changeDirTo("U")
				moved = True
		if snake.getX()-10 < 0 and moved==False:
			if snake.getY() <= size/2:
				snake.changeDirTo("D")
				moved = True
			else:
				snake.changeDirTo("U")
				moved = True
	if snake.getDir() != "L" and snake.getDir() != "R":	
		if snake.getY()+10 >= size and moved==False:
			if snake.getX() <= size/2:
				snake.changeDirTo("R")
				moved = True
			else:
				snake.changeDirTo("L")
				moved = True
		if snake.getY()-10 < 0 and moved==False:
			if snake.getX() <= size/2:
				moved = True
				snake.changeDirTo("R")
			else:
				moved = True
				snake.changeDirTo("L")

	if  moved==False:
		if snake.getX() < foodpos[0] :
			snake.changeDirTo("R")
			moved = True
		elif snake.getX() > foodpos[0]:
			snake.changeDirTo("L")
			moved = True
		else:	
			if snake.getY() < foodpos[1] :
				snake.changeDirTo("D")
				moved=True
			else:
				snake.changeDirTo("U")
				moved=True   			

	

def init(framerate):
	global size
	window = pygame.display.set_mode((size, size))
	pygame.display.set_caption("SNAKE")
	fps = pygame.time.Clock()

	score = 0

	snake = Snake(size)
	food = FoodSpawner(size)

	highscore = "\t Highscore: "+str(fIO.getHighScore())


	while True:
		# userInput(snake)

		foodpos = food.spawnFood()
		compInput(snake,foodpos)


		if(snake.move(foodpos) == 1):
			score += 1
			if(score%5 == 0 and score > 0):
				framerate += 1
			if(foodpos == snake.position):
    				food.setFoodOnScreen(False)



				


		window.fill(pygame.Color(0, 0, int(abs(numpy.sin(score)*50))))
		for pos in snake.getBody():
			pygame.draw.rect(window, pygame.Color(0, 255, 0), pygame.Rect(pos[0], pos[1], 10,10))
		pygame.draw.rect(window, pygame.Color(255, 0, 0), pygame.Rect(foodpos[0], foodpos[1], 10, 10))

		if snake.checkCollision() == 1:
			gameover(False, score, framerate)
		pygame.display.set_caption("Snake | Score:"+str(score)+highscore+"\t speed:"+str(framerate))
		pygame.display.flip()
		fps.tick(framerate)

		

			
init(baseFramerate)
