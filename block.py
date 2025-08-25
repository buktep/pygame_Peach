import pygame


class Block():
    def __init__(self, x,y, image):
        self.image = image
        self.rect = self.image.get_rect(x=x, y=y)
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))