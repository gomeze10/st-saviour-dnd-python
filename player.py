# player.py
import random

class Player:
    def __init__(self, name: str):
        self.name = name
        # Initialize luck and money here
        self.luck = random.randint(1, 100)
        self.money = 10
        self.position = 0

    def check_luck(self) -> int:
        print(f"{self.name}, your luck number is: {self.luck} out of 100")
        return self.luck

    def roll_d6(self) -> int:
        roll = random.randint(1, 6)
        print(f"{self.name}, you rolled a {roll}!")
        return roll
