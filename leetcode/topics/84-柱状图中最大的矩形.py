# -*- coding: utf-8 -*-

# Carl哥之单调栈
# 当一维数组, 要寻找任一元素右边or左边第一个比自己大or小的元素位置, 此时使用单调栈
# 单调栈本质，就是空间换时间, 因为在遍历过程中需要用一个栈来记录右边第一个比当前元素的元素, 优点是只需遍历一次
# 单调栈三部曲:
# 1. 单调栈存放的元素是什么?
#    单调栈只需存放元素下标i即可, 若需使用直接t[i]
# 2. 单调栈里元素是递增还是递减
# 3. 单调栈判断条件
#    a) 当前遍历元素T[i]小于栈顶元素T[st.top()]的情况
#    b) 当前遍历元素T[i]等于栈顶元素T[st.top()]的情况
#    c) 当前遍历元素T[i]大于栈顶元素T[st.top()]的情况

def aa(heights):
    # 数组首位增加0
    heights.insert(0, 0)
    heights.append(0)
    stack = [0]
    res = 0
    for i in range(1, len(heights)):
        while stack and heights[i] < heights[stack[-1]]:  # 情况c
            mid_height = heights[stack[-1]]
            stack.pop()
            if stack:
                area = (i - stack[-1] - 1) * mid_height  # width * height
                res = max(res, area)
        stack.append(i)
    return res


if __name__ == "__main__":
    print aa([2, 1, 5, 6, 2, 3])
    print aa([2, 4])
