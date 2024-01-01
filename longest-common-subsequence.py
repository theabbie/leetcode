import bisect

class Solution:
    def longestCommonSubsequence(self, a, b) -> int:
        m = len(a)
        n = len(b)
        order = []
        pos = [[] for _ in range(26)]
        for i in range(n - 1, -1, -1):
            pos[ord(b[i]) - ord('a')].append(i)
        for i in range(m):
            for j in pos[ord(a[i]) - ord('a')]:
                x = bisect.bisect_left(order, j)
                if x < len(order):
                    order[x] = j
                else:
                    order.append(j)
        return len(order)