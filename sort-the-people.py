class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        res = sorted(range(n), key = lambda i: -heights[i])
        return [names[i] for i in res]