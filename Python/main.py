

def average(x):
    sum = 0
    for i in x:
        sum += i
    return sum


def base_f(x, w):
    base = average(x)
    d = (base + w)
    h = len(x) + 1
    return d / h


# 24 + 30 + 27 + 18
x = [24, 30, 27, 18]
w = 35
print("Average: " + str(average(x)))
print(base_f(x, w))

