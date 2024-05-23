def round_winner(player1: str, player2: str) -> int:
    if player1 == "rock" and player2 == "scissors":
        return 1
    if player1 == "rock" and player2 == "paper":
        return 2
    if player1 == "scissors" and player2 == "rock":
        return 2
    if player1 == "scissors" and player2 == "paper":
        return 1
    if player1 == "paper" and player2 == "rock":
        return 1
    if player1 == "paper" and player2 == "scissors":
        return 2
    return 0