class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        mindiff = float('inf')
        arr.sort()
        for i in range(n - 1):
            mindiff = min(mindiff, arr[i + 1] - arr[i])
        op = []
        for i in range(n - 1):
            if arr[i + 1] - arr[i] == mindiff:
                op.append([arr[i], arr[i + 1]])
        return op