import random

def display_choices():
    print("\nSelect one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_input = input("Enter 1/2/3: ")
    
    options = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}
    return options.get(user_input, None)

def generate_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def evaluate_winner(player, opponent):
    if player == opponent:
        return "It's a Draw!"
    elif (player == "Rock" and opponent == "Scissors") or \
         (player == "Paper" and opponent == "Rock") or \
         (player == "Scissors" and opponent == "Paper"):
        return "You are the Champion!"
    else:
        return "The Computer is Victorious!"

def start_game():
    print("🎮 Welcome to the Rock-Paper-Scissors Arena!")
    player_score = 0
    opponent_score = 0

    while True:
        player_choice = display_choices()
        if not player_choice:
            print("Invalid choice. Please try again.")
            continue

        opponent_choice = generate_computer_choice()

        print(f"\nYou selected: {player_choice}")
        print(f"Computer selected: {opponent_choice}")

        outcome = evaluate_winner(player_choice, opponent_choice)
        print("Outcome:", outcome)

        # Score tracking
        if outcome == "You are the Champion!":
            player_score += 1
        elif outcome == "The Computer is Victorious!":
            opponent_score += 1

        print(f"Current Score => You: {player_score} | Computer: {opponent_score}")

        replay = input("\nWould you like to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    start_game()