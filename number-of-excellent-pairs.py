class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        res = 0
        ctr = [0] * 32
        for el in nums:
            x = "{:0b}".format(el).count("1")
            ctr[x] += 1
        for el in nums:
            x = "{:0b}".format(el).count("1")
            res += sum(ctr[max(k - x, 0):])
        return res