__author__ = 'sylwia'


def checkio(number):
    pigeon = 1
    feed_pigeon = [0]

    while number > 0:
        for pig in xrange(len(feed_pigeon)):
            feed_pigeon[pig] += 1 if number - 1 >= 0 else 0
            number -= 1

        pigeon += 1
        feed_pigeon += [0] * pigeon

    return len([x for x in feed_pigeon if x > 0])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(3) == 2
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
