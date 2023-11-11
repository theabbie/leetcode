from sortedcontainers import SortedList

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()
        l = SortedList()
        r = SortedList()
        for i in range(n):
            r.add(i)
        i = j = 0
        for el, pos in arr:
            while i < n and arr[i][0] <= el - valueDifference:
                l.add(arr[i][1])
                i += 1
            while j < n and arr[j][0] < el + valueDifference:
                r.remove(arr[j][1])
                j += 1
            if len(l) > 0 and l[0] <= pos - indexDifference:
                return (l[0], pos)
            if len(l) > 0 and l[-1] >= pos + indexDifference:
                return (pos, l[-1])
            if len(r) > 0 and r[0] <= pos - indexDifference:
                return (r[0], pos)
            if len(r) > 0 and r[-1] >= pos + indexDifference:
                return (pos, r[-1])
        return (-1, -1)