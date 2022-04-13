import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k & 1:
            def getMedian(arr):
                return arr[k // 2]
        else:
            def getMedian(arr):
                return (arr[(k // 2) - 1] + arr[k // 2]) / 2
        n = len(nums)
        medians = []
        window = sorted(nums[:k])
        for i in range(0, n - k):
            medians.append(getMedian(window))
            window.remove(nums[i])
            bisect.insort(window, nums[i + k])
        medians.append(getMedian(window))
        return medians