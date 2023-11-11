import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        v = {1}
        MAX = 1 << 32
        primes.sort()
        for _ in range(n - 1):
            curr = heapq.heappop(heap)
            for p in primes:
                if curr * p <= MAX:
                    if curr * p not in v:
                        v.add(curr * p)
                        heapq.heappush(heap, curr * p)
                else:
                    break
        return heap[0]