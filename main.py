import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

class Snake():
    def __init__(self):
        self.size = 10
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = WIDTH // 2, HEIGHT // 2
        self._color = "white"

    def draw_snake(self):
        pygame.draw.rect(screen, self._color, self.rect)

snake = Snake()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    snake.draw_snake()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()