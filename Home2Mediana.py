__author__ = 'sylwia'


def checkio(data):
    data = sorted(data)
    if len(data)%2 == 0:
        mediana = (data[int(len(data)/2) - 1] + data[int(len(data)/2)])/2.
    else:
        mediana = data[int(len(data)/2)]

    print mediana
    return mediana

checkio([1, 2, 2, 6, 4, 5])

# SOLUTION
#  data.sort()
#  l = len(data)
#  return (data[l//2] + data[(l-1)//2]) / 2

