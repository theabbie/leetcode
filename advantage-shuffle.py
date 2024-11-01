class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        a = sorted([(nums1[i], i) for i in range(n)])
        b = sorted([(nums2[i], i) for i in range(n)])
        beg = 1
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            pos = True
            for i in range(mid):
                if a[-mid + i][0] <= b[i][0]:
                    pos = False
                    break
            if pos:
                beg = mid + 1
            else:
                end = mid - 1
        l = beg - 1
        res = [0] * n
        for i in range(n):
            res[b[i][1]] = a[-l+i][0]
        return res