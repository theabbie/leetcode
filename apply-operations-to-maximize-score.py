import math

M = 10 ** 9 + 7

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        old = nums[:]
        MAX = max(nums) + 1
        v = [False] * MAX
        sp = [0] * MAX
        for i in range(2, MAX, 2):
            sp[i] = 2
        for i in range(3, MAX, 2):
            if not v[i]:
                sp[i] = i
                j = i
                while j * i < MAX:
                    if not v[j * i]:
                        v[j * i] = True
                        sp[j * i] = i
                    j += 2
        for i in range(n):
            ctr = set()
            curr = nums[i]
            while curr > 1:
                ctr.add(sp[curr])
                curr //= sp[curr]
            nums[i] = len(ctr)
        prev = [-1] * n
        nxt = [n] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                curr = stack.pop()
                nxt[curr] = i
            if len(stack) > 0:
                prev[i] = stack[-1]
            stack.append(i)
        res = 1
        nums = [(old[i], i) for i in range(n)]
        nums.sort(reverse = True)
        for v, pos in nums:
            ctr = (pos - prev[pos]) * (nxt[pos] - pos)
            ctr = min(ctr, k)
            res *= pow(v, ctr, M)
            res %= M
            k -= ctr
            if k <= 0:
                break
        return res