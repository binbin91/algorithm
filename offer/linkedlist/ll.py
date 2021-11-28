# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.__head = ListNode(0)
        self.__count = 0
 
    def insert(self, item):
        self.add_to_index(0, item)

    def append(self, item):
        self.add_to_index(self.__count, item)
        
    def add_to_index(self, index, item):
        if index < 0:
            index = 0
        elif index > self.__count:
            return

        self.__count += 1
        node = ListNode(item)
        pre, cur = None, self.__head
        for _ in range(index + 1):
            pre, cur = cur, cur.next
        else:
            pre.next, node.next = node, cur
         
    def get(self, index):
        if 0 <= index < self.__count:
            node = self.__head
            for _ in range(index + 1):
                node = node.next
            return node
        else:
            return -1

    def travel(self):
        if not self.__head.next: return
        cur = self.__head.next
        for i in range(self.__count):
            print cur.val
            cur = cur.next
