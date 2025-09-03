import pygame
from player import *
from ball import *
from block import *

screen_width = 800
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('aaa game')

#background
bg = pygame.image.load("asset/images/background.jpeg")
bg = pygame.transform.scale(bg,(800,600))

#player
py = pygame.image.load('asset/images/player.png')
py = pygame.transform.scale(py, (96,30))

#ball
bl = pygame.image.load('asset/images/ball.png')
bl = pygame.transform.scale(bl, (23,23))

#block
rooppap = pygame.image.load('asset/images/block.png')
rooppap = pygame.transform.scale(rooppap,(50,25))

#object
player = Plaaayer(340, 500, py)
ball = Ball(350, 300, bl)
block1 = Block(100, 100, rooppap)

#frame rate
fps = pygame.time.Clock()

#function
def ball_check():
    if ball.rect.colliderect(player.rect):
        ball.dy = -1

run = True
#game loop
while run == True:
    for aaa in pygame.event.get():
        if aaa.type == pygame.QUIT:
            run = False

    #BACKGROUND
    screen.blit(bg, (0,0))
    
    #BALL
    ball_check()
    ball.move()
    ball.check_edge()
    ball.draw(screen)
    
    #BLOCK
    block1.draw(screen)
    
    #PLAYER
    player.draw(screen)
    player.move()
    player.check_edge()
    
    fps.tick(60)
    pygame.display.update()

pygame.quit()