__author__ = 'sylwia'


def golf(n):
    while 1:
        n += 1
        if n == int(str(n)[::-1]) and not any(n % x == 0 for x in range(2, n) if x < n):
            return n


print golf(101)
print golf(1985)
print golf(2) == 3
print golf(13) == 101
print golf(101) == 131
