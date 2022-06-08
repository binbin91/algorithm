# -*- coding: utf-8 -*-


def aa(n1, n2):
    return list(set(n1) & set(n2))


if __name__ == "__main__":
    print aa([1,2,2,1], [2,2])
    print aa([4,9,5], [9,4,9,8,4])
