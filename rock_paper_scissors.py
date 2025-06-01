import random

# Available options
choices = ['rock', 'paper', 'scissors']

# Helper mapping for determining the winner
choice_to_index = {
    'rock': 0,
    'paper': 1,
    'scissors': 2
}

def play_round():
    """Play a single round of Rock Paper Scissors."""
    user_choice = input("Choose (rock/paper/scissors): ").strip().lower()
    if user_choice not in choice_to_index:
        print("Invalid choice. Try again.")
        return
    comp_choice = random.choice(choices)
    print(f"Computer chose: {comp_choice}")
    user_idx = choice_to_index[user_choice]
    comp_idx = choice_to_index[comp_choice]
    if user_idx == comp_idx:
        print("It's a tie!")
    elif (user_idx - comp_idx) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")


def main():
    """Run the Rock Paper Scissors game loop."""
    print("Welcome to Rock Paper Scissors!")
    while True:
        play_round()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
