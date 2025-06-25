import pygame
from base.scene import Scene
from components.position_component import PositionComponent
from components.render_component import RenderComponent
from config import LEVEL_BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

class LevelScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)

    def _init_entities(self):
        background = self.create_entity()
        background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_image.fill(LEVEL_BACKGROUND_COLOR)
        self.add_component(background, RenderComponent(background_image))
        self.add_component(background, PositionComponent(0, 0))