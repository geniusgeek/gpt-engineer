import sys
import pygame
from snake import Snake, Food

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.snake = Snake([(width // 2, height // 2)], (1, 0))
        self.food = Food(width, height, self.snake.body)
        self.game_over = False

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                self.snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                self.snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                self.snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                self.snake.direction = (1, 0)

    def update(self):
        self.snake.move()
        if self.snake.check_collision(self.width, self.height):
            self.game_over = True
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food = Food(self.width, self.height, self.snake.body)

    def is_game_over(self):
        return self.game_over
