# -*- coding: utf-8 -*-

# 已知
# 祖先的定义: 若节点p在节点root的左(右)子树, 或p=root，则称root是p的祖先
# 最近祖先的定义: 设节点root为节点p,q的某公共祖先, 若其root.left和root.right都不是p,q的公共祖先, 则称root是最近的公共祖先

# 解题
# 1.若root等于p,q，则直接返回root
# 2.递归左子节点和右子节点
# 3.当left为空返回right，当right为空返回left

def aa(root, p, q):
    if not root or root == p or root = q: return root
    left = aa(root.left, p, q)
    right = aa(root.right, p, q)
    if not left: return right
    if not right: return left
    return root
