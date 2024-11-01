MAX = 100001

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

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        graph = [set() for _ in range(n)]
        f = {}
        for i in range(n):
            curr = nums[i]
            while curr > 1:
                if sp[curr] in f:
                    graph[f[sp[curr]]].add(i)
                    graph[i].add(f[sp[curr]])
                else:
                    f[sp[curr]] = i
                curr //= sp[curr]
        res = 0
        v = [False] * n
        for i in range(n):
            if not v[i]:
                v[i] = True
                sz = 0
                stack = [i]
                while stack:
                    x = stack.pop()
                    sz += 1
                    for y in graph[x]:
                        if not v[y]:
                            v[y] = True
                            stack.append(y)
                res = max(res, sz)
        return res