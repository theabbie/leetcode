class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ctr = [0] * 102
        for a, b in nums:
            ctr[a] += 1
            ctr[b + 1] -= 1
        for i in range(1, 102):
            ctr[i] += ctr[i - 1]
        return len(ctr) - ctr.count(0)