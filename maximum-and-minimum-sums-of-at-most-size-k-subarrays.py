class Solution:
    def minsum(self, arr, k):
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
            lwidth = i - l - 1
            rwidth = r - i - 1
            up = min(lwidth, k)
            mid = max(k - rwidth - 1, 0)
            res += min(up + 1, mid) * (rwidth + 1) * arr[i]
            if mid <= up:
                res += arr[i] * (k * (up - mid + 1) - (up * (up + 1) // 2 - mid * (mid - 1) // 2))
        return res
    
    def maxsum(self, arr, k):
        n = len(arr)
        stack = []
        next_greater = [n] * n
        prev_greater = [-1] * n
        for i in range(n):
            while len(stack) > 0 and arr[i] > arr[stack[-1]]:
                curr = stack.pop()
                next_greater[curr] = i
            if len(stack) > 0:
                prev_greater[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(n):
            l = prev_greater[i]
            r = next_greater[i]
            lwidth = i - l - 1
            rwidth = r - i - 1
            up = min(lwidth, k)
            mid = max(k - rwidth - 1, 0)
            res += min(up + 1, mid) * (rwidth + 1) * arr[i]
            if mid <= up:
                res += arr[i] * (k * (up - mid + 1) - (up * (up + 1) // 2 - mid * (mid - 1) // 2))
        return res
    
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        return self.minsum(nums, k) + self.maxsum(nums, k)