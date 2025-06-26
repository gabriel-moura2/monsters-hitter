from base.component import Component

class RenderComponent(Component):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()