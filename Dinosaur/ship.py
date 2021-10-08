import pygame
import pygame.image
import pygame.surface
import pygame.rect

class Ship:
    def __init__(self, game) -> None:
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False
    def blitme(self) :
        self.screen.blit(self.image, self.rect)
    def update(self) :
        if self.move_right:
            self.rect.x +=1
        elif self.move_left:
            self.rect.x -=1

