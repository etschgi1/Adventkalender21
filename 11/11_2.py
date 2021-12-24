import numpy as np

global octos, neighbours
neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]


class octo():
    THRESHOLD = 9

    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.flash_count = 0
        self.already_flashed = False

    def getval(self):
        return self.val

    def blink(self):
        if self.already_flashed == False:
            self.val = 0
            self.already_flashed = True
            return 1
        return 0

    def reset_flash(self):
        if self.already_flashed:
            self.already_flashed = False
            self.val = 0
            return 1
        return 0


def update_neighbours(i, j):
    global octos, neighbours
    for n in neighbours:
        inei, jnei = i+n[0], j+n[1]
        if inei < 0 or jnei < 0:
            continue
        try:
            octos[inei][jnei].val += 1
        except IndexError:
            continue


def get_blinkers():
    counter = 0
    global octos
    for octorow in octos:
        for octo in octorow:
            if octo.getval() > 9:
                if octo.blink():
                    update_neighbours(octo.i, octo.j)
                    counter += 1
    return counter


def newround():
    global octos
    for octorow in octos:  # first increment
        for octo in octorow:
            octo.val += 1  # first increase
    roundscore = 0
    while(True):
        ret = get_blinkers()
        if ret:
            roundscore += ret
        else:
            break
    for octorow in octos:
        for octo in octorow:
            octo.reset_flash()

    return 1 if roundscore == len(octos)*len(octos[0]) else 0


def printocots():
    global octos
    for i in range(len(octos)):
        for j in range(len(octos[0])):
            print(octos[i][j].getval(), end=" ")
        print("")
    print("")


def main(inp):
    global octos
    octos = inp
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            octos[i][j] = octo(i, j, inp[i][j])
    printocots()
    print("start")
    round_count = 1
    while not newround():
        round_count += 1
    print("Last board")
    printocots()
    print(f"Simultanious flash at round: {round_count}")


FILENAME2 = "./test.txt"
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    input_ = [x.strip("\n") for x in input_]
    out = []
    for s in input_:
        temp = []
        for c in s:
            temp.append(int(c))
        out.append(temp)
    main(out)
