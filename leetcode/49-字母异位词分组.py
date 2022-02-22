# -*- coding: utf-8 -*-

def aa(strs):
    d = {}
    for s in strs:
        k = tuple(sorted(s))
        d[k] = d.get(k, []) + [s]
    return list(d.values())


if __name__ == "__main__":
    print aa(["eat", "tea", "tan", "ate", "nat", "bat"])
    print aa([""])
    print aa(["a"])
