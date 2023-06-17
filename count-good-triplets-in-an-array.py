class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = [[-1, -1, i] for i in range(n)]
        for i in range(n):
            pos[nums1[i]][0] = i
            pos[nums2[i]][1] = i
        pos.sort()
        ctr = [1] * n
        fw = FenwickTree([0] * n)
        for x, y, i in pos:
            ctr[i] *= fw.query(y)
            fw.update(y, 1)
        fw = FenwickTree([0] * n)
        for x, y, i in pos[::-1]:
            ctr[i] *= fw.query(n) - fw.query(y + 1)
            fw.update(y, 1)
        return sum(ctr)