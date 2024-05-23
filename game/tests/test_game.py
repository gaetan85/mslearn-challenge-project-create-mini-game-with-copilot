from ..engine import round_winner, Choice

def test_papper_wins_against_rock():
    assert round_winner(Choice.paper, Choice.rock) == 1

def test_rock_equal_rock():
    assert round_winner(Choice.rock, Choice.rock) == 0