import pygame
import sys
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def display_start_menu(self):
        self.screen.fill(BLACK)
        text = self.font.render("Press SPACE to start", True, WHITE)
        self.screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2))
        pygame.display.flip()

    def display_game_over_menu(self, score):
        self.screen.fill(BLACK)
        text = self.font.render(f"Game Over! Score: {score}", True, WHITE)
        self.screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
