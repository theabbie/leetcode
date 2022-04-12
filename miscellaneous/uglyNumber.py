import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        uglySet = {1}
        while len(uglies) < n * 10:
            for num in uglies[:]:
                for k in [2, 3, 5]:
                    p = num * k
                    if p not in uglySet:
                        heapq.heappush(uglies, p)
                        uglySet.add(p)
        return heapq.nsmallest(n, uglies)[n - 1]

print(Solution().nthUglyNumber(10))