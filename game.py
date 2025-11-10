import random
import time

from player import input
def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    name = input('Name: ')
    role = input('Role: ')

    print('Your name is ' + name + ' and your role is ' + role + '.')
    print_dramatic_text('Our adventure begins in a shady tavern ...')

    player_1 = Player(name, role, strength)
    roll = player_1.roll_20()
    draw_20(roll)
    return roll
