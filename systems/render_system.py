from base.system import System
from config import MENU_BACKGROUND_COLOR
from components.position_component import PositionComponent
from components.render_component import RenderComponent

class RenderSystem(System):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def process(self, dt):
        for entity_id, position, renderable in self.scene.get_components_for_entities(PositionComponent, RenderComponent):
            self.screen.blit(renderable.image, (int(position.x), int(position.y)))