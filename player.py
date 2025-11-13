import random
from draw import draw_d6
class Player:
    def __init__(self, name: str):
        self.name = name
        self.luck = random.randint(1, 100)
        self.money = 10

    def check_luck(self) -> int:
        luck = random.randint(1, 100)
        print(f"Your luck number is: {luck}")
        return luck

    def roll_d6(self) -> int:
        roll = random.randint(1, 6)
        return roll