# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self, Node=None):
        self.__head = Node

    def is_empty(self):
        return self.__head == None

    def head(self):
        return self.__head

    def add(self, item):
        node = ListNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self.__head
        while cur != None:
            print cur.val
            cur = cur.next
