class SQRT:
    def __init__(self, arr):
        n = len(arr)
        B = int(pow(n, 0.5) + 1)
        blocks = [[set(), set()] for _ in range(B)]
        self.total = 0
        for i in range(n):
            blocks[i // B][arr[i]].add(i % B)
            self.total += arr[i]
        self.B = B
        self.blocks = blocks
        
    def flip(self, l, r):
        i = l
        while i <= r:
            if i % self.B == 0 and i + self.B - 1 <= r:
                self.total -= len(self.blocks[i // self.B][1])
                self.blocks[i // self.B].reverse()
                self.total += len(self.blocks[i // self.B][1])
                i += self.B
            else:
                if i % self.B in self.blocks[i // self.B][0]:
                    self.blocks[i // self.B][0].remove(i % self.B)
                    self.blocks[i // self.B][1].add(i % self.B)
                    self.total += 1
                else:
                    self.blocks[i // self.B][1].remove(i % self.B)
                    self.blocks[i // self.B][0].add(i % self.B)
                    self.total -= 1
                i += 1

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        curr = sum(nums2)
        res = []
        sq = SQRT(nums1)
        for t, x, y in queries:
            if t == 1:
                sq.flip(x, y)
            if t == 2:
                curr += x * sq.total
            if t == 3:
                res.append(curr)
        return res