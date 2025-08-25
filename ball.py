import pygame

class Ball():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(x=x,y=y)
        self.dx = 1
        self.dy = 1
        self.speed = 3
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed
        
    def check_edge(self):
        if self.rect.y >= 600 - self.rect.h:
            self.rect.y = 600 - self.rect.h
            self.dy = -1
        if self.rect.x >= 800 - self.rect.w:
            self.rect.x = 800 - self.rect.w
            self.dx = -1
        if self.rect.y <= 0:
            self.rect.y = 0
            self.dy = 1
        if self.rect.x <= 0:
            self.rect.x = 0
            self.dx = 1