import heapq

class Solution:
    def largestSumAfterKNegations(self, nums, k):
        currSum = 0
        heap = []
        for num in nums:
            currSum += num
            heapq.heappush(heap, num)
        i = 0
        while i < k:
            item = heapq.heappop(heap)
            if item < 0:
                currSum -= 2 * item
                i += 1
            if item >= 0:
                if (k - i) % 2 == 0:
                    currSum += 2 * item
                else:
                    currSum -= 2 * item
                break
        return currSum

print(Solution().largestSumAfterKNegations([1,3,2,6,7,9], 3))