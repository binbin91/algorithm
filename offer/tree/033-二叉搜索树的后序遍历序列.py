# -*- coding: utf-8 -*-

# 已知
# 后序遍历: 节点按照[ 左子树 | 右子树 | 根节点] 排序
# 二叉树: 左子树中所有节点值 < 根节点的值, 右子树中的所有节点的值 > 根节点的值

# 后序遍历倒序(根-右-左) + 栈(存储值递增节点)
def aa(postorder):
    stack, root = [], float("+inf")
    for i in range(len(postorder)-1, -1, -1):
        # 若大于root则说明不满足二叉搜索树定义直接返回False
        if postorder[i] > root: return False
        while (stack and postorder[i] < stack[-1]):
            # 若遇递减节点, 要满足二叉树定义: 1. 递减节点的父节点要大于且接近递减节点  2. 递减节点的所有节点都要小于递减节点的父节点
            root = stack.pop()
        stack.append(postorder[i])
    return True


# 递归分治
def bb(postorder):
    def recur(i, j):
        if i >= j: return True
        # 划分左子树区间
        p = i
        while postorder[p] < postorder[j]: 
            p += 1
        m = p
        # 划分右子树区间
        while postorder[p] > postorder[j]:
            p += 1
        return p ==j and recur(i, m-1) and recur(m, j-1)
     return recur(0, len(postorder)-1)
