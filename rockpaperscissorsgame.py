import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Game rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    
    while True:
        print("\nCurrent Score:")
        print(f"Player: {player_score}  Computer: {computer_score}")
        
        # Get player choice
        player_choice = input("\nEnter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        
        if player_choice == 'quit':
            print("\nFinal Score:")
            print(f"Player: {player_score}  Computer: {computer_score}")
            print("Thanks for playing!")
            break
            
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
            
        # Get computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

# Start the game
rock_paper_scissors()