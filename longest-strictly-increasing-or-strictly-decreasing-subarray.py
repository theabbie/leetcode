class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def g(a):
            r = x = 1
            for i in range(len(a) - 2, -1, -1):
                if a[i] < a[i + 1]:
                    x += 1
                else:
                    x = 1
                r = max(r, x)
            return r
        return max(g(nums), g(nums[::-1]))