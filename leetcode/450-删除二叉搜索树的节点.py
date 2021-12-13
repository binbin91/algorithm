# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

def aa(root, key):
    if not root: return root
    if root.val = key:
        # 左右都为空, 删除节点，返回空为根节点
        if not root.left and not root.right:
            del root
            return
        # 左孩子为空右孩子不为空, 删除节点，右孩子补位，返回右孩子为根节点
        if not root.left and root.right:
            tmp, root = root, root.right
            del tmp
            return root
        # 右孩子为空左孩子不为空, 删除节点，左孩子补位，返回左孩子为根节点
        if root.left and not root.right:
            tmp, root = root, root.left
            del tmp
            return root
        # 左右孩子节点都不为空, 则将删除节点的左子树放到删除节点的右子树的最左边节点的左孩子位置
        else:
            v = root.right
            while v.left: v = v.left
            v.left, tmp, root = root.left, root, root.right
            del tmp
            return root
    if root.val > key: root.left = aa(root.left, key)
    if root.val < key: root.right = aa(root.right, key) 
    return root
