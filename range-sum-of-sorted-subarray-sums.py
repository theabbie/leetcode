class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        M = 10 ** 9 + 7
        vals = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                vals.append(s)
        vals.sort()
        return sum(vals[left-1:right]) % M