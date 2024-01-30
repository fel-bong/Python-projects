#rune runner
import random as rand
import pygame
from pygame import *
from pygame import K_SPACE
import math
import time

#initialize
pygame.init()

#game window
screen = pygame.display.set_mode((800,800))

#title (and icon)
pygame.display.set_caption('Rune Runner')

#background
background = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/ground background.jpeg')

#player 64x59
playerImg = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Soldier/soldier1_MAIN.png')
playerX = 400
playerY = 400
playerX_change = 0
playerY_change = 0

# player collision
def collision_player(enemyX, enemyY, playerX, playerY):
	distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
	if distance < 40:
		return True
	else:
		return False

#original
def originpath():
	global background
	if background == pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/ground background.jpeg'):
		return
	else:	
		background = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/ground background.jpeg')
#new Path
def path1():
	global background
	if background == pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Grass background.jpeg'):
		return
	else:
		background = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Grass background.jpeg')

#EnemySpawn1
spawn1_X = 460
spawn1_Y = 460

#enemy 60x60
enemyImg = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Enemy/Enemy1_MAIN.png')
enemyX = spawn1_X
enemyY = spawn1_Y
enemyX_change = 0
enemyY_change = 0

#enemymovement
starting_d = rand.randint(0, 4)
if starting_d == 1:
	enemyX_change = 2
if starting_d == 2:
	enemyX_change = -2
if starting_d == 3:
	enemyY_change = 2
if starting_d == 4:
	enemyY_change = -2

def enemy(x, y):
	screen.blit(enemyImg, (x, y))

def player(x, y):
	screen.blit(playerImg, (x, y))

#game loop
running = True
while running:
	screen.fill((255, 255, 255))
	#background
	screen.blit(background, (0, 0))
	#closewindow
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#death
	player_collision = collision_player(enemyX, enemyY, playerX, playerY)
	if player_collision:
		quit()

	#EnemyRandomMovement
	randomborderXleft = rand.randint(700,799)
	randomborderXright = rand.randint(1,100)
	randomborderYdown = rand.randint(1,100)
	randomborderYup = rand.randint(700,799)
	if enemyX <= randomborderXright:
		enemyX_change = 1
	if enemyX >= randomborderXleft:
		enemyX_change = -1
	if enemyY >= randomborderYup:
		enemyY_change = -1
	if enemyY <= randomborderYdown:
		enemyY_change = 1

	#PlayerMovement-keydown
	if event.type == pygame.KEYDOWN:
		#up/down
		if event.key == K_DOWN:
			playerImg = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Soldier/soldier1_MAIN.png')
			playerY_change = 2.8
		if event.key == K_UP:
			playerImg = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Soldier/Soldier1_walkingUP.png')
			playerY_change = -2.8
		# Right/Left
		if event.key == K_LEFT:
			playerImg = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Soldier/Soldier1_walkingLEFT.png')
			playerX_change = -2.8
		if event.key == K_RIGHT:
			playerImg = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Soldier/Soldier1_walkingRIGHT.png')
			playerX_change = 2.8
	#PlayerMovement-keyup
	if event.type == pygame.KEYUP:
		playerImg = pygame.image.load('/Applications/Python 3.8/Python_codes/RuneRunner/Soldier/soldier1_MAIN.png')
		if event.key == K_UP or event.key == K_DOWN:
			playerY_change = 0
		if event.key == K_LEFT or event.key == K_RIGHT:
			playerX_change = 0
	#borders
	if playerX <= 0:
		playerX = 735
		originpath()

	if playerX >= 736:
		playerX = 1
		path1()

	if playerY >= 736:
		playerY = 736
	if playerY <= 0:
		playerY = 0
	if enemyX <= 0:
		enemyX = 0
	if enemyX >= 736:
		enemyX = 736
	if enemyY >= 736:
		enemyY = 736
	if enemyY <= 0:
		enemyY = 0

	playerY += playerY_change
	playerX += playerX_change
	enemyX += enemyX_change
	enemyY += enemyY_change
	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()