import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result}")

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 5

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number} of {rounds}")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"\nScores after Round {round_number}: You: {user_score} | Computer: {computer_score}\n")

    if user_score > computer_score:
        print("Congratulations! You are the winner!")
    elif computer_score > user_score:
        print("The computer is the winner. Better luck next time!")
    else:
        print("The game is a tie overall!")

def play_again():
    while True:
        play_again = input("Do you want to play another set of 5 rounds? (yes/no): ").lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def start_game():
    while True:
        play_game()
        if not play_again():
            break

start_game()
