import bisect

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        f = [i for i in range(n) if digits[i] != 0]
        s = [i for i in range(n)]
        t = [i for i in range(n) if digits[i] in {0, 2, 4, 6, 8}]
        nums = []
        for i in f:
            for j in s:
                if i == j:
                    continue
                for k in t:
                    if i != k and j != k:
                        val = 100 * digits[i] + 10 * digits[j] + digits[k]
                        pos = bisect.bisect_left(nums, val)
                        if pos >= len(nums) or nums[pos] != val:
                            bisect.insort(nums, val)
        return nums