class Block:
    def __init__(self, size, mID, nxt = None):
        self.size = size
        self.mID = mID
        self.next = nxt

class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.head = Block(n, -1)
        
    def allocate(self, size: int, mID: int) -> int:
        curr = self.head
        l = 0
        while curr:
            if curr.size >= size and curr.mID == -1:
                prevID = curr.mID
                rem = curr.size - size
                curr.size = size
                curr.mID = mID
                if rem > 0:
                    curr.next = Block(rem, prevID, curr.next)
                return l
            l += curr.size
            curr = curr.next
        return -1

    def free(self, mID: int) -> int:
        curr = self.head
        res = 0
        while curr:
            if curr.mID == mID:
                res += curr.size
                curr.mID = -1
            curr = curr.next
        curr = self.head
        while curr:
            if curr.next and curr.mID == curr.next.mID == -1:
                curr.size += curr.next.size
                curr.next = curr.next.next
            else:
                curr = curr.next
        return res