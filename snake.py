import pygame
from settings import SIZE, WIDTH, HEIGHT, UP, DOWN, LEFT, RIGHT

class Snake():
    def __init__(self):
        self.size = SIZE
        self.direction = RIGHT
        self.body = [
            pygame.Rect(WIDTH // 2, HEIGHT // 2, SIZE, SIZE),
            pygame.Rect(WIDTH // 2 - SIZE, HEIGHT // 2, SIZE, SIZE),
            pygame.Rect(WIDTH // 2 - SIZE*2, HEIGHT // 2, SIZE, SIZE),
        ]
        self.head = self.body[0]
        self._color = "green"

    def draw_snake(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, self._color, part, border_radius=5)

    def move_snake(self):
        previous_positions = [part.topleft for part in self.body]

        # head movement
        self.head.x += self.direction[0]
        self.head.y += self.direction[1]

        # rest of the body
        for i in range(1, len(self.body)):
            self.body[i].topleft = previous_positions[i - 1]     

    def grow_snake(self):
        tail = self.body[-1]
        self.body.append(pygame.Rect(tail.x, tail.y, SIZE, SIZE))

    def set_direction(self, keys):
        if keys[pygame.K_UP] and self.direction != DOWN:
            self.direction = UP
        elif keys[pygame.K_DOWN] and self.direction != UP:
            self.direction = DOWN
        elif keys[pygame.K_LEFT] and self.direction != RIGHT:
            self.direction = LEFT
        elif keys[pygame.K_RIGHT] and self.direction != LEFT:
            self.direction = RIGHT

    def collision(self):
        screen_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        # out of screen
        if not screen_rect.contains(self.head):
            return True
        # crashes own body
        elif self.head in self.body[1:]:
            return True

    def get_state(self, stimulus):
        def danger_at(x, y):
            rect = pygame.Rect(x, y, SIZE, SIZE)
            # wall collision
            if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
                return 1
            # body collision
            if rect in self.body:
                return 1
            return 0

        x = self.head.x
        y = self.head.y
        dx, dy = self.direction

        danger_straight = danger_at(x + dx, y + dy)
        danger_left = danger_at(x - dy, y + dx)
        danger_right = danger_at(x + dy, y - dx)

        stimulus_left = stimulus.rect.x < x
        stimulus_right = stimulus.rect.x > x
        stimulus_up = stimulus.rect.y < y
        stimulus_down = stimulus.rect.y > y

        return (
            danger_straight,
            danger_left,
            danger_right,
            stimulus_left,
            stimulus_right,
            stimulus_up,
            stimulus_down
        )
