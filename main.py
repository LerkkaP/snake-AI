import pygame
import random

WIDTH = 800
HEIGHT = 600
SIZE = 25

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

class Snake():
    def __init__(self):
        self.size = SIZE
        self.head = pygame.Rect(0, 0, self.size, self.size)
        self.head.center = WIDTH // 2, HEIGHT // 2
        self.head.x = self.head.center[0]
        self.head.y = self.head.center[1]
        self._color = "green"

    def draw_snake(self):
        pygame.draw.rect(screen, self._color, self.head)

class Stimulus():
    def __init__(self):
        self._color = "red"
        self.x = random.randrange(0, WIDTH, SIZE)
        self.y = random.randrange(0, HEIGHT, SIZE)

    def draw_stimulus(self):
        pygame.draw.rect(screen, self._color, pygame.Rect(self.x, self.y, SIZE, SIZE))

snake = Snake()
stimulus = Stimulus()

def helper_grid():
    for x in range(0, WIDTH, SIZE):
        for y in range(0, HEIGHT, SIZE):
            rect = pygame.Rect(x, y, SIZE, SIZE)
            pygame.draw.rect(screen, "white", rect, 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    snake.draw_snake()
    stimulus.draw_stimulus()

    helper_grid()

    pygame.display.flip()

    clock.tick(8)

pygame.quit()