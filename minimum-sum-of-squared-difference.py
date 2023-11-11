class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        beg = 0
        end = max(diffs)
        mindiff = end
        ops = k1 + k2
        while beg <= end:
            mid = (beg + end) // 2
            curr = 0
            for i in range(n):
                curr += max(diffs[i] - mid, 0)
            if curr > ops:
                beg = mid + 1
            else:
                mindiff = mid
                end = mid - 1
        res = 0
        for i in range(n):
            extra = max(diffs[i] - mindiff, 0)
            diffs[i] -= extra
            ops -= extra
        diffs.sort(reverse = True)
        for i in range(n):
            if ops > 0 and diffs[i] > 0:
                diffs[i] -= 1
                ops -= 1
        return sum(el * el for el in diffs)