class Solution:
    def LongestCommonSubarray(self, X, Y, m, n):
        common = [[0 for k in range(n+1)] for l in range(m+1)]
        result = 0
        for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    common[i][j] = 0
                elif (X[i-1] == Y[j-1]):
                    common[i][j] = common[i-1][j-1] + 1
                    result = max(result, common[i][j])
                else:
                    common[i][j] = 0
        return result
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        return self.LongestCommonSubarray(nums1, nums2, len(nums1), len(nums2))