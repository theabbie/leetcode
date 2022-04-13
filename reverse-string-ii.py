class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = [c for c in s]
        for i in range(0, n, k):
            for j in range(i, i + (min(i + k, n) - i) // 2):
                if (i // k) % 2 == 0:
                    nj = min(j - (j % k) + k, n) - (j % k) - 1
                    s[j], s[nj] = s[nj], s[j]
        return "".join(s)