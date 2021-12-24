import numpy as np
import math as m


def calcconsumption(pos, goal):
    consumption = 0
    for p in pos:
        consumption += abs(p-goal)
    return consumption


def calcmodifiedconsumption(pos, goal):
    consumption = 0
    for p in pos:
        distance = abs(p-goal)
        consumption += (distance*(distance+1))/2  # info gaus formula
    return consumption


def main(pos):
    # pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]  # info just for test
    print(len(pos), np.mean(pos))
    min_, max_ = min(pos), max(pos)
    bestgoal, bestconsumption = 0, max_**3
    for c in range(min_, max_+1):
        if SECOND_PART:
            consumption = calcmodifiedconsumption(pos, c)
        else:
            consumption = calcconsumption(pos, c)
        if consumption < bestconsumption:
            bestconsumption = consumption
            bestgoal = c
    return (bestconsumption, bestgoal)


SECOND_PART = True  # flag for second puzzle
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    pos = f.readlines()
    f.close()
    pos = [int(x) for x in pos[0].split(",")]
    best, goalpos = main(pos)
    print(f"Best consumption: {best}, if all move to  {goalpos}")
