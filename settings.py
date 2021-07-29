import pygame

class Settings:
    def __init__(self):
        pygame.font.init()
        self.g = 0.098 /5
        self.bg_colour = (0,0,0)
        self.e = 0.8
        self.white = (255,255,255) 
        self.red = (200,0,0)
        self.font = pygame.font.SysFont(None, 40)