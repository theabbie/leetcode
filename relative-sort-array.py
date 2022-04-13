class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2index = {}
        for i, a in enumerate(arr2):
            arr2index[a] = i
        return sorted(arr1, key = lambda x: (arr2index[x], arr2index[x]) if x in arr2index else (float('inf'), x))