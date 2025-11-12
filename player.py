import random
from draw import draw_d20
class player:
    def __init__(self, name: str):
        self.name = name
        self.luck = random.randint(1, 100)
        self.money = 10

def check_luck(self) -> int:
    luck = random.randint(1, 100)
    print(f"Your luck number is: {luck}")

def roll_d20(self) -> int:
    roll = random.randint(1, 20)
    return roll