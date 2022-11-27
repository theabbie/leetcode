from collections import deque, Counter, defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        ctr = Counter(nums)
        for el in ctr:
            res += 1 << ctr[el]
            res -= ctr[el] + 1
            res -= ctr[el] * (ctr[el] - 1) // 2
        pos = defaultdict(list)
        q = deque()
        for i in range(n):
            pos[nums[i]].append(i)
            for j in range(i + 1, n):
                if nums[j] != nums[i]:
                    q.appendleft((nums[j] - nums[i], j, 2))
        while len(q) > 0:
            d, i, l = q.pop()
            if l >= 3:
                res += 1
            for j in pos[nums[i] + d]:
                if j > i:
                    q.appendleft((d, j, l + 1))
        return res