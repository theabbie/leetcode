class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        mindiff = float('inf')
        mindiffindexes = []
        arr.sort()
        for i in range(n - 1):
            currdiff = arr[i + 1] - arr[i]
            if currdiff < mindiff:
                mindiff = currdiff
                mindiffindexes = []
            if currdiff == mindiff:
                mindiffindexes.append(i)
        return [[arr[i], arr[i + 1]] for i in mindiffindexes]