from collections import Counter
import heapq

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        n = len(s)
        add = s.count('?')
        ctr = Counter()
        og = Counter()
        for c in s:
            if c != '?':
                og[c] += 1
                ctr[c] += 1
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in ctr:
                ctr[c] = 0
        heap = []
        for c in ctr:
            heapq.heappush(heap, (ctr[c], c))
        for _ in range(add):
            count, c = heapq.heappop(heap)
            ctr[c] += 1
            heapq.heappush(heap, (count + 1, c))
        s = list(s)
        for i in range(n):
            if s[i] == '?':
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if ctr[c] <= og[c]:
                        continue
                    s[i] = c
                    ctr[c] -= 1
                    break
        return "".join(s)