# -*- coding: utf-8 -*-

def aa(data):
    res = []
    for i in data:
        if i == ' ':
            res.append('%20')
        else:
            res.append(i)
    return ''.join(res)

if __name__ == "__main__":
    data = 'We are happy.'
    print aa(data)
