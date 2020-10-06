# Retornar a soma dos números que não se repetem
from memory_profiler import profile
import time

l = [3,3,4,4,7,8]

inicio = time.time()

@profile
def repeats(l):
    return sum([i for i in l if l.count(i) == 1])

fim = time.time()
print("Tempo de execução: ", fim-inicio)

if __name__ == '__main__':
    repeats(l)
