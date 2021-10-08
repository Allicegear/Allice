
from character import Characters
from settings import Settings
import sys
import pygame.display
import pygame
import pygame.event
from pygame.constants import QUIT
from ship import Ship

class GirlInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_w,self.setting.screen_h))
        pygame.display.set_caption("Girl Invasions")
        self.ship = Ship(self)
        #self.char = Characters(self)
    def run_game(self):
        while True:
            self._handle_event()
            self.ship.update()
            self._refresh_screen()
    def _handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = False    
    def _refresh_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        #self.char.blitme()
        pygame.display.flip()
if __name__ == '__main__':
    ai = GirlInvasion()
    ai.run_game()

