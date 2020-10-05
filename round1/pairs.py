l = [1, 2, 5, 8, -4, -3, 7, 6, 5]


def pairs(l):
    return sum([1 for i in range(len(l)//2) if l[i*2] - l[i*2+1] in [-1, 1]])


print(pairs(l))
