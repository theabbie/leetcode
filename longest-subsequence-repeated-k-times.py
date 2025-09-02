from collections import Counter

def f(s, k):
    c = Counter(s)
    use = [ch for ch, v in c.items() if v >= k]
    m = len(s) // k
    use.sort(reverse=True)
    n = len(s)

    nxt = [{ch: -1 for ch in use} for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        d = nxt[i + 1].copy()
        if s[i] in d:
            d[s[i]] = i
        nxt[i] = d

    suff = [{ch: 0 for ch in use} for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        d = suff[i + 1].copy()
        if s[i] in d:
            d[s[i]] += 1
        suff[i] = d

    def check(x):
        i = 0
        for ch in s:
            if i < len(x) and ch == x[i]:
                i += 1
        return i == len(x)

    cur = Counter()
    ans = ''

    def solve(pos, path):
        nonlocal ans
        if path:
            if len(path) > len(ans) or (len(path) == len(ans) and path > ans):
                if check(path * k):
                    ans = path
        if len(path) == m:
            return
        for ch in use:
            if cur[ch] < c[ch] // k:
                p = nxt[pos][ch]
                if p == -1:
                    continue
                cur[ch] += 1
                ok = True
                for u, v in cur.items():
                    if suff[p + 1][u] < v * (k - 1):
                        ok = False
                        break
                if ok:
                    solve(p + 1, path + ch)
                cur[ch] -= 1

    solve(0, '')
    return ans

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        return f(s, k)