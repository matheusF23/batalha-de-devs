grid = [['m', 'y', 'e'],['x', 'a', 'm'],['p', 'l', 'e']]
indexes = [1,3,5,8]

def grid_index(grid, indexes):
    return "".join([grid[(index-1)//len(grid)][(index-1)%len(grid)] for index in indexes])

print(grid_index(grid, indexes))
