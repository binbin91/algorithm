# -*- coding: utf-8 -*-


def aa(s):
    stack = []
    for i in s:
        try:
            stack.append(int(i))
        except:
            n2, n1 = stack.pop(), stack.pop()
            stack.append(cal(n1, n2, i))
    return stack[0]

def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return int(n1/float(n2))


if __name__ == "__main__":
    print aa(["2", "1", "+", "3", "*"])
    print aa(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
