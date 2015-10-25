__author__ = 'sylwia'


def safe_pawns(pawns):
    col = ('', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    counter = set()

    for pawn in pawns:
        left = col.index(pawn[0]) - 1 if col.index(pawn[0]) - 1 >= 0 else 0
        right = col.index(pawn[0]) + 1 if col.index(pawn[0]) + 1 <= 8 else 0

        left_pawn = col[left] + str(int(pawn[1]) + 1)
        right_pawn = col[right] + str(int(pawn[1]) + 1)

        counter.add(left_pawn) if left_pawn in pawns else 0
        counter.add(right_pawn) if right_pawn in pawns else 0

    return len(counter)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}) == 7
