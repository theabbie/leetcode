class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        minDist = float('inf')
        prev = None
        for i, num in enumerate(nums):
            if num == 1:
                if prev:
                    minDist = min(minDist, i - prev - 1)
                prev = i
        print(minDist)
        return minDist >= k

print(Solution().kLengthApart([1,0,1], 2))