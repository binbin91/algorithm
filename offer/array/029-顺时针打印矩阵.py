# -*- coding: utf-8 -*-

def matrix(array):
    if not array: return []
    l, r, t, b, res = 0, len(array[0])-1, 0, len(array)-1, []
    while True:
        for i in range(l, r+1):
            res.append(array[t][i])
        t += 1
        if t>b: break
      
        for i in range(t, b+1):
            res.append(array[i][r])
        r -= 1
        if l>r: break
 
        for i in range(r, l-1, -1):
            res.append(array[b][i])
        b -= 1
        if t>b: break
       
        for i in range(b, t-1, -1): 
            res.append(array[i][l])
        l += 1
        if l>r: break
    return res

if __name__ == "__main__":
    array = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    print matrix(array)
    print matrix([[1,2],[3,4]])
    print matrix([[1],[2],[3],[4]])
    print matrix([[1]])
