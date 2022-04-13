class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ctr = set()
        for i in range(1, n + 1):
            ctr.add(i)
        for num in nums:
            if num in ctr:
                ctr.remove(num)
        return list(ctr)