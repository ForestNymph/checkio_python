__author__ = 'sylwia'


def checkio1(game_result):
    print game_result[0]

    x = "X" * 3
    o = "O" * 3

    # Check all rows
    for i in range(0, len(game_result)):
        if game_result[i] == x:
            return "X"
        elif game_result[i] == o:
            return "O"

    # Check all columns
    for a in range(0, len(game_result)):
        result = ''
        for b in range(0, len(game_result)):
            result += game_result[b][a]
        if result == x:
            return "X"
        if result == o:
            return "O"

    # Skos
    if game_result[0][0] + game_result[1][1] + game_result[2][2] == x:
        return "X"
    if game_result[0][0] + game_result[1][1] + game_result[2][2] == o:
        return "O"
    if game_result[0][2] + game_result[1][1] + game_result[2][0] == x:
        return "X"
    if game_result[0][2] + game_result[1][1] + game_result[2][0] == o:
        return "O"

    return "D"


def checkio(game_result):
    for i in range(len(game_result)):
        if game_result[i][0] == game_result[i][1] == game_result[i][2] and game_result[i][0] != '.':
            return game_result[i][0]
        elif game_result[0][i] == game_result[1][i] == game_result[2][i] and game_result[0][i] != '.':
            return game_result[0][i]
        elif game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.' \
                or game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != '.':
            return game_result[1][1]

    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

    print checkio(["..O", "XOX", "O.."])
