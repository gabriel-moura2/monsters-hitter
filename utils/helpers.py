import pygame

def load_image(name):
    path = f"assets/images/{name}.png"
    return pygame.image.load(path).convert_alpha()

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return pygame.mixer.Sound(path)