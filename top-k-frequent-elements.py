import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        klargest = heapq.nlargest(k, [(value, key) for key, value in freq.items()])
        return [item[1] for item in klargest]