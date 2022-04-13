class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if 2 * k < n:
            for i in range(k):
                nums.insert(0, nums.pop())
        else:
            for i in range(n - k):
                nums.append(nums.pop(0))