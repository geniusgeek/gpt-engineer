from snake import Snake
from food import Food

class GameView:
    def __init__(self, snake: Snake, food: Food):
        self.snake = snake
        self.food = food

    def draw(self):
        pass
