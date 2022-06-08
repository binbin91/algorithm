# -*- coding: utf-8 -*-


def aa(s):
    if len(s) == 0: return False
    nxt = [0] * len(s) 
    getnext(nxt, s)
    if nxt[-1] != -1 and len(s) % (len(s) - (nxt[-1] + 1)) == 0:
        return True
    return False

def getnext(nxt, s):
    nxt[0] = -1
    j = -1
    for i in range(1, len(s)):
        while j >= 0 and s[i] != s[j+1]:
            j = nxt[j]
        if s[i] == s[j+1]:
            j+=1
        nxt[i] = j
    return nxt


if __name__ == "__main__":
    print aa("abab")
