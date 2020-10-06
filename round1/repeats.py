# Retornar a soma dos números que não se repetem
from memory_profiler import profile

l = [3,3,4,4,7,8]

@profile
def repeats(l):
    return sum([i for i in l if l.count(i) == 1])

if __name__ == '__main__':
    repeats(l)
