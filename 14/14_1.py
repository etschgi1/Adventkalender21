STEPS = 40


def polymerization(polymer, Rules):
    newpolymer = ""
    for c, i in enumerate(polymer):
        if c == len(polymer)-1:
            newpolymer += i
            return newpolymer
        try:
            to_insert = Rules[polymer[c:c+2]]
            # print(to_insert)
            newpolymer += i
            newpolymer += to_insert
        except KeyError:
            newpolymer += i


def main(polymer, rules):
    Rules = {x[:2]: x[-1] for x in rules}
    for i in range(STEPS):
        print(polymer)
        polymer = polymerization(polymer, Rules)
    counts = {}
    for c in polymer:  # find most and least common
        try:
            counts[c] += 1
        except KeyError:
            counts[c] = 1
    max_, min_ = max(counts, key=lambda key: counts[key]), min(
        counts, key=lambda key: counts[key])
    print(
        f"max: {max_}: {counts[max_]}, min: {min_}: {counts[min_]} - Diff: {counts[max_]-counts[min_]} ")


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
