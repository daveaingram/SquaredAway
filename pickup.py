import pygame
from config import PICKUP_SIZE

class Pickup(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((PICKUP_SIZE, PICKUP_SIZE))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
