

import random

CHOICES = ["rock", "paper", "scissors"]


def get_player_choice():
    """Prompt the player, convert to lowercase, validate, and return the choice."""
    choice = input("Enter rock, paper, scissors: ").strip().lower()
    while choice not in CHOICES:
        print(f'Sorry, "{choice}" is not a valid choice. Please try again.')
        choice = input("Enter rock, paper, scissors: ").strip().lower()
    return choice


def determine_winner(player, computer):
    """Compare the two choices and return "win", "loss", or "tie"."""
    if player == computer:
        return "tie"

    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if beats[player] == computer:
        return "win"
    return "loss"


def get_number_of_rounds():
    """Ask how many rounds to play and make sure it's a positive odd number."""
    response = input("How many rounds would you like to play: ")
    while True:
        if response.isdigit() and int(response) > 0 and int(response) % 2 == 1:
            return int(response)
        response = input("Sorry, the number must be an odd number. Please try again: ")


def main():
    print("Welcome to Rock Paper Scissors!")
    rounds = get_number_of_rounds()

    player_wins = 0
    computer_wins = 0
    rounds_played = 0

    # Ties don't count, so keep going until the requested number of rounds is decided
    while rounds_played < rounds:
        player_choice = get_player_choice()
        computer_choice = random.choice(CHOICES)
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You won!")
            player_wins += 1
            rounds_played += 1
        elif result == "loss":
            print("You lost!")
            computer_wins += 1
            rounds_played += 1
        else:
            print("Tie! Play again.")

    print("-------------------------------------------")
    print(f"Score — You: {player_wins} | Computer: {computer_wins}")
    if player_wins > computer_wins:
        print("You win!!!")
    else:
        print("The computer wins!")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
