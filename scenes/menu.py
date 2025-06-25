import pygame
from base.scene import Scene
from components.position_component import PositionComponent
from components.render_component import RenderComponent
from config import MENU_BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, FONT, TITLE_DISPLAY_CONFIG, START_DISPLAY_CONFIG

class MenuScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        self._init_entities()

    def _init_entities(self):
        background_entity = self.create_entity()
        background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_image.fill(MENU_BACKGROUND_COLOR)
        self.add_component(background_entity, RenderComponent(background_image))
        self.add_component(background_entity, PositionComponent(0, 0))

        title_entity = self.create_entity()
        font = pygame.font.Font(FONT, TITLE_DISPLAY_CONFIG["size"])
        self.add_component(title_entity, PositionComponent(TITLE_DISPLAY_CONFIG["position"][0], TITLE_DISPLAY_CONFIG["position"][1]))
        self.add_component(title_entity, RenderComponent(font.render(TITLE_DISPLAY_CONFIG["text"], True, TITLE_DISPLAY_CONFIG["color"])))

        start_entity = self.create_entity()
        font = pygame.font.Font(FONT, START_DISPLAY_CONFIG["size"])
        self.add_component(start_entity, PositionComponent(START_DISPLAY_CONFIG["position"][0], START_DISPLAY_CONFIG["position"][1]))
        self.add_component(start_entity, RenderComponent(font.render(START_DISPLAY_CONFIG["text"], True, START_DISPLAY_CONFIG["color"])))