import heapq

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        heap = []
        median = arr[(n - 1) // 2]
        res = sorted([(-abs(item - median), -item) for item in arr])
        return [-el[1] for el in res[:k]]