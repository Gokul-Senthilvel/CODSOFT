import random

# Initialize scores
user_score = 0
computer_score = 0

def get_user_choice():
    """
    Prompts the user to enter their choice (rock, paper, or scissors).
    Returns the user's choice as a string.
    """
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """
    Generates a random choice for the computer.
    Returns the computer's choice as a string.
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the user's choice and the computer's choice.
    Returns 'win', 'lose', or 'tie'.
    """
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

def play_game():
    """
    Plays a single round of the Rock-Paper-Scissors game.
    Updates the user's and computer's scores based on the result.
    """
    global user_score, computer_score

    print("\nRock-Paper-Scissors Game\n")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == 'win':
        print("You win!")
        user_score += 1
    elif result == 'lose':
        print("You lose!")
        computer_score += 1
    else:
        print("It's a tie!")

    print(f"Score: You {user_score} - Computer {computer_score}")

def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    """
    play_again = 'y'
    while play_again.lower() == 'y':
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()