def init_fish(timers):
    fish = {"0": 0, "1": 0, "2": 0, "3": 0,
            "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    for timer in timers:
        try:
            fish[str(timer)] += 1
        except KeyError:
            fish[str(timer)] = 0
    return fish


def main(input_):
    # info just for testing
    # input_ = [3, 4, 3, 1, 2]
    if DEBUG:
        print(input_)
    fish = init_fish(input_)
    # loop
    if DEBUG:
        print(f"Initial: {fish}")
    for j in range(DAYS):
        # check fish that can reproduce
        newfish = fish["0"]
        # move everything down
        for i in range(8):
            fish[str(i)] = fish[str(i+1)]
        fish["6"] += newfish
        fish["8"] = newfish
        if DEBUG:
            print(f"After {j+1} days: {sum(fish.values())}")
            # print(fish)
    print(f"Total fish after {DAYS} days: {sum(fish.values())}")


DAYS = 256
DEBUG = True
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    cont = f.readlines()
    f.close()
    cont = cont[0].split(",")
    main([int(x) for x in cont])
