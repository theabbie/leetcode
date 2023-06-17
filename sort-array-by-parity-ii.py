class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odds = []
        evens = []
        for i in range(n):
            if nums[i] & 1:
                odds.append(nums[i])
            else:
                evens.append(nums[i])
        for i in range(n):
            if i & 1:
                nums[i] = odds.pop()
            else:
                nums[i] = evens.pop()
        return nums