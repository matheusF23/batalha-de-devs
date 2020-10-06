# Retornar a soma dos números que não se repetem
from memory_profiler import profile
import time
import random

random.seed(1234)
l = [random.randint(0, 100) for i in range(20*10**3)]
print(len(l))

inicio = time.time()

@profile
def repeats(l):
    return sum([i for i in l if l.count(i) == 1])

if __name__ == '__main__':
    print(repeats(l))

fim = time.time()
print("Tempo de execução: ", fim-inicio)
