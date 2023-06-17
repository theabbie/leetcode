from sortedcontainers import SortedList

class Solution:
    def findnext(self, pos, i):
        beg = 0
        end = len(pos) - 1
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            if pos[mid] >= i:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res
    
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        ordered = sorted(nums)
        pos = {}
        for i in range(n):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
        i = 0
        res = 0
        deleted = SortedList()
        for curr in ordered:
            j = self.findnext(pos[curr], i)
            if j == -1:
                res += n + pos[curr][0] - i
                res -= deleted.bisect_right(pos[curr][0]) + len(deleted) - deleted.bisect_left(i)
                deleted.add(pos[curr][0])
                i = pos[curr][0]
                pos[curr].pop(0)
            else:
                res += pos[curr][j] - i
                res -= deleted.bisect_right(pos[curr][j]) - deleted.bisect_left(i)
                deleted.add(pos[curr][0])
                i = pos[curr][j]
                pos[curr].pop(j)
            res += 1
        return res