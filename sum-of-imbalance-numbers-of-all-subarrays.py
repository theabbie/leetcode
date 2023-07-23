from sortedcontainers import SortedList

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            curr = SortedList()
            ctr = 0
            for j in range(i, n):
                curr.add(nums[j])
                k = curr.bisect_left(nums[j])
                p = 0
                diff = 0
                for l in [k - 1, k + 1]:
                    if 0 <= l < len(curr):
                        p += 1
                        if l == k - 1:
                            diff -= curr[l]
                        else:
                            diff += curr[l]
                        if abs(curr[k] - curr[l]) > 1:
                            ctr += 1
                if p == 2 and diff > 1:
                    ctr -= 1
                res += ctr
        return res