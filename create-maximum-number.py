class Solution:
    def largestMerge(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        res = []
        i = j = 0
        while i < m and j < n:
            if a[i] > b[j]:
                res.append(a[i])
                i += 1
            elif b[j] > a[i]:
                res.append(b[j])
                j += 1
            else:
                if a[i:] >= b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
        res.extend(a[i:] + b[j:])
        return res
    
    def maxNum(self, arr, l):
        n = len(arr)
        stack = []
        for i in range(n):
            while stack and arr[i] > stack[-1] and len(stack) + (n - i - 1) >= l:
                stack.pop()
            stack.append(arr[i])
        while len(stack) > l:
            stack.pop()
        return stack
    
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = []
        for f in range(max(k - len(nums2), 0), min(k, len(nums1)) + 1):
            a = self.maxNum(nums1, f)
            b = self.maxNum(nums2, k - f)
            res = max(res, self.largestMerge(a, b))
        return res