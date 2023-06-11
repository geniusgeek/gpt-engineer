from snake import Snake
from food import Food

class GameController:
    def __init__(self, snake: Snake, food: Food):
        self.snake = snake
        self.food = food

    def handle_keypress(self, key):
        pass

    def update(self):
        pass
