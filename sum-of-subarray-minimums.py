from sortedcontainers import SortedList

M = 10 ** 9 + 7

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        zeroes = SortedList()
        for i in range(n):
            zeroes.add(i)
        zeroes.add(-1)
        zeroes.add(n)
        arr = sorted([(arr[i], i) for i in range(n)], reverse = True)
        res = 0
        for val, pos in arr:
            zeroes.remove(pos)
            left = pos - zeroes[zeroes.bisect_left(pos) - 1] - 1
            right = zeroes[zeroes.bisect_left(pos)] - pos - 1
            res += (left + 1) * (right + 1) * val
            res %= M
        return res