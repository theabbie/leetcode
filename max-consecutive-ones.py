class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums += [-1]
        maxOnes = 0
        curr = 0
        for num in nums:
            if num == 0 or num == -1:
                maxOnes = max(maxOnes, curr)
                curr = 0
            else:
                curr += 1
        return maxOnes