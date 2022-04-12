import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        valIndexes = {}
        for i, num in enumerate(nums):
            if num not in valIndexes:
                heapq.heappush(heap, num)
            valIndexes[num] = valIndexes.get(num, []) + [i]
        op = []
        rest = k
        biggest = heapq.nlargest(k, heap)
        while rest > 0:
            indexes = valIndexes[biggest.pop(0)]
            for index in indexes:
                heapq.heappush(op, index)
                rest -= 1
                if rest == 0:
                    break
        return [nums[i] for i in heapq.nsmallest(k, op)]