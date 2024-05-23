from engine import round_winner, Choice
import random

# generate a random choice for the computer
def generate_computer_choice():
    return random.choice(list(Choice))

def play():
    scores = {"player1": 0, "player2": 0}
    print("Playing game")
    print("You are player 1")
    while True:
        scores = round(scores)
        print("Scores:")
        print(f"Player 1: {scores['player1']}")
        print(f"Player 2: {scores['player2']}")
        # ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            break

def round(scores):
    end_scores = scores.copy()
    print("Playing round")
    # ask user for input
    user_choice = input("Enter your choice: ")
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice")
        return end_scores
    player1 = Choice[user_choice]
    # generate computer choice
    player2 = generate_computer_choice()
    print(f"Player 2 choice: {player2}")
    # determine winner
    winner = round_winner(player1, player2)
    # print winner
    if winner == 0:
        print("It's a tie!")
    elif winner == 1:
        print("You win!")
        end_scores["player1"] += 1
    else:
        print("You lose!")
        end_scores["player2"] += 1
    return end_scores

if __name__ == '__main__':
    play()