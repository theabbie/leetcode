from sortedcontainers import SortedList

def minops(A, B, s):
    A.sort(reverse = True)
    B = SortedList(B)
    u = 0
    for a in A:
        i = B.bisect_left(a)
        if i < len(B):
            B.pop(i)
        else:
            j = B.bisect_left(a - s)
            if j < len(B):
                B.pop(j)
                u += 1
            else:
                return float('inf')
    return u

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        tasks.sort()
        workers.sort(reverse = True)
        beg = 0
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            if minops(tasks[:mid], workers[:mid], strength) <= pills:
                beg = mid + 1
            else:
                end = mid - 1
        return beg - 1