# -*- coding: utf-8 -*-

# 分割字符串(split), 再倒序拼接字符串([::-1])

def aa(data):
    s = data.split(' ')
    res = []
    for i in s:
        if i != '':
            res.append(i)
    return ' '.join(res[::-1])

def bb(data):
    return ' '.join(data.strip().split()[::-1])

if __name__ == "__main__":
    data = "blue is the sky"
    print aa(data)
    print bb('student. a am I')
