import pygame
import settings
from pygame.sprite import Sprite
class Platform(Sprite):
    def __init__(self,sim,x,y,width,height,colour):
        super().__init__()
        self.screen = sim.screen
        self.colour = colour
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

    def draw_platform(self):
        pygame.draw.rect(self.screen,self.colour,self.rect)