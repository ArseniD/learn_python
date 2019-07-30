import pytest

from tennis import tennis_score


# the way to pass an arguments, to test case effectively
examples = (("expected_score", "player1_points", "player2_points", "comment"),
[
("Love-All", 0, 0, "even_scores"),
("Fifteen-All", 1, 1, "even_scores"),
("Thirty-All", 2, 2, "even_scores"),
("Love-Fifteen", 0, 1, "early_games_with_uneven_scores"),
("Fifteen-Love", 1, 0, "early_games_with_uneven_scores"),
("Thirty-Fifteen", 2, 1, "early_games_with_uneven_scores"),
("Forty-Thirty", 3, 2, "early_games_with_uneven_scores"),
("Advantage Player 1", 4, 3, "endgame_with_uneven_scores"),
("Advantage Player 2", 5, 6, "endgame_with_uneven_scores"),
("Advantage Player 1", 13, 12, "endgame_with_uneven_scores"),
("Deuce", 3, 3, "endgame_with_even_scores"),
("Deuce", 4, 4, "endgame_with_even_scores"),
("Deuce", 14, 14, "endgame_with_even_scores"),
("Win for Player 1", 4, 0, "there_is_a_winner"),
("Win for Player 2", 2, 4, "there_is_a_winner"),
("Win for Player 1", 6, 4, "there_is_a_winner"),
])


@pytest.mark.parametrize(*examples)
def test_tennis_score(expected_score, player1_points, player2_points, comment):
    """
    Parametrized test, which produces a many test cases based on the test data
    We could pull test data out of the data out of the database or
    a spreasheet, or some other kind of text file.

    Args:
        expected_score: a data that test should returns
        player1_points: a score of the first player
        player2_points: a score of the second player
        comment: a relevant test name, which used for description
    """
    assert expected_score == tennis_score(player1_points, player2_points)


# def test_early_game_scores_equal():
#     assert "Love-All" == tennis_score(0, 0)
#     assert "Fifteen-All" == tennis_score(1, 1)
#     assert "Thirty-All" == tennis_score(2, 2)
