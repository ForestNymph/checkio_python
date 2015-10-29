__author__ = 'sylwia'


def golf(n):
    while True:
        n += 1
        if n == int(str(n)[::-1]) and not any(n % x == 0 for x in xrange(2, n) if x < n):
            return n


print golf(101)
