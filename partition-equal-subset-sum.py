import heapq
import numpy as np

def add_poly(p, q):
    max_len = max(len(p), len(q))
    p = np.pad(p, (0, max_len - len(p)))
    q = np.pad(q, (0, max_len - len(q)))
    return p + q

def multiply_naive(p, q):
    return np.polynomial.polynomial.polymul(p, q)

class Solution:
    def canPartition(self, nums):
        s = sum(nums)
        if s & 1:
            return False
        s //= 2
        heap = []
        for num in nums:
            poly = np.zeros(num + 1, dtype=int)
            poly[0], poly[num] = 1, 1
            heapq.heappush(heap, (len(poly), poly.tolist()))
        while len(heap) > 1:
            _, poly1 = heapq.heappop(heap)
            _, poly2 = heapq.heappop(heap)
            result_poly = multiply_naive(np.array(poly1), np.array(poly2))
            heapq.heappush(heap, (len(result_poly), result_poly.tolist()))
        _, final_poly = heap[0]
        return bool(s < len(final_poly) and final_poly[s] > 0)