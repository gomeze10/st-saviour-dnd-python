import random
import time
from player import Player
from draw import draw_d6

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
    current_position = 0  # Initialize player's position on the board
    board_length = 54     # Define the length of the board

    print ('lets see how lucky you are!')
    
    # --- FIX 1: The 'check_luck()' function needs to be called to get a value.
    # --- We store the returned value in the 'luck' variable.
    p = Player(name)
    luck = p.check_luck() 

    if luck <= 25:
        print('oh jeez....')
    elif luck <= 75: # Covers 26 to 75 inclusive
        print('') # Prints a blank line
    else: # Covers 76 to 100 inclusive
        print('wow very lucky... for now..')

    # --- FIX 2: The 'check_luck()' call below was redundant.
    # check_luck() 
            
    print('Hello ' + name + '!')
    print_dramatic_text('welcome to monotpoly! ... its like monopoly, but not! because you are broke')
    print ('you have ' + str(money) + ' dollars')

    # --- FIX 3: Need to provide instructions for user input 'a'.
    user_choice = input("Type 'a' to roll the dice: ") 
    if user_choice.lower() == 'a':
        # Roll the first die
        roll1 = random.randint(1, 6)
        print(f"First roll: {roll1}")
        # Assuming draw_d6 can print the ASCII art for a single number
        draw_d6(roll1) 

        # Roll the second die
        roll2 = random.randint(1, 6)
        print(f"Second roll: {roll2}")
        # Assuming draw_d6 can print the ASCII art for a single number
        draw_d6(roll2)

        # Calculate and print the total
        roll_total = roll1 + roll2
        print(f'You rolled a total of {roll_total}')