STEPS = 40


def polymerization(polymer, Rules, steps, Running_count):
    Pairs = {}
    for c in range(len(polymer)-1):
        try:
            Pairs[polymer[c:c+2]] += 1
        except KeyError:
            Pairs[polymer[c:c+2]] = 1
    for count in range(steps):
        newly_inserted = []
        newly_decimated = []
        for pair in Pairs:
            try:
                to_insert = Rules[pair]
                try:
                    Running_count[to_insert] += Pairs[pair]
                except KeyError:
                    Running_count[to_insert] = Pairs[pair]
                newly_inserted += [(pair[0]+to_insert, Pairs[pair]),
                                   (to_insert+pair[1], Pairs[pair])]
                newly_decimated += [(pair, Pairs[pair])]
            except KeyError:
                print("Key Error")
        for new_decimated, count in newly_decimated:
            Pairs[new_decimated] -= count
            if Pairs[new_decimated] <= 0:
                if Pairs[new_decimated] == 0:
                    del Pairs[new_decimated]
                    continue
                raise Exception("Logikfehler")
        for new_insert, count in newly_inserted:
            try:
                Pairs[new_insert] += count
            except KeyError:
                Pairs[new_insert] = count
    return Running_count


def main(polymer, rules):
    Rules = {x[:2]: x[-1] for x in rules}
    Running_count = {}
    for c in polymer:
        try:
            Running_count[c] += 1
        except KeyError:
            Running_count[c] = 1
    Running_count = polymerization(polymer, Rules, STEPS, Running_count)
    print(Running_count)
    max_, min_ = max(Running_count, key=lambda key: Running_count[key]), min(
        Running_count, key=lambda key: Running_count[key])
    print(
        f"max: {max_}: {Running_count[max_]}, min: {min_}: {Running_count[min_]} - Diff: {Running_count[max_]-Running_count[min_]} ")


FILENAME2 = "./test.txt"
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    input_ = [x.strip("\n") for x in input_]
    rules = input_[2:]
    polymer = input_[0]
    main(polymer, rules)
