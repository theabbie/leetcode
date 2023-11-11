from collections import *
from sortedcontainers import SortedList

class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

M = 10 ** 9 + 7

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        pos = defaultdict(list)
        for i in range(n - 1, -1, -1):
            pos[nums[i]].append(i)
        res = 0
        curr = 0
        nextpos = SortedList()
        for el in pos:
            nextpos.add(pos[el][-1])
        for i in range(len(nextpos)):
            curr += (-2 * i - 1) * nextpos[i]
        curr += len(nextpos) * len(nextpos) * n
        fw = FenwickTree([0] * (n + 2))
        for el in nextpos:
            fw.update(el, el)
        for i in range(n):
            res += curr
            res %= M
            prev = pos[nums[i]].pop()
            prevpos = nextpos.bisect_left(prev)
            curr -= (-2 * prevpos - 1) * nextpos[prevpos]
            rightsum = fw.query(n + 2) - fw.query(prev + 1)
            curr += 2 * rightsum
            curr -= len(nextpos) * len(nextpos) * n
            nextpos.pop(prevpos)
            curr += len(nextpos) * len(nextpos) * n
            fw.update(prev, -prev)
            if len(pos[nums[i]]) > 0:
                nxt = pos[nums[i]][-1]
                curr -= len(nextpos) * len(nextpos) * n
                nextpos.add(nxt)
                prevpos = nextpos.bisect_left(nxt)
                curr += (-2 * prevpos - 1) * nextpos[prevpos]
                rightsum = fw.query(n + 2) - fw.query(nxt + 1)
                curr -= 2 * rightsum
                curr += len(nextpos) * len(nextpos) * n
                fw.update(nxt, nxt)
            curr %= M
        return res