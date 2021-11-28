# -*- coding: utf-8 -*-


def aa(s):
    stack = []
    for i in s:
        if i not in {"+", "-", "*", "/"}:
            stack.append(i)
        else:
            f, s = stack.pop(), stack.pop()
            stack.append(int(eval('{} {} {}'.format(f, i, s))))
    return int(stack.pop())


if __name__ == "__main__":
    print aa(["2", "1", "+", "3", "*"])
    print aa(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
