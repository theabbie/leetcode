from sortedcontainers import SortedList

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = Counter()
        bst = SortedList()
        res = 0
        while res < n and nums[res] == nums[0]:
            res += 1
        for i in range(n):
            if ctr[nums[i]] > 0:
                bst.remove(ctr[nums[i]])
            ctr[nums[i]] += 1
            bst.add(ctr[nums[i]])
            if i + 1 <= res:
                continue
            if bst[0] == bst[-1] == 1:
                res = i + 1
            if len(bst) == 1:
                continue
            if len(bst) >= 3:
                if bst[0] == 1 and bst[1] == bst[-1]:
                    res = i + 1
                if bst[0] == bst[-2] and bst[-1] == 1 + bst[-2]:
                    res = i + 1
            elif bst[0] == 1 or bst[1] == 1 + bst[0]:
                res = i + 1
        return res