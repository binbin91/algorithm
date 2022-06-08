# -*- coding: utf-8 -*-


def aa(s):
    res = list()
    for i in s:
        if res and res[-1] == i:
            res.pop()
        else:
            res.append(i)
    return "".join(res)


if __name__ == "__main__":
    print aa("abbaca")
