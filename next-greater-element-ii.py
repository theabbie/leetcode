class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        n = len(nums)
        mpow = [(0, 1)] * (n + 1)
        pw = [1]
        l = 0
        p = 1
        for i in range(1, n + 1):
            if p * 2 <= i:
                l += 1
                p *= 2
                pw.append(p)
            mpow[i] = (l, p)
        cache = {}
        def get(i, x):
            if x == 0:
                return nums[i]
            if (i, x) in cache:
                return cache[(i, x)]
            cache[(i, x)] = max(get(i, x - 1), get(i + pw[x - 1], x - 1))
            return cache[(i, x)]
        def getmax(i, j):
            x, px = mpow[j - i]
            return max(get(i, x), get(j - px, x))
        res = [-1] * (n // 2)
        for i in range(n // 2):
            beg = i
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                if getmax(i, mid + 1) > nums[i]:
                    res[i] = nums[mid]
                    end = mid - 1
                else:
                    beg = mid + 1
        return res