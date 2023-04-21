import pygame
from config import PLAYER_START_POS

class Player:
    def __init__(self, pos):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.velocity = pygame.math.Vector2(0, 0)
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        # Apply gravity
        self.velocity.y += 1

        # Move left and right
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        else:
            self.velocity.x = 0

        # Jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity.y = -20
            self.on_ground = False

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                elif self.velocity.y < 0:
                    self.rect.top = platform.rect.bottom
                self.velocity.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
