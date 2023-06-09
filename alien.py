import pygame
from pygame.sprite import Sprite


class Alien(Sprite):


     def __init__(self, ai_game):
         super().__init__()
         self.screen = ai_game.screen
         self.settings = ai_game.settings
         self.image = pygame.image.load('images/enemy.png')
         self.rect = self.image.get_rect()
         self.rect.x = self.rect.width
         self.rect.y = self.rect.height
         self.x = float(self.rect.x)

     def update(self):
         #Перемещает пришельца вправо
         self.x += self.settings.alien_speed
         self.rect.x = self.x
         #Перемещает пришельца влево или вправо.
         self.x += (self.settings.alien_speed *
                      self.settings.fleet_direction)

     def check_edges(self):
         #Возвращает True, если пришелец находится у края экрана.
         screen_rect = self.screen.get_rect()
         if self.rect.right >= screen_rect.right or self.rect.left <= 0:
             return True


     def blitime(self):

         self.screen.blit(self.image, self.rect)