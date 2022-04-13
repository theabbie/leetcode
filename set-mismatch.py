class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ctr = set()
        n = len(nums)
        for i in range(1, n + 1):
            ctr.add(i)
        for num in nums:
            if num in ctr:
                ctr.remove(num)
            else:
                dup = num
        return [dup, list(ctr)[0]]