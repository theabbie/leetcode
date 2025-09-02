class Solution:
    def check(self, intervals, k):
        intervals.sort(key=lambda x: x[1])
        count, last_end = 0, -float('inf')
        for start, end in intervals:
            if start >= last_end:
                count += 1
                last_end = end
                if count >= k:
                    return True
        return False
    
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
        n = len(s)
        p = [Counter() for _ in range(n + 1)]
        for i in range(n):
            p[i + 1] += p[i]
            p[i + 1][s[i]] += 1
        invs = []
        f = {}
        l = {}
        for i in range(n):
            if s[i] not in f:
                f[s[i]] = i
            l[s[i]] = i
        for c in f:
            left = f[c]
            right = l[c]
            while True:
                found = False
                for nc in f:
                    if p[right + 1][nc] - p[left][nc] > 0:
                        if f[nc] < left:
                            found = True
                        if l[nc] > right:
                            found = True
                        left = min(left, f[nc])
                        right = max(right, l[nc])
                if not found:
                    break
            if (left, right) == (0, n - 1):
                continue
            invs.append((left, right))
        return self.check(invs, k)