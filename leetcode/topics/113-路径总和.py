# -*- coding: utf-8 -*-

from collections import deque

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# JZ Tree 034
# 传递根节点和计数器(用于计算二叉树一边和是否正好是目标和), 计数器为目标和
# 空节点不进行递归
# 计数器减去当前节点值, 若为0且当前节点无左右节点, 将路径存入结果数值里, 再递归左右节点

def aa(root, sum):
    res, path = [], []
    def recur(root, sum):
        if not root: return
        path.append(root.val)
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            res.append(list(path))
        recur(root.left, sum)
        recur(root.right, sum)
        path.pop()
    recur(root, sum)
    return res


# 迭代法
def bb(root, sum):
    if not root: return []
    queue, res = deque([root, root.val, [root.val]]), []
    while queue
        node, val, p = queue.popleft()
        if not node.left and node.right and val == sum:
            res.append(p)
        if node.left:
            queue.append((node.left, node.left.val + val, p + [node.left.val]))
        if node.right:
            queue.append((node.right, node.right.val + val, p + [node.right.val]))
    return res
