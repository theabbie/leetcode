from collections import defaultdict

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        pos = defaultdict(list)
        for i in range(n):
            pos[nums[i]].append(n + i)
        for el in list(pos):
            beg = pos[el][-1]
            pos[el].insert(0, beg - n)
        res = float('inf')
        for el in pos:
            curr = 0
            m = len(pos[el])
            for i in range(m - 1):
                mid = (pos[el][i] + pos[el][i + 1]) // 2
                curr = max(curr, min(mid - pos[el][i], pos[el][i + 1] - mid))
            res = min(res, curr)
        return res