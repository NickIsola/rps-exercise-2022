#AUTOMATED TESTING "game_test.py FILE

from game import determine_winner


def test_determination_of_the_winner():

    assert determine_winner("rock", "rock") == "It's a tie!"
    assert determine_winner("rock", "paper") == "The computer won. It's ok"
    assert determine_winner("rock", "scissors") == "You win! Congrats"

    assert determine_winner("paper", "rock") == "You win! Congrats"
    assert determine_winner("paper", "paper") == "It's a tie!"
    assert determine_winner("paper", "scissors") == "The computer won. It's ok"

    assert determine_winner("scissors", "rock") == "The computer won. It's ok"
    assert determine_winner("scissors", "paper") == "You win! Congrats"
    assert determine_winner("scissors", "scissors") == "It's a tie!"
