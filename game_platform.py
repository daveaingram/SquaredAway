import pygame
from config import PLATFORM_WIDTH, PLATFORM_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)

