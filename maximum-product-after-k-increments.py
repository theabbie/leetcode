class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix = [0] + list(accumulate(nums))
        n = len(nums)

        beg = nums[0]
        end = nums[-1] + k
        rem = 0
        
        while beg <= end:
            mid = (beg + end) // 2
            idx = bisect_left(nums, mid)
            ops = mid * idx - prefix[idx]

            if ops <= k:
                rem = k - ops
                beg = mid + 1
            else:
                end = mid - 1

        res = 1

        for i in range(n):
            if nums[i] <= beg - 1:
                nums[i] = beg - 1 + int(rem > 0)
                rem -= 1
            res *= nums[i]
            res %= 1000000007

        return res