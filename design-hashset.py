class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.end = False

class MyHashSet:

    def __init__(self):
        self.root = Node()

    def add(self, key: int) -> None:
        curr = self.root
        while key:
            if key & 1:
                if curr.right == None:
                    curr.right = Node()
                curr = curr.right
            else:
                if curr.left == None:
                    curr.left = Node()
                curr = curr.left
            key = key >> 1
        curr.end = True

    def remove(self, key: int) -> None:
        curr = self.root
        while key:
            if curr == None:
                return None
            if key & 1:
                curr = curr.right
            else:
                curr = curr.left
            key = key >> 1
        if not curr or not curr.end:
            return
        curr.end = False

    def contains(self, key: int) -> bool:
        curr = self.root
        while key:
            if curr == None:
                return False
            if key & 1:
                curr = curr.right
            else:
                curr = curr.left
            key = key >> 1
        if not curr:
            return False
        return curr.end