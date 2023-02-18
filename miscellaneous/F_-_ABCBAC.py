n = int(input())

s = input()

class Solver:
    def powers(self, n, p, ip, M):
        pw = 1
        invpw = 1
        ppow = []
        invppow = []
        for _ in range(n):
            ppow.append(pw)
            invppow.append(invpw)
            pw = (pw * p) % M
            invpw = (invpw * ip) % M
        return ppow, invppow
    
    def hashes(self, s, p, M):
        n = len(s)
        h = [0] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] + self.ppow[i] * (ord(s[i]) - ord('a'))) % M
        return h

    def check(self, s, l, n):
        S = s[:n//2]
        return S[:l] + S[::-1] + S[-(n // 2 - l):] == s
    
    def find(self, s, n):
        if s == s[::-1]:
            return f"{s[:n // 2]}\n0"
        N = n // 2
        M = 10 ** 9 + 9
        p = 31
        self.ppow, self.invppow = self.powers(n + 1, p, pow(p, M - 2, M), M)
        subhash = lambda h, i, j: (self.invppow[i] * (h[j + 1] + M - h[i])) % M
        hashes = self.hashes(s, p, M)
        revhashes = self.hashes(s[::-1], p, M)
        for l in range(1, N + 1):
            if subhash(hashes, 0, l - 1) == subhash(revhashes, N - l, N - 1):
                if subhash(hashes, l, N - 1) == subhash(hashes, N + l, n - 1):
                    if self.check(s, l, n):
                        return f"{s[:N]}\n{l}"
        return -1

print(Solver().find(s, 2 * n))