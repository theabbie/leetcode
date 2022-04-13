class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        beg = 0
        end = n - 1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] > 0 and nums[mid - 1] < 0:
                beg = mid
                break
            elif beg == end:
                break
            elif nums[mid] < 0:
                beg = mid + 1
            else:
                end = mid
        op = []
        i = beg - 1
        j = beg
        while i >= 0 and j <= n - 1:
            if nums[i] * nums[i] < nums[j] * nums[j]:
                op.append(nums[i] * nums[i])
                i -= 1
            else:
                op.append(nums[j] * nums[j])
                j += 1
        while i >= 0:
            op.append(nums[i] * nums[i])
            i -= 1
        while j <= n - 1:
            op.append(nums[j] * nums[j])
            j += 1
        return op