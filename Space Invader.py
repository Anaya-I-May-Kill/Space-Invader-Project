import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 500))

# Background
background = pygame.image.load('Background.png')

# Sound
mixer.music.load("Background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
playerX = 370
playerY = 380
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0 , 736))
    enemyY.append(random.randint(50 , 150))
    enemyX_change.append(4)
    enemyX_change.append(40)
    
#Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletIMG = pygame.image.load('Bullet.png')
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x , y):
    score = font.render("Score : " + str(score_value) , True , (255 , 255 , 255))
    screen.blit(score , (x , y))
    

def game_over_text():
    over_text = over_font.render("GAME OVER" , True , (255 , 255 , 255))
    screen.blit(over_text , (200 , 500))
    
    
def player(x , y):
    screen.blit(playerImg , (x , y))
    
    
def enemy(x , y , i):
    screen.blit(enemyImg[i] , (x , y))
    
    
def fire_bullet(x , y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG , (x + 16 , y + 10))
    
    
def isCollision(enemyX , enemyY , bulletX , bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
    
# Game Loop