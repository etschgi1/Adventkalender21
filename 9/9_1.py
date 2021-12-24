
import numpy as np


def get_min_neighbour(field, i, j, i_dim, j_dim):
    # upper left right lower neighbour
    upper = (i-1, j) if i > 0 else None
    left = (i, j-1) if j > 0 else None
    right = (i, j+1) if j < j_dim-1 else None
    lower = (i+1, j) if i < i_dim-1 else None
    min_ = 9
    for neighbour in [upper, left, right, lower]:
        if neighbour != None:
            if min_ > field[neighbour[0]][neighbour[1]]:
                min_ = field[neighbour[0]][neighbour[1]]
    return min_


def main(inp):
    field = []
    for line in inp:
        temp = []
        for n in line:
            if n != '\n':
                temp.append(int(n))
        field.append(temp)
    field = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8,
                                                                             9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]  # testing
    field = np.array(field)
    risk_level = 0
    i_dim, j_dim = len(field), len(field[0])
    for i in range(i_dim):
        for j in range(j_dim):
            if get_min_neighbour(field, i, j, i_dim, j_dim) > field[i][j]:
                risk_level += field[i][j]+1
    return risk_level


FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    print(f"Total risk level = {main(input_)}")
