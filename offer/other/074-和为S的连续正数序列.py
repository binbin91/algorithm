# -*- coding: utf-8 -*-

def aa(target):
    i,j,s,res = 1,2,3,[]
    while i<j:
        if s == target: 
            res.append(list(range(i,j+1)))
        if s >= target: 
            s-=i 
            i+=1
        else: 
            j+=1 
            s+=j
    return res


if __name__ == "__main__":
    print aa(9)
