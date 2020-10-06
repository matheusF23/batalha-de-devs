# Retornar a soma dos números que não se repetem
from memory_profiler import profile
import time
import random

l = [random.randint(0, 1000) for i in range(10**4)]
print(len(l))

inicio = time.time()

@profile
def repeats(l):
    return sum([i for i in l if l.count(i) == 1])

if __name__ == '__main__':
    print(repeats(l))

fim = time.time()
print("Tempo de execução: ", fim-inicio)
