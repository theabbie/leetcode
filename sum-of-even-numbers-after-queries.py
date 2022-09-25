class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        evensum = 0
        for el in nums:
            if el % 2 == 0:
                evensum += el
        res = []
        for val, i in queries:
            if nums[i] % 2 == 0:
                evensum -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                evensum += nums[i]
            res.append(evensum)
        return res