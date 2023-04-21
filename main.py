import pygame
import sys
from config import WINDOW_SIZE, FPS, PLAYER_START_POS, STARTING_PLATFORM_POS, BLACK
from player import Player
from game_platform import Platform
from enemy import Enemy
from menu import Menu
import random
import pygame.time

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Side Scroller Game")
clock = pygame.time.Clock()

ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1


def initialize_game_objects():
    player = Player(PLAYER_START_POS)
    platforms = [Platform(STARTING_PLATFORM_POS)]

    grid_width = 4
    grid_height = 4
    cell_width = WINDOW_SIZE[0] // grid_width
    cell_height = WINDOW_SIZE[1] // grid_height

    for i in range(grid_height):
        for j in range(grid_width):
            x = random.randint(j * cell_width + 50, (j + 1) * cell_width - 50)
            y = random.randint(i * cell_height + 50, (i + 1) * cell_height - 50)
            platforms.append(Platform((x, y)))

    enemies = [Enemy((600, 470))]
    return player, platforms, enemies


def spawn_enemy(player, enemies):
    min_distance_from_player = 150
    x = random.randint(0, WINDOW_SIZE[0] - 50)
    y = random.randint(0, WINDOW_SIZE[1] - 100)

    while abs(player.rect.x - x) < min_distance_from_player and abs(player.rect.y - y) < min_distance_from_player:
        x = random.randint(0, WINDOW_SIZE[0] - 50)
        y = random.randint(0, WINDOW_SIZE[1] - 100)

    enemies.append(Enemy((x, y)))


def player_collides_with_enemy(player, enemies):
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            return True
    return False


def is_off_screen(enemy):
    return enemy.rect.y > WINDOW_SIZE[1] or enemy.rect.x > WINDOW_SIZE[0]


def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


def main():
    menu = Menu(screen)

    playing_game = False
    player, platforms, enemies = initialize_game_objects()

    pygame.time.set_timer(ENEMY_SPAWN_EVENT, 3000)

    score = 0
    score_timer = 0

    while True:

        delta_time = clock.tick(FPS)

        if not playing_game:
            menu.display_start_menu()
            score_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if playing_game and event.type == ENEMY_SPAWN_EVENT:
                spawn_enemy(player, enemies)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing_game = True

        if playing_game:
            player.update(platforms)
            for enemy in enemies:
                enemy.update()

            # Remove off-screen enemies
            enemies = [enemy for enemy in enemies if not is_off_screen(enemy)]

            score_timer += delta_time
            if score_timer >= 1000:  # Increment score every 1000 milliseconds (1 second)
                score += 1
                score_timer = 0

            screen.fill(BLACK)
            screen.blit(player.image, player.rect)
            for platform in platforms:
                screen.blit(platform.image, platform.rect)
            for enemy in enemies:
                screen.blit(enemy.image, enemy.rect)

            draw_text(screen, f"Score: {score}", 36, (255, 255, 255), 10, 10)
            pygame.display.flip()

            if player.rect.y > WINDOW_SIZE[1] or player_collides_with_enemy(player, enemies):
                playing_game = False
                menu.display_game_over_menu(score)
                player, platforms, enemies = initialize_game_objects()
                score = 0

        clock.tick(FPS)

if __name__ == "__main__":
    main()

