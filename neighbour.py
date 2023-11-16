i=[
        [2, 8, 3],
        [1, 4, 0],
        [7, 6, 5]
    ]
import copy

def get_neighbors(m,w):
    l = []
    x, y = 0, 0
    f = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                x, y = i, j
                f = 1
                break
        if f == 1:
            break

    if y - 1 >= 0:
        new_matrix = copy.deepcopy(m)
        new_matrix[x][y], new_matrix[x][y - 1] = new_matrix[x][y - 1], new_matrix[x][y]
        l.append((new_matrix,w+1))

    if y + 1 <= 2:
        new_matrix = copy.deepcopy(m)
        new_matrix[x][y], new_matrix[x][y + 1] = new_matrix[x][y + 1], new_matrix[x][y]
        l.append((new_matrix,w+1))

    if x - 1 >= 0:
        new_matrix = copy.deepcopy(m)
        new_matrix[x - 1][y], new_matrix[x][y] = new_matrix[x][y], new_matrix[x - 1][y]
        l.append((new_matrix,w+1))

    if x + 1 <= 2:
        new_matrix = copy.deepcopy(m)
        new_matrix[x + 1][y], new_matrix[x][y] = new_matrix[x][y], new_matrix[x + 1][y]
        l.append((new_matrix,w+1))

    return l


# Example usage:
print(get_neighbors(i,1))