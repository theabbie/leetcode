class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        g = [[] for _ in range(n + 1)]
        for i in range(n):
            g[n].append(i)
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    g[i].append(j)
        M = 10 ** 9 + 7
        cache = {}
        def count(i, used):
            if used + 1 == 1 << n:
                return 1
            key = (i, used)
            if key in cache:
                return cache[key]
            res = 0
            for j in g[i]:
                if not used & (1 << j):
                    res += count(j, used | (1 << j))
                    res %= M
            cache[key] = res
            return res
        return count(n, 0)