import pygame
from pygame import Vector2

import configs

pygame.init()

window = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
begin = True

snake_rect = None
snake_length = None
snake_parts = None
snake_direction = None

def update_screen():
    pygame.display.flip()
class Snake:
    def show_snake_parts():
        snake_parts.append(snake_rect.copy())

while running:
    if begin:
        begin = False
        snake_rect = pygame.rect.Rect([200, 200, configs.SNAKE_PART_SIZE, configs.SNAKE_PART_SIZE])
        snake_length = 1
        snake_parts = []
        snake_direction = Vector2(0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False


    window.fill(configs.BG_COLOUR)

    for i in range(0, configs.SCREEN_SIZE, configs.GRID_CELL_SIZE):
        pygame.draw.line(window, configs.GRID_COLOUR, (i, 0), (i, configs.SCREEN_SIZE))
        pygame.draw.line(window, configs.GRID_COLOUR, (0, i), (configs.SCREEN_SIZE, i))

    snake_rect.move_ip(snake_direction)
    Snake.show_snake_parts()

    [pygame.draw.rect(window, configs.SNAKE_COLOUR, snake_part) for snake_part in snake_parts]

    update_screen()

    clock.tick(configs.FPS)

pygame.quit()