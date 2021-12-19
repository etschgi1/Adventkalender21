import binascii
from dataclasses import dataclass
global PACKAGES, VCOUNT


def hex_to_bin(hex_):
    bins = ""
    for h in hex_:
        h = "0x"+h
        bin_ = bin(int(h, 16))[2:]
        while len(bin_) < 4:
            bin_ = '0'+bin_
        bins += bin_
    return bins


@dataclass
class Package:
    Version: int
    ID: int
    length_type: bool
    length: int
    subpackage: str


@dataclass
class Literal_package:
    Version: int
    ID: int
    Num: int


def get_int(binstring):
    s = binstring[::-1]
    out = 0
    for i, c in enumerate(s):
        if c == '1':
            out += 2**i
    return out


def get_package_num_and_end(s, padding=True):
    index = 0
    binnum = ""
    while True:
        binnum += s[index+1:index+5]
        if s[index] == '0':
            break
        index += 5
    package_len = 6 + (index+5)  # 6 from VVVTTT fields for actual num
    if padding:
        package_len += 4-package_len % 4 if package_len % 4 else 0   # filling zeros
    return (get_int(binnum), package_len)


def one_in_rest(rest):
    for c in rest:
        if c == '1':
            return True
    return False


def readpackage(stack):
    global PACKAGES, VCOUNT
    while stack:
        top = stack.pop()
        Ver, ID = get_int(top[:3]), get_int(top[3:6])
        VCOUNT += Ver
        if ID != 4:
            length_type = True if top[6:7] == '1' else False
            if length_type:  # contains subpackages:
                num_packages = get_int(top[7:7+11])
                stack.append(top[18:])
            else:
                subarray_len = get_int(top[7:7+15])
                stack.append(top[22:22+subarray_len])
                try:
                    rest = top[22+subarray_len:]
                    if one_in_rest(rest):
                        stack.append(rest)
                except IndexError:
                    pass
        else:
            Num, package_len = get_package_num_and_end(top[6:], False)
            try:
                rest = top[package_len:]
                if one_in_rest(rest):
                    stack.append(rest)
            except IndexError:
                pass
            PACKAGES.append(Literal_package(Ver, ID, Num))
    return


def initpackages(inp):
    global PACKAGES, VCOUNT
    VCOUNT = 0
    PACKAGES = []
    inp = readpackage([inp])  # remaining str
    print(VCOUNT, PACKAGES)


def main(inp):
    # info test:
    # inp = "A0016C880162017C3686B18A3D4780"
    inp = hex_to_bin(inp)
    print(inp)
    initpackages(inp)


FILENAME = "./input.txt"
if __name__ == "__main__":
    input_ = ""
    with open(FILENAME, "r") as f:
        input_ = f.read()
    input_ = input_.strip()
    main(input_)
