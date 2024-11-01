from sortedcontainers import SortedList

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        q = len(removeQueries)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        vals = sorted([(removeQueries[i], i) for i in range(q)])
        prev = [-1] * q
        nxt = [n] * q
        stack = []
        for el, i in vals:
            while stack and i <= stack[-1]:
                curr = stack.pop()
                nxt[curr] = removeQueries[i]
            if stack:
                prev[i] = removeQueries[stack[-1]]
            stack.append(i)
        sums = SortedList([p[n]])
        res = []
        for i in range(q):
            pos = removeQueries[i]
            l = prev[i] + 1
            r = nxt[i] - 1
            sums.remove(p[r + 1] - p[l])
            sums.add(p[pos] - p[l])
            sums.add(p[r + 1] - p[pos + 1])
            res.append(sums[-1])
        return res