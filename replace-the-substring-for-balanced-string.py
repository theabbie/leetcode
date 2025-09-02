class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        Q = [0] * (n + 1)
        W = [0] * (n + 1)
        E = [0] * (n + 1)
        R = [0] * (n + 1)
        for i in range(n):
            Q[i + 1] = Q[i] + int(s[i] == 'Q')
            W[i + 1] = W[i] + int(s[i] == 'W')
            E[i + 1] = E[i] + int(s[i] == 'E')
            R[i + 1] = R[i] + int(s[i] == 'R')
        k = n // 4
        res = n
        for i in range(n):
            beg = i - 1
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                q = Q[mid + 1] - Q[i]
                w = W[mid + 1] - W[i]
                e = E[mid + 1] - E[i]
                r = R[mid + 1] - R[i]
                if q >= Q[n] - k and w >= W[n] - k and e >= E[n] - k and r >= R[n] - k:
                    end = mid - 1
                else:
                    beg = mid + 1
            if end + 1 < n:
                res = min(res, end - i + 2)
        return res