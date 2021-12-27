# -*- coding: utf-8 -*-


def aa(preorder, inorder):
    if not preorder: return
 
    # 前序遍历第一个就是当前的中间点
    root_val = preorder[0]
    root = TreeNode(root_val)
 
    # 获取切割点, 切割中序数组得到左右部分
    idx = inorder.index(root_val)
    in_left = inorder[:idx]
    in_right = inorder[idx+1:]
    
    # 切割前序数组得到左右部分, PS:中序数组大小一定要跟前序数组大小相同
    pre_left = preorder[1:1+len(in_left)]
    pre_right = preorder[1+len(in_left):]

    # 递归
    root.left = aa(pre_left, in_left)
    root.right = aa(pre_right, in_right)
    return root
