import heapq
import numpy as np

MOD = 10**9 + 7

def add_poly(p, q):
    max_len = max(len(p), len(q))
    p = np.pad(p, (0, max_len - len(p)))
    q = np.pad(q, (0, max_len - len(q)))
    return (p + q) % MOD

def multiply_naive(p, q, n):
    result = np.polynomial.polynomial.polymul(p, q) % MOD
    return result[:n+1]

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        heap = []
        for i in range(1, n + 1):
            a = pow(i, x)
            if a > n:
                break
            poly = np.zeros(a + 1, dtype=int)
            poly[0], poly[a] = 1, 1
            heapq.heappush(heap, (len(poly), poly.tolist()))
        
        while len(heap) > 1:
            _, poly1 = heapq.heappop(heap)
            _, poly2 = heapq.heappop(heap)
            result_poly = multiply_naive(np.array(poly1), np.array(poly2), n)
            heapq.heappush(heap, (len(result_poly), result_poly.tolist()))
        
        _, final_poly = heap[0]
        if len(final_poly) < n + 1:
            return 0
        return int(final_poly[n] % MOD)