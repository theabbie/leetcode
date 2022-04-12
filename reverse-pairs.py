import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        sortednums = []
        ctr = 0
        for i in range(n):
            k = bisect.bisect_right(sortednums, 2 * nums[i])
            ctr += i - k
            bisect.insort(sortednums, nums[i])
        return ctr