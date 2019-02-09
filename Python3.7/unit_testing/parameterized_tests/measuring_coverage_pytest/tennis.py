def tennis_score(player1_points, player2_points):
    game = TennisGame("Player 1", "Player 2")
    game.player1_points = player1_points
    game.player2_points = player2_points
    return game.score()


class TennisGame:
    """
    A simple tennis game

    args:
        player1 - the name of the first player
        player2 - the name of the secong player

    return: a score of the game between 2 players
    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_points = 0
        self.player2_points = 0

    def score(self):
        if self.player1_points == self.player2_points:
            # if self.player1_points < 3 and self.player2_points < 3:
            #     return "{0}-All".format(score_names[self.player1_points])
            # else:
            #     return "Deuce"
            result = {
                        0: "Love-All",
                        1: "Fifteen-All",
                        2: "Thirty-All"
                    }.get(self.player1_points, "Deuce")
            return result
        # if self.player1_points != self.player2_points:
        else:
            if self.player1_points <= 3 and self.player2_points <= 3:
                # return "{0}-{1}".format(score_names[self.player1_points],
                                # score_names[self.player2_points])
                result = {
                            0: "Love",
                            1: "Fifteen",
                            2: "Thirty",
                            3: "Forty"
                        }
                return f'{result[self.player1_points]}-{result[self.player2_points]}'
            elif self.player1_points - 1 == self.player2_points:
                return "Advantage " + self.player1
            elif self.player2_points - 1 == self.player1_points:
                    return "Advantage " + self.player2
            else:
                if self.player1_points > self.player2_points:
                    return "Win for Player 1"
                if self.player1_points < self.player2_points:
                    return "Win for Player 2"
