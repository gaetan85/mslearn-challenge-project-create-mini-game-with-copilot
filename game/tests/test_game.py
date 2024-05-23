from ..engine import round_winner

def test_papper_wins_against_rock():
    assert round_winner("paper", "rock") == 1
