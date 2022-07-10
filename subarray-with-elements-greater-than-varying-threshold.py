class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        s = []
        left = [-1] * (n + 1)
        right = [n] * (n + 1)
        for i in range(n):
            while (len(s) != 0 and
                   nums[s[-1]] >= nums[i]):
                s.pop()
            if len(s) != 0:
                left[i] = s[-1]
            s.append(i)
        s = []
        for i in range(n - 1, -1, -1):
            while (len(s) != 0 and nums[s[-1]] >= nums[i]):
                s.pop()
            if len(s) != 0:
                right[i] = s[-1]
            s.append(i)
        for i in range(n):
            l = right[i] - left[i] - 1
            if l * nums[i] > threshold:
                return l
        return -1