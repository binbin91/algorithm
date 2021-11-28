# -*- coding: utf-8 -*-

def aa(n1, n2, n3, n4):
    hm = dict()
    for i in n1:
        for j in n2:
            if i + j in hm:
                hm[i+j] += 1
            else:
                hm[i+j] = 1
     
    count = 0
    for i in n3:
        for j in n4:
            k = - i - j
            if k in hm:
                count += hm[k]
    return count


if __name__ == "__main__":
    print aa([1,2], [-2,-1], [-1,2], [0,2])
