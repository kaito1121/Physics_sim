import pygame
import settings
from pygame.sprite import Sprite
class Ball(Sprite):
    def __init__(self,sim,x,y):
        super().__init__()
        self.screen = sim.screen
        self.settings = settings.Settings()
        self.tx = 0
        self.ty = 0
        self.vx = x/150
        self.vy = y/150
        self.rect = pygame.Rect(0, 1000, 10,10)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
       # self.rect  pygame.Circle

    def update(self):
        self.vy -= self.settings.g
        self.x += self.vx
        self.y += - self.vy +  self.settings.g/2
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.settings.white, self.rect)

    def _check_ball(self):
        if self.y >=  1000:
            self.vy *= -self.settings.e
            self.y = 999