import bisect

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        lis = [[] for _ in range(k)]
        res = n
        for i in range(n):
            x = bisect.bisect_left(lis[i % k], (arr[i], i))
            if x < len(lis[i % k]):
                lis[i % k][x] = (arr[i], i)
            else:
                lis[i % k].append((arr[i], i))
                res -= 1
        return res