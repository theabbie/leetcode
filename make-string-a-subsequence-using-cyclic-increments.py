from collections import defaultdict

class Solution:
    def find(self, arr, val, n):
        beg = 0
        end = len(arr) - 1
        res = n
        while beg <= end:
            mid = (beg + end) // 2
            if arr[mid] > val:
                res = arr[mid]
                end = mid - 1
            else:
                beg = mid + 1
        return res
    
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        pos = defaultdict(list)
        for i in range(n):
            pos[str1[i]].append(i)
        res = True
        prev = -1
        for c in str2:
            x = ord(c) - ord('a')
            minpos = n
            for diff in range(2):
                cc = chr(ord('a') + (26 + x - diff) % 26)
                minpos = min(minpos, self.find(pos[cc], prev, n))
            prev = minpos
            if prev == n:
                res = False
                break
        return res