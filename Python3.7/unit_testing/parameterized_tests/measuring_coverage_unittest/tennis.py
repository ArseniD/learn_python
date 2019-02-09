score_names = ["Love", "Fifteen", "Thirty", "Forty"]


def tennis_score(player1_points, player2_points):
    if player1_points == player2_points:
        if player1_points < 3 and player2_points < 3:
            return "{0}-All".format(score_names[player1_points])
        else:
            return "Deuce"
    if player1_points != player2_points:
        if player1_points <= 3 and player2_points <= 3:
            return "{0}-{1}".format(score_names[player1_points],
                            score_names[player2_points])
        if player1_points - 1 == player2_points:
            return "Advantage Player 1"
        if player2_points - 1 == player1_points:
                return "Advantage Player 2"
        else:
            if player1_points > player2_points:
                return "Win for Player 1"
            if player1_points < player2_points:
                return "Win for Player 2"
