import pygame

class Plaaayer():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self):
        press = pygame.key.get_pressed()
        if press[pygame.K_RIGHT] or press[pygame.K_d]:
            self.rect.x += 1
        if press[pygame.K_LEFT] or press[pygame.K_a]:
            self.rect.x -= 1
        if press[pygame.K_UP] or press[pygame.K_w]:
            self.rect.y -= 1
        if press[pygame.K_DOWN] or press[pygame.K_s]:
            self.rect.y += 1
            
    def check_edge(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 600 - self.rect.h:
            self.rect.y = 600 - self.rect.h
        if self.rect.x >= 800 - self.rect.w:
            self.rect.x = 800 - self.rect.w
