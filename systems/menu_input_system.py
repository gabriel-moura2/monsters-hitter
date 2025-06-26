import pygame
from base.system import System
from scenes.level import LevelScene
from systems.level_input_system import LevelInputSystem

class MenuInputSystem(System):
    def process(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                new_scene = LevelScene(self.scene.manager)
                new_scene.add_system(LevelInputSystem())
                self.scene.manager.change_scene(new_scene)