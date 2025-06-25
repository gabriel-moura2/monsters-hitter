import pygame, asyncio
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from core.scene_manager import SceneManager

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = SceneManager(self.screen)
        
    async def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            self.scene_manager.system_process(dt)
            pygame.display.flip()
            await asyncio.sleep(0)