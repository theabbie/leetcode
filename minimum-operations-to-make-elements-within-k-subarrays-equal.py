from sortedcontainers import SortedList

class Solution:
    def ops(self, arr, k):
        left, right = SortedList(), SortedList()
        left_sum, right_sum = 0, 0
        res = []
        def rebalance():
            nonlocal left_sum, right_sum
            window = len(left) + len(right)
            required_left = (window + 1) // 2
            while len(left) > required_left:
                x = left.pop()
                left_sum -= x
                right.add(x)
                right_sum += x
            while len(left) < required_left:
                if not right:
                    break
                x = right.pop(0)
                right_sum -= x
                left.add(x)
                left_sum += x
        def add(x):
            nonlocal left_sum, right_sum
            if not left or x <= left[-1]:
                left.add(x)
                left_sum += x
            else:
                right.add(x)
                right_sum += x
            rebalance()
        def remove(x):
            nonlocal left_sum, right_sum
            if left and x <= left[-1]:
                idx = left.bisect_left(x)
                left_sum -= left[idx]
                left.pop(idx)
            else:
                idx = right.bisect_left(x)
                right_sum -= right[idx]
                right.pop(idx)
            rebalance()
        for i, x in enumerate(arr):
            add(x)
            if i >= k:
                remove(arr[i-k])
            if i >= k-1:
                m = left[-1]
                cost = m * len(left) - left_sum + right_sum - m * len(right)
                res.append(cost)
        return res

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        mops = self.ops(nums, x)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0
        for i in range(n - 1, -1, -1):
            for rem in range(k + 1):
                dp[i][rem] = dp[i + 1][rem]
                if i + x <= n and rem:
                    dp[i][rem] = min(dp[i][rem], mops[i] + dp[i + x][rem - 1])
        return dp[0][k]