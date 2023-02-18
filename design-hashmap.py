class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        self.end = False

class MyHashMap:

    def __init__(self):
        self.root = Node()

    def put(self, key: int, value: int) -> None:
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
        curr.val = value
        curr.end = True

    def get(self, key: int) -> int:
        curr = self.root
        while key:
            if curr == None:
                return -1
            if key & 1:
                curr = curr.right
            else:
                curr = curr.left
            key = key >> 1
        if not curr or not curr.end:
            return -1
        return curr.val

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