class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Initilize two pointers
        begin = 0
        end = len(nums) - 1 
        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]: # Fail to estimate which side is sorted
                end -= 1  # In worst case: O(n)
            elif nums[mid] > nums[end]: # Left side of mid is sorted
                if  nums[begin] <= target and target < nums[mid]: # Target in the left side
                    end = mid - 1
                else: # in right side
                    begin = mid + 1
            else: # Right side is sorted
                if  nums[mid] < target and target <= nums[end]: # Target in the right side
                    begin = mid + 1
                else: # in left side
                    end = mid - 1
        return False