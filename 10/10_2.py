global POINTS, open_, close_, CLOSE_OPEN_REL
POINTS = {"(": 1, "[": 2, "{": 3, "<": 4}
open_, close_ = "({[<", ")}]>"
CLOSE_OPEN_REL = {")": "(", "]": "[", "}": "{", ">": "<"}


def getsyntaxerrorpoints(line):
    global POINTS, open_, close_, CLOSE_OPEN_REL
    lastopend = []  # use a stack
    opening_counts = {"(": 0, "[": 0, "{": 0, "<": 0}
    closing_counts = {")": 0, "]": 0, "}": 0, ">": 0}
    for c, brac in enumerate(line):
        if brac in open_:  # opening
            opening_counts[str(brac)] += 1
            lastopend.append(brac)
            continue
        else:
            closing_counts[str(brac)] += 1
            if lastopend.pop() != CLOSE_OPEN_REL[brac]:
                return 0  # avoid faulty lines
    # get closing bracs
    total = 0
    while lastopend:
        total *= 5
        total += POINTS[lastopend.pop()]
    print(total)
    return total


def main(inp):
    total = []
    # inp = ["""[({(<(())[]>[[{[]{<()<>>""", """[(()[<>])]({[<{<<[]>>(""", """{([(<{}[<>[]}>{[]{[(<()>""", """(((({<>}<{<{<>}{[]{[]{}""", """[[<[([]))<([[{}[[()]]]""",
    #       """[{[{({}]{}}([{[{{{}}([]""", """{<[[]]>}<{[{[{[]{()[[[]""", """[<(<(<(<{}))><([]([]()""", """<{([([[(<>()){}]>(<<{{""", """<{([{{}}[<[[[<>{}]]]>[]]"""]
    for line in inp:
        ret = getsyntaxerrorpoints(line)
        if ret:
            total.append(ret)
    # get middle score
    total.sort()
    mid_ = len(total)//2
    print(f"Total syntax error points = {total,total[mid_]}")


FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    input_ = [x.strip("\n") for x in input_]
    main(input_)
