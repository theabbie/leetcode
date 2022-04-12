class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        beg = 0
        end = n - 1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] == target:
                return mid
            elif beg == end:
                break
            elif nums[mid] > target:
                end = mid
            else:
                beg = mid + 1
        return -1