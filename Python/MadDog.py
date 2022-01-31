import numpy as np

data = [2, 2, 5, 6, 3, 1, 8, 10, 40, 3, 5, 6]


def average(data):
    sum = 0
    for i in data:
        sum += i
    return sum / len(data)


def find_outliers(data):
    data = np.array(data)
    av = int(average(data)*2)
    pos = 0
    for i in data:
        pos += 1
        if i >= av:
            data[pos - 1] = data[pos - 2] / 2

    return data

