from base.scene import Scene
from pygame import Surface
from systems.render_system import RenderSystem
from systems.menu_input_system import MenuInputSystem

class SceneManager:
    def __init__(self, screen: Surface):
        from scenes.menu import MenuScene
        self.current_scene = MenuScene(self)
        self.screen = screen
        self.current_scene.add_system(MenuInputSystem())
        self.current_scene.add_system(RenderSystem(self.screen))
    
    def system_process(self, dt):
        self.current_scene.process_systems(dt)

    def change_scene(self, new_scene: Scene):
        self.current_scene = new_scene
        self.current_scene.add_system(RenderSystem(self.screen))