MAXN = 10 ** 5

version = -1

tree = [(float('-inf'), version)] * (4 * MAXN + 5)

def get(pos):
    if tree[pos][1] < version:
        return float('-inf')
    return tree[pos][0]

class SegTree:
    def __init__(self):
        self.tree = tree
        
    def update(self, i, v, x, y, root):
        if x + 1 == y:
            self.tree[root] = (v, version)
            return
        mid = (x + y) // 2
        if i < mid:
            self.update(i, v, x, mid, 2 * root)
        else:
            self.update(i, v, mid, y, 2 * root + 1)
        self.tree[root] = (max(get(2 * root), get(2 * root + 1)), version)
        
    def nextGreater(self, i, v, x, y, root):
        if x + 1 == y:
            if get(root) <= v:
                return -1
            return x
        mid = (x + y) // 2
        if get(2 * root) > v and mid > i:
            curr = self.nextGreater(i, v, x, mid, 2 * root)
            if curr != -1:
                return curr
        return self.nextGreater(i, v, mid, y, 2 * root + 1)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        global version
        nums = nums + nums
        n = len(nums)
        version += 1
        segtree = SegTree()
        for i in range(n):
            segtree.update(i, nums[i], 0, n, 1)
        nums.append(-1)
        return [nums[segtree.nextGreater(i + 1, nums[i], 0, n, 1)] for i in range(n // 2)]