import pygame
import random

WIDTH = 600
HEIGHT = 400
SIZE = 25

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

UP    = (0, -SIZE)
DOWN  = (0, SIZE)
LEFT  = (-SIZE, 0)
RIGHT = (SIZE, 0)

class Snake():
    def __init__(self):
        self.size = SIZE
        self.head = pygame.Rect(WIDTH // 2, HEIGHT // 2, self.size, self.size)
        self.direction = RIGHT
        self._color = "green"

    def draw_snake(self):
        pygame.draw.rect(screen, self._color, self.head)

    def move_snake(self):
        self.head.x += self.direction[0]
        self.head.y += self.direction[1]

    def set_direction(self, keys):
        if keys[pygame.K_UP] and self.direction != DOWN:
            self.direction = UP
        elif keys[pygame.K_DOWN] and self.direction != UP:
            self.direction = DOWN
        elif keys[pygame.K_LEFT] and self.direction != RIGHT:
            self.direction = LEFT
        elif keys[pygame.K_RIGHT] and self.direction != LEFT:
            self.direction = RIGHT

class Stimulus():
    def __init__(self):
        self._color = "red"
        self.rect = pygame.Rect(random.randrange(0, WIDTH, SIZE),
                                random.randrange(0, HEIGHT, SIZE),
                                SIZE,
                                SIZE)

    def draw_stimulus(self):
        pygame.draw.rect(screen, self._color, self.rect)        

    def collision(self, head_rect):
        if self.rect.colliderect(head_rect):
            self.rect.topleft = (
                random.randrange(0, WIDTH, SIZE),
                random.randrange(0, HEIGHT, SIZE)
            )

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

    keys = pygame.key.get_pressed() 

    screen.fill("black")

    snake.draw_snake()
    stimulus.draw_stimulus()
    stimulus.collision(snake.head)
    snake.set_direction(keys)
    snake.move_snake()

    helper_grid()

    pygame.display.flip()

    clock.tick(10)

pygame.quit()