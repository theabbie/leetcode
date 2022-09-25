class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        order = sorted(nums)
        diff = {}
        p = [0]
        for el in order:
            p.append(p[-1] + el)
        for i in range(1, n + 1):
            diff[order[i - 1]] = order[i - 1] * (2 * i - n) - 2 * p[i] + p[-1]
        return [diff[el] for el in nums]