class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        beg = 0
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            if mid < n - 1 and arr[mid] == arr[mid + 1]:
                i = mid
                j = mid + 1
            elif mid >  0 and arr[mid] == arr[mid - 1]:
                i = mid - 1
                j = mid
            else:
                return arr[mid]
            if i % 2 == 0:
                beg = i + 1
            else:
                end = i