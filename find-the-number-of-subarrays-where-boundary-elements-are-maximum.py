from collections import *
import bisect

class Solution:
    def numberOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        M = 10 ** 9 + 7
        pos = defaultdict(list)
        for i in range(n):
            pos[arr[i]].append(i)
        stack = []
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        for i in range(n):
            while len(stack) > 0 and arr[i] > arr[stack[-1]]:
                curr = stack.pop()
                next_smaller[curr] = i
            if len(stack) > 0:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(n):
            l = prev_smaller[i]
            r = next_smaller[i]
            res += (bisect.bisect_right(pos[arr[i]], r - 1) - bisect.bisect_left(pos[arr[i]], i)) * (bisect.bisect_right(pos[arr[i]], i) - bisect.bisect_left(pos[arr[i]], l + 1))
        return res