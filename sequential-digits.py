import bisect
import math

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        n = len(nums)
        a = int(1 + math.log10(low))
        b = int(1 + math.log10(high))
        op = []
        for l in range(a, b + 1):
            for i in range(n - l + 1):
                curr = int(nums[i:i + l])
                if curr >= low and curr <= high:
                    bisect.insort(op, curr)
        return op