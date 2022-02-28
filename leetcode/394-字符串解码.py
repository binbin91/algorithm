# -*- coding: utf-8 -*-


def aa(s):
    stack, res, m = [], '', 0
    for i in s:
        if i == '[': 
            stack.append([m, res])
            res, m = '', 0
        elif i == ']':
            cm, lr = stack.pop()
            res = lr + cm * res
        elif '0' <= i <= '9':
            m = m * 10 + int(i)
        else:
            res += i
    return res 


if __name__ == "__main__":
    print aa("3[a]2[bc]")
    print aa("3[a2[c]]")
    print aa("2[abc]3[cd]ef")
    print aa("abc3[cd]xyz")
