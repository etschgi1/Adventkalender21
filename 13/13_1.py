def fold_x(coords, fold):
    # fold left
    coords = sorted(coords, key=lambda coord: coord[0])
    index = 0
    for i in range(len(coords)):
        if coords[i][0] > fold:
            break
        index += 1
    for coord in coords[i:]:
        newx = fold - (coord[0]-fold)
        if (newx, coord[1]) not in coords:
            coords.append((newx, coord[1]))
        coords.remove(coord)
    return coords


def fold_y(coords, fold):
    # fold up
    coords = sorted(coords, key=lambda coord: coord[1])
    index = 0
    for i in range(len(coords)):
        if coords[i][1] > fold:
            break
        index += 1
    for coord in coords[i:]:
        newy = fold - (coord[1]-fold)
        if (coord[0], newy) not in coords:
            coords.append((coord[0], newy))
        coords.remove(coord)
    return coords


def fold_paper(coords, fold):
    if fold[0] == "x":
        fold = int(fold.split("=")[-1])
        return fold_x(coords, fold)
    elif fold[0] == "y":
        fold = int(fold.split("=")[-1])
        return fold_y(coords, fold)
    else:
        raise Exception("Unknown fold axis")


def print_paper(coords):
    coords = sorted(coords, key=lambda coord: (coord[0], coord[1]))
    max_x = max([x[0] for x in coords])
    max_y = max([x[1] for x in coords])
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in coords:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def main(coords, folds):
    # print_paper(coords)
    for fold in folds:
        print(coords)
        coords = fold_paper(coords, fold)
        print(len(coords))
    print_paper(coords)


FILENAME2 = "./test.txt"
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    input_ = [x.strip("\n") for x in input_]
    # input_ = ["start-A", "start-b", "A-c", "A-b",
    #          "b-d", "A-end", "b-end"]  # just for testing
    flag = False
    coords, folds = [], []
    for l in input_:
        if l == "XXX":
            flag = True
            continue
        if flag:
            l = l.split(" ")[-1]
            folds.append(l)
            continue
        x, y = l.split(",")
        coords.append((int(x), int(y)))

    main(coords, folds)
