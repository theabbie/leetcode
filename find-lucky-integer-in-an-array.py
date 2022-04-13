from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ctr = Counter(arr)
        return max([k for k, v in ctr.items() if k == v] + [-1])