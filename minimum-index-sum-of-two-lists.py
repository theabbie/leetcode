class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1pos = {}
        l2pos = {}
        for i, num in enumerate(list1):
            l1pos[num] = i
        for i, num in enumerate(list2):
            l2pos[num] = i
        common = set.intersection(set(list1), set(list2))
        sums = {}
        for c in common:
            curr = l1pos[c] + l2pos[c]
            sums[curr] = sums.get(curr, []) + [c]
        return sums[min(sums.keys())]