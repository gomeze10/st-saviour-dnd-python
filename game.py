import random
import time
from player import Player # Assuming player.py defines a Player class
from draw import draw_d6 # Assuming draw.py defines a draw_d6 function

def print_dramatic_text(text: str, delay=0.05):
    """Prints text character by character with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def apply_board_event(player, position):
    """Checks the position and applies the associated event."""
    # Define events for specific positions
    board_events = {
        1: ("A homeless guy felt bad for you and gave you some change.", "gain", 1),
        2: ("You got mugged by a six year old, ", 'lose', 3),
        3: ("You found a dollar on the ground!", 'gain', 1),
        4: ("You stood in a cool people only zone and got fined", 'lose', 4),
        5: ("You thought you found 2 dollars! it was a leaf", 'gain', 0),
        7: ("You got pickpocketed of $2!", 'lose', 2),
        10: ("You found a hidden stash of coins!", 'gain', 3),
        12: ("A kind stranger gave you $5!", 'gain', 5),
        15: ("You received a small inheritance!", 'gain', 8),
        18: ("You stepped on a street vendor's merchandise and had to pay a $3 fine!", 'lose', 3),
        21: ("Lost your wallet! $5 gone!", 'lose', 5),
        24: ("Won a small bet on a street game!", 'gain', 4),
        25: ("You found a winning lottery ticket worth $10!", 'gain', 10),
        28: ("Had to pay for an emergency taxi ride: $3!", 'lose', 3),
        30: ("A rogue tax collector took $4 from you!", 'lose', 4),
        33: ("Found some forgotten cash in an old coat pocket!", 'gain', 2),
        36: ("Paid a surprise utility bill: $6!", 'lose', 6),
        38: ("You did a quick chore for a shop owner and earned $2!", 'gain', 2),
        40: ("Invested in a good cause, and it paid off! Gained $7!", 'gain', 7),
        42: ("Parking ticket fine: $4!", 'lose', 4),
    }

    if position in board_events:
        description, event_type, amount = board_events[position]
        event_happened = True
        # Check if the player is lucky enough to try and avoid the event
        if player.luck > 70:
            print_dramatic_text(f"You landed on an event! Your high luck (score: {player.luck}) might help you avoid this event! Rolling for a save...")
            save_roll1 = random.randint(1, 6)
            # draw_d6(save_roll1) # Commented out as draw_d6 not provided in context
            save_roll2 = random.randint(1, 6)
            # draw_d6(save_roll2) # Commented out as draw_d6 not provided in context
            print(f"Save roll 1: {save_roll1}, Save roll 2: {save_roll2}")

            # If either die is greater than 4, the event does not happen
            if save_roll1 > 4 or save_roll2 > 4:
                print_dramatic_text("Phew! Your luck saved you. You avoided the event!")
                event_happened = False
            else:
                print_dramatic_text("Bad luck with the save rolls! The event still affects you.")

        if event_happened:
            print_dramatic_text(description)
            if event_type == 'gain':
                player.money += amount # Modify player's money directly
                print(f"You gained ${amount}.")
            elif event_type == 'lose':
                player.money -= amount # Modify player's money directly
                print(f"You lost ${amount}.")
            # Ensure money doesn't drop below zero
            if player.money < 0:
                player.money = 0
                print_dramatic_text("You are completely broke!")
            print(f"You now have ${player.money}.")

def create_players():
    """Prompts the user for the number of players and their names."""
    num_players = 0
    while num_players < 1:
        try:
            num_players = int(input("How many players (1 or more)? "))
            if num_players < 1:
                print("Please enter a number of players greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    players = []
    for i in range(num_players):
        player_name = input(f"Enter name for Player {i + 1}: ")
        new_player = Player(player_name) # Initialize the player's position and money
        new_player.position = 0
        new_player.money = 10 # Example starting money
        new_player.luck = random.randint(1, 100) # Example luck initialization
        players.append(new_player)
    return players

if __name__ == '__main__':
    # --- Character Creation (Multiplayer style) ---
    players = create_players()
    board_length = 44
    rent_threshold = 20
    game_running = True
    print("\n--- Game Start ---")

    for current_player in players:
        # Display the luck value just once at the start of their turn
        luck = current_player.luck
        name = current_player.name
        if luck <= 25:
            print_dramatic_text(f"{name}\'s luck: {luck}, oh jeez....") # Corrected f-string syntax
        elif luck > 25 and luck < 75:
            print(f"{name}\'s luck: {luck}, not too bad")
        elif luck > 75:
            print_dramatic_text(f"{name}\'s luck: {luck}, wow very lucky for you...") # Corrected f-string syntax

    while game_running:
        for current_player in players:
            print(f"\n--- {current_player.name}'s Turn (Money: ${current_player.money}, Position: {current_player.position}) ---")
            
            user_choice = input("Type 'a' to roll the dice, or 'q' to quit game: ")

            if user_choice.lower() == 'q':
                print_dramatic_text("Thanks for playing Mononpoly!") # Corrected typo
                game_running = False
                break # Exit the inner player loop
            elif user_choice.lower() == 'a':
                previous_position = current_player.position

                # Roll dice
                roll1 = random.randint(1, 6)
                roll2 = random.randint(1, 6)
                print(f"First roll: {roll1}")
                draw_d6(roll1) # Assuming draw_d6 is working
                print(f"Second roll: {roll2}")
                draw_d6(roll2) # Assuming draw_d6 is working
                roll_total = roll1 + roll2

                # Calculate new position and check if Go was passed
                current_player.position = (current_player.position + roll_total) % board_length
                print(f"You rolled a total of {roll_total}.")
                print(f"Your current position is: {current_player.position}")

                if current_player.position < previous_position:
                    current_player.money += 2
                    print_dramatic_text("You passed Go! You received $100! but there is a 98 percent income tax, so you only got 2")
                    print(f"You now have ${current_player.money}.")

                # --- Apply Board Event ---
                # Pass the player object to the event function so it can modify their money directly
                apply_board_event(current_player, current_player.position)

                # Check win condition after all events
                if current_player.money >= rent_threshold:
                    print_dramatic_text(f"{current_player.name} made rent! for this month..")
                # Here it just continues to the next player/turn
            else:
                print_dramatic_text("Invalid input. Please type 'a' to roll or 'q' to quit.")