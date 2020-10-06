from memory_profiler import profile
import time

grid = [['m', 'y', 'e'],['x', 'a', 'm'],['p', 'l', 'e']]
indexes = [1,3,5,8]

inicio = time.time()

@profile
def grid_index(grid, indexes):
    return "".join([grid[(index-1)//len(grid)][(index-1)%len(grid)] for index in indexes])

fim = time.time()
print("Tempo de execução: ", fim-inicio)

if __name__ == '__main__':
    print(grid_index(grid, indexes))
