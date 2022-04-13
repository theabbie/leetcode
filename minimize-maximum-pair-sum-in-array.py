import heapq

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        minheap = []
        maxheap = []
        for num in nums:
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
        n = len(nums)
        smallest = heapq.nlargest(n // 2, minheap)
        biggest = heapq.nlargest(n // 2, maxheap)
        return max(smallest[i] - biggest[i] for i in range(n // 2))