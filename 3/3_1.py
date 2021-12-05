FILENAME = "./input.txt"
FILENAME2 = "./test.txt"


def binlist_to_dec(list):
    len_ = len(list)
    start = len_-1
    out = 0
    for n in range(len_):
        if list[n] == 1:
            out += 2**start
        start -= 1
    return out


def main():
    f = open(FILENAME, "r")
    lines = f.readlines()
    lines = [x.strip('\n') for x in lines]
    # print(lines)
    num_len = len(lines[0])
    list_len = len(lines)
    mcb = [0]*num_len
    for count, num in enumerate(lines):
        for c, char in enumerate(num):
            if char == "1":
                mcb[c] += 1
    mcb = [1 if x > int(list_len/2) else 0 for x in mcb]
    gamma = mcb
    epsilon = [1 if x == 0 else 0 for x in gamma]
    gamma = binlist_to_dec(gamma)
    epsilon = binlist_to_dec(epsilon)
    res = gamma*epsilon
    print(f"gamma val = {gamma}")
    print(f"epsilon val = {epsilon}")
    print(f"res = {res}")


if __name__ == "__main__":
    main()
