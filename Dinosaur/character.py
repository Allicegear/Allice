import pygame
import pygame.image
import pygame.surface
import pygame.rect

class Characters:
    def __init__(self, game) -> None:
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    def blitme(self) :
        self.screen.fill((123,22,3))
        self.screen.blit(self.image, self.rect)
        

