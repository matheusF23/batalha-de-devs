from memory_profiler import profile
import time
import random
import string


random.seed(1234)
indexes = [random.randint(1, 10**6) for i in range(10**5)]


grid = [[random.choice(string.ascii_lowercase) for coluna in range(10**3)] for linha in range(10**3)]

inicio = time.time()

@profile
def grid_index(grid, indexes):
    return "".join([grid[(index-1)//len(grid)][(index-1)%len(grid)] for index in indexes])


if __name__ == '__main__':
    grid_index(grid, indexes)

fim = time.time()
print("Tempo de execução: ", fim-inicio)
