class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        for num in nums:
            for i in range(n):
                curr = num[:i] + str(1 - int(num[i])) + num[i + 1:]
                if curr not in nums:
                    return curr