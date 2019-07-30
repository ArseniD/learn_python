import unittest

from tennis import tennis_score

# test data
test_case_data = {
"even_scores":                     [("Love-All", 0, 0),
                                    ("Fifteen-All", 1, 1),
                                    ("Thirty-All", 2, 2)],

"early_games_with_uneven_scores":  [("Love-Fifteen", 0, 1),
                                    ("Fifteen-Love", 1, 0),
                                    ("Thirty-Fifteen", 2, 1),
                                    ("Forty-Thirty", 3, 2)],

"endgame_with_uneven_scores":       [("Advantage Player 1", 4, 3),
                                     ("Advantage Player 2", 5, 6),
                                     ("Advantage Player 1", 13, 12)],

"endgame_with_even_scores":         [("Deuce", 3, 3),
                                     ("Deuce", 4, 4),
                                     ("Deuce", 14, 14)],

"there_is_a_winner":                [("Win for Player 1", 4, 0),
                                     ("Win for Player 2", 2, 4),
                                     ("Win for Player 1", 6, 4)],
}


def tennis_test_template(*args):
    """
    The function that returns a function, function foo is going to be renamed
    and put onto tennis test as a test case

    args:
            any arguments we get to the template, straigt to the custom assert,
            assert_tennis_score.

    """
    def foo(self):
        self.assert_tennis_score(*args)
    return foo


class TennisTest(unittest.TestCase):

    # def test_even_scores_zero_ponts(self):
    #     self.assertEqual("Love-All", tennis_score(0, 0))

    # def test_even_scores_early_game(self):
    #     self.assert_tennis_score("Love-All", 0, 0)
    #     self.assert_tennis_score("Fifteen-All", 1, 1)
    #     self.assert_tennis_score("Thirty-All", 2, 2)
    #     self.assert_tennis_score("Forty-All", 3, 3)

    # def test_early_game_with_uneven_scores(self):
    #     self.assert_tennis_score("Love-Fifteen", 0, 1)
    #     self.assert_tennis_score("Fifteen-Love", 1, 0)
    #     self.assert_tennis_score("Love-Thirty", 0, 2)
    #     self.assert_tennis_score("Forty-Thirty", 3, 2)

    def assert_tennis_score(self, expected_score, player1_points,
                                                    player2_points):
        """
        A custom assert test

        Example:
            expected_score = "Deuce"
            player1_points = 3
            player2_points = 3
        """
        self.assertEqual(expected_score, tennis_score(player1_points,
                                                        player2_points))


# Goes through all of the items in the test data we defined above
for behaviour, test_case in test_case_data.items():
    for tennis_test_case_data in test_case:
        expected_output, player1_score, player2_score = tennis_test_case_data
        # Creates a unique test name from data
        test_name = "test_{0}_{1}_{2}".format(behaviour, player1_score,
                                                         player2_score)
        # Calls template method to generate a suitable function
        tennis_test_case = tennis_test_template(*tennis_test_case_data)
        # Using setattr, a meta-programming tecnique, to add that function to
        # tennis test
        setattr(TennisTest, test_name, tennis_test_case)
