# -*- coding: utf-8 -*-

def aa(nums, target):
    r = dict()
    for i, v in enumerate(nums):
        if target - v not in r:
            r[v] = i
        else:
            return [r[target-v], i] 


if __name__ == "__main__":
    print aa([2,7,11,15], 9)
