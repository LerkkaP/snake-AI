import pygame
from snake import Snake
from stimulus import Stimulus
from settings import WIDTH, HEIGHT, FPS, BLACK

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

snake = Snake()
stimulus = Stimulus()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() 
    snake.set_direction(keys)
    snake.move_snake()
    
    if stimulus.collision(snake.head):
        snake.grow_snake()
    if snake.collision():
        running = False

    screen.fill(BLACK)
    snake.draw_snake(screen)
    stimulus.draw_stimulus(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()