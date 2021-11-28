# -*- coding: utf-8 -*-

# 已知
# 前序遍历: 节点按照 [ 根节点 | 左子树 | 右子树 ] 排序
# 中序遍历: 节点按照 [ 左子树 | 根节点 | 右子树 ] 排序

# 解题
# 1.前序遍历的首元素为树的根节点node的值
# 2.中序遍历中搜索根节点node的索引, 可将中序遍历划分为 左子树-根节点-右子树
# 3.根据中序遍历中的左(右)子树的节点数量，可将前序遍历划分为 根节点-左子树-右子树
# 三步确定根节点、左子树根节点、右子树根节点
# 
# 分治: 1. 建立根节点node -> preorder[root]  2. 划分左右子树 3. 左右子树递归 4. 回溯返回node

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


def aa(preorder, inorder):
    def recur(root, left, right):
        # 递归终止
        if left > right: return 
        # 建立根节点
        node = TreeNode(preorder[root])
        # 划分根节点、左子树、右子树
        i = dic[preorder[root]]
        # 左子树: 根节点索引(root+1)  中序遍历左边界(left), 中序遍历右边界(i-1) 
        node.left = recur(root+1, left, i-1)
        # 右子树: 根节点索引(i-left+root+1)  中序遍历左边界(i+1), 中序遍历右边界(right) 
        node.right = recur(i-left+root+1, i+1, right)
        return node
    
    dic, preorder = {}, preorder
    for i in range(len(inorder)):
        dic[inorder[i]] = i
    return recur(0, 0, len(inorder)-1)


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print aa(preorder, inorder)
