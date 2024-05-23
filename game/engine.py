from enum import Enum

Choice = Enum("Choice", ["rock", "paper", "scissors"])

def round_winner(player1: Choice, player2: Choice) -> int:
    if player1 == Choice.rock:
        if player2 == Choice.rock:
            return 0
        if player2 == Choice.paper:
            return 2
        return 1
    if player1 == Choice.paper:
        if player2 == Choice.rock:
            return 1
        if player2 == Choice.paper:
            return 0
        return 2
    if player2 == Choice.rock:
        return 2
    
