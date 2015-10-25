__author__ = 'sylwia'


def checkio(data):

    new_dict = {}
    new_list = []

    for i in data:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1

    for j in data:
        if new_dict[j] > 1:
            new_list.append(j)

    print new_list
    return new_list


#  SOLUTION
#  list.count(x)
    #  Return the number of times x appears in the list.

def checkio1(data):
    data = [num for num in data.count() > 1]
    return data

checkio([1, 2, 3, 1, 3])  # == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5])  # == []
checkio([5, 5, 5, 5, 5])  # == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8])  # == [10, 9, 10, 10, 9]
checkio([1, 2, 3])

