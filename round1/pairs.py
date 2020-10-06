from memory_profiler import profile
import time

l = [1, 2, 5, 8, -4, -3, 7, 6, 5]

inicio = time.time()

@profile
def pairs(l):
    return sum([1 for i in range(len(l)//2) if l[i*2] - l[i*2+1] in [-1, 1]])

fim = time.time()
print("Tempo de execução: ", fim-inicio)

if __name__ == '__main__':
    print(pairs(l))
