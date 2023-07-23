from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()
        i = 0
        order = SortedList()
        left = [-1] * n
        for el, pos in arr:
            while i < n and arr[i][0] < el - 2:
                order.add(arr[i][1])
                i += 1
            j = order.bisect_left(pos)
            if 0 <= j - 1 < len(order):
                left[pos] = order[j - 1]
        arr.reverse()
        i = 0
        order = SortedList()
        for el, pos in arr:
            while i < n and arr[i][0] > el + 2:
                order.add(arr[i][1])
                i += 1
            j = order.bisect_left(pos)
            if 0 <= j - 1 < len(order):
                left[pos] = max(left[pos], order[j - 1])
        res = 0
        mleft = -1
        for i in range(n):
            mleft = max(mleft, left[i])
            res += i - mleft
        return res