import pygame
from player import *
from ball import *
from block import *

screen_width = 800
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('aaa game')

bg = pygame.image.load("asset/images/background.jpeg")
bg = pygame.transform.scale(bg,(800,600))

py = pygame.image.load('asset/images/player.png')
py = pygame.transform.scale(py, (96,30))

bl = pygame.image.load('asset/images/ball.png')
bl = pygame.transform.scale(bl, (23,23))

rooppap = pygame.image.load('asset/images/block.png')
rooppap = pygame.transform.scale(rooppap,(50,25))

block1 = Block(100, 100, rooppap)

player = Plaaayer(340, 500, py)

ball = Ball(350, 300, bl)

fps = pygame.time.Clock()
def ball_check():
    if ball.rect.colliderect(player.rect):
        ball.dy = -1

run = True
while run == True:
    for aaa in pygame.event.get():
        if aaa.type == pygame.QUIT:
            run = False

    screen.blit(bg, (0,0))
    ball_check()
    ball.move()
    ball.check_edge()
    ball.draw(screen)
    block1.draw(screen)
    player.draw(screen)
    player.move()
    player.check_edge()
    fps.tick(60)
    pygame.display.update()