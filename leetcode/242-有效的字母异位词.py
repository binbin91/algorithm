# -*- coding: utf-8 -*-

import collections


def aa(s, t):
    sd = collections.defaultdict(int)
    td = collections.defaultdict(int)
   
    for i in s: sd[i] += 1
    for i in t: td[i] += 1
    return sd == td


if __name__ == "__main__":
    print aa("anagram", "nagaram")
    print aa("rat", "car")
