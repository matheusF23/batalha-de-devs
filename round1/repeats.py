# Retornar a soma dos números que não se repetem

l = [4, 5, 7, 5, 4, 8]
def repeats(l):
    return sum([i for i in l if l.count(i) == 1])

print(repeats(l))