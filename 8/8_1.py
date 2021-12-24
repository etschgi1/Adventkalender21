UNIQUE_SEGMENTS = {2: 1, 4: 4, 3: 7, 7: 8}


def sort(s):
    s = sorted(s)
    out = ""
    for l in s:
        out += l
    return out


def getnumocc_simple(signal, encoded):
    Segments = {}
    for s in signal:
        # sort string
        s = sort(s)
        try:
            num = UNIQUE_SEGMENTS[len(s)]
            try:
                Segments[s]  # look if already found
            except KeyError:
                Segments[s] = num
        except KeyError:
            pass  # for now
    num_unique = 0
    for w in encoded:
        w = sort(w)
        try:
            Segments[w]
            num_unique += 1
        except KeyError:
            pass
    print(num_unique)
    return num_unique


def main(signal, encoded):
    total_occ = 0
    for signal, encoded in zip(signal, encoded):
        total_occ += getnumocc_simple(signal, encoded)
    print(total_occ)


FILENAME2 = "./test.txt"
FILENAME = "./input.txt"
if __name__ == "__main__":
    f = open(FILENAME, "r")
    in_ = f.readlines()
    f.close()
    signal_patterns, output_encoded = [], []
    for line in in_:
        split = line.split(" | ")
        signal_patterns.append(split[0].split(" "))
        output_encoded.append([x.strip() for x in split[1].split(" ")])
    main(signal_patterns, output_encoded)
