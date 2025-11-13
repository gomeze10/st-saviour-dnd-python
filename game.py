import random
import time
from player import Player
from draw import draw_d6

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def apply_board_event(player, position, money):
    """Checks the position and applies the associated event."""
    # Define events for specific positions
    board_events = {
        3: ("You found a dollar on the ground!", "gain", 1),
        7: ("You got pickpocketed of $2!", "lose", 2),
        12: ("A kind stranger gave you $5!", "gain", 5),
        18: ("You stepped on a street vendor's merchandise and had to pay a $3 fine!", "lose", 3),
        25: ("You found a winning lottery ticket worth $10!", "gain", 10),
        30: ("A rogue tax collector took $4 from you!", "lose", 4),
        38: ("You did a quick chore for a shop owner and earned $2!", "gain", 2),
    }
    
    if position in board_events:
        description, event_type, amount = board_events[position]

        event_happened = True
        # Check if the player is lucky enough to try and avoid the event
        if luck > 70:
            print_dramatic_text(f"You landed on an event! Your high luck (score: {luck}) might help you avoid this event! Rolling for a save...")
            save_roll1 = random.randint(1, 6)
            draw_d6(save_roll1)
            save_roll2 = random.randint(1, 6)
            draw_d6(save_roll2)
            print(f"Save roll 1: {save_roll1}, Save roll 2: {save_roll2}")

            # If either die is greater than 4, the event does not happen
            if save_roll1 > 4 or save_roll2 > 4:
                print_dramatic_text("Phew! Your luck saved you. You avoided the event!")
                event_happened = False
            else:
                print_dramatic_text("Bad luck with the save rolls! The event still affects you.")

        if event_happened:
            print_dramatic_text(description)
            if event_type == "gain":
                money += amount
                print(f"You gained ${amount}.")
            elif event_type == "lose":
                money -= amount
                print(f"You lost ${amount}.")

            # Ensure money doesn't drop below zero
            if money < 0:
                money = 0
                print_dramatic_text("You are completely broke!")

            print(f"You now have ${money}.")

    return money

if __name__ == '__main__':
    # --- Character Creation ---
    name = input('What is your name? ')
    p = Player(name)

    # Collect character class input (simple example)
    money = 10
    board_length = 44
    original_position = 0
    current_position = 0

    print ('lets see how lucky you are!')
    luck = p.check_luck()
    if luck <= 25:
        print_dramatic_text('oh jeez....')
    elif luck <= 75:
        print_dramatic_text('')
    else:
        print_dramatic_text('wow very lucky... for now... but is it really that good?')

    # --- Print Character Sheet ---
    print("\n--- Character Sheet ---")
    print(f"Name: {p.name}")
    print(f"Starting Money: ${money}")
    print("-----------------------\n")

    print_dramatic_text('Welcome to Monotpoly! ... its like Monopoly, but not! because you are broke.')
    print (f'You have ${money}.')

    # --- Game Loop ---
    while True:
        user_choice = input("Type 'a' to roll the dice, or 'q' to quit: ")

        if user_choice.lower() == 'a':
            previous_position = current_position
            
            # Roll dice
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            print(f"First roll: {roll1}")
            draw_d6(roll1)
            print(f"Second roll: {roll2}")
            draw_d6(roll2)
            roll_total = roll1 + roll2

            # Calculate new position and check if "Go" was passed
            current_position = (current_position + roll_total) % board_length
            
            print(f'You rolled a total of {roll_total}.')
            print(f"Your current position is: {current_position}")

            if current_position < previous_position:
                money += 2
                print_dramatic_text("You passed Go! You received $100! but there is a 98 percent income tax, so you only got 2")
                print(f"You now have ${money}, you need 20 to make rent for this month")
            
            # --- Apply Board Event ---
            money = apply_board_event(p, current_position, money)

            # Check win condition after all events
            if money >= 20:
                print_dramatic_text ('you made rent! for this month.. press q to end game, a to continue playing for next month!!')

        elif user_choice.lower() == 'q':
            print_dramatic_text("Thanks for playing Monotpoly!")
            break
        
        # This part handles the win condition check for the *next* loop iteration if 'a' was selected and the user has enough money
        if money >= 20:
             # This check is technically redundant here as the break condition will be handled by the next user input ('q' or 'a')
             pass 
        else:
             # Ensure the game continues if rent isn't met and user hasn't quit
             pass