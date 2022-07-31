class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        for i in range(n):
            while len(stack) > 0 and arr[i] < arr[stack[-1]]:
                curr = stack.pop()
                next_smaller[curr] = i
            if len(stack) > 0:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(n):
            l = prev_smaller[i]
            r = next_smaller[i]
            res += (i - l) * (r - i) * arr[i]
        return res % (10 ** 9 + 7)