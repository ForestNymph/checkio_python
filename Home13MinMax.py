__author__ = 'sylwia, checkio'


def find_value(ismax, key, container):
    # condition for searching max or min
    # if min then takes first number from the list and compare to others
    res = 0 if ismax else container[0]
    list_element = 0
    list_res = 0
    for item in container:
        if key is not None:
            list_element, item = item, key(item)
        if ismax:
            if item > res:
                list_res = list_element
                res = item
        else:
            if item < res:
                list_res = list_element
                res = item
                # result for max function
                # res = item if item > res and ismax else res
                # result for min function
                # res = item if item < res and not ismax else res
    return res if key is None else list_res


def result(state, key, *args):
    if isinstance(args[0], str):
        container = [ord(x) for x in args[0]]
        return chr(find_value(state, key, container))
    elif isinstance(args[0], int):
        return find_value(state, key, list(args))
    elif isinstance(args[0], tuple):
        return find_value(state, key, args[0])
    elif isinstance(args[0], float):
        f = find_value(state, key, list(args))
        numbers = [int(x) for x in list(args)]
        i = numbers.index(int(f))
        return list(args)[i]
    elif isinstance(args[0], list):
        # if args is two or more dimnesial list
        ar = list(args) if len(args) > 1 else args[0]
        return find_value(state, key, list(ar))
    elif isinstance(args[0], set):
        return find_value(state, key, list(args[0]))
    elif args[0].next():
        return find_value(state, key, list(args[0]))
    return 0


def min1(*args, **kwargs):
    key = kwargs.get("key", None)
    # print result(False, key, *args)
    return result(False, key, *args)


def max1(*args, **kwargs):
    key = kwargs.get("key", None)
    # print result(True, key, *args)
    return result(True, key, *args)


def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    return reduce(lambda M, x: x if key(x) < key(M) else M, args if len(args) > 1 else args[0])


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    return reduce(lambda M, x: x if key(x) > key(M) else M, args if len(args) > 1 else args[0])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum) == [1, 2, 3]
    assert max([[9, 5], [1, 2], [3, 4]], key=lambda x: x[1]) == [9, 5], "lambda key"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]) == [7]
    assert min({1, 2, 3, 4, -10}) == -10
    assert max(x + 5 for x in range(6)) == 10
    assert min(abs(i) for i in range(-10, 10)) == 0
    assert min((9,)) == 9
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max("hello") == "o", "From string"
    assert min("hello") == "e", "From string"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
