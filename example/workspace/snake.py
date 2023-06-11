from dataclasses import dataclass

@dataclass
class Snake:
    body: list
    direction: str

    def move(self):
        pass

    def grow(self):
        pass

    def check_collision(self, width, height):
        pass
