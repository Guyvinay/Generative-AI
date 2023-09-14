import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'user'
    else:
        return 'computer'

def update_score(winner, scores):
    if winner == 'user':
        scores['user'] += 1
    elif winner == 'computer':
        scores['computer'] += 1
    else:
        scores['draw'] += 1
    return scores

def display_score(scores):
    print(f"User: {scores['user']} | Computer: {scores['computer']} | Draws: {scores['draw']}")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def main():
    print("Welcome to Rock, Paper, Scissors!")
    scores = {'user': 0, 'computer': 0, 'draw': 0}
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        scores = update_score(winner, scores)
        display_score(scores)
        
        if not play_again():
            break
    
    print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()
