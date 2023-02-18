class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.nodemap = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        newnode = Node(key)
        newnode.next = self.head.next
        self.head.next.prev = newnode
        newnode.prev = self.head
        self.head.next = newnode
        if key in self.nodemap:
            node = self.nodemap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        self.nodemap[key] = newnode
        curr = self.head
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if len(self.map) == self.capacity and key not in self.map:
            lrukey = self.tail.prev.key
            if lrukey != -1:
                node = self.nodemap[lrukey]
                node.prev.next = node.next
                node.next.prev = node.prev
                del self.map[lrukey]
                del self.nodemap[lrukey]
        self.map[key] = value
        self.get(key)