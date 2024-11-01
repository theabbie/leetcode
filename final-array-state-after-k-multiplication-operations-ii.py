from collections import *
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        M = 10 ** 9 + 7
        n = len(nums)
        q = deque()
        ops = [0] * n
        ctr = [0] * n
        ones = 0
        vals = []
        for i in range(n):
            heapq.heappush(vals, (nums[i], i))
        while k:
            val, i = heapq.heappop(vals)
            ops[i] += 1
            q.append(i)
            ones -= int(ctr[i] == 1)
            ctr[i] += 1
            ones += int(ctr[i] == 1)
            if len(q) > n:
                j = q.popleft()
                ones -= int(ctr[j] == 1)
                ctr[j] -= 1
                ones += int(ctr[j] == 1)
            heapq.heappush(vals, (val * multiplier, i))
            k -= 1
            if ones == n:
                break
        q = list(q)
        for i in range(n):
            ops[i] += k // n
        for i in range(k % n):
            ops[q[i]] += 1
        return [(nums[i] * pow(multiplier, ops[i], M)) % M for i in range(n)]
        