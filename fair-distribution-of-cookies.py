class Solution:
    def distribute(self, cookies, i, n, k, buckets):
        if i >= n:
            self.minmax = min(self.minmax, max(buckets))
            return
        for j in range(k):
            buckets[j] += cookies[i]
            self.distribute(cookies, i + 1, n, k, buckets)
            buckets[j] -= cookies[i]
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        if n == k:
            return max(cookies)
        buckets = [0] * k
        self.minmax = float('inf')
        self.distribute(cookies, 0, n, k, buckets)
        return self.minmax