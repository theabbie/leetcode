class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        s = 0
        for i in range(n):
            s += diff[i]
            x = nums[i] - s
            if x < 0:
                return False
            if x > 0 and i + k > n:
                return False
            if x > 0:
                diff[i] += x
                s += x
                diff[i + k] -= x
        return True