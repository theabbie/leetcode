class Solution:
    def isAP(self, arr):
        arr.sort()
        n = len(arr)
        d = arr[1] - arr[0]
        for i in range(1, n - 1):
            if arr[i + 1] - arr[i] != d:
                return False
        return True
        
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        return [self.isAP(nums[l[i]:r[i]+1]) for i in range(n)]
            