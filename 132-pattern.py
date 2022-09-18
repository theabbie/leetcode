from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        smallest = [float('inf')]
        for i in range(n):
            smallest.append(min(smallest[-1], nums[i]))
        order = SortedList()
        for i in range(n - 1, -1, -1):
            j = order.bisect_left(nums[i])
            if len(order) > 0 and j <= len(order):
                if j > 0:
                    j -= 1
                if nums[i] > smallest[i] and nums[i] > order[j] and order[j] > smallest[i]:
                    return True
            order.add(nums[i])
        return False