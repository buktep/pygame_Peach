import pygame
from player import *

screen_width = 800
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('aaa game')

bg = pygame.image.load("asset/images/background.jpeg")
bg = pygame.transform.scale(bg,(800,600))

py = pygame.image.load('asset/images/player.png')
py = pygame.transform.scale(py, (96,30))

player = Plaaayer(340, 500, py)

fps = pygame.time.Clock()

run = True
while run == True:
    for aaa in pygame.event.get():
        if aaa.type == pygame.QUIT:
            run = False

    screen.blit(bg, (0,0))
    player.draw(screen)
    player.move()
    player.check_edge()
    fps.tick(60)
    pygame.display.update()