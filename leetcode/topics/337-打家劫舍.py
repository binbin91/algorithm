# -*- coding: utf-8 -*-

# Carl哥,动规五部曲:
# 1. 确定dp数组以及下标含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导数组


def rob(root):
    res = aa(root) 
    return max(res[0], res[1])

# dp数组, 下标0记录不偷该节点所得到的最大金钱, 下标1记录偷该节点所得到的最大金钱
def aa(root):
    if not root: return (0, 0)
    l = aa(root.left)
    r = aa(root.right)
    v1 = root.val + l[1] + r[1] # 偷当前节点, 不偷子节点
    v2 = max(l[0], l[1]) + max(r[0], r[1]) # 不偷当前节点, 偷子节点
    return (v1, v2) 
