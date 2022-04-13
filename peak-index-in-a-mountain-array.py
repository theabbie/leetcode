class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        old = True
        new = True
        for i in range(len(arr) - 1):
            new = arr[i + 1] > arr[i]
            if new ^ old:
                return i
            old = new