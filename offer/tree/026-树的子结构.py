# -*- coding: utf-8 -*-

# 先序遍历+判断
# 若树B是树A的子结构，则子结构的根节点可能为树A的任意一个节点. 因此判断树B是否是树A的子结构，需要以下两部
# 1. 先序遍历树A中的每个节点na  2. 判断树A中以na为根节点的子树是否包含树B 

def aa(a, b):
    def recur(a, b):
        # 节点a为空, 说明树B已经匹配完成, 所以返回True
        if not b: return True
        # 节点b为空，说明已经越过树A叶子节点 ｜ 若a和b的值不同，即表示匹配失败返回False
        if not a or a.val != b.val: return False
        return recur(a.left, b.left) and recur(a.right, b.right) 
    # 若树B是树A子结构, 需要满足以下3种情况:
    # 1. 节点a为根节点的子树包含树b  2. 树B是树A左子树的子结构 3. 树B是树A右子树的子结构
    return bool(a and b) and (recur(a, b) or aa(a.left, b) or aa(a.right, b)) 
