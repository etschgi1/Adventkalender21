FILENAME = "./input.txt"
FILENAME2 = "./test.txt"


def binlist_to_dec(list_, string=False):
    len_ = len(list_)
    if(string):
        list_ = list_[0]
        len_ = len(list_)
    start = len_-1
    out = 0
    for n in range(len_):
        if (string):
            if list_[n] == '1':
                out += 2**start
        else:
            if list_[n] == 1:
                out += 2**start
        start -= 1
    return out


def getmcblcb(lines):
    num_len = len(lines[0])
    list_len = len(lines)
    mcb = [0]*num_len
    for count, num in enumerate(lines):
        for c, char in enumerate(num):
            if char == "1":
                mcb[c] += 1
    mcb = [1 if x >= list_len/2 else 0 for x in mcb]
    lcb = [1 if x == 0 else 0 for x in mcb]
    return (mcb, lcb)


def getnewlines(lines, bits, pos):
    print(lines, bits, pos)
    out = []
    for x in lines:
        if x[pos] == str(bits[pos]):
            out.append(x)
    return out


def main():
    f = open(FILENAME, "r")
    lines = f.readlines()
    lines = [x.strip('\n') for x in lines]
    lines_mcb, lines_lcb = lines, lines
    for i in range(len(lines[0])):
        mcb, _ = getmcblcb(lines_mcb)
        lines_mcb = getnewlines(lines_mcb, mcb, i)
        if(len(lines_mcb) == 1):
            break
    for i in range(len(lines[0])):
        _, lcb = getmcblcb(lines_lcb)
        lines_lcb = getnewlines(lines_lcb, lcb, i)
        if(len(lines_lcb) == 1):
            break
    print(lines_mcb, lines_lcb)
    oxygen, co2 = binlist_to_dec(
        lines_mcb, True), binlist_to_dec(lines_lcb, True)
    print(f"oxygen: {oxygen}\t co2: {co2}\t res = {co2*oxygen}")


if __name__ == "__main__":
    main()
