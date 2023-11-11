from collections import Counter

MAX = 1 + 10 ** 6

v = [False] * MAX
sp = [0] * MAX

for i in range(2, MAX, 2):
    sp[i] = 2

for i in range(3, MAX, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < MAX:
            if not v[j * i]:
                v[j * i] = True
                sp[j * i] = i
            j += 2

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        bothcount = 0
        left = Counter()
        right = Counter()
        for el in nums:
            curr = el
            while curr > 1:
                right[sp[curr]] += 1
                curr //= sp[curr]
        for i in range(n - 1):
            curr = nums[i]
            while curr > 1:
                bothcount -= int(left[sp[curr]] > 0 and right[sp[curr]] > 0)
                right[sp[curr]] -= 1
                left[sp[curr]] += 1
                bothcount += int(left[sp[curr]] > 0 and right[sp[curr]] > 0)
                curr //= sp[curr]
            if bothcount == 0:
                return i
        return -1