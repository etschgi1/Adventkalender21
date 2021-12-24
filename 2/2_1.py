FILENAME = "./input.txt"
horizontal_pos = 0
depth = 0


def main():
    f = open(FILENAME, "r")
    l = f.readlines()
    l = [x.strip("\n") for x in l]
    dir_, dist = [], []
    for e in l:
        c = e.split(" ")
        dir_.append(c[0])
        dist.append(c[1])
    distance = {"forward": 0, "up": 0, "down": 0}
    aim = 0
    depth = 0
    for c, e in enumerate(dir_):
        if e == "down":
            aim += int(dist[c])
        elif e == "up":
            aim -= int(dist[c])
        else:  # forward
            distance["forward"] += int(dist[c])
            depth += aim*int(dist[c])
    # print(distance, distance["down"]-distance["up"],
    #       (distance["down"]-distance["up"])*distance["forward"])
    print(distance["forward"], depth, depth*distance["forward"])


if __name__ == "__main__":
    main()
