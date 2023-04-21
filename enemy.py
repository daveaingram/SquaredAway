import pygame
from config import ENEMY_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.rect.x -= ENEMY_SPEED

