global POINTS, open_, close_, CLOSE_OPEN_REL
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
open_, close_ = "({[<", ")}]>"
CLOSE_OPEN_REL = {")": "(", "]": "[", "}": "{", ">": "<"}


def getsyntaxerrorpoints(line):
    global POINTS, open_, close_, CLOSE_OPEN_REL
    lastopend = []  # use a stack
    opening_counts = {"(": 0, "[": 0, "{": 0, "<": 0}
    closing_counts = {")": 0, "]": 0, "}": 0, ">": 0}
    for brac in line:
        if brac in open_:  # opening
            opening_counts[str(brac)] += 1
            lastopend.append(brac)
            continue
        else:
            closing_counts[str(brac)] += 1
            if lastopend.pop() != CLOSE_OPEN_REL[brac]:
                return POINTS[brac]
    return 0


def main(inp):
    total = 0
    inp = ["""[({(<(())[]>[[{[]{<()<>>""", """[(()[<>])]({[<{<<[]>>(""", """{([(<{}[<>[]}>{[]{[(<()>""", """(((({<>}<{<{<>}{[]{[]{}""", """[[<[([]))<([[{}[[()]]]""",
           """[{[{({}]{}}([{[{{{}}([]""", """{<[[]]>}<{[{[{[]{()[[[]""", """[<(<(<(<{}))><([]([]()""", """<{([([[(<>()){}]>(<<{{""", """<{([{{}}[<[[[<>{}]]]>[]]"""]
    for line in inp:
        total += getsyntaxerrorpoints(line)
    print(f"Total syntax error points = {total}")


FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    input_ = f.readlines()
    f.close()
    input_ = [x.strip("\n") for x in input_]
    main(input_)
