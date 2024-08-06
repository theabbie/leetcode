from sortedcontainers import SortedList

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        marked = SortedList()
        unmarked = SortedList()
        s = 0
        for i in range(n):
            unmarked.add((nums[i], i))
            s += nums[i]
        track = [False] * n
        res = []
        for i, k in queries:
            if not track[i]:
                track[i] = True
                marked.add((nums[i], i))
                unmarked.remove((nums[i], i))
                s -= nums[i]
            while len(unmarked) > 0 and k:
                val, pos = unmarked.pop(0)
                track[pos] = True
                marked.add((val, pos))
                s -= val
                k -= 1
            res.append(s)
        return res