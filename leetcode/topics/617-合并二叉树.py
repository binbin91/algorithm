# -*- coding: utf-8 -*-

from collections import deque

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 传入两个二叉树跟节点, 返回合并后的二叉树跟节点 
# 若r1为空返回r2, 若r2为空返回r1
# 两棵树元素相加
#   r1左子树合并: 合并r1左子树与r2左子树
#   r2右子树合并: 合并r1右子树与r2右子树

def aa(r1, r2):
    if not r1: return r2
    if not r2: return r1
    r1.val += r2.val
    r1.left = aa(r1.left, r2.left)
    r1.right = aa(r1.right, r2.right)
    return r1


# 迭代法(前序遍历)
def bb(r1, r2):
    if not r1: return r2
    if not r2: return r1
    queue = deque()
    queue.append([r1])
    queue.append([r2])
    while queue:
        n1, n2 = queue.popleft(), queue.popleft()
        # 当两个节点都有左子树时, 才会往queue放入
        if n1.left and n2.left:
            queue.append(n1.left)
            queue.append(n2.left)
        # 当两个节点都有右子树时, 才会往queue放入
        if n1.right and n2.right:
            queue.append(n1.right)
            queue.append(n2.right)
        # 更新当前节点, 并改变当前节点左右孩子
        n1.val += n2.val
        if not n1.left and n2.left:
            n1.left = n2.left
        if not n1.right and n2.right:
            n1.right = n2.right
    return r1
