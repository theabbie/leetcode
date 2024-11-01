from collections import Counter

class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        M = 10 ** 9 + 7
        n = len(nums)
        for i in range(len(queries)):
            queries[i].append(i)
        res = [0] * len(queries)
        queries.sort()
        s = defaultdict(Counter)
        j = n - 1
        for i in range(len(queries) - 1, -1, -1):
            while j >= queries[i][0]:
                x = 1
                while x * x <= n:
                    s[x][j % x] += nums[j]
                    s[x][j % x] %= M
                    x += 1
                j -= 1
            if queries[i][1] * queries[i][1] <= n:
                res[queries[i][2]] = s[queries[i][1]][queries[i][0] % queries[i][1]]
            else:
                curr = 0
                pos = queries[i][0]
                while pos < n:
                    curr += nums[pos]
                    curr %= M
                    pos += queries[i][1]
                res[queries[i][2]] = curr
        return res