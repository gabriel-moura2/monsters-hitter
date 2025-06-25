import pygame
from base.system import System

class QuitSystem(System):
    def process(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()