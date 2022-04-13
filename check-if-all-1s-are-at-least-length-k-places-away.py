class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        minDist = float('inf')
        prev = None
        numOnes = 0
        for i, num in enumerate(nums):
            if num == 1:
                numOnes += 1
                if prev:
                    minDist = min(minDist, i - prev - 1)
                prev = i
        if numOnes <= 1:
            return True
        if minDist == float('inf'):
            return False
        return minDist >= k