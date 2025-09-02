class Solution:
    def maxProduct(self, nums, k, limit):
        @cache
        def zero(i, tot, add, has):
            if i == len(nums):
                return has and tot == k

            if zero(i + 1, tot, add, has):
                return True

            if nums[i] <= limit:
                new_tot = tot + nums[i] if add else tot - nums[i]
                new_has = has or (nums[i] == 0)
                if zero(i + 1, new_tot, not add, new_has):
                    return True

            return False

        @cache
        def dp(i, p, rem, mx, emp):
            if i >= len(nums):
                if not emp and rem == 0:
                    return 1
                return float('-inf')
            a = dp(i + 1, p, rem, mx, emp)
            b = float('-inf')
            if nums[i] <= mx:
                b = nums[i] * dp(i + 1, -p, rem - p * nums[i], mx // nums[i] if nums[i] > 0 else float('inf'), False)
            return max(a, b)

        return max(dp(0, 1, k, limit, True), 0 if zero(0, 0, True, False) else -1, -1)