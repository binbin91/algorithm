# -*- coding: utf-8 -*-

import collections

def serialize(data):
    if not root: return "[]"
    res, queue = [], collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")
    return '[' + ','.join(res) + ']'


# 序列化列表vals, 去掉首尾中括号以逗号分割
# 定义根节点和队列
# 构建node左右子节点
def deserialize(data):
    if data == '[]': return 
    vals, i = data[1:-1].split(','), 1
    root = TreeNode(int(vals[0]))
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if vals[i] != 'null':
            node.left = TreeNode(int(vals[i]))
            queue.append(node.left)
        i += 1
        if vals[i] != 'null':
            node.right = TreeNode(int(vals[i]))
            queue.append(node.right)
        i += 1
    return root
