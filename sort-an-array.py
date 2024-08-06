class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def mergesort(i, j):
            if i + 1 == j:
                return
            mid = (i + j) // 2
            mergesort(i, mid)
            mergesort(mid, j)
            vals = []
            x = i
            y = mid
            while x < mid and y < j:
                if nums[x] <= nums[y]:
                    vals.append(nums[x])
                    x += 1
                else:
                    vals.append(nums[y])
                    y += 1
            while x < mid:
                vals.append(nums[x])
                x += 1
            while y < j:
                vals.append(nums[y])
                y += 1
            for x in range(i, j):
                nums[x] = vals[x - i]
        mergesort(0, n)
        return nums