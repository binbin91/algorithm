# -*- coding: utf-8 -*-

from collections import defaultdict


class TreeNode(object):
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.isword = False

class Trie(object):
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        cur = self.root
        for w in word: cur = cur.children[w]
        cur.isword = True

    def search(self, word):
        cur = self.root
        for w in word:
            cur = cur.children.get(w)
            if cur is None: return False
        return cur.isword

    def startsWith(self, prefix):
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur is None: return False
        return True
