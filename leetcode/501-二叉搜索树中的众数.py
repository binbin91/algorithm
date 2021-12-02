# -*- coding: utf-8 -*-

# 已知二叉搜索树: 
#  1. 左子树中所有节点值 < 根节点的值
#  2. 右子树中的所有节点的值 > 根节点的值
#  3. 它的左右子树也分别为二叉搜索树

# 中序遍历, 输出的二叉搜索树节点的数值是有序序列
def aa(root):
    stack, cur, pre, cnt, max_cnt, res = [], root, None, 0, 0, []
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if pre is None: cnt = 1
            elif pre.val == cur.val: cnt += 1
            else: cnt = 1
            if cnt == max_cnt: res.append(cur.val)
            if cnt > max_cnt: 
                max_cnt = cnt
                res.clear()
                res.append(cur.val)
            pre = cur
            cur = cur.right
    return res
