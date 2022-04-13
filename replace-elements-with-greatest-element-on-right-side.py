class Solution:
#     def makeSeg(self, arr, i, j):
#         seg = self.seg
#         if (i, j) in seg:
#             return seg[(i, j)]
#         if i == j:
#             seg[(i, j)] = arr[i]
#             return arr[i]
#         mid = (i + j) // 2
#         curr = max(self.makeSeg(arr, i, mid), self.makeSeg(arr, mid + 1, j))
#         seg[(i, j)] = curr
#         return curr
    
#     def getMax(self, arr, i, j, ni, nj):
#         seg = self.seg
#         if ni >= i and nj <= j:
#             return seg[(ni, nj)]
#         if (ni < i and nj < i) or (ni > j and nj > j):
#             return float('-inf')
#         mid = (ni + nj) // 2
#         return max(self.getMax(arr, i, j, ni, mid), self.getMax(arr, i, j, mid + 1, nj))
    
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         n = len(arr)
#         self.seg = {}
#         self.makeSeg(arr, 0, n - 1)
#         for i in range(n):
#             if i < n - 1:
#                 arr[i] = self.getMax(arr, i + 1, n, 0, n - 1)
#             else:
#                 arr[i] = -1
#         return arr

    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        op = [-1] * n
        currMax = float('-inf')
        for i in range(n - 1, 0, -1):
            currMax = max(currMax, arr[i])
            op[i - 1] = currMax
        return op