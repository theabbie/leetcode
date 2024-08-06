from sortedcontainers import SortedList

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i > 0:
            fn = lambda k: (float('inf') if nums[k] <= nums[i - 1] else nums[k], -k)
            closest = min(range(i, n), key = fn)
            nums[i - 1], nums[closest] = nums[closest], nums[i - 1]
        for p in range((n - i) // 2):
            nums[i + p], nums[n - p - 1] = nums[n - p - 1], nums[i + p]
    
    def getMinSwaps(self, num: str, k: int) -> int:
        n = len(num)
        vals = [int(c) for c in num]
        old = vals[:]
        for _ in range(k):
            self.nextPermutation(vals)
        res = 0
        pos = [[] for _ in range(10)]
        for i in range(n):
            pos[vals[i]].append(i)
        ctr = [0] * 10
        p = []
        bst = SortedList()
        for i in range(n):
            res += len(bst) - bst.bisect_left(pos[old[i]][ctr[old[i]]] + 1)
            bst.add(pos[old[i]][ctr[old[i]]])
            ctr[old[i]] += 1
        return res