# -*- coding: utf-8 -*-

import collections


def aa(r, m):
    hm = collections.defaultdict(int)
   
    for i in m: hm[i] += 1
    for i in r:
        v = hm.get(i)
        if v is None or v == 0:
            return False
        else:
            hm[i] -= 1
    return True


if __name__ == "__main__":
    print aa("a", "b")
    print aa("aa", "ab")
    print aa("aa", "aab")
