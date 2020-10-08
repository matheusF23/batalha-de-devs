from memory_profiler import profile
import time
import random


random.seed(1234)
l = [random.randint(0, 100) for i in range(10**5)]
print(len(l))

inicio = time.time()


@profile
def pairs(l):
    return sum([1 for i in range(len(l)//2) if l[i*2] - l[i*2+1] in [-1, 1]])


if __name__ == '__main__':
    print(pairs(l))

fim = time.time()
print("Tempo de execução: ", fim-inicio)
