
import numpy as np
global IDIM
global JDIM


def get_min_neighbour(field, i, j, i_dim, j_dim):
    global IDIM, JDIM
    # upper left right lower neighbour
    upper = (i-1, j) if i > 0 else None
    left = (i, j-1) if j > 0 else None
    right = (i, j+1) if j < JDIM-1 else None
    lower = (i+1, j) if i < IDIM-1 else None
    min_ = 9
    for neighbour in [upper, left, right, lower]:
        if neighbour != None:
            if min_ > field[neighbour[0]][neighbour[1]]:
                min_ = field[neighbour[0]][neighbour[1]]
    return min_


def get_neighbour_without_9(field, inbasin, i, j):
    global IDIM, JDIM
    upper = (i-1, j) if i > 0 else None
    left = (i, j-1) if j > 0 else None
    right = (i, j+1) if j < JDIM-1 else None
    lower = (i+1, j) if i < IDIM-1 else None
    newcount = 0
    for neighbour in [upper, left, right, lower]:
        if neighbour != None and neighbour not in inbasin and field[neighbour[0]][neighbour[1]] != 9:
            inbasin.append(neighbour)
            newcount += 1
    if newcount:
        for pos in range(len(inbasin)-newcount, len(inbasin)):
            i, j = inbasin[pos]
            get_neighbour_without_9(field, inbasin, i, j)
    else:
        return inbasin


def get_basin_size(field, low_point):
    i, j = low_point
    inbasin = [low_point]  # low_point already in basin
    oldbasinlen = len(inbasin)
    while True:
        get_neighbour_without_9(field, inbasin, i, j)
        if oldbasinlen == len(inbasin):
            return len(inbasin)
        oldbasinlen = len(inbasin)


def main(inp):
    global IDIM, JDIM
    field = []
    for line in inp:
        temp = []
        for n in line:
            if n != '\n':
                temp.append(int(n))
        field.append(temp)
    # field = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8,
    #                                                                          9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]  # testing
    low_points = []
    field = np.array(field)
    i_dim, j_dim = len(field), len(field[0])
    IDIM, JDIM = i_dim, j_dim
    for i in range(i_dim):
        for j in range(j_dim):
            if get_min_neighbour(field, i, j, i_dim, j_dim) > field[i][j]:
                low_points.append((i, j))
    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(get_basin_size(field, low_point))
    return basin_sizes


FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    main_ret = main(input_)
    main_ret.sort(reverse=True)
    print(
        f"Biggest 3 basins: {main_ret[:3]} - multiplied = {main_ret[0]*main_ret[1]*main_ret[2]}")
