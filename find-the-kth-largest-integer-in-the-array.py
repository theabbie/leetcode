import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        kthlargest = heapq.nlargest(k, [int(num) for num in nums])
        return str(kthlargest[k - 1])