# -*- coding: utf-8 -*-


def aa(s):
    stack = []
    mp = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for i in s:
        if i in mp:
            stack.append(mp[i])
        elif not stack or stack[-1] != i:
            return False
        else:
            stack.pop()
    return True if not stack else False

def bb(s):
    stack = []
    for i in s:
        if i == '(': stack.append(')')
        elif i == '[': stack.append(']')
        elif i == '{': stack.append('}')
        elif not stack or stack[-1] != i: return False
        else: stack.pop()
    return True if not stack else False


if __name__ == "__main__":
    print aa("()")
    print bb("(]")
