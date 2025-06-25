class SceneManager:
    def __init__(self):
        from scenes.menu import MenuScene
        self.current_scene = MenuScene(self)
    
    def system_process(self, dt):
        self.current_scene.process_systems(dt)

    def change_scene(self, new_scene):
        self.current_scene = new_scene