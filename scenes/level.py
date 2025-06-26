import pygame
from base.scene import Scene
from components.position_component import PositionComponent
from components.render_component import RenderComponent
from config import LEVEL_BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SIZE, BALL_COLOR

class LevelScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        self._init_entities()

    def _init_entities(self):
        background = self.create_entity()
        background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_image.fill(LEVEL_BACKGROUND_COLOR)
        self.add_component(background, RenderComponent(background_image))
        self.add_component(background, PositionComponent(0, 0))

        ball_entity = self.create_entity()
        ball_image = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(ball_image, BALL_COLOR, (BALL_SIZE / 2, BALL_SIZE / 2), BALL_SIZE / 2)
        self.add_component(ball_entity, RenderComponent(ball_image))
        self.add_component(ball_entity, PositionComponent(SCREEN_WIDTH / 2, SCREEN_HEIGHT - BALL_SIZE))