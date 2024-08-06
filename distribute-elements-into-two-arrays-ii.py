from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums.reverse()
        greaterCount = lambda s, val: len(s) - s.bisect_left(val + 1)
        aset = SortedList()
        bset = SortedList()
        a = []
        b = []
        a.append(nums.pop())
        b.append(nums.pop())
        aset.add(a[-1])
        bset.add(b[-1])
        while len(nums) > 0:
            val = nums.pop()
            x = greaterCount(aset, val)
            y = greaterCount(bset, val)
            if x > y or (x == y and len(a) <= len(b)):
                a.append(val)
                aset.add(val)
            elif y > x or (x == y and len(b) < len(a)):
                b.append(val)
                bset.add(val)
        return a + b