from sortedcontainers import SortedList

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pos = defaultdict(list)
        for i in range(n - 1, -1, -1):
            pos[nums[i]].append(i)
        bst = SortedList()
        for el in pos:
            bst.add(pos[el][-1])
        res = 0
        for i in range(n):
            a = bst[k - 1] if k - 1 < len(bst) else n
            b = bst[k] if k < len(bst) else n
            res += b - a
            bst.remove(pos[nums[i]].pop())
            if len(pos[nums[i]]) > 0:
                bst.add(pos[nums[i]][-1])
            else:
                bst.add(n)
        return res