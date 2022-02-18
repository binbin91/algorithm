# -*- coding: utf-8 -*-

# 后续遍历
# 进阶, 不使用额外空间
def aa(root):
    while root:
        # 若左子树存在才进行操作
        if root.left:
            # 找到左子树最深的右子树
            sl = root.left
            while sl.right: sl = sl.right
            # 将root右子树挂到左子树最深的右子树
            sl.right = root.right
            # 将左子树挂到右子树
            root.right = root.left
            # 清空root左子树
            root.left = None
        root = root.right
    return
