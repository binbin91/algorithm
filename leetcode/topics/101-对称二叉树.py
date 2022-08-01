# -*- coding: utf-8 -*-

# Carl哥,二叉树递归三部曲:
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归逻辑

# 本题, 需要比较根节点的两个子树是否是相互翻转, 进而判断这个树是不是对称树
# So
# 1, 参数为左子树节点和右子树节点
# 2, 比较数值相不相同:
#    节点为空: 左节点为空右节点不为空返回false, 左为空右不为空返回false, 左右都为空返回true
#    节点不为空: 左右数值不相等返回false
# 3, 单层递归逻辑就是处理左右不为空, 且数值相等
#    比较外侧是否对称, 传入左节点左孩子, 右节点右孩子
#    比如内侧是否对称, 传入左节点右孩子, 右节点左孩子
#    若左右都对称返回true, 否则返回false

def aa(root):
    def recur(l, r):
        if not l and not r: return True
        if not l or not r or l.val != r.val: return False
        return recur(l.left, r.right) and recur(l.right, r.left)
    return recur(root.left, root.right) if root else True


# 迭代法(使用栈)
def bb(root):
    if not root: return True
    stack = []
    stack.append(root.left)
    stack.append(root.right)
    while stack:
        ln, rn = stack.pop(), stack.pop()
        if not ln and not rn:
            continue
        if not ln or not rn or ln.val != rn.val:
            return False
        res.append(ln.left)
        res.append(rn.right)
        res.append(ln.right)
        res.append(rn.left)
    return True
