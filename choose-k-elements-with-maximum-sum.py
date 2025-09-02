import heapq

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        items = [(nums1[i], i, nums2[i]) for i in range(n)]
        items.sort(key=lambda item: item[0])
        res = [0] * n
        minHeap = []
        currentSum = 0
        i = 0
        while i < n:
            j = i
            while j < n and items[j][0] == items[i][0]:
                j += 1
            for t in range(i, j):
                numVal, origIndex, num2Val = items[t]
                res[origIndex] = currentSum
            for t in range(i, j):
                numVal, origIndex, num2Val = items[t]
                if len(minHeap) < k:
                    heapq.heappush(minHeap, num2Val)
                    currentSum += num2Val
                elif num2Val > minHeap[0]:
                    currentSum -= heapq.heappop(minHeap)
                    heapq.heappush(minHeap, num2Val)
                    currentSum += num2Val
            i = j
        return res