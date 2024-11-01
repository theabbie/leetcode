class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()
        def check(x, y):
            m = len(x)
            n = len(y)
            j = 0
            pf = [0] * (n + 1)
            sf = [0] * (n + 1)
            for i in range(m):
                if j < n and x[i] == y[j]:
                    pf[j + 1] = i + 1
                    j += 1
            j = n - 1
            for i in range(m - 1, -1, -1):
                if j >= 0 and x[i] == y[j]:
                    sf[n - j] = m - i
                    j -= 1
            for l in range(n + 1):
                if pf[l] == l and sf[n - l] == n - l:
                    return True
            return False
        return check(a, b) or check(b, a)