from systems.render_system import RenderSystem
from systems.quit_system import QuitSystem

class SceneManager:
    def __init__(self, screen):
        from scenes.menu import MenuScene
        self.current_scene = MenuScene(self)
        self.screen = screen
        self.current_scene.add_system(RenderSystem(self.screen))
        self.current_scene.add_system(QuitSystem())
    
    def system_process(self, dt):
        self.current_scene.process_systems(dt)

    def change_scene(self, new_scene):
        self.current_scene = new_scene