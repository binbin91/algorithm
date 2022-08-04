# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 中序遍历, 输出的二叉搜索树节点的数值是有序序列, 有了这个特性, 就相当于判断一个序列是不是递增的
def aa(root):
    stack, cur, pre = [], root, None
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            # 判断当前节点和前继节点的大小关系是否满足递增关系
            if pre and cur.val <= pre.val:
                return False
            pre, cur = cur, cur.right
    return True
