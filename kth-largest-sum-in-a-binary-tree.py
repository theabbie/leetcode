from collections import *

class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return -1
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
    
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        res = []
        q = deque([root])
        while q:
            curr = 0
            n = len(q)
            for _ in range(n):
                r = q.pop()
                curr += r.val
                if r.left:
                    q.appendleft(r.left)
                if r.right:
                    q.appendleft(r.right)
            res.append(curr)
        return self.findKthLargest(res, k)