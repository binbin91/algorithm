# -*- coding: utf-8 -*-

from collections import deque


def aa(r1, r2):
    if not r1: return r2
    if not r2: return r1
    r1.val += r2.val
    r1.left = aa(r1.left, r2.left)
    r1.right = aa(r1.right, r2.right)
    return r1


def bb(r1, r2):
    if not r1: return r2
    if not r2: return r1
    queue = deque([r1])
    queue.append([r2])
    while queue:
        n1, n2 = queue.popleft(), queue.popleft()
        if n1.left and n2.left:
            queue.append(n1.left)
            queue.append(n2.left)
        if n1.right and n2.right:
            queue.append(n1.right)
            queue.append(n2.right)
        n1.val += n2.val
        if not n1.left and not n2.left:
            n1.left = n2.left
        if not n1.right and not n1.right:
            n1.right = n2.right
    return r1
