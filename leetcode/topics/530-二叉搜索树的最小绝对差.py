# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 中序遍历, 输出的二叉搜索树节点的数值是有序序列, 有了这个特性, 就相当于在一个有序序列上求俩个数最小差值
def aa(root):
    stack, cur, pre, res = [], root, None, float("inf") 
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if pre: res = min(res, cur.val - pre.val) 
            pre, cur = cur, cur.right
    return res
