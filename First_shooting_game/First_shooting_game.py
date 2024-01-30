# copy into pycharm to run
import math
import pygame
import random

# initialize the Pygame
pygame.init()

# create game window
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('Felipe')

# background
background = pygame.image.load('./background.png')

# explosion
explosionImg = pygame.image.load('./icons8-bang-64.png')
explosionX = 0
explosionY = 0
explosionX_move = 0


def explosion(x, y):
    screen.blit(explosionImg, (x, y))


# player 64x64
playerImg = pygame.image.load('./icons8-fighter-jet-64.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Target 64x64
targetImg = []
targetX = []
targetY = []
targetX_move = []
targetY_move = []
num_of_targets = 6

for i in range(num_of_targets):
    targetImg.append(pygame.image.load('./comet Right.png'))
    targetX.append(random.randint(100, 700))
    targetY.append(random.randint(50, 150))
    targetX_move.append(1.2)
    targetY_move.append(0.22)


def target(x, y, i):
    screen.blit(targetImg[i], (x, y))


# Bullet 25x25
bulletImg = pygame.image.load('./icons8-bullet-25.png')
bulletX = playerX
bulletY = playerY
bulletY_move = 3.3
bullet_state = 'ready'


# Bullet = ready OR bullet = Fire
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 20, y + 10))


# bullet collision (IMPORT MATH)
def is_collision(targetX, targetY, bulletX, bulletY):
    distance = math.sqrt(math.pow(targetX - bulletX, 2) + math.pow(targetY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# player collision
def collision_player(targetX, targetY, playerX, playerY):
    distance = math.sqrt(math.pow(targetX - playerX, 2) + math.pow(targetY - playerY, 2))
    if distance < 27:
        return True
    else:
        return False


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


# Game over txt
end_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_txt():
    end_text = end_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(end_text, (200, 250))


# player lives txt
lives_font = pygame.font.Font('freesansbold.ttf', 32)
lives_value = 3
lives_textX = 650
lives_textY = 10


def player_lives_txt(x, y):
    lives_txt = lives_font.render("Lives: " + str(lives_value), True, (0, 0, 0))
    screen.blit(lives_txt, (x, y))


# Game loop
running = True
while running:
    # RGB colour of background
    screen.fill((255, 255, 255))
    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check keystroke - movement
        if event.type == pygame.KEYDOWN:
            # Up/Down
            if event.key == pygame.K_DOWN:
                playerY_change = 3
            if event.key == pygame.K_UP:
                playerY_change = -3
            # Right/Left
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            # Shoot bullets
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletY = playerY
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # Let go of key(s)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        # borders
        if playerX <= 0:
            playerX = 0
        if playerX >= 736:
            playerX = 736
        if playerY >= 536:
            playerY = 536
        if playerY <= 400:
            playerY = 400
    # Target movement
    for i in range(num_of_targets):

        # Game over
        if targetY[i] >= 536:
            for j in range(num_of_targets):
                targetY[j] = 2000
            game_over_txt()
            break

        if targetX[i] >= 735:
            targetImg[i] = pygame.image.load('./comet Left.png')
            targetX_move[i] = -0.5
            targetY[i] += 20
        if targetX[i] <= 1:
            targetImg[i] = pygame.image.load('./comet Right.png')
            targetX_move[i] = 0.5
            targetY[i] += 5

        # collision
        collision = is_collision(targetX[i], targetY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = 'ready'
            score_value += 1
            targetX[i] = random.randint(100, 700)
            targetY[i] = random.randint(50, 150)
        target(targetX[i], targetY[i], i)
        targetX[i] += targetX_move[i]
        targetY[i] += targetY_move[i]

        player_collision = collision_player(targetX[i], targetY[i], playerX, playerY)
        if player_collision:
            lives_value -= 1
            targetX[i] = random.randint(100, 700)
            targetY[i] = random.randint(50, 150)
        target(targetX[i], targetY[i], i)
        targetX[i] += targetX_move[i]
        targetY[i] += targetY_move[i]

        if lives_value <= 0:
            for j in range(num_of_targets):
                targetY[j] = 2000
            game_over_txt()
            break

    # Bullet_movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_move
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = 'ready'

    playerY += playerY_change
    playerX += playerX_change
    player(playerX, playerY)
    show_score(textX, textY)
    player_lives_txt(lives_textX, lives_textY)
    pygame.display.update()
