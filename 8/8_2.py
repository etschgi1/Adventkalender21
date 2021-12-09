UNIQUE_SEGMENTS = {2: 1, 4: 4, 3: 7, 7: 8}
# Segment Positions:
# 0000
# 1  2
# 1  2
# 3333
# 4  5
# 4  5
# 6666
SEGMENT_POSITIONS = {0: "x", 1: "x", 2: "x", 3: "x", 4: "x", 5: "x", 6: "x"}


def sort(s):
    s = sorted(s)
    out = ""
    for l in s:
        out += l
    return out


def identify_rest(Segments, Known_segments):
    global SEGMENT_POSITIONS, UNIQUE_SEGMENTS
    Counts = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
    left_over_letters = ["a", "b", "c", "d", "e", "f", "g"]
    SEGMENT_POSITIONS = {0: "x", 1: "x",
                         2: "x", 3: "x", 4: "x", 5: "x", 6: "x"}
    for v in Segments.keys():
        for l in v:
            Counts[l] += 1
    # first get Segments 4,5
    for key, val in Counts.items():
        if val == 4:  # 4th segment
            SEGMENT_POSITIONS[4] = key
            left_over_letters.remove(key)
        elif val == 9:  # 5th segment
            SEGMENT_POSITIONS[5] = key
            left_over_letters.remove(key)
    # set segment 2 with known pos of 1
    string1 = Known_segments[1]
    if string1[0] in SEGMENT_POSITIONS.values():
        SEGMENT_POSITIONS[2] = string1[1]
        left_over_letters.remove(string1[1])
    else:
        SEGMENT_POSITIONS[2] = string1[0]
        left_over_letters.remove(string1[0])
    # set seg 0 with pos of 7 top
    string7 = Known_segments[7]
    for l in string7:
        if l not in SEGMENT_POSITIONS.values():
            SEGMENT_POSITIONS[0] = l
            left_over_letters.remove(l)
            break
    # set 1 pos
    for key, val in Counts.items():
        if val == 6:  # 1 segment
            SEGMENT_POSITIONS[1] = key
            left_over_letters.remove(key)
    string8 = Known_segments[8]
    string4 = Known_segments[4]
    for l in string4:
        if l in left_over_letters:
            SEGMENT_POSITIONS[3] = l
            left_over_letters.remove(l)
    SEGMENT_POSITIONS[6] = left_over_letters[0]

    for key, val in Segments.items():
        if val not in UNIQUE_SEGMENTS.values():
            Segments[key] = getnum(key)
    return Segments


def getnum(key):
    global SEGMENT_POSITIONS, UNIQUE_SEGMENTS
    if len(key) == 6:  # 0 or 6
        if SEGMENT_POSITIONS[3] in key:
            if SEGMENT_POSITIONS[2] in key:
                return 9
            return 6
        return 0
    elif len(key) == 5:  # 2,3,5 or 9
        if SEGMENT_POSITIONS[2] not in key:
            return 5
        elif SEGMENT_POSITIONS[5] in key:
            return 3
        return 2
    else:
        raise Exception("Error in getnum")


def get_sum_of_num_encoded(signal, encoded):
    global SEGMENT_POSITIONS, UNIQUE_SEGMENTS
    Segments = {}
    Known_segments = {}
    for s in signal:
        # sort string
        s = sort(s)
        try:
            num = UNIQUE_SEGMENTS[len(s)]
            try:
                Segments[s]  # look if already found
            except KeyError:
                Segments[s] = num
                Known_segments[num] = s
        except KeyError:
            Segments[s] = -1
    Segments = identify_rest(Segments, Known_segments)
    lokalnum = ""
    for w in encoded:
        w = sort(w)
        try:
            lokalnum += str(Segments[w])
        except KeyError:
            raise Exception("Error in encoding")
    print(lokalnum)
    return int(lokalnum)


def main(signal, encoded):
    total_sum = 0
    for signal, encoded in zip(signal, encoded):
        total_sum += get_sum_of_num_encoded(signal, encoded)
    print(total_sum)


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
