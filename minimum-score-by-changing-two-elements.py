class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = float('inf')
        for i in [0, 1, n - 2, n - 1]:
            for j in [0, 1, n - 2, n - 1]:
                for x in [i - 1, i + 1]:
                    for y in [j - 1, j + 1]:
                        if 0 <= x < n and 0 <= y < n:
                            oldi = nums[i]
                            oldj = nums[j]
                            nums[i] = nums[x]
                            nums[j] = nums[y]
                            s = sorted(nums)
                            mindiff = min(s[i + 1] - s[i] for i in range(n - 1))
                            res = min(res, s[-1] - s[0] + mindiff)
                            nums[i] = oldi
                            nums[j] = oldj
        return res