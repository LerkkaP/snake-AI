import pygame
import random
from settings import WIDTH, HEIGHT, SIZE, RED

class Stimulus():
    def __init__(self, snake_body):
        self.snake_body = snake_body
        self.rect = self.random_position()
        
    def random_position(self):
        while True:
            new_pos = pygame.Rect(
                random.randrange(0, WIDTH, SIZE),
                random.randrange(0, HEIGHT, SIZE),
                SIZE,
                SIZE
            )
            if new_pos not in self.snake_body:
                return new_pos

    def draw_stimulus(self, screen):
        pygame.draw.rect(screen, RED, self.rect)        

    def collision(self, head):
        if self.rect.colliderect(head):
            self.rect = self.random_position()
            return True
        return False