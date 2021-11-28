# -*- coding: utf-8 -*-

# 辅助栈，若辅助栈栈底是出栈节点，则辅助栈出栈
def aa(pushed, popped):
    stack, i = [], 0
    for nums in pushed:
        stack.append(nums)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return not stack
