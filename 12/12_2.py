CAVES = {}
Complete_paths = []
Paths = [['start', True]]


def main():
    while Paths:
        path = Paths.pop()
        flag = path[-1]
        lastcave_of_path = path[-2]
        neighbors = CAVES[lastcave_of_path]
        for cave in neighbors:
            if cave == 'end':
                Complete_paths.append(path+[cave, flag])
            elif cave == 'start':
                continue
            elif cave.isupper() or cave not in path:
                Paths.append(path+[cave, flag])
            elif flag:
                Paths.append(path+[cave, False])
    print(len(Complete_paths))


FILENAME2 = "./test.txt"
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    input_ = [x.strip("\n") for x in input_]
    # input_ = ["start-A", "start-b", "A-c", "A-b",
    #          "b-d", "A-end", "b-end"]  # just for testing
    edges = []
    for i in input_:
        start, end = tuple(i.split("-"))
        if start not in CAVES:
            CAVES[start] = []
        if end not in CAVES:
            CAVES[end] = []
        CAVES[start].append(end)
        CAVES[end].append(start)
    main()
