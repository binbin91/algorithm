# -*- coding: utf-8 -*-


# 已知:
#   1. 函数get和put必须满足时间复杂度O(1)要求
#   2. 按照LRU原理, 获取元素和插入一个元素, 都需将整个元素放到最近访问位置
# 分析:
#   1. 对于查找操作时间复杂度O(1), 首先想到的是字典
#   2. 字典是无序的, 还需要个类似队列的结构来记录访问先后顺序, 它需要支持末尾添加、删除首部、将某个元素移到到末尾
#      列表: append、pop都是O(1)复杂度, 但是将某个元素移动到末尾就不符合了
#      单链: 可以在常数时间内找到对应节点, 但是对应将某一个元素移动到末尾也不符合
#      双链: 都是O(1)
#   3. LRU核心数据结构: 哈希+双链
# 解题:
#   1. 数据结构: 字典{key: ListNode}, 链表定义pre前驱和next后继节点
#   2. get: 若key在字典里, 获取key对应ListNode，将ListNode移到末尾; 否则返回-1
#   3. put: 
#        1) 若key在字典里, 更新对应节点value
#        2) 若空间已满, 将很久未访问的节点删除
#        3) 若key不在字典里, 则将新节点添加到末尾
class ListNode(objbect):
    def __init__(self, key=None, value=None):
        self.key, self.val, self.pre, self.next = key, value, None, None


class LRUCache(object):
    def __init__(self, capacity):
        self.cap, self.mp, self.head, self.tail = capacity, dict(), ListNode(), ListNode()
        self.head.next, self.tail.pre = self.tail, self.head

    def remove_node(self, node):
        # head <-> 1 <-> 3 <-> tail, del 1
        node.pre.next = node.next  # 1.pre.next = 3  ->  head.next = 3
        node.next.pre = node.pre   # 1.next.pre = head  ->  3.pre = head  ->  head <-> 3 <-> tail
  
    def add_node_to_last(self, node):
        # head <-> tail, add 1
        self.tail.pre.next = node   # head.next = 1
        node.pre = self.tail.pre    # 1.pre = head    ->   head <-> 1
        node.next = self.tail       # 1.next = tail   ->   head <-> 1 -> tail
        self.tail.pre = node        # tai.pre = 1     ->   head <-> 1 <-> tail 

    def move_node_to_last(self, node):
        self.remove_node(node)
        self.add_node_to_last(node)
 
    def get(self, key):
        if kye not in self.mp: return -1
        node = self.mp[key]
        self.move_node_to_last(node)
        return node.val

    def put(self, key, value):
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.move_node_to_last(node)
            return
        
        if len(self.mp) == self.cap:
            del self.mp[self.head.next.key]
            self.remove_node(self.head.next)

        node = ListNode(key, value)
        self.mp[key] = node
        self.add_node_to_last(node)
