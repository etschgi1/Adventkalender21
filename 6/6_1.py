class Fish:
    def __init__(self, timer):
        self.timer = timer

    def reset_timer(self):
        self.timer = 6

    def try_reproduction(self):
        if self.timer == 0:  # reproduce
            newfish = Fish(8)
            self.reset_timer()
            return newfish
        self.timer -= 1
        return None


def init_fish(timers):
    fish = []
    for timer in timers:
        fish.append(Fish(timer))
    return fish


def main(input_):
    # info just for testing
    # input_ = [3, 4, 3, 1, 2]
    if DEBUG:
        print(input_)
    fish = init_fish(input_)
    # loop
    if DEBUG:
        print(f"Initial: {[f.timer for f in fish]}")
    for i in range(DAYS):
        new_fish = []
        for f in fish:
            pot_new_fish = f.try_reproduction()
            if pot_new_fish != None:
                new_fish.append(pot_new_fish)
        for f in new_fish:
            fish.append(f)
        if DEBUG:
            print(f"After {i+1} days: {len(fish)}")
    print(f"Total fish after {DAYS} days: {len(fish)}")


DAYS = 256
DEBUG = True
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    cont = f.readlines()
    f.close()
    cont = cont[0].split(",")
    main([int(x) for x in cont])
