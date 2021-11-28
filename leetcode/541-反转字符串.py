# -*- coding: utf-8 -*-


def aa(s, k):
    ss = [i for i in s]
    n = len(s)
    for i in range(0, n, 2*k):
        ss[i:i+k] = ss[i:i+k][::-1]
    return "".join(ss)


if __name__ == "__main__":
    print aa("abcdefg", 2)
