from collections import deque

# class Solution:
#     def shortestSubarray(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         currSum = 0
#         sumTill = [currSum]
#         currSmallest = (0, n + 1)
#         for num in nums:
#             currSum += num
#             sumTill.append(currSum)
#         for i in range(n + 1):
#             for j in range(i + 1, n + 1):
#                 if sumTill[j] - sumTill[i] >= k:
#                     if (j - i) < currSmallest[1] - currSmallest[0]:
#                         currSmallest = (i, j)
#                 if (j - i) >= currSmallest[1] - currSmallest[0]:
#                     break
#         diff = currSmallest[1] - currSmallest[0]
#         if diff == n + 1:
#             return -1
#         else:
#             return diff

# class Solution:
#     def shortestSubarray(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         currSum = 0
#         sumTill = [currSum]
#         for num in nums:
#             currSum += num
#             sumTill.append(currSum)
#         for j in range(1, n + 1):
#             for i in range(n + 1 - j):
#                 if sumTill[i + j] - sumTill[i] >= k:
#                     return j
#         return -1

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        currSum = 0
        sumTill = [currSum]
        for num in nums:
            currSum += num
            sumTill.append(currSum)
        minLen = n + 1
        q = deque()
        for i, s in enumerate(sumTill):
            while q and s <= sumTill[q[-1]]:
                q.pop()
            while q and s - sumTill[q[0]] >= k:
                minLen = min(minLen, i - q.popleft())
            q.append(i)
        if minLen == n + 1:
            return -1
        return minLen