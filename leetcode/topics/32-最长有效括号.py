# -*- coding: utf-8 -*-


# 使用辅助栈, 找到可以匹配的索引号, 然后找出最长连续数列
def aa(s):
    stack, res, lg = [-1], 0, len(s)
    for i in range(lg):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack: stack.append(i)
            else: res = max(res, i-stack[-1])
    return res


if __name__ == "__main__":
    print aa("(()")
    print aa(")()())")
    print aa("")
