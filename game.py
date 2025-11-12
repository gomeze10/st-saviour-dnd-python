import random
import time

from player import player
from player import check_luck
from draw import draw_d20
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

    name = input('What is your name? ')
    money = 10

    print ('lets see how lucky you are!')
    
def check_luck():
    luck = random.randint(1, 100)
    print(f"Your luck number is: {luck} out of 100") # Optional: show the number

    if luck <= 25:
        print('oh jeeves....')
    elif luck <= 75: # Covers 26 to 75 inclusive
        print('') # Prints a blank line
    else: # Covers 76 to 100 inclusive
        print('wow very lucky... for now..')

# Call the function to run the code
check_luck()
        

print('Hello ' + name + '!')
print_dramatic_text('welcome to monotpoly! ... its like monopoly, but not! because you are broke')
print ('you have ' + str(money) + ' dollars')

print ('press A to roll dice')
if input == 'A' or 'a':
    player_1 = player(name)
    roll = draw_d20(1)
    draw_d20(roll)