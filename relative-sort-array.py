class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {}
        for i in range(len(arr2)):
            if arr2[i] not in pos:
                pos[arr2[i]] = (i, i)
        return sorted(arr1, key = lambda x: pos.get(x, (float('inf'), x)))