from bisect import *

def larger(arr, val):
    beg = 0
    end = len(arr) - 1
    res = -1
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] >= val:
            res = arr[mid]
            end = mid - 1
        else:
            beg = mid + 1
    return res

def smaller(arr, val):
    beg = 0
    end = len(arr) - 1
    res = -1
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] <= val:
            res = arr[mid]
            beg = mid + 1
        else:
            end = mid - 1
    return res

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        plates = [i for i in range(n) if s[i] == '*']
        candles = [i for i in range(n) if s[i] == '|']
        res = []
        for l, r in queries:
            l = larger(candles, l)
            r = smaller(candles, r)
            if l >= r or l == - 1 or r == -1:
                res.append(0)
                continue
            res.append(bisect_right(plates, r) - bisect_left(plates, l))
        return res
        