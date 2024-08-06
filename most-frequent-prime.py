from collections import Counter

def is_prime(n):
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        res = (0, -1)
        ctr = Counter()
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == dy == 0:
                            continue
                        val = 0
                        x = i
                        y = j
                        while 0 <= x < m and 0 <= y < n:
                            val = 10 * val + mat[x][y]
                            ctr[val] += 1
                            x += dx
                            y += dy
        for el in ctr:
            if el > 10 and is_prime(el):
                res = max(res, (ctr[el], el))
        return res[1]