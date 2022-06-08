# -*- coding: utf-8 -*-


def aa(s):
    s = s.strip()
    i = j = len(s)-1
    res = []
    while i >= 0:
        while i >= 0 and s[i] != ' ':
            i -= 1
        res.append(s[i+1:j+1])
        while s[i] == ' ':
            i -= 1
        j = i
    return ' '.join(res) 


if __name__ == "__main__":
    data = "blue is the sky"
    print aa(data)
