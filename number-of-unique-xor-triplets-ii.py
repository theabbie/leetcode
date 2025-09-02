class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        s = {nums[i] ^ nums[j] for i in range(n) for j in range(i, n)}
        return len({el ^ x for el in set(nums) for x in s})